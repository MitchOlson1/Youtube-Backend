from django.db import models

# Create your models here.

class Comment(models.Model):
    video_id = models.CharField(blank = True, null = True, max_length = 50)
    comment =  models.CharField(blank = True, null = True, max_length = 200)
    likes = models.IntegerField(null = 0)
    dislikes = models.BigIntegerField(null = 0)


class Reply(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE, blank = True, null = True)
    reply = models.CharField(blank = True, null = True, max_length = 200)