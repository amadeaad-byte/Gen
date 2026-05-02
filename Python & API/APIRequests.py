# Running API in Python (AFTER Testing in Postman!)
import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=51.5072&longitude=-0.1276&current_weather=true"
response = requests.get(url)
data = response.json()
print(data["current_weather"])