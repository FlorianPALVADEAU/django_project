from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=200)
    
    
class Image(models.Model):
    name = models.TextField(max_length=100)
    url = models.TextField(max_length=400)
    stock = models.IntegerField()
    prix = models.IntegerField()
    