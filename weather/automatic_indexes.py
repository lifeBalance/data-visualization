from pathlib import Path
import csv
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt

# Instance of Path (Switch the paths below to check script work with both files)
# path = Path('weather_data/sitka_weather_2021_simple.csv') # whole year temp.
path = Path('weather_data/death_valley_2021_simple.csv') # whole year temp.

# Extract the content of the file, and split it in lines.
lines = path.read_text().splitlines()

# Create an instance of CSV reader (to parse the csv data)
reader = csv.reader(lines)  # Pass the lines to the constructor.
header_row = next(reader)   # Store 1st line in header_row (move cursor to 2nd)

# Extract dates and high and low temperatures.
dates, highs, lows = [], [], []

# Find the indices of the maximum and minimum temperatures
tmax_idx = header_row.index('TMAX')
tmin_idx = header_row.index('TMIN')

# Find the Station name
station_name_idx = header_row.index('NAME')

# The reader object returns the lines one after another.
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    station_name = ''
    try:
        if station_name == '':
            station_name = row[station_name_idx]
        high = int(row[tmax_idx]) # Cast string to integer.
        low = int(row[tmin_idx])
    except ValueError:
        print(f'Missing data for {current_date}')
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

# Plot the high temperatures in a line graph.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5) # Draw lines with some transparency
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title(f'{station_name.capitalize()}\n Daily High and Low Temperatures, 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # Plot dates diagonally to prevent overlapping.
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

# Set scale of y-axis to match the Sitka scale
plt.ylim(10, 140)
# ax.set_ylim(10, 140) Another way of accomplishing line above. 
plt.yticks(np.arange(10, 140, 10))

plt.show()