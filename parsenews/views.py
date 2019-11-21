from django.shortcuts import render
from datetime import datetime

from .models import *


# Create your views here.


def home(request):
    
    newsdb = News.objects.all().order_by('id')

    viewdict = dict()

    viewdict = {
        'news' : newsdb
    }
        


    
    return render(request,'newsbox/index.html',viewdict)
    