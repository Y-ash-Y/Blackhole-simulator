# physics.py – GR constants & basic metric helpers (Schwarzschild first)
import numpy as np

# Geometric units (G=c=1)
M = 1.0                     # black hole mass
RS = 2.0 * M                # Schwarzschild radius
B_CRIT = 3.0 * np.sqrt(3.0) * M  # critical impact parameter (b_crit = 3√3 M)

def binet_rhs(phi, y):
    """
    ODE for null geodesics in the equatorial plane using Binet’s form:
      u'' + u = 3 M u^2, with u(φ) = 1/r(φ)
    y = [u, u']  → y' = [u', 3 M u^2 - u]
    """
    u, up = y
    return np.array([up, 3.0 * M * u*u - u])

def r_from_u(u):
    # Protect against division by zero or tiny negatives from roundoff
    u = max(u, 1e-15)
    return 1.0 / u
