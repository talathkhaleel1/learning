# Display gifs of a cute/funny topic using: https://developers.giphy.com/docs/
#
# Obtain an API key
# Create a program that:
# Asks for user input
# Using the user input term searches the images in the API
# Generates an HTML file consisting the first 16 results as <img> tags

import requests, json

images = input("Specify the kind of gify you want:")
api_key ="W2vKTkTqC9GHlmlXySI1h8SvbOGkTwhd"
response = requests.get("https://api.giphy.com/v1/gifs/search?api_key="+ api_key +"&q="+images)
cute_images = json.loads(response.text)
print(cute_images)

def get_gif_data_dictionary(cute_images):# unpack dictionary from list
    gif_list_of_urls = []
    for i in range(len(cute_images)):# unpack dictionary from list
        gif_list_of_urls.append(cute_images[i]["images"]["preview_gif"]["url"])
    return gif_list_of_urls
print(get_gif_data_dictionary(cute_images))



