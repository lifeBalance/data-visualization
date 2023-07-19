from pathlib import Path
import json

# Instantiate a Path object
path = Path('eq_data/eq_data_1_day_m1.geojson')

# Read the text content into a variable, using the read_text method
contents = path.read_text()

# Convert the string contents into a Python representation (a single dictionary)
all_eq_data = json.loads(contents)
# print(type(all_eq_data)) # <class 'dict'>

# Create a more readable version of the file in our filesystem.
# path = Path('eq_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4) # Prettify the file.
# path.write_text(readable_contents) # Write the file to disk.

# Extract all the earthquakes from the dataset stored under the 'features' key.
all_eq_dicts = all_eq_data['features'] # 160 earthquakes.
# print(len(all_eq_dicts)) # 160

# Extract the magnitudes to a separate list.
mags = []
for eq in all_eq_dicts:
    mag = eq['properties']['mag'] # Magnitudes are nested under 'properties'.
    mags.append(mag)

print(mags[:10]) # Print a list with the last 10 magnitudes.
