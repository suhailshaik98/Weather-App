from django.shortcuts import render
from django.http import HttpResponse
from polls import app
import json

def home(request):
    resultdict = app.weatherapi()
    # if resultdict==None:
    #     return JsonResponse('API Rejected Data')
    ans = resultdict["data"]
    # return JsonResponse(ans,safe=False)
    json_data = json.dumps(ans)  # Convert data to JSON format
    
    response = HttpResponse(json_data, content_type='application/json')  # Set JSON content type
    
    return response