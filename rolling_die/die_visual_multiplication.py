from die import Die
import plotly.express as px # px is an alias for the plotly.express module

# Create a .
die_1 = Die() # No need to pass args to constructor, 6 sides by default.
die_2 = Die()

# make some rolls, and store the results in a list.
results = []
for roll_num in range(3000):
    roll = die_1.roll() * die_2.roll() # Let's multiply the results
    results.append(roll)

# Store the frequency of each value (1 to 6) in a list.
frequencies = []

# If we want to generate a range from 1 to 6, the 2nd argument to the range
# function must be 7, because upper boundary is not inclusive!
max_result = die_1.num_sides * die_2.num_sides # 36 (when we get 2 sixes)
possible_results = range(2, max_result+1) # range from 2 to 36.

# Traverse the 1 to 6 range, and count how many time each value appears in results.
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# Visualize the results
title = 'Results of Rolling two D6 Die 3,000 times, multiplying the results.'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)

# Show a label for each bar
fig.update_layout(xaxis_dtick=1)

fig.show()