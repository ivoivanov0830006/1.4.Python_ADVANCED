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


"""
------------------------------------- Another Solution ---------------------------------

def forecast(*args):
    locations = {}
    for el in args:
        if el[0] not in locations:
            locations[el[0]] = el[1]
    sorted_result = {k: v for k,v in sorted(locations.items(), key=lambda x: (x[1], x[0]))}
    sunny = ''
    cloudy = ''
    rainy = ''
    for key, value in sorted_result.items():
        if value == 'Sunny':
            sunny += f'{key} - {value}\n'
        elif value == 'Cloudy':
            cloudy += f'{key} - {value}\n'
        elif value == 'Rainy':
            rainy += f'{key} - {value}\n'

    return sunny + cloudy + rainy
