import numpy as np

from src.melfa_kinematics.transforms import (
    Rz,
    T,
    translation
)

R1 = Rz(np.pi / 4)

p1 = np.array([1, 0, 0])

H1 = T(R1, p1)

H2 = translation(1, 0, 0)

H_total = H1 @ H2

print(H_total)