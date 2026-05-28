import numpy as np
import matplotlib.pyplot as plt

from src.melfa_kinematics.transforms import (
    Rz,
    T,
    translation
)

from src.melfa_kinematics.robot import SerialRobot

from src.melfa_kinematics.plotting import (
    setup_3d_axes,
    set_axes_equal
)

robot = SerialRobot()

H1 = T(Rz(np.pi / 4), np.array([1, 0, 0]))
H2 = translation(1, 0, 0)

robot.add_transform(H1)
robot.add_transform(H2)

fig, ax = setup_3d_axes()

robot.plot(ax)

set_axes_equal(ax, limit=3)

plt.show()