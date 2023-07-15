import matplotlib.pyplot as plt # alias the pyplot module to plt (convention)

input_values = [1, 2, 3, 4, 5]  # values used for x axis
# 1st 5 terms of a square number sequence.
square_seq = [1, 4, 9, 16, 25]  # values used for y axis

# Set the theme
plt.style.use('seaborn')

# Unpack return value of a call to the subplots method:
# - fig represents the entire figure (collection of plots).
# - ax represents a single plot in the figure.
fig, ax = plt.subplots()

# Plot the point at coordinates 2, 4.
ax.scatter(2, 4, s=200)

# Set chart title and label axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()
