import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def draw_cylinder(radius, height, num_sides=30):
    """
    Draws a 3D cylinder with the specified radius, height, and number of sides.

    Args:
        radius: The radius of the cylinder's base.
        height: The height of the cylinder.
        num_sides: The number of sides to approximate the cylinder's circular base.
    """

    # Generate the theta values for the circle
    theta = np.linspace(0, 2 * np.pi, num_sides)

    # Generate the x, y, and z coordinates for the top and bottom circles
    x_top = radius * np.cos(theta)
    y_top = radius * np.sin(theta)
    z_top = np.ones(num_sides) * height

    x_bottom = radius * np.cos(theta)
    y_bottom = radius * np.sin(theta)
    z_bottom = np.zeros(num_sides)

    # Create the figure and axes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the top and bottom circles
    ax.plot(x_top, y_top, z_top, color='blue')
    ax.plot(x_bottom, y_bottom, z_bottom, color='blue')

    # Plot the side of the cylinder
    for i in range(num_sides):
        ax.plot([x_top[i], x_bottom[i]], [y_top[i], y_bottom[i]], [z_top[i], z_bottom[i]], color='blue')

    # Set the axis labels and limits
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-radius - 1, radius + 1)
    ax.set_ylim(-radius - 1, radius + 1)
    ax.set_zlim(0, height + 1)

    # Show the plot
    plt.show()

# Example usage
radius = 2
height = 5
num_sides = 50
draw_cylinder(radius, height, num_sides)

draw_cylinder(2, 5, 50)