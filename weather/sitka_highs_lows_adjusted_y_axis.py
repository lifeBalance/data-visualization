from pathlib import Path
import csv
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt

# Instance of Path
path = Path('weather_data/sitka_weather_2021_simple.csv') # whole year temp.

# Extract the content of the file, and split it in lines.
lines = path.read_text().splitlines()

# Create an instance of CSV reader (to parse the csv data)
reader = csv.reader(lines)  # Pass the lines to the constructor.
header_row = next(reader)   # Store 1st line in header_row (move cursor to 2nd)

# Extract dates and high and low temperatures.
dates, highs, lows = [], [], []

# The reader object returns the lines one after another.
for row in reader:
    high = int(row[4]) # Cast string to integer.
    low = int(row[5])
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
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
ax.set_title('Daily High and Low Temperatures, 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # Plot dates diagonally to prevent overlapping.
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

# Set scale of y-axis to match the Sitka scale
plt.ylim(10, 140)
# ax.set_ylim(10, 140) Another way of accomplishing line above. 
plt.yticks(np.arange(10, 140, 10))

plt.show()