# Black Hole Simulation (Python + Blender)
A physically grounded GR simulation with cinematic rendering via Blender.
- Python: geodesics + ray tracing (Schwarzschild, later Kerr)
- Blender: import trajectories, render accretion disk & lensing

## Quick Start
1) Create venv and install:
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt

2) Run a basic photon orbit demo:
   python .\examples\photon_orbits.py

3) Export rays for Blender:
   python .\examples\starfield_lensing.py  # writes CSVs to data/trajectories

4) Render in Blender (example):
   blender -b .\blender\blackhole_scene.blend -P .\blender\render_blackhole.py

Note: `bpy` is provided by Blender's own Python. You do NOT pip-install it here.
