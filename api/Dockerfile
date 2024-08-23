# ベースイメージ
FROM python:3.12.5-slim AS base

# 作業ディレクトリを設定
WORKDIR /app

# Poetryのインストール
COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# アプリケーションのソースコードをコピー
COPY . .

# -------------------------------------------
# ステージ1: 開発用
# -------------------------------------------
FROM base AS development

# ホットリロードなど開発用のコマンドを実行
CMD ["python", "-Xfrozen_modules=off", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# -------------------------------------------
# ステージ2: 本番用
# -------------------------------------------
FROM base AS production

# 不要な開発依存を削除
RUN poetry install --no-dev --no-interaction --no-ansi

# FastAPIを起動
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
