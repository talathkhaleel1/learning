import requests, json

IP_address = "37.191.56.241"

input_ip_address = requests.get("https://get.geojs.io/v1/ip/geo/"+ IP_address + ".json")
ip_address_location_details = json.loads(input_ip_address.text)
latitude = str(ip_address_location_details["latitude"])
longitude = str(ip_address_location_details["longitude"])
print(latitude, longitude)

woeid = requests.get('https://www.metaweather.com/api/location/search/?lattlong=' +latitude + "," + longitude)
woeid_details = json.loads(woeid.text)
for i in range(len(woeid_details)):
    woeid_dictionary = woeid_details[i]
    print(woeid_dictionary)
    # woe_id = str(woeid_details[0]["woeid"])
    # return woe_id
    # weather_data = requests.get("https://www.metaweather.com/api/location/"+woe_id)
    # weather_state = json.loads(weather_data.text)
    # weather_condition = weather_state["consolidated_weather"][0]["weather_state_name"]
    # print(weather_condition)