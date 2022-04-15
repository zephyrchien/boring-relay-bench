#!/bin/sh

name=$1
proto=$2
thread=$3

echo "name = $name, proto = $proto, thread = $thread"
mkdir -p $proto
iperf3 -c 172.17.0.2 -p 8080 -t 60 -P $thread >> "${proto}/${name}_${proto}_${thread}_thread_iperf.txt"
