import requests, json
from flask import Flask, request, jsonify

app = Flask("ip_waether")

IP_address = "37.191.56.241"

@app.route("/lattlong")
def get_coordinates_from_IP():
    global IP_address
    input_ip_address = requests.get("https://get.geojs.io/v1/ip/geo/"+ IP_address + ".json")
    ip_address_location_details = json.loads(input_ip_address.text)
    latitude = str(ip_address_location_details["latitude"])
    longitude = str(ip_address_location_details["longitude"])
    coordinates = (latitude, longitude)
    return coordinates

@app.route("/woeid")
def get_woeid_details():
    latitude = request.args["latitude"]
    longitude = request.args["longitude"]
    woeid = requests.get('https://www.metaweather.com/api/location/search/?lattlong=' +latitude + "," + longitude)
    woeid_details = json.loads(woeid.text)
    for i in range(len(woeid_details)):
        woeid_dictionary = woeid_details[i]
        return woeid_dictionary

@app.route("/woe/id/<city_name>")
def get_woeid(city_name):
    print(city_name)
    latitude = request.args["latitude"]
    longitude = request.args["longitude"]
    woeid = requests.get('https://www.metaweather.com/api/location/search/?lattlong=' + latitude + "," + longitude)
    woeid_details = json.loads(woeid.text)
    for i in range(len(woeid_details)):
        woeid_dictionary = woeid_details[i]
        if city_name == woeid_dictionary["title"]:
            return jsonify(woeid_dictionary["woeid"])

    # woe_id = str(woeid_details[0]["woeid"])
    # return woe_id
# weather_data = requests.get("https://www.metaweather.com/api/location/"+woe_id)
# weather_state = json.loads(weather_data.text)
# weather_condition = weather_state["consolidated_weather"][0]["weather_state_name"]
# print(weather_condition)

