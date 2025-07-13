# Main script to run and plot a single photon trajectory
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from .constants import M, r_s
from .geodesics import geodesic_rhs
from .plot_utils import plot_trajectory

# Initial conditions
r0 = 10.0
phi0 = 0.0
t0 = 0.0
impact_parameter = 5.0
f = 1 - 2 * M / r0
dr_dlambda = -np.sqrt(f * (1 - (impact_parameter / r0)**2))
dphi_dlambda = impact_parameter / (r0**2)
dt_dlambda = 1.0 / f

y0 = [t0, r0, phi0, dt_dlambda, dr_dlambda, dphi_dlambda]

# Integrate geodesic
sol = solve_ivp(geodesic_rhs, [0, 100], y0, rtol=1e-8, atol=1e-10)

# Extract and plot
r = sol.y[1]
phi = sol.y[2]
x = r * np.cos(phi)
y = r * np.sin(phi)
plot_trajectory(x, y, r_s)
