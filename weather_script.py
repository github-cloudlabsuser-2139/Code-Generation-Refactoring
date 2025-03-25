import requests

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        # Construct the API request URL
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"  # Use "imperial" for Fahrenheit
        }
        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"]
            }
            return weather
        elif response.status_code == 404:
            return {"error": "City not found."}
        else:
            return {"error": f"An error occurred: {response.status_code}"}

if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual OpenWeatherMap API key
    api_key = "ec0fec2490f9b68847a01b940ae15d86"
    app = WeatherApp(api_key)

    city = input("Enter the city name: ")
    weather = app.get_weather(city)

    if "error" in weather:
        print(weather["error"])
    else:
        print(f"City: {weather['city']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Weather: {weather['description']}")