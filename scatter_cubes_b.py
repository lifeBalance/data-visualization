import matplotlib.pyplot as plt # alias the pyplot module to plt (convention)

x_values = range(1, 5001)  # generate values from 1 to 5000 (5001 not included)
y_values = [x**3 for x in x_values]  # list comprehension

# Set the theme
plt.style.use('seaborn')

# Unpack return value of a call to the subplots method:
# - fig represents the entire figure (collection of plots).
# - ax represents a single plot in the figure.
fig, ax = plt.subplots()

# colormap with light green for low values and dark green for high values
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# Set chart title and label axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set the range for each axis. It takes an array of 4 values:
# - minimum value for x-axis
# - maximum value for x-axis
# - minimum value for y-axis
# - maximum value for y-axis
ax.axis([0, 5000, 0, 125_000_000_000])
ax.ticklabel_format(style='plain') # No scientific notation.

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show() # Show plot in viewes
