from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class TwitterUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    followers = models.ManyToManyField("self",symmetrical=False,blank=True)
    displayname = models.CharField(max_length=140,null=True,blank=True)
    

