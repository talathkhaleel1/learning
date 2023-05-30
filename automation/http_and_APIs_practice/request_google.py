import requests
import json

response = requests.get("https://www.google.com/") # sending an http request to get a response
print(response.status_code)
print(response.url)
print(response.text) # to print the text part of the response - returns the html code of the webpage

try:
    response_error = requests.get("https://www.goolegoole.com/tyuyio")
    print(response_error)
except Exception:
    print("Sorry, did not connect.")

