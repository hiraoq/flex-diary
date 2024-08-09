#!/bin/bash

# gradlewスクリプトの権限を変更(バインドマウントのため実行時に変更する必要がある)
chmod +x /app/gradlew

# 指定されたコマンドを実行
exec "$@"
