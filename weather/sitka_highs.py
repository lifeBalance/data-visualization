from pathlib import Path
import csv

# Instance of Path
path = Path('weather_data/sitka_weather_07-2021_simple.csv')

# Extract the content of the file, and split it in lines.
lines = path.read_text().splitlines()

# Create an instance of CSV reader (to parse the csv data)
reader = csv.reader(lines)  # Pass the lines to the constructor.
header_row = next(reader)   # Store 1st line in header_row (move cursor to 2nd)

# Print the fields in the Header.
for index, column_header in enumerate(header_row):
    print(index, column_header)