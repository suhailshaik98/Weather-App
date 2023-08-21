from django.shortcuts import render
from django.http import HttpResponse
from polls import app

# def home(request):
#     resultdict=app.weatherapi()
#     ans=resultdict["data"]
#     return HttpResponse(ans)

def home(request):
    resultdict = app.weatherapi()

    if resultdict is not None and "data" in resultdict:
        ans = resultdict["data"]
        return HttpResponse(ans)
    else:
        return HttpResponse("Weather data not available")
