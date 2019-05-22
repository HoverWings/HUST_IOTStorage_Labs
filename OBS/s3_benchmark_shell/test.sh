#!/bin.bash



 ~/go/bin/s3-benchmark -a 4VFY6G1OGS0VU5ELE6FL -s e4fWg5uC9BSfrrL6zmuWV4x42MQpPtPjW2Isq3gW -u http://127.0.0.1:9000 -b wasabi-benchmark \
    -d 3 -t 1 -z 1K | tail -1 > qwe.csv
