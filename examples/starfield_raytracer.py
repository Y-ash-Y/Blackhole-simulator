# examples/starfield_raytracer.py
"""
Black Hole Ray Tracer (Full 3D directions)
------------------------------------------
- Observer at r_obs = 50M
- Camera with FOV, resolution
- For each pixel: launch ray backward, integrate
- Output: distorted starfield with Einstein ring
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tqdm import tqdm
from src.integrator import integrate_single_ray
from src.physics import RS

# -----------------------
# Settings
# -----------------------
WIDTH, HEIGHT = 400, 400     # output resolution
FOV = np.deg2rad(90)         # field of view
OBS_R = 50.0                 # observer distance

# Load background starfield (equirectangular)
STARFIELD_PATH = "examples\Figure_1.png"
sky_img = Image.open(STARFIELD_PATH).convert("RGB")
sky_arr = np.array(sky_img)
sky_h, sky_w, _ = sky_arr.shape

def sample_sky(theta, phi):
    """
    Map spherical coords (theta, phi) to a pixel in the starfield.
    θ ∈ [0, π], φ ∈ [0, 2π]
    """
    u = (phi % (2*np.pi)) / (2*np.pi)     # [0,1]
    v = theta / np.pi                     # [0,1]
    px = int(u * (sky_w - 1))
    py = int((1 - v) * (sky_h - 1))       # flip so north is up
    return sky_arr[py, px, :] / 255.0

# -----------------------
# Camera → Ray
# -----------------------
def pixel_to_ray(i, j):
    """
    Convert pixel (i,j) into an initial ray impact parameter.
    Returns b (impact parameter).
    NOTE: Full 3D version would also handle inclination.
    """
    # Normalized pixel coords in [-1,1]
    x = (2 * i / WIDTH - 1)
    y = (2 * j / HEIGHT - 1)

    # Convert to angle from center (small angle approx)
    angle = np.sqrt(x**2 + y**2) * (FOV/2)

    # Impact parameter
    b = OBS_R * np.tan(angle)
    return b, np.arctan2(y, x)

# -----------------------
# Rendering
# -----------------------
def render():
    image = np.zeros((HEIGHT, WIDTH, 3))

    for j in tqdm(range(HEIGHT), desc="Rendering"):
        for i in range(WIDTH):
            b, phi0 = pixel_to_ray(i, j)
            try:
                ray = integrate_single_ray(b)
                if ray.regime == "captured":
                    color = np.array([0,0,0])
                else:
                    # Final escape direction
                    phi_end = ray.phi[-1]
                    theta = np.pi/2   # TODO: full θ integration
                    color = sample_sky(theta, phi_end)
            except:
                color = np.array([1,0,1])  # magenta = error
            image[j,i,:] = color

    return image

# -----------------------
# Main
# -----------------------
if __name__ == "__main__":
    img = render()
    plt.imshow(img, origin="lower")
    plt.title("Black Hole Lensing (Full Ray Tracer)")
    plt.axis("off")
    plt.savefig("outputs/lensing_raytracer.png", dpi=150)
    plt.show()
