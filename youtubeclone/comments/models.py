from django.db import models

# Create your models here.

class Comment(models.Model):
    video_id = models.CharField(blank = True, null = True, max_length = 50)
    comment =  models.CharField(blank = True, null = True, max_length = 200)
    title = models.CharField(blank = True, null = True, max_length = 200)
    description = models.CharField(blank = True, null = True, max_length = 200)
    replies = models.CharField(blank = True, null = True, max_length = 200)
    likes = models.BigIntegerField()
    dislikes = models.BigIntegerField()


class Reply(models.Model):
