apt -y update
apt -y install python3-pip tmux supervisor
apt -y update

pip3 install celery flower virtualenv

# supervisor configuration

mkdir /var/log/celery
mv celery.conf /etc/supervisor/conf.d/celery.conf
