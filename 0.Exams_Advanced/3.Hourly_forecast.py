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


------------------------------------ Problem to resolve --------------------------------

Write a function called forecast that stores information about the weather, and returns sorted 
information for all locations. The function will receive a different number of arguments. The 
arguments will be passed as tuples with two elements - the first one is the location, and the 
second one is the weather:
        Location name: string
                        any string
        Weather: string
                "Sunny"
                "Rainy"
            "Cloudy"
First, sort all locations by weather. First are positioned the locations with sunny weather, 
next are the locations with cloudy weather, and last are the locations with rainy weather. For 
each sequence of locations (e.g. all sunny locations), sort them by their name in ascending order 
(alphabetically).
In the end, return the output as described below.
Note: Submit only the function in the judge system
Input
There will be no input from the console, just parameters passed to your function
Output
The output should look like this:
"{first_sorted_location} - {weather}"
"{second_sorted_location} - {weather}"
…
"{last_sorted_location} - {weather}"
Constraints
Each tuple given will always contain the location with its weather.
You will never receive the same location twice or more times.
-------------------------------------- Example inputs ----------------------------------
Test Code
print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))	
Output    
New York - Sunny
Sofia - Sunny
London - Cloudy
---------------------------------
Test Code
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))	
---------------------------------
Output    
Beijing - Sunny
Bourgas - Sunny
Peru - Sunny
Tokyo - Sunny
Florence - Cloudy
Sofia - Cloudy
Hong Kong - Rainy
----------------------------------
Test Code
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))	
Output      
Sofia - Rainy
Tokyo - Rainy

"""
