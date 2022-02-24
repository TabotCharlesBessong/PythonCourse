
from ast import comprehension


# similar to list comprehension 

cities = {'New York':42,'Boston':76,'Los Angeles':102,'Chicago':54}

cityInC = {key:round(((value - 32)/1.8)) for (key,value) in cities.items() }

weather = {'New York':42,'Boston':'sunny','Los Angeles':'sunny','Chicago':54}

sunnyWeather = {key: value for (key,value) in weather.items() if value == 'sunny'}

descCities = {key: ('WARM' if value >= 50 else 'COLD' ) for (key,value) in cities.items() }

print(cityInC)
print(sunnyWeather)
print(descCities)