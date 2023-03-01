import requests
import json

def get_weather_data(city):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":city}

    headers = {
        "X-RapidAPI-Key": "7720096032msh98ea79839f45fa5p1c7ea8jsn69adcb3ba4df",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return json.loads(response.text)

def write_weather_data(data):
    with open('weather.json', 'w', encoding='UTF8') as response_file:
        json.dump(json.loads(data), response_file, indent=4)

weather_data = get_weather_data('Madrid')
write_weather_data(weather_data)
