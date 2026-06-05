#!/usr/bin/env bash
set -euo pipefail

# セルフホストの Redis から RDB スナップショットを取得し、
# マネージドへの移行用に dump.rdb として保存する（本書第12章）。
# 取得した RDB は、移行先サービスの import 機能で読み込ませる。

OLD_HOST="${1:-old-redis.example.com}"
OLD_PORT="${2:-6379}"

redis-cli -h "$OLD_HOST" -p "$OLD_PORT" --rdb dump.rdb

echo "saved: dump.rdb (from ${OLD_HOST}:${OLD_PORT})"
