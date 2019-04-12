# Start celery worker

celery -A proj worker --loglevel=info

# Shutdown running celery process

celery -A proj control shutdown

# View running celery processes

ps aux|grep 'celery worker'

# Kill running celery processes

sudo kill -9 id1 id2 id3 ...

# or

pkill -f "celery worker"

# View active workers

python3
from celery import Celery
celery = Celery('proj',
broker='',
backend='')
celery.control.inspect().active()
