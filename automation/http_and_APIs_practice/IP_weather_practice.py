# Create a program that gets an IP address as user input then it prints the weather on the\
# IP address location.
# Use the following APIs:
# https://www.metaweather.com/api/
# https://www.geojs.io/docs/v1/endpoints/geo/

import requests
import json

IP_address = "37.191.56.241"# here store IP address. start menu --> cmd --> ipconfig --> IPv4 address
#How to get this number
input_IP_address = requests.get("https://get.geojs.io/v1/ip/geo/"+IP_address+".json")
IP_address_location = json.loads(input_IP_address.text)
print(IP_address_location) # from this location get latitude and longitude

def get_lat_and_long(IP_address_location):
    latitude = IP_address_location["latitude"]
    longitude = IP_address_location["longitude"]
    location_coordinates = str(latitude + "," + longitude)
    return location_coordinates

coordinates = get_lat_and_long(IP_address_location)

def get_location_of_coordinates(coordinates):
    input_coordinates = requests.get("https://www.metaweather.com/api/location/search/?lattlong="+coordinates)
    location_of_coordinates = json.loads(input_coordinates.text)
    return location_of_coordinates

location_of_coordinates = get_location_of_coordinates(coordinates)
print(location_of_coordinates)

def get_where_on_earth_id(location_of_coordinates):
    for i in range(len(location_of_coordinates)):
        location_directory = location_of_coordinates[i]
        where_on_earth_id = location_directory["woeid"]
        return where_on_earth_id

where_on_earth_id = get_where_on_earth_id(location_of_coordinates)
print(where_on_earth_id)

def get_woeid_details(where_on_earth_id):
    where_on_earth_id_data = requests.get('https://www.metaweather.com/api/location/' + str(where_on_earth_id) + "'")
    woeid_details = json.loads(where_on_earth_id_data.text) # when I debug it is saying 404 error
    return woeid_details

# woeid_details = get_woeid_details(where_on_earth_id)
print(get_woeid_details(where_on_earth_id))

# from the data obtained from the above function we need to extract data\
# for the key "weather_state_name"