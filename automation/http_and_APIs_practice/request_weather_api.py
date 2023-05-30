import requests
# from lxml import etree
import json

# Some APIs require registration prior to getting data from them while others do not.\
# The keywords to know this is Create an account and register. Also a link is specified \
# where this can be done

latitude  = 51.5072
longitude = 0.1276 # co-ordinates of London
# in case you need co-ordinates of a place look for them in google and you can assign those co-ordinates

response = requests.get("http://www.7timer.info/bin/astro.php?lon=" + str(longitude) +\
                        "&lat=" + str(latitude) + "&ac=0&lang=en&unit=metric&output=json&tzshift=0")
# no spaces after or before quote marks in the url
# edit in parameters for "output = json" to get a json file
response_in_json_format = json.loads(response.text) # json.loads is the parse for json file
print(response_in_json_format["dataseries"]) # returns values associated with key "dataseries"
print(response_in_json_format["dataseries"][0]) # returns first element from the dataseries
print(response_in_json_format["dataseries"][0]["wind10m"]["direction"]) # value of a nested keys in the first element of the dataseries




### xml get request ###
# response = requests.get("http://www.7timer.info/bin/astro.php?lon=113.17&lat=23.09&ac=0&lang=en&unit=metric&output=xml&tzshift=0")
# # edit in parameters for "output = xml" to get a json file
# tree = etree.parse(response.text)
# print(tree.xpath("product name/dataseries/data/wind10m_direction/text()"))