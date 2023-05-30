import requests, json
from flask import Flask, request,jsonify, render_template

app = Flask("holiday_us")

year = 2021
country = "US"

@app.route("/date")
def get_holiday_name():
    global year, country
    response_holiday_list = requests.get("https://date.nager.at/api/v3/PublicHolidays/"+ str(year) + "/" + country)
    us_list_of_holidays = json.loads(response_holiday_list.text)
    day = request.args["day"]
    month = request.args["month"]
    



response_date_and_nameday_list = requests.get("https://nameday.abalin.net/namedays")
list_of_namedays = json.loads(response_date_and_nameday_list.text)
print(list_of_namedays)








