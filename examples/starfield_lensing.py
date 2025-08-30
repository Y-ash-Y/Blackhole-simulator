# examples/starfield_lensing_demo.py
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from src.integrator import integrate_single_ray
from src.physics import B_CRIT

# Image settings
WIDTH, HEIGHT = 200, 200
FOV = np.deg2rad(90)   # 90-degree field of view
OBS_R = 50.0           # observer distance from BH (M=1 units)

def background_color(theta, phi):
    """
    Very simple synthetic 'sky':
    - Blue upper half, orange lower half
    - Vertical stripes in phi
    """
    if theta < np.pi/2:  # upper hemisphere
        base = np.array([0.1, 0.3, 0.8])  # blue
    else:
        base = np.array([0.9, 0.5, 0.1])  # orange
    stripe = (np.sin(5*phi) > 0) * 0.2  # stripe modulation
    return np.clip(base + stripe, 0, 1)

def render():
    image = np.zeros((HEIGHT, WIDTH, 3))

    # Camera pixel grid in [-1,1]
    xs = np.linspace(-1, 1, WIDTH)
    ys = np.linspace(-1, 1, HEIGHT)

    for j, y in enumerate(tqdm(ys, desc="Rendering")):
        for i, x in enumerate(xs):
            # Map pixel → impact parameter b
            # Approximate: b ~ OBS_R * tan(angle)
            angle = np.sqrt(x**2 + y**2) * (FOV/2)
            b = OBS_R * np.tan(angle)

            # Integrate ray
            try:
                ray = integrate_single_ray(b)
                if ray.regime == "captured":
                    color = np.array([0,0,0])  # inside horizon
                else:
                    # Escape: map to "sky" based on final angle
                    phi_end = ray.phi[-1]
                    r_end = ray.r[-1]
                    theta = np.pi/2  # equatorial simplification
                    color = background_color(theta, phi_end)
            except Exception as e:
                color = np.array([1,0,1])  # magenta error pixels

            image[j, i, :] = color

    return image

if __name__ == "__main__":
    img = render()
    plt.imshow(img, origin="lower")
    plt.title("Synthetic Starfield Lensing (Schwarzschild BH)")
    plt.axis("off")
    plt.savefig("outputs/lensing_demo.png", dpi=150)
    plt.show()
