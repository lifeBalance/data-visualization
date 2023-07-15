import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Generate data of a random walk.
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=14)
ax.set_aspect('equal')
plt.show()