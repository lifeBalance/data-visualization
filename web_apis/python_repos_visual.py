import requests
import plotly.express as px

# URL of the github web API (too long, let's use two lines)
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

# Set the headers of our request (check github docs).
headers = {"Accept": "application/vnd.github.v3+json"}

# Make the request agains the url, using the headers and store response in res.
res = requests.get(url, headers=headers)

# res is an instance of Response; let's print the value of the 'status_code' property.
# Print status code to monitor any possible request/response issue.
print(f"Status code: {res.status_code}")

# The json method parses the response body (a JSON string) into a dictionary.
response_dict = res.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Extract array of repos
repos = response_dict['items'] # Repos are under the 'items' key.

repo_names, stars = [], []
# Traverse the array of repos, extracting names and stars to separate arrays.
for repo in repos:
    repo_names.append(repo['name'])
    stars.append(repo['stargazers_count'])

# Make visualization.
fig = px.bar(x=repo_names, y=stars)
fig.show()