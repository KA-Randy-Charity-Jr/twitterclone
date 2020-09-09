from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from twitteruser.forms import LoginForm,SignupForm
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification
from django.views.generic import TemplateView
# Create your views here.




def user_view(request, username):
    
    followers=TwitterUser.objects.filter(followers=TwitterUser.objects.get(username=username))
    thecount = 0
    if request.user.is_authenticated:
        count = Notification.objects.filter(tagged=request.user, isread=False)
        if count:
            thecount=count.count
    isfollow = False
    user = TwitterUser.objects.get(username=username)
    tweets=Tweet.objects.filter(user=user).order_by("-id")
    if TwitterUser.objects.filter(username=username,followers=request.user):
        isfollow = True
    return render(request, "user.html", {"user": user, "isfollow": isfollow, "tweets": tweets, "count": thecount, "followers": followers})

class UserView(TemplateView):
    def get(self,request, username):
        followers=TwitterUser.objects.filter(followers=TwitterUser.objects.get(username=username))
        thecount = 0
        if request.user.is_authenticated:
            count = Notification.objects.filter(tagged=request.user, isread=False)
            if count:
                thecount=count.count
        isfollow = False
        user = TwitterUser.objects.get(username=username)
        tweets=Tweet.objects.filter(user=user).order_by("-id")
        if TwitterUser.objects.filter(username=username,followers=request.user):
            isfollow = True
        return render(request, "user.html", {"user": user, "isfollow": isfollow, "tweets": tweets, "count": thecount, "followers": followers})
    
def follow_view(request, username):
    user = TwitterUser.objects.get(username=username)
    user.followers.add(request.user)
    user.save()
    return HttpResponseRedirect(f"/user/{username}")
def unfollow_view(request, username):
    user = TwitterUser.objects.get(username=username)
    user.followers.remove(request.user)
    user.save()
    return HttpResponseRedirect(f"/user/{username}")
    



    