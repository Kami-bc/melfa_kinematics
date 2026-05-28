import numpy as np
import matplotlib.pyplot as plt

from src.melfa_kinematics.transforms import Rz, T
from src.melfa_kinematics.plotting import setup_3d_axes, draw_frame


fig, ax = setup_3d_axes()

R = Rz(np.pi / 4)

p = np.array([1, 1, 0])

H = T(R, p)

draw_frame(ax, p, R, length=0.5)

plt.show()