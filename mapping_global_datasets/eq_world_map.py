from pathlib import Path
import json

import plotly.express as px

# Instantiate a Path object
path = Path('eq_data/eq_data_1_day_m1.geojson')

# Read the text content into a variable, using the read_text method
contents = path.read_text()

# Convert the string contents into a Python representation (a single dictionary)
all_eq_data = json.loads(contents)

# Extract all the earthquakes from the dataset stored under the 'features' key.
all_eq_dicts = all_eq_data['features'] # 160 earthquakes.

# Empty lists for the magnitudes, longitudes and latitudes.
mags, lons, lats = [], [], []
for eq in all_eq_dicts:
    mag = eq['properties']['mag'] # Magnitudes are nested under 'properties'.
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, title=title)
fig.show()