import matplotlib.pyplot as plt # alias the pyplot module to plt (convention)

square_seq = [1, 4, 9, 16, 25] # 1st 5 terms of a square number sequence.

# Unpack return value of a call to the subplots method:
# - fig represents the entire figure (collection of plots).
# - ax represents a single plot in the figure.
fig, ax = plt.subplots()

# The plot method call tries to plot the data given as argument.
ax.plot(square_seq)

plt.show()
# If when you try to run the script (python mpl_squares.py) you get the error:
#
#   UserWarning: Matplotlib is currently using agg, which is a non-GUI backend,
#   so cannot show the figure.
#
# You need to install a GUI backend; in Fedora you'd do:
#
#   sudo dnf install python3-tkinter