#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install build-essential tcl8.5
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make

