# Plotting utilities for black hole simulation
import matplotlib.pyplot as plt

def plot_trajectory(x, y, r_s):
    plt.figure(figsize=(6,6))
    plt.plot(x, y, label="Photon Path")
    circle = plt.Circle((0, 0), r_s, color='black', label='Event Horizon')
    plt.gca().add_artist(circle)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Photon Trajectory around Schwarzschild Black Hole")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()
