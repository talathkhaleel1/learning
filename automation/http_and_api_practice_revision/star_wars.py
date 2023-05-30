# Get Star Wars information, using the given API: https://swapi.dev/
#
# Create a program:
#
# Asks for a name
# Searches for the characters with that name using the endpoint https://swapi.dev/api/people/?search=name
# It should list the following information:
# name
# height
# mass
# hair color
# skin color
# eye color

import requests, json


character_name = "Luke Skywalker"
response = requests.get("https://swapi.dev/api/people/?search=" + character_name)
star_war_data = json.loads(response.text)

def get_all_star_war_characters_details(star_war_data):
    star_war_character_details = star_war_data["results"]
    return star_war_character_details
all_star_war_characters_details = get_all_star_war_characters_details(star_war_data)


def get_requested_star_war_character_detail(all_star_war_characters_details):
    for i in range(len(all_star_war_characters_details)):
        star_war_character_dictionary = all_star_war_characters_details[i]
        return "name: ", star_war_character_dictionary["name"],\
               "height: ", star_war_character_dictionary["height"],\
               "mass: ", star_war_character_dictionary["mass"],\
               "hair color: ", star_war_character_dictionary["hair_color"],\
               "skin color: ", star_war_character_dictionary["skin_color"],\
               "eye color: ", star_war_character_dictionary["eye_color"]
star_war_specific_character_details = get_requested_star_war_character_detail(all_star_war_characters_details)

print(star_war_specific_character_details)


