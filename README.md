# Flex Diary UI

## 概要
「Flex Diary UI」はシンプルな日記アプリケーションです。このアプリケーションはユーザーが日々の出来事を記録し、管理するためのツールです。Vite、React、Redux、React Hook Form、TypeScript、MUIを使用して構築されます。また、テストにはVitestを使用します。

## 機能
1. **ユーザー登録**
   - 新規ユーザー登録
   - ログイン/ログアウト機能

2. **日記管理**
   - 新しい日記の作成
   - 既存の日記の閲覧、編集、削除
   - 日記の一覧表示

3. **UI/UX**
   - MUIを使用したモダンなデザイン
   - レスポンシブデザイン対応

4. **フォームバリデーション**
   - React Hook Formを使用したフォームの入力チェック

## 使用技術
- **Vite**: フロントエンドビルドツール
- **React**: UIライブラリ
- **Redux**: 状態管理
- **React Hook Form**: フォーム管理ライブラリ
- **TypeScript**: 型付けJavaScript
- **MUI (Material-UI)**: デザインコンポーネントライブラリ
- **Vitest**: テストフレームワーク

## ディレクトリ構成
\`\`\`
flex-diary-ui/
├── public/
├── src/
│   ├── components/
│   │   ├── DiaryEntry.tsx
│   │   ├── DiaryList.tsx
│   │   └── UserForm.tsx
│   ├── features/
│   │   ├── diary/
│   │   │   ├── diarySlice.ts
│   │   │   ├── DiaryForm.tsx
│   │   │   └── DiaryItem.tsx
│   │   ├── user/
│   │   │   ├── userSlice.ts
│   │   │   └── UserAuth.tsx
│   ├── hooks/
│   ├── App.tsx
│   ├── main.tsx
│   ├── store.ts
│   └── types/
├── tests/
│   ├── diary.test.ts
│   └── user.test.ts
├── .eslintrc.js
├── .prettierrc
├── index.html
└── package.json
\`\`\`

## インストールとセットアップ
1. プロジェクトを作成します。
   \`\`\`sh
   npx degit reduxjs/redux-templates/packages/vite-template-redux flex-diary-ui
   cd flex-diary-ui
   \`\`\`

2. 必要なパッケージをインストールします。
   \`\`\`sh
   npm install @mui/material @emotion/react @emotion/styled
   npm install react-hook-form
   npm install vitest --save-dev
   \`\`\`

3. プロジェクトを起動します。
   \`\`\`sh
   npm run dev
   \`\`\`

## テスト
Vitestを使用してテストを実行します。
\`\`\`sh
npm run test
\`\`\`

## 仕様詳細

### ユーザー登録
- **機能**: 新規ユーザー登録、ログイン、ログアウト
- **フォーム**: ユーザーネーム、パスワード
- **バリデーション**: 必須項目チェック、パスワードの強度チェック

### 日記管理
- **機能**: 日記の作成、編集、削除、閲覧
- **フォーム**: タイトル、本文、日付
- **バリデーション**: 必須項目チェック、本文の最大文字数チェック

### UI/UX
- **デザイン**: MUIを使用した直感的なインターフェース
- **レスポンシブ**: モバイルファーストのデザイン

### フォームバリデーション
- **React Hook Form**を使用して、ユーザー入力を効率的に管理
- **バリデーションロジック**をカスタマイズして、ユーザーエクスペリエンスを向上

## 開発者向け情報
### コーディングスタイル !!TODO:導入!!
- **ESLint**と**Prettier**を使用して一貫したコーディングスタイルを維持

### 環境設定 !!TODO:確認!!
- **Node.js**バージョン: 14.x 以上
- **TypeScript**バージョン: 4.x 以上

## コントリビューション
バグ報告や機能提案は、Issueを通じて行ってください。プルリクエストも歓迎します。

---

このREADMEはflex-diary-uiプロジェクトの初期設定および開発ガイドラインを提供します。アプリケーションの各コンポーネントや機能の詳細については、プロジェクトディレクトリ内の各ファイルを参照してください。

---

# vite-template-redux

Uses [Vite](https://vitejs.dev/), [Vitest](https://vitest.dev/), and [React Testing Library](https://github.com/testing-library/react-testing-library) to create a modern [React](https://react.dev/) app compatible with [Create React App](https://create-react-app.dev/)

```sh
npx degit reduxjs/redux-templates/packages/vite-template-redux my-app
```

## Goals

- Easy migration from Create React App or Vite
- As beginner friendly as Create React App
- Optimized performance compared to Create React App
- Customizable without ejecting

## Scripts

- `dev`/`start` - start dev server and open browser
- `build` - build for production
- `preview` - locally preview production build
- `test` - launch test runner

## Inspiration

- [Create React App](https://github.com/facebook/create-react-app/tree/main/packages/cra-template)
- [Vite](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react)
- [Vitest](https://github.com/vitest-dev/vitest/tree/main/examples/react-testing-lib)