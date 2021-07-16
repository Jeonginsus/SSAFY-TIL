import requests

country = "1132599"
day = 2

url = f'https://www.metaweather.com/api/location/{country}/'

response = requests.get(url).json()

totomorrow_weather = response['consolidated_weather'][day]['weather_state_name']

print(f'totomorow weather is {totomorrow_weather}')