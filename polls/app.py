# def weatherapi():
#     #write logic for getting the data from the api and returning the values inside a dictionary
#     resultdict={}
#     value="43"
#     resultdict["data"]=value
#     return resultdict

import requests

import requests
from datetime import datetime

def convertdatafromapi(data):
#   maindata=data['data']
#   timelines=maindata['timelines']
  timelines=data['timelines']
  timedetails=timelines[0]
  actualdatalist=timedetails['intervals']
  datalist=[]
  for samplestarttime in actualdatalist:
    data_dictionary={}
    timestamp=samplestarttime['startTime']
    temperature=samplestarttime['values']['temperature']
    day=timestamp[5:-10]
    convertobject=datetime.strptime(timestamp,"%Y-%m-%dT%H:%M:%SZ")
    convertotime=convertobject.strftime("%I:%M %p")
    #     data_dictionary={
    #   timestamp:[{
    #     'time':convertotime,
    #     'day':day,
    #     'temperature':temperature

    #   }]
    # }

    data_dictionary['timestamp']=timestamp
    data_dictionary['temperature']=temperature
    data_dictionary['day']=day
    data_dictionary['time']=convertotime
    datalist.append(data_dictionary)
  return datalist

def weatherapi():
    # URL of the weather API
    # api_url = 'https://api.tomorrow.io/v4/timelines?location=40.75872069597532,-73.98529171943665&fields=temperature&timesteps=1h&units=metric&apikey=FxGDjcWkMnzkG87VU4qS1APaHnGbG5HO'

    try:
        # response = requests.get(api_url)

        # if response.status_code == 200:
        if True:
            # Parsing the JSON response
            # weather_data = response.json()
            weather_data={'timelines': [{'timestep': '1h', 'endTime': '2023-08-18T22:00:00Z', 'startTime': '2023-08-13T22:00:00Z', 'intervals': [{'startTime': '2023-08-13T22:00:00Z', 'values': {'temperature': 28.19}}, {'startTime': '2023-08-13T23:00:00Z', 'values': {'temperature': 28.44}}, {'startTime': '2023-08-14T00:00:00Z', 'values': {'temperature': 26.28}}, {'startTime': '2023-08-14T01:00:00Z', 'values': {'temperature': 24.91}}, {'startTime': '2023-08-14T02:00:00Z', 'values': {'temperature': 23.97}}, {'startTime': '2023-08-14T03:00:00Z', 'values': {'temperature': 23.09}}, {'startTime': '2023-08-14T04:00:00Z', 'values': {'temperature': 22.36}}, {'startTime': '2023-08-14T05:00:00Z', 'values': {'temperature': 21.81}}, {'startTime': '2023-08-14T06:00:00Z', 'values': {'temperature': 21.47}}, {'startTime': '2023-08-14T07:00:00Z', 'values': {'temperature': 21.04}}, {'startTime': '2023-08-14T08:00:00Z', 'values': {'temperature': 20.74}}, {'startTime': '2023-08-14T09:00:00Z', 'values': {'temperature': 20.57}}, {'startTime': '2023-08-14T10:00:00Z', 'values': {'temperature': 20.39}}, {'startTime': '2023-08-14T11:00:00Z', 'values': {'temperature': 20.66}}, {'startTime': '2023-08-14T12:00:00Z', 'values': {'temperature': 21.77}}, {'startTime': '2023-08-14T13:00:00Z', 'values': {'temperature': 22.52}}, {'startTime': '2023-08-14T14:00:00Z', 'values': {'temperature': 23.72}}, {'startTime': '2023-08-14T15:00:00Z', 'values': {'temperature': 25.03}}, {'startTime': '2023-08-14T16:00:00Z', 'values': {'temperature': 26.69}}, {'startTime': '2023-08-14T17:00:00Z', 'values': {'temperature': 27.71}}, {'startTime': '2023-08-14T18:00:00Z', 'values': {'temperature': 28.97}}, {'startTime': '2023-08-14T19:00:00Z', 'values': {'temperature': 29.02}}, {'startTime': '2023-08-14T20:00:00Z', 'values': {'temperature': 29.77}}, {'startTime': '2023-08-14T21:00:00Z', 'values': {'temperature': 29.75}}, {'startTime': '2023-08-14T22:00:00Z', 'values': {'temperature': 28.55}}, {'startTime': '2023-08-14T23:00:00Z', 'values': {'temperature': 26.95}}, {'startTime': '2023-08-15T00:00:00Z', 'values': {'temperature': 24.63}}, {'startTime': '2023-08-15T01:00:00Z', 'values': {'temperature': 23.56}}, {'startTime': '2023-08-15T02:00:00Z', 'values': {'temperature': 23.02}}, {'startTime': '2023-08-15T03:00:00Z', 'values': {'temperature': 22.68}}, {'startTime': '2023-08-15T04:00:00Z', 'values': {'temperature': 22.05}}, {'startTime': '2023-08-15T05:00:00Z', 'values': {'temperature': 21.35}}, {'startTime': '2023-08-15T06:00:00Z', 'values': {'temperature': 20.04}}, {'startTime': '2023-08-15T07:00:00Z', 'values': {'temperature': 19.98}}, {'startTime': '2023-08-15T08:00:00Z', 'values': {'temperature': 20.49}}, {'startTime': '2023-08-15T09:00:00Z', 'values': {'temperature': 21.27}}, {'startTime': '2023-08-15T10:00:00Z', 'values': {'temperature': 21.84}}, {'startTime': '2023-08-15T11:00:00Z', 'values': {'temperature': 22.42}}, {'startTime': '2023-08-15T12:00:00Z', 'values': {'temperature': 23.54}}, {'startTime': '2023-08-15T13:00:00Z', 'values': {'temperature': 24.63}}, {'startTime': '2023-08-15T14:00:00Z', 'values': {'temperature': 25.73}}, {'startTime': '2023-08-15T15:00:00Z', 'values': {'temperature': 26.83}}, {'startTime': '2023-08-15T16:00:00Z', 'values': {'temperature': 26.31}}, {'startTime': '2023-08-15T17:00:00Z', 'values': {'temperature': 30.42}}, {'startTime': '2023-08-15T18:00:00Z', 'values': {'temperature': 30.37}}, {'startTime': '2023-08-15T19:00:00Z', 'values': {'temperature': 30.55}}, {'startTime': '2023-08-15T20:00:00Z', 'values': {'temperature': 29.08}}, {'startTime': '2023-08-15T21:00:00Z', 'values': {'temperature': 28.35}}, {'startTime': '2023-08-15T22:00:00Z', 'values': {'temperature': 28.2}}, {'startTime': '2023-08-15T23:00:00Z', 'values': {'temperature': 26.57}}, {'startTime': '2023-08-16T00:00:00Z', 'values': {'temperature': 25.43}}, {'startTime': '2023-08-16T01:00:00Z', 'values': {'temperature': 24.58}}, {'startTime': '2023-08-16T02:00:00Z', 'values': {'temperature': 23.91}}, {'startTime': '2023-08-16T03:00:00Z', 'values': {'temperature': 24.68}}, {'startTime': '2023-08-16T04:00:00Z', 'values': {'temperature': 23.61}}, {'startTime': '2023-08-16T05:00:00Z', 'values': {'temperature': 22.54}}, {'startTime': '2023-08-16T06:00:00Z', 'values': {'temperature': 21.82}}, {'startTime': '2023-08-16T07:00:00Z', 'values': {'temperature': 22.02}}, {'startTime': '2023-08-16T08:00:00Z', 'values': {'temperature': 22.14}}, {'startTime': '2023-08-16T09:00:00Z', 'values': {'temperature': 21.93}}, {'startTime': '2023-08-16T10:00:00Z', 'values': {'temperature': 21.14}}, {'startTime': '2023-08-16T11:00:00Z', 'values': {'temperature': 21.16}}, {'startTime': '2023-08-16T12:00:00Z', 'values': {'temperature': 21.67}}, {'startTime': '2023-08-16T13:00:00Z', 'values': {'temperature': 22.7}}, {'startTime': '2023-08-16T14:00:00Z', 'values': {'temperature': 24.18}}, {'startTime': '2023-08-16T15:00:00Z', 'values': {'temperature': 25.68}}, {'startTime': '2023-08-16T16:00:00Z', 'values': {'temperature': 27.08}}, {'startTime': '2023-08-16T17:00:00Z', 'values': {'temperature': 27.94}}, {'startTime': '2023-08-16T18:00:00Z', 'values': {'temperature': 28.44}}, {'startTime': '2023-08-16T19:00:00Z', 'values': {'temperature': 28.43}}, {'startTime': '2023-08-16T20:00:00Z', 'values': {'temperature': 28.49}}, {'startTime': '2023-08-16T21:00:00Z', 'values': {'temperature': 28.53}}, {'startTime': '2023-08-16T22:00:00Z', 'values': {'temperature': 27.88}}, {'startTime': '2023-08-16T23:00:00Z', 'values': {'temperature': 26.5}}, {'startTime': '2023-08-17T00:00:00Z', 'values': {'temperature': 25.31}}, {'startTime': '2023-08-17T01:00:00Z', 'values': {'temperature': 24.65}}, {'startTime': '2023-08-17T02:00:00Z', 'values': {'temperature': 24.25}}, {'startTime': '2023-08-17T03:00:00Z', 'values': {'temperature': 23.89}}, {'startTime': '2023-08-17T04:00:00Z', 'values': {'temperature': 23.91}}, {'startTime': '2023-08-17T05:00:00Z', 'values': {'temperature': 23.57}}, {'startTime': '2023-08-17T06:00:00Z', 'values': {'temperature': 23.48}}, {'startTime': '2023-08-17T07:00:00Z', 'values': {'temperature': 23.55}}, {'startTime': '2023-08-17T08:00:00Z', 'values': {'temperature': 23.26}}, {'startTime': '2023-08-17T09:00:00Z', 'values': {'temperature': 22.93}}, {'startTime': '2023-08-17T10:00:00Z', 'values': {'temperature': 22.62}}, {'startTime': '2023-08-17T11:00:00Z', 'values': {'temperature': 22.75}}, {'startTime': '2023-08-17T12:00:00Z', 'values': {'temperature': 23.81}}, {'startTime': '2023-08-17T13:00:00Z', 'values': {'temperature': 25.15}}, {'startTime': '2023-08-17T14:00:00Z', 'values': {'temperature': 26.23}}, {'startTime': '2023-08-17T15:00:00Z', 'values': {'temperature': 27.43}}, {'startTime': '2023-08-17T16:00:00Z', 'values': {'temperature': 29.22}}, {'startTime': '2023-08-17T17:00:00Z', 'values': {'temperature': 30.39}}, {'startTime': '2023-08-17T18:00:00Z', 'values': {'temperature': 30.8}}, {'startTime': '2023-08-17T19:00:00Z', 'values': {'temperature': 30.8}}, {'startTime': '2023-08-17T20:00:00Z', 'values': {'temperature': 30.35}}, {'startTime': '2023-08-17T21:00:00Z', 'values': {'temperature': 29.29}}, {'startTime': '2023-08-17T22:00:00Z', 'values': {'temperature': 27.7}}, {'startTime': '2023-08-17T23:00:00Z', 'values': {'temperature': 27.2}}, {'startTime': '2023-08-18T00:00:00Z', 'values': {'temperature': 27.43}}, {'startTime': '2023-08-18T01:00:00Z', 'values': {'temperature': 27.12}}, {'startTime': '2023-08-18T02:00:00Z', 'values': {'temperature': 26.41}}, {'startTime': '2023-08-18T03:00:00Z', 'values': {'temperature': 26.07}}, {'startTime': '2023-08-18T04:00:00Z', 'values': {'temperature': 26.16}}, {'startTime': '2023-08-18T05:00:00Z', 'values': {'temperature': 25.94}}, {'startTime': '2023-08-18T06:00:00Z', 'values': {'temperature': 26.28}}, {'startTime': '2023-08-18T07:00:00Z', 'values': {'temperature': 25.84}}, {'startTime': '2023-08-18T08:00:00Z', 'values': {'temperature': 25.54}}, {'startTime': '2023-08-18T09:00:00Z', 'values': {'temperature': 25.25}}, {'startTime': '2023-08-18T10:00:00Z', 'values': {'temperature': 25}}, {'startTime': '2023-08-18T11:00:00Z', 'values': {'temperature': 25.27}}, {'startTime': '2023-08-18T12:00:00Z', 'values': {'temperature': 25.75}}, {'startTime': '2023-08-18T13:00:00Z', 'values': {'temperature': 26.54}}, {'startTime': '2023-08-18T14:00:00Z', 'values': {'temperature': 27.33}}, {'startTime': '2023-08-18T15:00:00Z', 'values': {'temperature': 28.12}}, {'startTime': '2023-08-18T16:00:00Z', 'values': {'temperature': 28.3}}, {'startTime': '2023-08-18T17:00:00Z', 'values': {'temperature': 28.49}}, {'startTime': '2023-08-18T18:00:00Z', 'values': {'temperature': 28.67}}, {'startTime': '2023-08-18T19:00:00Z', 'values': {'temperature': 28.5}}, {'startTime': '2023-08-18T20:00:00Z', 'values': {'temperature': 28.33}}, {'startTime': '2023-08-18T21:00:00Z', 'values': {'temperature': 28.15}}, {'startTime': '2023-08-18T22:00:00Z', 'values': {'temperature': 26.74}}]}]}
            timeframe=convertdatafromapi(weather_data)
            print(timeframe)

            # temperature_data = weather_data["data"]["timelines"][0]["intervals"][0]["values"]["temperature"]
            temperature_data = weather_data["timelines"][0]["intervals"][0]["values"]["temperature"]
            
            timeframe.append(temperature_data)
            resultdict = {
                "data": timeframe
                # "timeframe":timeframe
            }

            return resultdict
        else:
            print("API request failed with status code:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("API request error:", e)
        return None

# Calling the function to get weather data
# weather_data = weatherapi()
# if weather_data:
#     print("Weather data:", weather_data)
# else:
#     print("Failed to fetch weather data")

    