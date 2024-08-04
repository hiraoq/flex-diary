# ステージ1: ビルドステージ
FROM node:16-alpine AS build

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係のインストール
COPY package.json package-lock.json ./
RUN npm install

# アプリケーションのソースコードをコピー
COPY . .

# アプリケーションをビルド
RUN npm run build

# ステージ2: 実行ステージ
FROM nginx:alpine

# ビルド成果物をnginxの静的ファイルサービングディレクトリにコピー
COPY --from=build /app/dist /usr/share/nginx/html

# nginxの設定ファイルを上書き（必要に応じて）
# COPY nginx.conf /etc/nginx/nginx.conf

# ポート80をエクスポーズ
EXPOSE 80

# コンテナ起動時にnginxを実行
CMD ["nginx", "-g", "daemon off;"]
