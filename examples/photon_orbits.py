# examples/photon_orbits.py
from src.integrator import integrate_photon_bundle
from src.physics import B_CRIT
from src.visualization import demo_plot

if __name__ == "__main__":
    b_vals = [1.20*B_CRIT, 1.00*B_CRIT, 0.80*B_CRIT]
    rays = integrate_photon_bundle(b_vals)
    demo_plot(rays)
