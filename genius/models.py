from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    lyrics = models.TextField()