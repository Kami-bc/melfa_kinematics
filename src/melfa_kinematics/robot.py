import numpy as np

from src.melfa_kinematics.plotting import draw_frame

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

    def all_frames(self):

        frames = [np.eye(4)]

        H_total = np.eye(4)

        for H in self.transforms:

            H_total = H_total @ H

            frames.append(H_total.copy())

        return frames

    def plot(self, ax, length=0.5):

        frames = self.all_frames()

        positions = []

        for H in frames:

            R = H[0:3, 0:3]
            p = H[0:3, 3]

            positions.append(p)

            draw_frame(ax, p, R, length=length)

        for i in range(len(positions) - 1):

            p1 = positions[i]
            p2 = positions[i + 1]

            ax.plot(
                [p1[0], p2[0]],
                [p1[1], p2[1]],
                [p1[2], p2[2]],
                linewidth=2
            )