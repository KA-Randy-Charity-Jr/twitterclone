from django.shortcuts import render
from tweet.models import Tweet,TwitterUser
from notification.models import Notification
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
@login_required
def index_view(request):
    anumber= 0
    thecount = 0
    if request.user.is_authenticated:
        count = Notification.objects.filter(tagged=request.user, isread=False)
        if count:
            thecount=count.count
    
    myusers={}
    if request.user.is_authenticated:
        myusers= TwitterUser.objects.filter(followers=request.user)
    mytweets = Tweet.objects.all().order_by("-id")
    for tweet in mytweets:
        if  tweet.user in myusers:
            anumber += 1
        elif tweet.user == request.user:
            anumber +=1        

    return render(request, 'index.html', {"tweets": mytweets, "users": myusers, "count": thecount, "anumber": anumber})
 
class IndexView(LoginRequiredMixin,TemplateView):
    def get(self, request):
        anumber= 0
        thecount = 0
        if request.user.is_authenticated:
            count = Notification.objects.filter(tagged=request.user, isread=False)
            if count:
                thecount=count.count
    
        myusers={}
        if request.user.is_authenticated:
            myusers= TwitterUser.objects.filter(followers=request.user)
        mytweets = Tweet.objects.all().order_by("-id")
        for tweet in mytweets:
            if tweet.user in myusers:
                anumber += 1
            elif tweet.user == request.user:
                anumber +=1        
        return render(request,'index.html',{"tweets":mytweets,"users":myusers,"count":thecount,"anumber":anumber})
