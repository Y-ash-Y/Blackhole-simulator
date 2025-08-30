# blender_export.py – write trajectories/ray bundles to CSV for Blender import
import csv, os
from typing import List
from .integrator import Ray

def export_rays_to_csv(rays: List[Ray], out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    for i, rr in enumerate(rays):
        path = os.path.join(out_dir, f"ray_{i:04d}.csv")
        with open(path, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["x","y","z"])
            for x,y in zip(rr.x, rr.y):
                w.writerow([x, y, 0.0])
