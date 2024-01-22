import matplotlib.pyplot as plt
import numpy as np

def plot_ellipse(center, semi_major, semi_minor):
    h, k = center

    # Create a range of theta values
    theta = np.linspace(0, 2*np.pi, 100)

    # Parametric equations for an ellipse
    x = h + semi_major * np.cos(theta)
    y = k + semi_minor * np.sin(theta)

    # Plot the ellipse
    plt.plot(x, y, label="Ellipse")

    # Annotate each point with its coordinates
    #for xi, yi in zip(x, y):
    #    plt.text(xi, yi, f'({xi:.2f}, {yi:.2f})', fontsize=8, ha='right', va='bottom')

    # Plot center
    plt.plot(h, k, 'ro', label="Center")

    plt.title("Graph of the Ellipse")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")

    # Set equal aspect ratio
    plt.axis('equal')

    plt.grid(True)
    plt.legend()
    plt.show()

# Get center and semi-axes from user input
center_x = float(input("Enter the x-coordinate of the center: "))
center_y = float(input("Enter the y-coordinate of the center: "))
semi_major = float(input("Enter the semi-major axis length: "))
semi_minor = float(input("Enter the semi-minor axis length: "))

# Plot the ellipse with coordinates
plot_ellipse((center_x, center_y), semi_major, semi_minor)
