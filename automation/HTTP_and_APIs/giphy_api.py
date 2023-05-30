# Display gifs of a cute/funny topic using: https://developers.giphy.com/docs/
#
# Obtain an API key (This is obtained by registering on the website, as in authorisation)
# Create a program that:
# Asks for user input
# Using the user input term searches the images in the API
# Generates an HTML file consisting the first 16 results as <img> tags

import requests
import json

images = input("Please specify the image type you desire to see: ")
cute_or_funny_gifs = requests.get("https://api.giphy.com/v1/gifs/search?api_key=W2vKTkTqC9GHlmlXySI1h8SvbOGkTwhd&q=images")
# print(cute_or_funny_gifs.text)
cute_funny_gifs = json.loads(cute_or_funny_gifs.text)
print(cute_funny_gifs)

def list_of_gifs_data(cute_funny_gifs):# unpack list from dictionary
    gifs_data = cute_funny_gifs["data"]
    return gifs_data
print (list_of_gifs_data(cute_funny_gifs)) #gifs_data =

gifs_data = (list_of_gifs_data(cute_funny_gifs))
def get_gif_data_dictionary(gifs_data):# unpack dictionary from list
    gif_list_of_urls = []
    for i in range(len(gifs_data)):# unpack dictionary from list
        gif_list_of_urls.append(gifs_data[i]["images"]["preview_gif"]["url"])
    return gif_list_of_urls
print(get_gif_data_dictionary(gifs_data))

url_image_links = (get_gif_data_dictionary(gifs_data))
def store_image_links(url_image_links):
    images_links = ""
# <img src="link..."> # try printing the first one
# print('<img src="' + url_image_links[0] + '">')
    for url in url_image_links:
        images_links += '<img src="' + str(url) + '">'
    return images_links
image_links = store_image_links(url_image_links)

#need to write a function in which all the above functions and below html file are called and actioned

html_file = '<!doctype html><html><head></head><body>' + image_links + '</body></html>'
file = open("gif.html", "w")
file.write(html_file)
