import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
import djcelery


 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsParser.settings')
 
app = Celery('NewsParser')
app.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
 
app.conf.beat_schedule = {
    'parsenews.cron.NewsUpdateJob': {
        'task': '.tasks.update_news',
        'schedule': crontab(minute='*/5'),
    },
}