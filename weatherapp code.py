Python 3.12.0b3 (tags/v3.12.0b3:f992a60, Jun 20 2023, 12:25:40) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
... 
... def get_weather(api_key, city):
...     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
...     response = requests.get(url)
...     data = response.json()
...     if data["cod"] != "404":
...         weather = data["weather"][0]["main"]
...         temperature = data["main"]["temp"]
...         humidity = data["main"]["humidity"]
...         return weather, temperature, humidity
...     else:
...         return None
... 
... def main():
...     api_key = "6672d98b681995b8b60679ae532f5b14"
...     city = input("Enter a city: ")
...     result = get_weather(api_key, city)
...     if result:
...         weather, temperature, humidity = result
...         print(f"Weather in {city}: {weather}")
...         print(f"Temperature: {temperature} K")
...         print(f"Humidity: {humidity}%")
...     else:
...         print("City not found.")
... 
... if _name_ == "_main_":
