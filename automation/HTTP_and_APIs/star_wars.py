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

hero = "Ankin"
star_wars_characters = requests.get("https://swapi.dev/api/people/?search=hero")
star_wars_dictionary =json.loads(star_wars_characters.text)



def star_wars_results_dictionary(star_wars_dictionary):
    character_all_details = star_wars_dictionary["results"]
    return character_all_details


# character_complete_details =(star_wars_results_dictionary(star_wars_dictionary))


def character_requested_details(character_complete_details):
    for i in range(len(character_complete_details)):
        star_war_charcter_details = character_complete_details[i]# unpack dictionary from list
        return "name: ", star_war_charcter_details["name"],\
               "height: ", star_war_charcter_details["height"],\
               "mass: ", star_war_charcter_details["mass"],\
               "hair color: ", star_war_charcter_details["hair_color"],\
               "skin color: ", star_war_charcter_details["skin_color"],\
               "eye color: ", star_war_charcter_details["eye_color"]

def character_details_according_to_name_specified(dictionary_name):
    character_complete_details = (star_wars_results_dictionary(dictionary_name))
    name_specific_character_details = (character_requested_details(character_complete_details))
    return name_specific_character_details

print(character_details_according_to_name_specified(star_wars_dictionary))


