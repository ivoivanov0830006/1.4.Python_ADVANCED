def forecast(*args):
    weather_forecast = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": []
    }
    for location in args:
        city, weather = location[0], location[1]
        weather_forecast[weather].append(city)

    result = ""
    for key, value in weather_forecast.items():
        sorted_cities = sorted(value)
        for city_name in sorted_cities:
            result += f"{city_name} - {key}\n"
    return result


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
