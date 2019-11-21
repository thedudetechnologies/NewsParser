from NewsParser.celery import app
from .models import *
from .functions import get_news   
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
import os
from celery import Celery
from celery import task  



# os.environ[ 'DJANGO_SETTINGS_MODULE' ] = "NewsParser.settings"

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*')),
    name="update_news",
    ignore_result=True
)
def update_db():

    get_news()
    logger.info("News Update")
