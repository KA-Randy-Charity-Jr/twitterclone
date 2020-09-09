from django.shortcuts import render
from tweet.form import TweetForm
from tweet.models import Tweet
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from notification.models import Notification
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
import re
# Create your views here.

@login_required
def createtweet_view(request):
   
    thecount=0
    form = TweetForm()
    return render(request, "form.html", {"form": form,"count":thecount})
    
class CreateTweet(TemplateView):
    def get(self, request):
        thecount = 0
        if request.user.is_authenticated:
            count = Notification.objects.filter(tagged=request.user, isread=False)
            if count:
                thecount = count.count
        form = TweetForm()
        return render(request, "form.html", {"form": form, "count": thecount})
    def post(self, request):
        if request.method == "POST":
            form = TweetForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                newtweet=Tweet.objects.create(tweet=data.get("text"), user=request.user)
                mentions= re.findall(r"@(\w+)",data.get("text"))
                if mentions:
                    users = TwitterUser.objects.all()
                    for mention in mentions:
                        matchuser = TwitterUser.objects.get(username=mention)
                        if matchuser:
                            Notification.objects.create(
                                tagged=matchuser,
                                tweet=newtweet,
                                isread=False)
            
                return HttpResponseRedirect(reverse("homepage"))
def tweet_view(request, tweet_id):
    thecount = 0
    count = Notification.objects.filter(tagged=request.user, isread=False)
    if count:
        thecount=count.count
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request,"tweet.html",{"tweet":tweet,"count":thecount})


class TweetView(TemplateView):
    def get(self, request, tweet_id):
        thecount = 0
        count = Notification.objects.filter(tagged=request.user, isread=False)
        if count:
            thecount=count.count
        tweet = Tweet.objects.get(id=tweet_id)
        return render(request,"tweet.html",{"tweet":tweet,"count":thecount})
                