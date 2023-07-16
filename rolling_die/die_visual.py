from die import Die
import plotly.express as px # px is an alias for the plotly.express module

# Create a .
die = Die() # No need to pass args to constructor, 6 sides by default.

# make some rolls, and store the results in a list.
results = []
for roll_num in range(1000):
    roll = die.roll() # random integer between 1 an 6.
    results.append(roll)

# Store the frequency of each value (1 to 6) in a list.
frequencies = []

# If we want to generate a range from 1 to 6, the 2nd argument to the range
# function must be 7, because upper boundary is not inclusive!
possible_results = range(1, die.num_sides+1) # 1, 2, 3, 4, 5, 6

# Traverse the 1 to 6 range, and count how many time each value appears in results.
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# Visualize the results
title = 'Results of Rolling one D6 1,000 times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)
fig.show()