from random import choice # The choice function chooses a random list item

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize the attributes of the walk instance."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Decide which direction to go, and how far in that direction."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Call get_step method for x and y coordinates.
            x_step = self.get_step()
            y_step = self.get_step()

            # Rejects moves that go nowwhere (don't add them to the walk)
            if x_step == 0 and y_step == 0:
                continue # loop again for a proper step, son

            # Calculate the new position. Start at the last position (-1) in
            # the x and y coordinates, and move the corresponding step.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
