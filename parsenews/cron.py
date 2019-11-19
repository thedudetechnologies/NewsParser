import datetime
import logging
import pytz
import requests
import time
from django.conf import settings
from django.utils import formats, timezone
from django_cron import CronJobBase, Schedule



class NewsUpdateJob(CronJobBase):
    RUN_EVERY_MINS = 5 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'parsenews.NewsUpdateJob' 
    def news_update():
        URL = 'https://news.google.com/rss/search?pz=1&cf=all&q=nse$&hl=en-IN&gl=IN&ceid=IN:en' 

        feed = fp.parse(URL)
        try:
            for post in feed.entries:
                # print(post.title)
                # print(post.keys())
                title  = post.title
                link = post.link
                nid = post.id
                published = post.published
                summary = post.summary
                print("I Run")
                news_instance = News.objects.create(title=title,link=link,nid=nid,published=published,summary=summary) 
        except expression as e:
            print("Data Not Update",e)
            
