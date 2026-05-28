import numpy as np


class SerialRobot:

    def __init__(self):
        self.transforms = []

    def add_transform(self, H):
        self.transforms.append(H)

    def forward_kinematics(self):

        H_total = np.eye(4)

        for H in self.transforms:
            H_total = H_total @ H

        return H_total