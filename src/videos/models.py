from django.db import models

# Create your models here.

class Video(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True ,null=True)
    slug=models.SlugField(blank=True,null=True)
    video_id=models.CharField(max_length=200)


    #timestamp
    #updated
     #state
    #publish_timestamp

class VideoProxy(Video):
    class Meta:
        proxy=True