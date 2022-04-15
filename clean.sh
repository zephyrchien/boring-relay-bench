#!/bin/sh

name=$1
proto=$2
thread=$3

echo "name = $name, proto = $proto, thread = $thread"

sed -i '/CPU/d' "${proto}/${name}_${proto}_${thread}_thread_cpu_mem.txt"
sed -i '/172.17.0.2/d' "${proto}/${name}_${proto}_${thread}_thread_iperf.txt"
