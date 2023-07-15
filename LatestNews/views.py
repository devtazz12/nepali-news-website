from django.shortcuts import render
import requests
import datetime
import nepali_datetime
import pandas as pd
import csv
from .models import politicalNews, topheadlines, sportsNews, worldNews, monoranjan, Item

from .models import upatiyaka, bichar, bigyanPrabidhi


def index(request):
    politicalnews=politicalNews.objects.all()
    topHeadlines=topheadlines.objects.all()
    sportnews= sportsNews.objects.all()
    worldnews = worldNews.objects.all()
    Monoranjan = monoranjan.objects.all()
    items = Item.objects.all()
    Upatiyaka = upatiyaka.objects.all()
    Bichar = bichar.objects.all()
    bigyanprabidhi = bigyanPrabidhi.objects.all()
    
    current_datetime = nepali_datetime.datetime.now().strftime('%d %B %Y %H:%M')
    context = { 'current_datetime': current_datetime,
                'politicalnews' : politicalnews,
                'topHeadlines' : topHeadlines,
                'sportnews' : sportnews,
                'worldnews' :worldnews,
                'Monoranjan' : Monoranjan,
                'items':items,
                'Upatiyaka' :Upatiyaka,
                'Bichar' : Bichar,
                'bigyanprabidhi' : bigyanprabidhi,
               }
     
    
    return render(request, 'index.html', context)
