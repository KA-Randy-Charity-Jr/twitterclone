"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitterclone_app import views as index
from twitteruser import views as twitteruser
from tweet import views as tweet
from notification import views as notification
from authentication import views as authentication
urlpatterns = [
    path('', index.index_view, name='homepage'),
    path('login/', authentication.login_view, name="login"),
    path('logout/', authentication.logout_view, name="logout"),
    path('addtweet/', tweet.createtweet_view, name="addtweet"),
    path('tweet/<int:tweet_id>', tweet.tweet_view, name="tweet"),
    path('user/<str:username>/', twitteruser.user_view, name="user"),
    path('follow/<str:username>', twitteruser.follow_view, name="follow"),
    path('unfollow/<str:username>', twitteruser.unfollow_view, name="unfollow"),
    path('notification/',notification.notification_view,name="notification"),
    path('signup/',authentication.signup_view,name="signup"),
    path('admin/', admin.site.urls),

]