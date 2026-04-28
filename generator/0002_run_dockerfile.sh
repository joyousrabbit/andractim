#!/bin/bash

image="python"
tag="andractim"
name="python_andractim"

nvidia-docker run -it --rm\
    --ipc=host \
    --net=host \
    --volume="$PWD:/root:rw"\
    --name=$name\
    --privileged=True \
    $image:$tag
