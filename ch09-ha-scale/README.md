# ch09-ha-scale — 高可用性とスケール

『Redis の教科書』第9章のサンプルです。レプリケーション・Sentinel・Cluster の 3 構成を用意しています。すべて Redis 8.8（`redis:8-alpine`）です。

## レプリケーション

```bash
cd replication
docker compose up -d
redis-cli < ../examples/replication.redis   # INFO replication / WAIT
docker compose down
```

マスター 1 + レプリカ 1。レプリカは既定で read-only。`WAIT` で書き込みのレプリカ伝播を待てます。

## Sentinel（自動フェイルオーバー）

```bash
cd sentinel
docker compose up -d
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster
docker compose down
```

Sentinel がマスターを監視し、down を検知したらレプリカを昇格します。`sentinel.conf` の `resolve-hostnames yes` は Docker のコンテナ名解決のために必要です。

## Cluster（水平スケール）

```bash
cd cluster
docker compose up -d
bash create-cluster.sh                        # 3 マスター + 3 レプリカを構成
redis-cli -c -p 7001 < ../examples/cluster-keys.redis
docker compose down
```

16,384 のハッシュスロットを CRC16 で 3 マスターに分散します。`{...}` のハッシュタグで、関連キーを同じスロットに集められます（`MSET` のマルチキー操作に必要）。`redis-cli -c` の `-c` はクラスタモードでのリダイレクト追従です。

> 本書本文の出力値は、これらの構成を実機（Docker）で起動して取得しています。
