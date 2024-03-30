from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"user/index.html")

def find(request):
    return render(request,"user/find.html")

def view(request):
    return render(request,"user/view.html")

def login(request):
    return render(request,"user/login.html")

def profile(request):
    return render(request,"user/profilepage.html")
