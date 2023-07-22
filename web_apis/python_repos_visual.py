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
repos = response_dict["items"]  # Repos are under the 'items' key.

# Repo links array for the x-axis, stars array for the y-axis.
repo_links, stars, hover_texts = [], [], []
# Traverse the array of repos, extracting names and stars to separate arrays.
for repo in repos:
    # Build the links to the repos using the url and repo name.
    repo_name = repo["name"]
    repo_url = repo['html_url']
    repo_links.append(f'<a href="{repo_url}">{repo_name}</a>')
    stars.append(repo["stargazers_count"])

    # Build hover texts.
    owner = repo["owner"]["login"]
    description = repo["description"]
    hover_texts.append(f"{owner}<br />{description}")

title = "Most-Starred Python Projects on GitHub"
labels = {"x": "Repository", "y": "Stars"}
# Make visualization (uses arrays to build x and y axes).
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
# Increase font size for axes titles.
fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20
)
# Customize how the data is represented (e.g. the color of the bars).
# Note: In plotly slang, a trace is a collection of data on a chart.
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()
