# visualization.py – quick 2D plots
import matplotlib.pyplot as plt
from .physics import RS, M

def demo_plot(rays, title="Photon trajectories near a Schwarzschild black hole (M=1)"):
    fig, ax = plt.subplots(figsize=(7,7))

    # Horizon and photon sphere
    BH = plt.Circle((0,0), RS, alpha=0.3, label="Horizon (r=2M)")
    PS = plt.Circle((0,0), 3.0*M, fill=False, linestyle="--", label="Photon sphere (r=3M)")
    ax.add_patch(BH); ax.add_patch(PS)

    # Trajectories
    for rr in rays:
        ax.plot(rr.x, rr.y, lw=2, label=f"b={rr.b:.3f} ({rr.regime})")

    ax.set_aspect("equal", "box")
    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    plt.show()
