from django.db import models

# Create your models here.

class Comment(models.Model):
    video_id = models.CharField(blank=True, null= True, max_length=50)
    comment =  models.CharField(blank=True, null= True, max_length=50)

class Reply(models.Model):
