#!/bin/bash

export APOLLO_ROOT=/home/ronghang/workspace/apollocaffe
export LD_LIBRARY_PATH=/usr/local/cuda-7.0/lib64:$LD_LIBRARY_PATH:$APOLLO_ROOT/build/lib
export PYTHONPATH=$PYTHONPATH:$APOLLO_ROOT/python:$APOLLO_ROOT/python/caffe/proto

python main.py -c config/vqa_nmn.yml
#python main.py -c config/geo_nmn.yml
