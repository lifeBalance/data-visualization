from pathlib import Path
import csv

# Instance of Path
path = Path('weather_data/sitka_weather_07-2021_simple.csv')

# Extract the content of the file, and split it in lines.
lines = path.read_text().splitlines()

# Create an instance of CSV reader (to parse the csv data)
reader = csv.reader(lines)  # Pass the lines to the constructor.
header_row = next(reader)   # Store 1st line in header_row (move cursor to 2nd)

# Extract the high temperatures.
highs = []
print('typeof reader', type(reader)) # <class '_csv.reader'>

# The reader object returns the lines one after another.
for row in reader:
    high = int(row[4]) # Cast string to integer.
    highs.append(high)

print(highs)