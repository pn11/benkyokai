#!/bin/bash

for v in "0.6" "0.7" "1.0"
do
    docker run -it --rm -v `pwd -P`:/data julia:$v bash -c "cd /data; julia compare.jl"
done



