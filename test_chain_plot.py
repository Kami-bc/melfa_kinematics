import numpy as np
import matplotlib.pyplot as plt

from src.melfa_kinematics.transforms import (
    Rz,
    T,
    translation
)

from src.melfa_kinematics.plotting import (
    setup_3d_axes,
    draw_frame,
    set_axes_equal
)

fig, ax = setup_3d_axes()

# Frame base
R0 = np.eye(3)
p0 = np.array([0, 0, 0])

draw_frame(ax, p0, R0, length=0.5)

# Primer joint
R1 = Rz(np.pi / 4)

p1 = np.array([1, 0, 0])

H1 = T(R1, p1)

draw_frame(
    ax,
    H1[0:3, 3],
    H1[0:3, 0:3],
    length=0.5
)

# Segundo joint
H2 = translation(1, 0, 0)

H_total = H1 @ H2

draw_frame(
    ax,
    H_total[0:3, 3],
    H_total[0:3, 0:3],
    length=0.5
)

set_axes_equal(ax, limit=3)

plt.show()