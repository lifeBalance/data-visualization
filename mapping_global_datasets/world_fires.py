from pathlib import Path
import csv

import plotly.express as px

# Instantiate a Path object
path = Path("data/world_fires_1_day.csv")

# Read the text content into a variable, using the read_text method
contents = path.read_text()

# Extract the content of the file, and split it in lines.
lines = path.read_text().splitlines()

# Create an instance of CSV reader (to parse the csv data)
reader = csv.reader(lines)  # Pass the lines to the constructor.
header_row = next(reader)   # Store 1st line in header_row (move cursor to 2nd)

# Find the name of the brightness
longitude_idx = header_row.index('longitude')
latitude_idx = header_row.index('latitude')
brightness_idx = header_row.index('brightness')

# Empty lists for the magnitudes, longitudes, latitudes, and earthquake names.
brightness, longitudes, latitudes = [], [], []
for row in reader:
    brightness.append(float(row[brightness_idx]))
    longitudes.append(float(row[longitude_idx]))
    latitudes.append(float(row[latitude_idx]))


title = 'World Fires'
fig = px.scatter_geo(
    lat=latitudes,
    lon=longitudes,
    size=brightness,
    title=title,
    color=brightness,
    range_color=[300, 400],
    color_continuous_scale="Inferno",   # from dark blue to bright yellow.
    labels={"color": "Brightness"},     # Label for the color scale.
    projection='natural earth',         # Round the ends of the map.
)

# To see the available color scales, run:
print(px.colors.named_colorscales())
print(px.colors.named_colorscales().index('viridis'))

fig.show()
