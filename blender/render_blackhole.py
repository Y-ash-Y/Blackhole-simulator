# render_blackhole.py – run inside Blender (blender -b scene.blend -P this.py)
import bpy, os, csv

TRAJ_DIR = os.path.join(os.path.dirname(bpy.data.filepath), "..", "data", "trajectories")
TRAJ_DIR = os.path.abspath(TRAJ_DIR)
OUT_DIR  = os.path.join(os.path.dirname(bpy.data.filepath), "..", "outputs", "renders")
OUT_DIR  = os.path.abspath(OUT_DIR)
os.makedirs(OUT_DIR, exist_ok=True)

def make_curve_from_csv(csv_path, name):
    # Create a poly curve from points in CSV (x,y,z)
    curve_data = bpy.data.curves.new(name=name, type='CURVE')
    curve_data.dimensions = '3D'
    spline = curve_data.splines.new('POLY')
    pts = []
    with open(csv_path, newline='') as f:
        r = csv.DictReader(f)
        for row in r:
            pts.append((float(row["x"]), float(row["y"]), float(row["z"])))
    spline.points.add(len(pts)-1)
    for i, p in enumerate(pts):
        spline.points[i].co = (p[0], p[1], p[2], 1.0)
    curve_obj = bpy.data.objects.new(name, curve_data)
    bpy.context.collection.objects.link(curve_obj)
    return curve_obj

# Import all trajectories
if os.path.isdir(TRAJ_DIR):
    for fname in sorted(os.listdir(TRAJ_DIR)):
        if fname.endswith(".csv"):
            make_curve_from_csv(os.path.join(TRAJ_DIR, fname), name=fname[:-4])

# Simple camera & light if missing
if "Camera" not in bpy.data.objects:
    bpy.ops.object.camera_add(location=(0, -40, 8), rotation=(1.2, 0, 0))
if "Light" not in bpy.data.objects:
    bpy.ops.object.light_add(type='SUN', location=(10, -10, 20))

# Render
bpy.context.scene.render.filepath = os.path.join(OUT_DIR, "frame_0001.png")
bpy.ops.render.render(write_still=True)
print("Rendered to:", bpy.context.scene.render.filepath)
