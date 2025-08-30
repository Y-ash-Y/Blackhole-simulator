# Black Hole Simulator 🌌

A Python + Blender-powered **General Relativity black hole simulator**, inspired by *Interstellar* and NASA visualizations.

---

## ✨ Features
- Photon orbits in Schwarzschild spacetime (deflected, critical, captured).
- Ray tracing of a real starfield → Einstein rings and lensing effects.
- Export geodesics to Blender for cinematic rendering.
- Planned:
  - Kerr black hole (rotation, like *Interstellar*)
  - Accretion disk with Doppler boosting + gravitational redshift
  - Observer time dilation and spaghettification

---

## 📂 Project Structure
   src/ # physics, integrator, visualization, ray tracer, Blender export
   examples/ # demo scripts: photon orbits, starfield lensing, ray tracer
   data/ # starfield images + trajectories
   outputs/ # rendered images
   blender/ # Blender scene + rendering scripts
   notebooks/ # derivations & experiments

---

## 🚀 Quick Start

Clone the repository:
```bash
git clone https://github.com/Y-ash-Y/Blackhole-simulator.git
cd Blackhole-simulator

python -m venv .venv
.\.venv\Scripts\activate   # Windows
# or source .venv/bin/activate for Linux/macOS

pip install -r requirements.txt
