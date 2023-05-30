# Create a program that gets an IP address as user input \
# then it prints the weather on the IP address location.
#
# Use the following APIs:
#
# https://www.metaweather.com/api/
# https://www.geojs.io/docs/v1/endpoints/geo/

import requests
import json

IP_address = "37.191.56.241"
input_IP_address = requests.get("https://get.geojs.io/v1/ip/geo/" + IP_address +".json")
IP_address_dictionary = json.loads(input_IP_address.text)# get lat and longitude from this dictionary
print(IP_address_dictionary)# then use it in metaweather API code

def get_coordinates(IP_address_dictionary):# getting coordinates
    longitude = IP_address_dictionary["longitude"]
    latitude = IP_address_dictionary["latitude"]
    coordinates = str(latitude + "," + longitude)
    return coordinates

coordinates = get_coordinates(IP_address_dictionary)
input_coordinates = requests.get("https://www.metaweather.com/api/location/search/?lattlong=" + coordinates)
location_of_IP_address = json.loads(input_coordinates.text)
print(location_of_IP_address)

