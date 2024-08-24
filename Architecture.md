### 設計方針の最終まとめ（MongoDB中心）

#### 1. **レイヤードアーキテクチャの採用**
   - アプリケーションを`Router`, `Service`, `Repository`, `Entity`, `Schema`のレイヤーに分割し、各レイヤーの責任を明確にします。
   - これにより、各レイヤーが独立して開発・変更できるため、システム全体の保守性と拡張性が向上します。

#### 2. **依存性注入の利用**
   - FastAPIの依存性注入機能を使用して、`Service`, `Repository`層の依存関係を管理します。
   - 依存性注入の設定は`Dependency.py`に集約し、切り替えや管理を容易にします。

#### 3. **インターフェースと実装クラスの命名規則**
   - インターフェースは`I`で始まるクラス名を使用し、実装クラスは`Impl`で終わるクラス名を使用します。
   - 例えば、`IUserRepository`がインターフェースで、その実装は`UserRepositoryImpl`とします。

#### 4. **リポジトリ層のインターフェース化**
   - `Repository`層は、データベース操作を抽象化し、インターフェース(`IUserRepository`)を通じて操作します。
   - インターフェースを使用することで、データベースのバックエンドを変更する際、リポジトリの実装を差し替えるだけで対応可能です。

#### 5. **ジェネリック型を用いたリポジトリの実装**
   - `Repository`インターフェースはジェネリック型を用いて、扱うエンティティの型を柔軟に指定できるようにします。
   - これにより、型安全性を保ちながら、異なるデータベースのエンティティを扱うことができます。

#### 6. **エンティティ定義のデータベース分離**
   - エンティティは、データベース固有の構造や特性に依存するため、データベースごとに個別のフォルダに定義します。
   - 各データベース用のエンティティは、`Models/Mongo/User.py`や`Models/Postgres/User.py`のように別フォルダに配置します。

#### 7. **インポートの切り替えによる柔軟なデータベース対応**
   - `Models/__init__.py`を利用して、使用するデータベースのエンティティを簡単に切り替えられるようにします。
   - これにより、他のコード（`Repository`, `Service`など）は特定のデータベースに依存せずに開発できます。

#### 8. **命名規則の統一**
   - クラス名とファイル名を一致させ、ファイル名をクラス名と同様にキャメルケースで命名します。例えば、`UserRepositoryImpl.py`のようにします。
   - これにより、ファイル名とクラス名が一致し、特にPythonに不慣れな開発者にとっても読みやすくなります。

### MongoDBに基づく設計例

#### 1. プロジェクト構成
```plaintext
Project/
│
├── Models/
│   ├── Mongo/
│   │   └── User.py  # MongoDB用のUserエンティティ
│   ├── Postgres/
│   │   └── User.py  # PostgreSQL用のUserエンティティ（将来的な切り替え用）
│   └── __init__.py  # データベースに応じたエンティティのインポート
│
├── Repositories/
│   └── UserRepositoryImpl.py  # リポジトリクラスの実装
│
├── Services/
│   └── UserService.py  # サービスクラス
│
├── Dependency.py  # 依存性注入の設定
└── Main.py  # アプリケーションエントリーポイント
```

#### 2. MongoDB用のエンティティ定義（`Models/Mongo/User.py`）
```python
from beanie import Document

class User(Document):
    name: str
    email: str
```
#### 3. リポジトリインターフェース（Repositories/IUserRepository.py）
```python
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class IUserRepository(ABC, Generic[T]):
    @abstractmethod
    async def get_user_by_email(self, email: str) -> T:
        pass

    @abstractmethod
    async def create_user(self, user_data: dict) -> T:
        pass
```
#### 4. MongoDB用のリポジトリ実装（Repositories/UserRepositoryImpl.py）
```python
from Models.User import User
from Repositories.IUserRepository import IUserRepository

class UserRepositoryImpl(IUserRepository[User]):
    async def get_user_by_email(self, email: str) -> User:
        return await User.find_one(User.email == email)

    async def create_user(self, user_data: dict) -> User:
        user = User(**user_data)
        await user.insert()
        return user
```
#### 5. 依存性注入の設定（Dependency.py）
```python
from Repositories.UserRepositoryImpl import UserRepositoryImpl
from Services.UserService import UserService

def get_user_repository() -> UserRepositoryImpl:
    return UserRepositoryImpl()

def get_user_service(user_repository: UserRepositoryImpl = Depends(get_user_repository)) -> UserService:
    return UserService(user_repository)

```
#### 6. インポートの切り替え（Models/__init__.py）
MongoDBを使用する場合:
```python
from .Mongo.User import User
```
将来的にPostgreSQLに変更する場合は、PostgresディレクトリのUser.pyをインポートするだけで対応できます。
