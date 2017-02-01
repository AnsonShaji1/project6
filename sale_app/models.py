from django.db import models
from django.contrib.auth.models import User
import os 

def upload_location(instance,filename):
    return "%s/%s" %(instance.id,filename)


class Post(models.Model):
    author=models.ForeignKey(User)
    title=models.CharField(max_length=2000)
    image=models.ImageField(upload_to=upload_location,null=True,blank=True,width_field="width_field",height_field="height_field")
    height_field=models.IntegerField(default=0)
    width_field=models.IntegerField(default=0)
    text=models.TextField(max_length=100000)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.title




