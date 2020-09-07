from django.shortcuts import render
from notification.models import Notification

# Create your views here.
def notification_view(request):
    thecount = 0
    if request.user.is_authenticated:
        count = Notification.objects.filter(tagged=request.user, isread=False)
        if count:
            thecount=count.count
    array=[]
    notifications = Notification.objects.filter(tagged=request.user)
    for notification in notifications:
        if notification.isread== False:
            notification.isread = True
            array.append(notification.tweet)
            notification.save()

    return render(request,"notification.html",{"notifications":array,"count":thecount})