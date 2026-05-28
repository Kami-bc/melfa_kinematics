import numpy as np
import matplotlib.pyplot as plt

from src.melfa_kinematics.transforms import Rz, T
from src.melfa_kinematics.plotting import (
    setup_3d_axes,
    draw_frame,
    draw_vector,
    set_axes_equal
)

fig, ax = setup_3d_axes()

R = Rz(np.pi / 4)

p = np.array([1, 1, 0])

H = T(R, p)

draw_frame(ax, p, R, length=0.5)

v = np.array([1, 0.5, 1])

draw_vector(
    ax,
    origin=np.array([0, 0, 0]),
    vector=v,
    color='m'
)

set_axes_equal(ax, limit=2)
plt.show()