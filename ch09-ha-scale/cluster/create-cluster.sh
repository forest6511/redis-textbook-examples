#!/usr/bin/env bash
set -euo pipefail

# 6 ノード起動後にクラスタを作成する。--cluster-replicas 1 で
# 各マスターにレプリカ 1 台を割り当てる（3 マスター + 3 レプリカ）。
# host.docker.internal でホスト経由の到達アドレスを使う。

redis-cli --cluster create \
  127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 \
  127.0.0.1:7004 127.0.0.1:7005 127.0.0.1:7006 \
  --cluster-replicas 1 \
  --cluster-yes

# 確認
redis-cli -p 7001 CLUSTER INFO
redis-cli -p 7001 CLUSTER NODES
