import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/31353677.json'
res = requests.get(url)
print(f'Status code: {res.status_code}')

# Explore the structure of the data.
res_dict = res.json() # Parse the JSON string into a dictionary.
res_formatted = json.dumps(res_dict, indent=4) # Again to JSON string, but formatted.
print(res_formatted) # Print the pretty JSON string.