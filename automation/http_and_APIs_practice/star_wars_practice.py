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

import requests
import json

hero = "Luke Skywalker"
star_wars_api_page = requests.get("https://swapi.dev/api/people/?search=hero")
star_wars_api_content = json.loads(star_wars_api_page.text)
# print(star_wars_api_content)

def get_results_list(star_wars_api_content):
    data_in_results_key = star_wars_api_content["results"]
    return data_in_results_key

# star_wars_results_key = get_results_list(star_wars_api_content)

def get_specific_star_wars_charcter_details(star_wars_results_key):
    for i in range(len(star_wars_results_key)):
        star_wars_dictionary = star_wars_results_key[i] # unpacking dictionary
        return "name: ", star_wars_dictionary["name"],\
               "height: ", star_wars_dictionary["height"],\
               "mass: ", star_wars_dictionary["mass"],\
               "hair_color: ", star_wars_dictionary["hair_color"],\
               "skin_color: ", star_wars_dictionary["skin_color"],\
               "eye_color: ", star_wars_dictionary["eye_color"]

# specific_character_details = get_specific_star_wars_charcter_details(star_wars_results_key)

def get_specific_character_details(dictionary):
    star_wars_results_key = get_results_list(dictionary)
    specific_character_details = get_specific_star_wars_charcter_details(star_wars_results_key)
    return specific_character_details

print(get_specific_star_wars_charcter_details(star_wars_api_content))
