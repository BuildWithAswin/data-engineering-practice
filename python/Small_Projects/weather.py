import requests


def get_weather(city):
    API_KEY = "6ce0ed8f279a4cb9284d6e698f3d9753"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    print(response.status_code)
    print(response.text)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print(f"\n Weather in {city.title()}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.capitalize()}")
    else:
        print("City not found or error fetching data.")


city_name = input("Enter city name: ").strip()
get_weather(city_name)
