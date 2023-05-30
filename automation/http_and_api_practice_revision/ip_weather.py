# Create a program that gets an IP address as user input then it prints the weather on the IP address \
# location.
#
# Use the following APIs:
#
# https://www.metaweather.com/api/ https://www.geojs.io/docs/v1/endpoints/geo/

import requests, json

IP_address = "37.191.56.241"

input_ip_address = requests.get("https://get.geojs.io/v1/ip/geo/"+ IP_address + ".json")
ip_address_location_details = json.loads(input_ip_address.text)
latitude = str(ip_address_location_details["latitude"])
longitude = str(ip_address_location_details["longitude"])
# print(latitude, longitude)
woeid = requests.get('https://www.metaweather.com/api/location/search/?lattlong=' +latitude + "," + longitude)
woeid_details = json.loads(woeid.text)
# print(woeid_details)
woe_id = str(woeid_details[0]["woeid"])
# print(woe_id)
weather_data = requests.get("https://www.metaweather.com/api/location/"+woe_id)
weather_state = json.loads(weather_data.text)
weather_condition = weather_state["consolidated_weather"][0]["weather_state_name"]
print(weather_condition)


