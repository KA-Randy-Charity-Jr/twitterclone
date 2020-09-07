from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from twitteruser.forms import LoginForm,SignupForm
from twitteruser.models import TwitterUser

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user= authenticate(request,username=data.get("username"),password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next',reverse("homepage")))
    form = LoginForm()
    return render(request,"login.html",{"form":form})  

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

    
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            newuser = TwitterUser.objects.create_user(username=data.get("username"), password=data.get("password"),displayname=data.get("displayname"))
            login(request, newuser)
            return HttpResponseRedirect(reverse("homepage"))
    form = SignupForm()
    return render(request, "form.html", {"form": form})
