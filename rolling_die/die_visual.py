from die import Die
import plotly.express as px

# Create a .
die = Die() # No need to pass args to constructor, 6 sides by default.

# make some rolls, and store the results in a list.
results = []
for roll_num in range(1000):
    roll = die.roll() # random integer between 1 an 6.
    results.append(roll)

# Analyze the results.
frequencies = []
poss_results = range(1, die.num_sides+1) # num_sides+1 because 2nd arg. not included
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)
# Visualize the results
fig = px.bar(x=poss_results, y=frequencies)
fig.show()