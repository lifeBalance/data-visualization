from pathlib import Path
import json

import plotly.express as px

# Instantiate a Path object
path = Path("eq_data/eq_data_30_day_m1.json")

# Read the text content into a variable, using the read_text method
contents = path.read_text()

# Convert the string contents into a Python representation (a single dictionary)
all_eq_data = json.loads(contents)

# Extract all the earthquakes from the dataset stored under the 'features' key.
all_eq_dicts = all_eq_data["features"]  # 160 earthquakes.

# Empty lists for the magnitudes, longitudes, latitudes, and earthquake names.
mags, lons, lats, eq_titles = [], [], [], []
for eq in all_eq_dicts:
    mags.append(eq["properties"]["mag"])
    lons.append(eq["geometry"]["coordinates"][0])
    lats.append(eq["geometry"]["coordinates"][1])
    eq_titles.append(eq['properties']['title'])

title = all_eq_data['metadata']['title']
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title=title,
    color=mags,
    color_continuous_scale="Viridis",   # from dark blue to bright yellow.
    labels={"color": "Magnitude"},      # Label for the color scale.
    projection='natural earth',         # Round the ends of the map.
    hover_name=eq_titles,               # Show eq name on hover.
)

# To see the available color scales, run:
print(px.colors.named_colorscales())

fig.show()
