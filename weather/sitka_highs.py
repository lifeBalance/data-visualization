from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Instance of Path
path = Path('weather_data/sitka_weather_2021_simple.csv') # whole year temp.

# Extract the content of the file, and split it in lines.
lines = path.read_text().splitlines()

# Create an instance of CSV reader (to parse the csv data)
reader = csv.reader(lines)  # Pass the lines to the constructor.
header_row = next(reader)   # Store 1st line in header_row (move cursor to 2nd)

# Extract dates and high temperatures.
dates, highs = [], []

# The reader object returns the lines one after another.
for row in reader:
    high = int(row[4]) # Cast string to integer.
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    highs.append(high)
    dates.append(current_date)

# print(highs)
# Plot the high temperatures in a line graph.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Format plot.
ax.set_title('Daily High Temperatures, 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # Plot dates diagonally to prevent overlapping.
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()