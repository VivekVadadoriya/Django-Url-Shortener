from django.shortcuts import render, HttpResponse, redirect
from .models import urlModel
import random


# Create your views here.

def home(request):
    return render(request, "index.html")


def makeshorturl(request):
    if request.method == "POST":
        longurl = request.POST['longurl']
        s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
        shorturl = ("".join(random.sample(s, 5)))
        obj = urlModel.objects.create(longurl=longurl, shorturl=shorturl)
        shorturl = "https://vurl.herokuapp.com/" + shorturl
        keys = {"shorturl": shorturl, "longurl": longurl}
    return render(request, "shortener.html", keys)


def redirecturl(request, shorturl):
    try:
        obj = urlModel.objects.get(shorturl=shorturl)
    except urlModel.DoesNotExist:
        obj = None
    if obj is not None:
        obj.count += 1
        obj.save()
        return redirect(obj.longurl)
    else:
        return HttpResponse("Check your Url")
