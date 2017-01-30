from django.db import models
from django.contrib.auth.models import User
import os 


class Post(models.Model):
    author=models.ForeignKey(User)
    title=models.CharField(max_length=2000)
    image=models.FileField(null=True,blank=True)
    text=models.TextField(max_length=100000)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.title




