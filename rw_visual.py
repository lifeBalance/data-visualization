import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new random walks, until the user quits.

while True:
    # Generate data of a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use("classic")
    fig, ax = plt.subplots()
    # Generate a list of numbers with the same amounts of points in the walk.
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors="none",
        s=14,
    )
    ax.set_aspect("equal")
    # Emphasize first and last points of the walk
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break