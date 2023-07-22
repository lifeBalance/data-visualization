from operator import itemgetter
from pathlib import Path
import json

import requests
import plotly.express as px

# Make an API call, and store the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
res = requests.get(url)
print(f"Status code: {res.status_code}")

# Process information about each submission.
submission_ids = res.json()  # Parse the JSON string into an array of ids.
# print(submission_ids)

# Make an API request for each id
submission_dicts = []
for id in submission_ids[:50]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
    r = requests.get(url)
    print(f"Submission ID: {id}\tStatus: {r.status_code}")
    response_dict = r.json()  # Parse the JSON string into a dictionary.
    print(response_dict)      # Print it!

    # Another way of checking if the 'descendants' key exists in dictionary.
    # try:
    #     comments = response_dict['descendants']
    # except KeyError:
    #     comments = 0
    # Build a dictionary for each submission.
    submission_dict = {
        "title": response_dict["title"],
        "author": response_dict["by"],
        "hn_link": f"https://news.ycombinator.com/item?id={id}",
        "comments": response_dict["descendants"]
        if "descendants" in response_dict # Shorter way: ternary operator.
        else 0,
    }
    submission_dicts.append(submission_dict)

# Order the submissions in the array by amount of comments in reverse, in order
# to get the most commented submissions at the top of our list.
submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

# Print the submissions.
for submission in submission_dicts:
    print(f"\nTitle: {submission['title']}")
    print(f"Author: {submission['author']}")
    print(f"Discussion: {submission['hn_link']}")
    print(f"Comments: {int(submission['comments'])}")

# Create a Path object for the file.
path = Path('./hn_submissions.json')
# Convert the array into a JSON string.
json_content = json.dumps(submission_dicts, indent=4)
# Write the JSON content to disk.
path.write_text(json_content)

authors, submission_links, comments, hover_texts = [], [], [], []
for submission in submission_dicts[:10]:
    link = submission['hn_link']
    title = submission['title']
    submission_links.append(f'<a href="{link}">{title}</a>')
    authors.append(submission['author'])
    comments.append(submission['comments'])
    hover_texts.append(submission['title'])

title = 'Top 10 Submissions in Hacker News (by number of Comments).'
labels = {'x': 'Author', 'y': 'Comments'}
# Make visualization (uses arrays to build x and y axes).
fig = px.bar(x=authors, y=comments, title=title, labels=labels, hover_name=hover_texts)
# Increase font size for axes titles.
fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20
)
# Customize how the data is represented (e.g. the color of the bars).
# Note: In plotly slang, a trace is a collection of data on a chart.
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()
