from typing import KeysView
import requests

# URL of the github web API (too long, let's use two lines)
url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

# Set the headers of our request (check github docs).
headers = { 'Accept': 'application/vnd.github.v3+json' }

# Make the request agains the url, using the headers and store response in res.
res = requests.get(url, headers=headers)

# res is an instance of Response; let's print the value of the 'status_code' property.
print(f'Status code: {res.status_code}')

# By the way, res is an instance (an object) of the Response class.
print(type(res)) # <class 'requests.models.Response'>

# The json method parses the response body (a JSON string) into a dictionary.
response_dict = res.json()

# Print the keys
for key in response_dict.keys():
    print(f' - {key}')