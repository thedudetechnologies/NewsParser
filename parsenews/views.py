from django.shortcuts import render
import feedparser as fp
import json
from time import mktime
from datetime import datetime
import requests 
from .models import *

# Create your views here.
def home(request):
    
    URL = 'https://news.google.com/rss/search?pz=1&cf=all&q=nse$&hl=en-IN&gl=IN&ceid=IN:en' 

    feed = fp.parse(URL)
    newsdb = News.objects.all()

    viewdict = dict()
    for post in feed.entries:
        # print(post.title)
        # print(post.keys())
        
            
        title  = post.title
        link = post.link
        nid = post.id
        published = post.published
        summary = post.summary
        # lst = [title,link,nid,published,summary]
        
        # news_instance = News.objects.create(title=title,link=link,nid=nid,published=published,summary=summary)
        viewdict = {
            'news' : newsdb
        }
        
        # print("---------> News Details <----------- ")
        # print("Title :",post.title)
        # print("title_detail:", post.title_detail)
        # print("links : ",post.links)
        # print("link : ",post.link)
        # print("id",post.id)
        # print("guidislink",post.guidislink)
        # print("published :",post.published)
        # print("published_parsed:", post.published_parsed)
        # print("summary : ",post.summary.text())
        # print("----------->summary_detail: ",post.summary_detail)
        # print("source",post.source)
          
       

    
    return render(request,'newsbox/index.html',viewdict)
    