import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny") # getting response object in variable page
print(type(page))
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched
print("------")
x = page.json() # short form of json.loads(page.text) , turn page.text into a python object
print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2)) # pretty print the results