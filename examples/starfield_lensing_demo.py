# examples/starfield_lensing_demo.py
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tqdm import tqdm
from src.integrator import integrate_single_ray

# Settings
WIDTH, HEIGHT = 300, 300   # output resolution
FOV = np.deg2rad(90)       # 90° field of view
OBS_R = 50.0               # observer radius (far away)

# Load starfield image (equirectangular)
STARFIELD_PATH = "examples\Figure_1.png"
sky_img = Image.open(STARFIELD_PATH).convert("RGB")
sky_arr = np.array(sky_img)
sky_h, sky_w, _ = sky_arr.shape

def sample_sky(theta, phi):
    """
    Map spherical coords (theta, phi) to pixel in starfield.
    theta ∈ [0, π], phi ∈ [0, 2π]
    """
    u = (phi % (2*np.pi)) / (2*np.pi)   # normalize [0,1]
    v = theta / np.pi                   # normalize [0,1]
    px = int(u * (sky_w-1))
    py = int((1-v) * (sky_h-1))         # flip v so north is up
    return sky_arr[py, px, :] / 255.0

def render():
    image = np.zeros((HEIGHT, WIDTH, 3))

    xs = np.linspace(-1, 1, WIDTH)
    ys = np.linspace(-1, 1, HEIGHT)

    for j, y in enumerate(tqdm(ys, desc="Rendering")):
        for i, x in enumerate(xs):
            # Pixel → impact parameter
            angle = np.sqrt(x**2 + y**2) * (FOV/2)
            b = OBS_R * np.tan(angle)

            try:
                ray = integrate_single_ray(b)
                if ray.regime == "captured":
                    color = np.array([0,0,0])  # black hole shadow
                else:
                    # Final escape direction
                    phi_end = ray.phi[-1]
                    theta = np.pi/2  # equatorial approx
                    color = sample_sky(theta, phi_end)
            except:
                color = np.array([1,0,1])  # magenta debug

            image[j, i, :] = color

    return image

if __name__ == "__main__":
    img = render()
    plt.imshow(img, origin="lower")
    plt.title("Black Hole Lensing of Real Starfield")
    plt.axis("off")
    plt.savefig("outputs/lensing_starfield.png", dpi=150)
    plt.show()
