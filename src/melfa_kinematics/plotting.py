import matplotlib.pyplot as plt
import numpy as np


def setup_3d_axes():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    return fig, ax


def draw_frame(ax, origin, R, length=1.0):

    x_axis = R[:, 0] * length
    y_axis = R[:, 1] * length
    z_axis = R[:, 2] * length

    ax.quiver(
        origin[0], origin[1], origin[2],
        x_axis[0], x_axis[1], x_axis[2],
        color='r'
    )

    ax.quiver(
        origin[0], origin[1], origin[2],
        y_axis[0], y_axis[1], y_axis[2],
        color='g'
    )

    ax.quiver(
        origin[0], origin[1], origin[2],
        z_axis[0], z_axis[1], z_axis[2],
        color='b'
    )