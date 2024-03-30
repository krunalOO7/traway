from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"operator/index.html")

def createtrip(request):
    return render(request,"operator/createtrip.html")

def tripinfo(request):
    return render(request,"operator/tripinfo.html")

def profile(request):
    return render(request,"operator/profile.html")

def viewtrips(request):
    return render(request,"operator/viewtrips.html")