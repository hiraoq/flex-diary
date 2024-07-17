# ベースイメージとしてAmazon Corretto 21を使用
FROM amazoncorretto:21 AS builder
WORKDIR /app
COPY . .
# Gradleを使用してプロジェクトをビルド
RUN ./gradlew build --no-daemon

# 実行環境としてAmazon Corretto 21を使用
FROM amazoncorretto:21
WORKDIR /app
# ビルド成果物をコピー
COPY --from=builder /app/build/libs/*.jar app.jar
# アプリケーションを実行
ENTRYPOINT ["java", "-jar", "app.jar"]

