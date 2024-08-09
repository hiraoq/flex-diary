# ベースイメージとしてAmazon Corretto 21を使用
FROM amazoncorretto:21 AS builder
WORKDIR /app
COPY . .
# gradlew に実行権限を付与する
RUN chmod +x ./gradlew
# Gradleを使用してプロジェクトをビルド
RUN ./gradlew build --no-daemon -x test

# 本番用のステージ
FROM amazoncorretto:21 AS production
WORKDIR /app
COPY --from=builder /app/build/libs/app.jar /app/app.jar
ENTRYPOINT ["java", "-jar", "/app/app.jar"]

# 開発用のステージ
FROM amazoncorretto:21 AS development
WORKDIR /app
COPY . .
# entrypoint.shをコピーして実行権限を付与
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
# Gradleキャッシュディレクトリを指定
ENV GRADLE_USER_HOME=/app/.gradle
# ホットリロード等を有効に
ENV SPRING_PROFILES_ACTIVE=dev
# 実行時にトリガーしたい処理
ENTRYPOINT ["./gradlew", "bootRun"]