import requests

name = 'insu'
url = f'https://api.nationalize.io?name={name}'

response = requests.get(url).json()

print(response['country'][0]['country_id'])
