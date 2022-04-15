#!/bin/sh

name=$1
proto=$2
thread=$3

echo "name = $name, proto = $proto, thread = $thread"
mkdir -p $proto
docker stats --format \
"table {{.CPUPerc}}\t{{.MemUsage}}" \
>> "${proto}/${name}_${proto}_${thread}_thread_cpu_mem.txt"
