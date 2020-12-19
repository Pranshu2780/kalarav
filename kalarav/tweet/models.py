from django.db import models

# Create your models here.

class Tweet(models.Model):
    # id=default value
    content = models.TextField(blank=True,null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)