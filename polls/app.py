# def weatherapi():
#     #write logic for getting the data from the api and returning the values inside a dictionary
#     resultdict={}
#     value="43"
#     resultdict["data"]=value
#     return resultdict

import requests

def weatherapi():
    # URL of the weather API
    api_url = 'https://api.tomorrow.io/v4/timelines?location=40.75872069597532,-73.98529171943665&fields=temperature&timesteps=1h&units=metric&apikey=FxGDjcWkMnzkG87VU4qS1APaHnGbG5HO'

    try:
        # Sending a GET request to the API
        response = requests.get(api_url)

        # Checking if the request was successful (status code 200)
        if response.status_code == 200:
            # Parsing the JSON response
            weather_data = response.json()

            # Extracting the relevant weather value from the API response
            # The structure of the response is a bit more complex
            temperature_data = weather_data["data"]["timelines"][0]["intervals"][0]["values"]["temperature"]

            # Creating a dictionary to store the result
            resultdict = {
                "data": temperature_data
            }

            return resultdict
        else:
            print("API request failed with status code:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("API request error:", e)
        return None

# Calling the function to get weather data
weather_data = weatherapi()
if weather_data:
    print("Weather data:", weather_data)
else:
    print("Failed to fetch weather data")

    