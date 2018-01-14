from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=15,unique=True,null=False,default="")
    password = models.CharField(max_length=32,null=False,default="")
    nick = models.CharField(max_length=50,null=False,default="")
    photo = models.TextField(null=False,default="")
    signature = models.TextField(null=False,default="")
    sex = models.CharField(max_length=10,default="")
    latitude = models.CharField(max_length=32,default="0")
    longitude = models.CharField(max_length=32,default="0")
    curbind = models.IntegerField(null=False,default=0)
    lastbind = models.TextField(null=False,default="")
    token = models.TextField(null=False,default="")