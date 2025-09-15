import requests

API_KEY = "f13a86caca59ec7363a2d40c86d02c36" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
def get_weather(CITY):
  
    request_url = f"{BASE_URL}?q={CITY}&appid={API_KEY}"

    response = requests.get(request_url)

    if response.status_code == 200:

        data = response.json()
        
        # The weather description is inside a LIST, which is inside the 'weather' key.
        weather_description = data['weather'][0]['description']
        # The temperature is inside the 'main' key.
        temperature_kelvin = data['main']['temp']
        #  Kelvin to Celsius (0°K = -273.15°C)
        temperature_celsius = temperature_kelvin - 273.15

        city_name = data['name']

        humidity = data['main']['humidity']
        
    
        print(f"Weather in {city_name}:")
        print(f"Description: {weather_description.capitalize()}")
        print(f"Temperature: {temperature_celsius:.1f} °C") 
        print(f"Humidity: {humidity}%")
        
    else:
        print("An error occurred.", response.status_code)
        print(response.text) 

def main():
    print("=== Simple Weather App ===")
    city = input("Please enter a city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()