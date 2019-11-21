import feedparser as fp
from .models import News
def get_news():
    
    URL = 'https://news.google.com/rss/search?pz=1&cf=all&q=nse$&hl=en-IN&gl=IN&ceid=IN:en'
    
    feed = fp.parse(URL)
    print("i Called")
    for post in feed.entries:
        # print(post.title)
        # print(post.keys())
        title  = post.title
        link = post.link
        nid = post.id
        published = post.published
        summary = post.summary
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
          
       
        
        check_exist = News.objects.filter(nid=post.id)
        if check_exist:
            # print("already exist ") 
            pass
        else:
            news_instance = News.objects.create(title=title,link=link,nid=nid,published=published,summary=summary)
    