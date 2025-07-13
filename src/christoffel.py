# Christoffel symbol calculation for Schwarzschild metric (equatorial plane)
from .constants import M, r_s

def christoffel(mu, alpha, beta, x):
    r = x[1]
    if r <= r_s:
        return 0  # Beyond event horizon
    f = 1 - 2 * M / r
    # Indices: 0=t, 1=r, 2=phi
    if mu == 1 and alpha == 0 and beta == 0:
        return M / (r**2) * f
    if mu == 1 and alpha == 1 and beta == 1:
        return -M / (r**2 * f)
    if mu == 1 and alpha == 2 and beta == 2:
        return -r * f
    if mu == 0 and alpha == 0 and beta == 1:
        return M / (r**2 * f)
    if mu == 0 and alpha == 1 and beta == 0:
        return M / (r**2 * f)
    if mu == 2 and alpha == 2 and beta == 1:
        return 1 / r
    if mu == 2 and alpha == 1 and beta == 2:
        return 1 / r
    return 0
