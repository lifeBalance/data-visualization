from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Instance of Path
path = Path('weather_data/death_valley_2021_simple.csv') # whole year temp.

# Extract the content of the file, and split it in lines.
lines = path.read_text().splitlines()

# Create an instance of CSV reader (to parse the csv data)
reader = csv.reader(lines)  # Pass the lines to the constructor.
header_row = next(reader)   # Store 1st line in header_row (move cursor to 2nd)

# Check order of headers!
# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# Extract dates and high and low temperatures.
dates, highs, lows = [], [], []

# The reader object returns the lines one after another.
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    # Handle missing information in the dataset (sadly often).
    try:
        high = int(row[3]) # Adjust indices to order or headers in Death Valley file
        low = int(row[4])
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
ax.set_title('Daily High and Low Temperatures, 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # Plot dates diagonally to prevent overlapping.
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()