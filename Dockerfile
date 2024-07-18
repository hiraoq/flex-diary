# ベースイメージとしてAmazon Corretto 21を使用
FROM amazoncorretto:21 AS builder
WORKDIR /app
COPY . .
# gradlew に実行権限を付与する
RUN chmod +x ./gradlew
# Gradleを使用してプロジェクトをビルド
RUN ./gradlew build --no-daemon -x test

# 実行環境としてAmazon Corretto 21を使用
FROM amazoncorretto:21
WORKDIR /app
# ビルド成果物をコピー
COPY --from=builder /app/build/libs/*.jar /app/
# アプリケーションを実行
ENTRYPOINT ["java", "-jar", "/app/app.jar"]
