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
# gradlew に実行権限を付与する
RUN chmod +x ./gradlew
ENV SPRING_PROFILES_ACTIVE=dev
ENV GRADLE_OPTS="-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005"
ENTRYPOINT ["./gradlew", "bootRun"]