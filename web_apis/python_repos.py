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
# print(type(res)) # <class 'requests.models.Response'>

# The json method parses the response body (a JSON string) into a dictionary.
response_dict = res.json()

# Print the information
print(f'Total repositories: {response_dict["total_count"]}')
print(f'Complete results: {not response_dict["incomplete_results"]}')

# Extract some attributes to separate variables.
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

# Examine the 1st repo.
first_repo = repo_dicts[0]
# print(f'Keys: {first_repo.keys()}') # Check all available keys (first level).

print("\nSelected information about the first repository:")
print(f"Name: {first_repo['name']}")
print(f"Owner: {first_repo['owner']['login']}")
print(f"URL: {first_repo['html_url']}")
print(f"Created: {first_repo['created_at']}")
print(f"Updated: {first_repo['updated_at']}")
print(f"Description: {first_repo['description']}")
