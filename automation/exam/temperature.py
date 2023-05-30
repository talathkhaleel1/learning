import requests,json

from flask import Flask, jsonify, request, render_template

app = Flask("Average temperature calculator")

@app.route("/temperature/<cityname>")
def get_avg_temp(cityname):
    input_city = requests.get("https://geocode.xyz/" + cityname + "?json=1")
    city_details = json.loads(input_city.text)
    city_location_details = city_details["alt"]["loc"]
    for i in range(len(city_location_details)):
        city_specification = city_location_details[i]
        if cityname == city_specification["city"]:
            latitude =  str(city_specification["latt"])
            longitude = str(city_specification["longt"])
            input_city_coordinates = requests.get("https://api.open-meteo.com/v1/forecast?latitude=" + latitude + "&longitude=" + longitude + "&hourly=temperature_2m")
            weather_details = json.loads(input_city_coordinates.text)
            list_of_temp = weather_details["hourly"]["temperature_2m"]
            avg_temp = sum(list_of_temp) / len(list_of_temp)
            return jsonify(avg_temp)
        return "Inappropriate city name."


@app.route("/usage")
def render_html():
    render_template("temperature.html", city ="Budapest", country = "Hungary", averagetemp = get_avg_temp("Budapest") )




# https://geocode.xyz/Hauptstr.,+57632+Berzhausen?json=1

# https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m

# latitude:"47.47"
# longitude:"19.04"
# input_city_coordinates = requests.get("https://api.open-meteo.com/v1/forecast?latitude="+ "47.47"+ "&longitude=" +"19.04" + "&hourly=temperature_2m")
# weather_details = json.loads(input_city_coordinates.text)
# # print(weather_details)
# list_of_temp = weather_details["hourly"]["temperature_2m"]
# print(list_of_temp)
# avg_temp = sum(list_of_temp)/len(list_of_temp)
# print(avg_temp)