# ベースイメージ
FROM node:16-alpine AS base

# 共通の作業ディレクトリを設定
WORKDIR /app

# 依存関係のインストール
COPY package.json package-lock.json ./
RUN npm install

# アプリケーションのソースコードをコピー
COPY . .

# -------------------------------------------
# ステージ1: 開発用ビルド
# -------------------------------------------
FROM base AS development

RUN chown -R node:node /app
# ホットリロードなど開発用のコマンドを実行
CMD ["npm", "run", "dev"]

# -------------------------------------------
# ステージ2: 本番用ビルド
# -------------------------------------------
FROM base AS build

# 本番用にアプリケーションをビルド
RUN npm run build

# Nginxを使用して本番環境をセットアップ
FROM nginx:alpine AS production

# ビルド成果物をnginxの静的ファイルサービングディレクトリにコピー
COPY --from=build /app/dist /usr/share/nginx/html

# nginxの設定ファイルをコピー
COPY nginx.conf /etc/nginx/nginx.conf

# ポート80をエクスポーズ
EXPOSE 80

# コンテナ起動時にnginxを実行
CMD ["nginx", "-g", "daemon off;"]

