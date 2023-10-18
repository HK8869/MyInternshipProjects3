import requests

# Replace with your OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"

def fetch_weather_data(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(complete_url)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return None

def display_weather_data(data):
    if data is None:
        print("Error fetching weather data. Please check your network connection or city name.")
    else:
        main_data = data.get("main", {})
        weather_data = data.get("weather", [{}])[0]

        temperature = main_data.get("temp")
        humidity = main_data.get("humidity")
        weather = weather_data.get("description")

        print(f"Weather in {data.get('name')}, {data.get('sys')['country']}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {weather.capitalize()}")

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    weather_data = fetch_weather_data(city_name)
    display_weather_data(weather_data)
