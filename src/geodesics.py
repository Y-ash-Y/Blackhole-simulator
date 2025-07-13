# Geodesic ODEs for photon in Schwarzschild spacetime
import numpy as np
from .christoffel import christoffel

def geodesic_rhs(lambda_, y):
    dydlambda = np.zeros(6)
    x = y[:3]
    dx = y[3:]
    dydlambda[0:3] = dx
    for mu in range(3):
        sum_term = 0
        for alpha in range(3):
            for beta in range(3):
                sum_term += christoffel(mu, alpha, beta, x) * dx[alpha] * dx[beta]
        dydlambda[3 + mu] = -sum_term
    return dydlambda
