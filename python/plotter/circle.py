import matplotlib.pyplot as plt
import numpy as np

def plot_circle(center, radius):
    h, k = center

    # Create a range of theta values
    theta = np.linspace(0, 2*np.pi, 100)

    # Parametric equations for a circle
    x = h + radius * np.cos(theta)
    y = k + radius * np.sin(theta)

    # Plot the circle
    plt.plot(x, y, label="Circle")
    #for x, y in zip(x, y):
    #    plt.text(x, y, f'({x:.2f}, {y:.2f})', fontsize=8, ha='right', va='bottom')

    # Plot center
    plt.plot(h, k, 'ro', label="Center")
    plt.axis('equal')
    plt.title("Graph of the Circle")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.grid(True)
    plt.legend()
    plt.show()

# Get center and radius from user input
center_x = float(input("Enter the x-coordinate of the center: "))
center_y = float(input("Enter the y-coordinate of the center: "))
radius = float(input("Enter the radius of the circle: "))

# Plot the circle
plot_circle((center_x, center_y), radius)
