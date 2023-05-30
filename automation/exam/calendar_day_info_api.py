import requests, json
from flask import Flask, request, jsonify

app = Flask("Calendar day info")


year = 2021
country = "US"

@app.route("/date")
def get_holiday_name():
    global year, country
    response_holiday_list = requests.get("https://date.nager.at/api/v3/PublicHolidays/"+ str(year) + "/" + country)
    us_list_of_holidays = json.loads(response_holiday_list.text)
    for i in range(len(us_list_of_holidays)):
        us_holiday_details = us_list_of_holidays[i]
        date = request.args["date"]
        if date == us_holiday_details["date"]:
            return jsonify(us_holiday_details["name"], us_holiday_details["localName"])
        return "No holiday recorded on this date."

#ip stated for checking : http://127.0.0.1:5000/date?date=2021-01-01