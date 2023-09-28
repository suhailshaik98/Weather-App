from django.shortcuts import render
from django.http import HttpResponse
from polls import app
import json
import redis
from datetime import datetime
import pytz


def home(request):
    redis_server = redis.Redis(host='172.17.0.1', port=6380, db=0)
    get_api_data=redis_server.get('api_data')
    if get_api_data is None or oldtimechecker(get_api_data) is False:
        resultdict = app.weatherapi()
        ans = resultdict["data"]
        json_data=json.dumps(ans)
        redis_server.set('api_data',json_data)
        response=HttpResponse(json_data, content_type='application/json')
    else:
        response=HttpResponse(get_api_data,content_type='application/json')    
    return response

def oldtimechecker(jsondata):
    api_data=json.loads(jsondata)
    get_latest_time=api_data[-2]['timestamp']
    # target_date = datetime.strptime(get_latest_time, "%Y-%m-%dT%H:%M:%SZ")
    target_date_utc = datetime.strptime(get_latest_time, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=pytz.UTC)
    edt_timezone = pytz.timezone('US/Eastern')
    target_date = target_date_utc.astimezone(edt_timezone)
    current_date = datetime.now(edt_timezone)
    if current_date >= target_date:
        return False
    else:
        return True
