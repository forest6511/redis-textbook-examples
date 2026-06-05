# ch12-managed — マネージドRedisと選定

『Redis の教科書』第12章のサンプルです。

この章はマネージドサービス（ElastiCache / Memorystore / Upstash / Momento）の選定が中心で、実機検証の対象ではありません。料金・対応バージョンは各社公式ドキュメントを一次ソースにしています。

実行できるのは、セルフホストからの移行用スクリプトのみです。

## セルフホストから RDB をダンプ

```bash
bash scripts/dump-rdb.sh old-redis.example.com 6379
# -> dump.rdb を取得。移行先マネージドの import 機能で読み込ませる
```

`redis-cli --rdb` で対象 Redis の RDB スナップショットを取得します（第8章の RDB を移行に使う形）。取得後の取り込み方法は移行先サービスごとに異なります（多くは S3 等に置いてインポート）。
