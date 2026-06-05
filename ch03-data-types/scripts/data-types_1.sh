#!/usr/bin/env bash
set -euo pipefail

redis-cli EVAL "redis.call('SET', KEYS[1], ARGV[1]) \
return redis.call('GET', KEYS[1])" 1 mykey hello
