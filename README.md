
# FlexDiary 仕様書

## 概要
FlexDiaryは、テンプレートに従って日記を記録できるウェブアプリケーションです。ユーザーは、事前に定義されたテンプレートを使用して、日々の活動や感情を記録することができます。このアプリケーションは、ユーザーが毎日の日記をテンプレートにしたがって速やかにストレスなく書くことと、後からデータを見返して分析できるようにすることを目的としています。

## 主要機能

### 1. 日記の記録
- **テンプレートによる日記作成:**
  - 毎日、同じテンプレートに基づいて日記を記録します。
  - テンプレートの例:
    - 今日食べたもの
    - 飲んだ薬
    - 勉強したこと
    - 楽しかったこと
    - 摂取カロリー

- **テンプレートのカスタマイズ:**
  - ユーザーはテンプレートに任意の項目を追加したり削除したりしてカスタマイズできます。
  - カスタマイズ可能なフィールドの例:
    - テキストフィールド（自由記述）
    - 数値フィールド（カロリーや時間など）
    - リストフィールド（食べたものリスト）

- **テンプレートのデータ構造:**
  ```json
  {
    "template_id": "unique-template-id",
    "name": "Daily Journal Template",
    "description": "A template for daily journaling",
    "fields": [
      {
        "field_id": "field-1",
        "label": "What did you eat today?",
        "type": "text",
        "required": true
      },
      {
        "field_id": "field-2",
        "label": "How many calories did you consume?",
        "type": "number",
        "required": false
      },
      {
        "field_id": "field-3",
        "label": "What was the highlight of your day?",
        "type": "text",
        "required": true
      }
    ]
  }
  ```

- **日記エントリーのデータ構造:**
  ```json
  {
    "diary_id": "unique-diary-id",
    "template_id": "unique-template-id",
    "date": "2024-08-23",
    "entries": [
      {
        "field_id": "field-1",
        "value": "Pasta and salad"
      },
      {
        "field_id": "field-2",
        "value": 600
      },
      {
        "field_id": "field-3",
        "value": "Meeting with an old friend"
      }
    ],
    "metadata": {
      "mood": "happy",
      "tags": ["food", "friends"],
      "externalData": [
        {
          "service": "GitHub",
          "data": {
            "commits": 3
          }
        }
      ]
    }
  }
  ```

### 2. データの自動取得
- **外部サービスからの行動履歴データ取得:**
  - ユーザーが利用したWebサービスからデータを自動的に日記に追加します。
  - 例:
    - GitHubへのコミット
    - YouTubeで見た動画
    - ChatGPTとのチャット内容
  - これらのデータはAPIを使用して取得し、毎日の日記に自動的に追加されます。

### 3. データの管理と分析
- **日記データの保存と管理:**
  - MongoDBを使用して日記データを保存します。
  - ユーザーごとにデータを管理し、後から検索・分析が可能です。

- **データ分析機能:**
  - ユーザーは日記データをフィルタリングし、特定の期間やキーワードに基づいてデータを分析できます。
  - 分析結果はグラフやチャートで視覚化します。

### 4. ユーザー認証と管理
- **簡易認証:**
  - 基本的な認証機能を提供します。ユーザーは一度ログインすれば、セッションが維持され、再度ログインする必要がありません。

### 5. TODOリスト（予定）
  - TODOリスト機能を追加する予定です。ユーザーは日々のタスクを簡単に管理できます。
  - 将来的に日記とTODOリストの連携を検討しています。

## アーキテクチャ

### 1. バックエンド
- **技術スタック:**
  - フレームワーク: FastAPI
  - データベース: MongoDB
  - 認証: JWT
  - GraphQL: Strawberry

- **データ構造:**
  - ユーザー:
    ```json
    {
      "username": "string",
      "email": "string",
      "role": "string"
    }
    ```

  - 日記:
    ```json
    {
      "title": "string",
      "content": "string",
      "date": "ISODate",
      "metadata": {
        "mood": "string",
        "tags": ["string"],
        "externalData": [
          {
            "service": "string",
            "data": "object"
          }
        ]
      }
    }
    ```

  - テンプレートと日記エントリーの詳細なデータ構造は上記参照。

### 2. フロントエンド
- **技術スタック:**
  - フレームワーク: React
  - UIライブラリ: MUI
  - 開発ツール: Vite

- **GraphQLの統合:**
  - フロントエンドからのデータ取得にはGraphQLを使用します。
  - Apollo ClientなどのGraphQLクライアントを使用して、柔軟かつ効率的なデータアクセスを提供します。

## 開発環境

### 1. 開発ツール
- **Pythonバージョン管理:** asdf
- **依存関係管理:** Poetry
- **コンテナ化:** Docker、Docker Compose

### 2. ディレクトリ構造
```bash
flex-diary/
├── api/
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── poetry.lock
│   ├── app/
│   │   ├── main.py
│   │   ├── schema.py
│   ├── scripts/
│   │   └── import_data.py
│   └── data/
│       ├── users.json
│       └── diaries.json
├── ui/
│   ├── Dockerfile
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
├── docker-compose.yml
└── README.md
```

### 3. 環境構築手順
1. リポジトリをクローン
2. `docker-compose up --build` で環境を起動
3. GraphQLエンドポイント: `http://localhost:8000/graphql` で動作確認

## 運用・拡張

### 1. データスキーマの変更
- **マイグレーション手順:** 
  - データ構造の変更が必要な場合、Pythonスクリプトを使用して既存データを新しい構造に移行します。
  - 運用中のデータのマイグレーションには、データベースバックアップを取得してから段階的に移行を行います。

### 2. カスタム機能の追加
- **外部API連携:** 
  - 新しい外部サービスと連携する場合、対応するAPIエンドポイントを追加し、必要な認証を行います。
  - 必要に応じて、MongoDBに新しいフィールドやコレクションを追加してデータを保存します。

### 3. 未定部分について
- **認証システム:** 現時点でJWTを予定していますが、実装方法や詳細は未定です。
- **TODOリストとの連携:** TODOリスト機能の開発は基本的な日記機能の開発完了後になる予定で、具体的な仕様はまだ決目る必要がありません。今後の仕様決定に応じて、フロントエンドやバックエンドでの実装が進められます。
