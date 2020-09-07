from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser

# Create your models here.
class Tweet(models.Model):
    post_date = models.DateTimeField(default=timezone.now)
    tweet = models.CharField(max_length=240)
    user = models.ForeignKey(TwitterUser,on_delete=models.CASCADE,related_name="tweet_user")
    