import matplotlib.pyplot as plt

from modified_random_walk import RandomWalk

# Keep making new random walks, until the user quits.

while True:
    # Generate data of a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=96) # 1920x1080=96dpi

    # Generate a list of numbers with the same amounts of points in the walk.
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors="none",
        s=1,
    )
    ax.set_aspect("equal")

    # Emphasize first and last points of the walk
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)
    
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
