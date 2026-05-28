import numpy as np

from src.melfa_kinematics.transforms import (
    Rz,
    T,
    translation
)

from src.melfa_kinematics.robot import SerialRobot


robot = SerialRobot()

H1 = T(Rz(np.pi / 4), np.array([1, 0, 0]))
H2 = translation(1, 0, 0)

robot.add_transform(H1)
robot.add_transform(H2)

H_final = robot.forward_kinematics()

print(H_final)