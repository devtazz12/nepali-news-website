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

def get_model_from_file_name(file_name):
    # Define the mapping between file names and models
    model_mapping = {
        'politicalnews.csv': politicalNews,
        'topheadlines.csv': topheadlines,
        'sportnews.csv': sportsNews,
        'worldnews.csv': worldNews,
        'upatiyakas.csv': upatiyaka,
        'bigyanprabidhis.csv': bigyanPrabidhi,
        'bichars.csv': bichar,
        'lokpriyas.csv': Item,
        'monoranjans.csv': monoranjan,
    }

    # Get the corresponding model based on the file name
    return model_mapping.get(file_name, None)


def cvstodatabase(csv_file):
    model = get_model_from_file_name(csv_file.name)
    if model == politicalNews:
        politicalNews.objects.all().delete()
    elif model == topheadlines:
        topheadlines.objects.all().delete()
    elif model == sportsNews:
        sportsNews.objects.all().delete()
    elif model == monoranjan:
        monoranjan.objects.all().delete()
    elif model == upatiyaka:
        upatiyaka.objects.all().delete()
    elif model == bigyanPrabidhi:
        bigyanPrabidhi.objects.all().delete()
    elif model == bichar:
        bichar.objects.all().delete()
    elif model == worldNews:
        worldNews.objects.all().delete()
    elif model == Item:
        Item.objects.all().delete()
        
    
    with open('static/media/' + csv_file.name, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            # Assuming the CSV file has two columns: 'name' and 'email'
            title = row[0]
            link = row[1]
            description = row[2]
            image_url = row[3]
            
            # Create a new CSVData object and save it to the database
            if model == politicalNews:
                csv_data = politicalNews(title=title, description=description, image_url=image_url, link=link)
                csv_data.save()
            elif model == topheadlines:
                csv_data = topheadlines(title=title, description=description, image_url=image_url, link=link)
                csv_data.save()
            elif model == sportsNews:
                csv_data = sportsNews(title=title, description=description, image_url=image_url, link=link)
                csv_data.save()
            elif model == monoranjan:
                csv_data = monoranjan(title=title, description=description, image_url=image_url, link=link)
                csv_data.save()
            elif model == bichar:
                csv_data = bichar(title=title, description=description, image_url=image_url, link=link)
                csv_data.save()
            elif model == bigyanPrabidhi:
                csv_data = bigyanPrabidhi(title=title, description=description, image_url=image_url, link=link)
                csv_data.save()
            elif model == worldNews:
                csv_data = worldNews(title=title, description=description, image_url=image_url, link=link)
                csv_data.save()
            elif model == Item:
                csv_data = Item(title=title, description=description, image_url=image_url, link=link)
                csv_data.save()
            elif model == upatiyaka:
                csv_data = upatiyaka(title=title, description=description, image_url=image_url, link=link)
                csv_data.save()

                    

def files(request):
    if request.method == 'POST' and request.FILES['csvFile']:
        csv_file = request.FILES['csvFile']
        # Process the CSV file here (e.g., save it, read data, etc.)
        # Replace this with your actual file processing logic
        # Example: Save the file in the 'media' directory
        with open('static/media/' + csv_file.name, 'wb') as file:
            for chunk in csv_file.chunks():
                file.write(chunk)
                
        cvstodatabase(csv_file)
    
    return render(request, 'fileUpload.html')


