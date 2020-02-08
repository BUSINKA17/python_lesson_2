import requests
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
requests = requests.get(url)
print(response)
data = json.loads(response.text)
print(data)