# integrator.py – ODE wrappers & events
import numpy as np
from dataclasses import dataclass
from typing import List
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from .physics import M, RS, B_CRIT, binet_rhs, r_from_u

RTOL, ATOL = 1e-9, 1e-12
R_INFINITY = 500.0
PHI_SPAN = 20.0

@dataclass
class Ray:
    b: float
    phi: np.ndarray
    r: np.ndarray
    x: np.ndarray
    y: np.ndarray
    regime: str  # "deflected" | "critical" | "captured"

def _events():
    def at_infinity(phi, y):
        r = r_from_u(y[0])
        return r - R_INFINITY
    at_infinity.terminal = False
    at_infinity.direction = 0

    def at_horizon(phi, y):
        r = r_from_u(y[0])
        return r - RS
    at_horizon.terminal = True
    at_horizon.direction = -1

    return (at_infinity, at_horizon)

def _closest_approach_from_b(b: float):
    """
    Solve for r_min given impact parameter b using cubic equation:
       r^3 - b^2 r + 2 M b^2 = 0
    For b >= B_CRIT, returns real root r > 2M (closest approach).
    For b < B_CRIT, returns None (no turning point, capture).
    """
    if b < B_CRIT:
        return None

    # Coefficients of cubic: r^3 - b^2 r + 2 M b^2 = 0
    coeffs = [1.0, 0.0, -b**2, 2.0*M*b**2]
    roots = np.roots(coeffs)

    # Pick the real root greater than horizon
    real_roots = [r.real for r in roots if abs(r.imag) < 1e-8]
    candidates = [r for r in real_roots if r > RS]
    if not candidates:
        raise RuntimeError(f"No valid turning point found for b={b}")
    return min(candidates)  # the closest approach


def integrate_single_ray(b: float) -> Ray:
    evts = _events()

    if b > B_CRIT*(1 + 1e-6):
        regime = "deflected"
        rmin = _closest_approach_from_b(b)
        u0 = 1.0 / rmin
        y0 = np.array([u0, 0.0])
        span = (-PHI_SPAN, PHI_SPAN)

    elif abs(b - B_CRIT) <= 1e-6:
        regime = "critical"
        u0 = 1.0 / (3.0*M)                 # photon sphere
        y0 = np.array([u0*(1 + 1e-6), 0.0]) # slight nudge from perfect orbit
        span = (-PHI_SPAN, PHI_SPAN)

    else:
        regime = "captured"
        # Start far away on the left and integrate to center to get a reasonable mid-state,
        # then integrate symmetrically about 0 to visualize the plunge.
        phi0 = -PHI_SPAN
        u0, up0 = 1e-6, 1.0/b               # rough asymptotic slope ~ 1/b
        mid = solve_ivp(binet_rhs, (phi0, 0.0), [u0, up0], rtol=RTOL, atol=ATOL, events=evts)
        y0 = mid.y[:, -1]
        span = (-PHI_SPAN/2, PHI_SPAN/2)

    sol = solve_ivp(binet_rhs, span, y0, rtol=RTOL, atol=ATOL, events=evts)
    phi = sol.t
    u = np.maximum(sol.y[0], 1e-15)
    r = 1.0 / u
    x, y = r*np.cos(phi), r*np.sin(phi)
    return Ray(b=b, phi=phi, r=r, x=x, y=y, regime=regime)

def integrate_photon_bundle(b_list: List[float]) -> List[Ray]:
    return [integrate_single_ray(b) for b in b_list]
