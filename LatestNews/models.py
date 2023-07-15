from django.db import models

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(default=None, null=True)
    image_url = models.URLField(max_length=2000, null=True)
    link = models.URLField(max_length=2000)

    def __str__(self):
        return self.title
    
    
class sportsNews(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(default=None, null=True)
    image_url = models.URLField(max_length=2000, null=True)
    link = models.URLField(max_length=2000)

    def __str__(self):
        return self.title
    
class politicalNews(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(default=None, null=True)
    image_url = models.URLField(max_length=2000, null=True)
    link = models.URLField(max_length=2000)

    def __str__(self):
        return self.title
class upatiyaka(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(default=None, null=True)
    image_url = models.URLField(max_length=2000, null=True)
    link = models.URLField(max_length=2000)

    def __str__(self):
        return self.title
    
class worldNews(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(default=None, null=True)
    image_url = models.URLField(max_length=2000, null=True)
    link = models.URLField(max_length=2000)

    def __str__(self):
        return self.title
    
    
class monoranjan(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(default=None, null=True)
    image_url = models.URLField(max_length=2000, null=True)
    link = models.URLField(max_length=2000)

    def __str__(self):
        return self.title
    
class bigyanPrabidhi(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(default=None, null=True)
    image_url = models.URLField(max_length=2000, null=True)
    link = models.URLField(max_length=2000)

    def __str__(self):
        return self.title
    
class bichar(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField( default=None, null=True)
    image_url = models.URLField(max_length=2000, null=True)
    link = models.URLField(max_length=2000)

    def __str__(self):
        return self.title
    
    
class topheadlines(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(default=None, null=True)
    image_url = models.URLField(max_length=2000, null=True)
    link = models.URLField(max_length=2000)

    def __str__(self):
        return self.title

