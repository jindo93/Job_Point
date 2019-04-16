#!/usr/bin/env bash

apt-get -y update
wget -O- https://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc | sudo apt-key add -
echo "deb https://packages.erlang-solutions.com/ubuntu bionic contrib" | sudo tee /etc/apt/sources.list.d/rabbitmq.list
apt-get -y update
apt-get -y install erlang
# check if both are necessary
wget -O- https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc | sudo apt-key add -
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -

echo "deb https://dl.bintray.com/rabbitmq/debian $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/rabbitmq.list

apt-get -y update
apt-get -y install rabbitmq-server
rabbitmq-plugins enable rabbitmq_management
echo "use http://IPADDRESS:15672 for rabbitmq browser"
echo "set password by running: rabbitmqctl add_user _myuser _mypassword"
echo "set user role by running: rabbitmqctl set_user_tags _myuser administrator"
echo 'set permission by running: rabbitmqctl set_permissions -p <myvhost> <myuser> ".*" ".*" ".*"'


##### Notes #####
### setup:
# sudo rabbitmqctl add_user myuser mypassword
# rabbitmqctl add_vhost myvhost
# sudo rabbitmqctl set_user_tags myuser mytag
# sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"


### start the server:
# sudo rabbitmq-server

### run the server in background:
# sudo rabbitmq-server -detached

### stop server:
# sudo rabbitmqctl stop

