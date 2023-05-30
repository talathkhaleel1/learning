import requests, json
from flask import Flask, request, jsonify, render_template


character_name = ""
response = requests.get("https://swapi.dev/api/people/?search=" + character_name)
star_war_data = json.loads(response.text)

def get_all_star_war_characters_details(star_war_data):
    star_war_character_details = star_war_data["results"]
    return star_war_character_details
all_star_war_characters_details = get_all_star_war_characters_details(star_war_data)
print(all_star_war_characters_details)

app = Flask("Star wars")

@app.route("/character")
def get_character_details(): # query parameter
    for i in range(len(all_star_war_characters_details)):
        star_war_dictionary = all_star_war_characters_details[i]
        character = request.args["character"]
        if character == star_war_dictionary["name"]:
            return star_war_dictionary["url"]

@app.route("/name/<name>")
def get_films(name):
    for i in range(len(all_star_war_characters_details)):
        star_war_dictionary = all_star_war_characters_details[i]
        if name == star_war_dictionary["name"]:
            return star_war_dictionary["birth_year"]

@app.route("/html")
def render_html():
    return render_template("star_war.html", character = 'C-3PO')
