# 🕳️ Black Hole Simulator (PHY473 Project)

A Python-based 3D simulation of a black hole inspired by *Interstellar*, built from scratch using General Relativity. The project demonstrates how photons move through curved spacetime around a Schwarzschild black hole — no GPUs, just raw physics and code.

## 💡 Features

- Solve null geodesics using manually defined Christoffel symbols
- Visualize gravitational lensing and photon trajectories
- Build a backward ray tracer (each pixel = 1 light ray)
- Add an accretion disk with relativistic Doppler & redshift effects
- Simulate time dilation for observers near vs far from the event horizon

## 📚 Based On

This project uses concepts from:
- General Relativity (Schwarzschild metric)
- Numerical ODE integration (Runge-Kutta)
- Tensor calculus (Christoffel symbols)
- Computational physics (ray tracing)
- Interpolation, numerical differentiation, error analysis

## 🛠️ Stack

- Python 3.x
- NumPy, SciPy
- Matplotlib
- (Optional) Numba, VPython, PyOpenGL for future acceleration

## 🧪 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Y-ash-Y/Blackhole-simulator.git
   cd Blackhole-simulator
   ```

