import data

# print(data.weather)
weather_data = data.weather

print(weather_data.keys())
# print(weather_data['list'])

forcast_container = weather_data['list']
print(type(forcast_container))
print(len(forcast_container))

first_item_in_forcast_container = forcast_container[0]
print(first_item_in_forcast_container.keys())

# ATTEMPT TO ACCESS REQUIRED VALUES FROM FIRST ITEM IN FORCAST LIST

time = first_item_in_forcast_container['dt_txt']
temp = first_item_in_forcast_container['main']['temp']
pressure = first_item_in_forcast_container['main']['pressure']
wind = first_item_in_forcast_container['wind']['speed']

clouds = first_item_in_forcast_container['weather']
print(clouds[0]['description'])

cloud_description = clouds[0]['description']

print(time, temp, wind, pressure, cloud_description)

# ATTAMPT TO ACCESS FOR ALL 40 FORCASTS IN LIST
print("Time".center(20), "Temp".center(7), "Wind".center(5), "Pressure".center(9), "Cloud_desc".center(17), sep = " | ")
print("-"*70)

for forcast in forcast_container:
    time        = forcast['dt_txt']
    temp        = forcast['main']['temp']
    pressure    = forcast['main']['pressure']
    wind        = forcast['wind']['speed']
    clouds      = forcast['weather']
    cloud_description = clouds[0]['description']

    print(f"{time}".center(20), f"{temp}".center(7), f"{wind}".center(5), f"{pressure}".center(9), f"{cloud_description}".center(17), sep = " | ")