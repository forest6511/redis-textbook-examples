// go-redis で Redis に接続する最小例。
package main

import (
	"context"
	"fmt"

	"github.com/redis/go-redis/v9"
)

func main() {
	ctx := context.Background()

	// Password が空文字なら認証なしで接続する
	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "",
		DB:       0,
	})

	res, err := rdb.Set(ctx, "user:1:name", "alice", 0).Result()
	if err != nil {
		panic(err)
	}
	fmt.Println(res) // >>> OK

	val, err := rdb.Get(ctx, "user:1:name").Result()
	if err != nil {
		panic(err)
	}
	fmt.Println(val) // >>> alice
}
