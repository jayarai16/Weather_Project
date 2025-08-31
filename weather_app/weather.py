import requests

def weather_data(city):
    api_key = "79aea6bbde03f90d89b5fced79def369"
    base_url = "http://api.openweathermap.org/data/2.5/weather?units=metric&q="

    url = f"{base_url}{city}&appid={api_key}"

    response = requests.get(url)

# Convert response to JSON
    data = response.json()

# Print data
    if response.status_code == 200:
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Weather:", data["weather"][0]["description"])
    else:
        print("Error:", data["message"])
    data={
        'city':data["name"],
        "temperature": data["main"]["temp"],
        "weather":data["weather"][0]["description"]
    }
    return data
    