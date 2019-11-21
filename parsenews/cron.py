import datetime
import logging
import time
from django.conf import settings
from django.utils import formats, timezone
from django_cron import CronJobBase, Schedule
from .functions import get_news



class NewsUpdateJob(CronJobBase):
    RUN_EVERY_MINS = 5 

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'parsenews.NewsUpdateJob' 
    
    def do(self):
        print("I Run")    
        save = get_news()
        return save    
