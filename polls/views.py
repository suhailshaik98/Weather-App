from django.shortcuts import render
from django.http import HttpResponse
from polls import app

def home(request):
    resultdict=app.weatherapi()
    ans=resultdict["data"]
    return HttpResponse(ans)