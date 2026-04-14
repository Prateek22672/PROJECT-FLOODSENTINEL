import requests

API_KEY = "b02953f351863a6c8a19605530622f3b"

city = "Visakhapatnam"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(data)