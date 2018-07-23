import numpy as np

from src.util.ArrayUtil import ArrayUtil


class DrawUtil:

    @staticmethod
    def calculate_margin_max_coordinates(x, y, z):
        margin = max(ArrayUtil.find_max(x), ArrayUtil.find_max(y), ArrayUtil.find_max(z))
        margin = margin * 2
        return margin

    @staticmethod
    def draw_sphere(max_coordinates, alpha, line_width, ax):
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)

        x_sphere = max_coordinates * np.outer(np.cos(u), np.sin(v))
        y_sphere = max_coordinates * np.outer(np.sin(u), np.sin(v))
        z_sphere = max_coordinates * np.outer(np.ones(np.size(u)), np.cos(v))
        ax.plot_surface(x_sphere,
                        y_sphere,
                        z_sphere,
                        rstride=4,
                        cstride=4,
                        color='none',
                        linewidth=line_width,
                        alpha=alpha)

    @staticmethod
    def draw_axis_vectors(margin, head_ratio, ax):
        soa = np.array([[0, 0, 0, margin, 0, 0], [0, 0, 0, 0, margin, 0],
                        [0, 0, 0, 0, 0, margin]])

        OX, OY, OZ, OU, OV, OW = zip(*soa)
        ax.set_aspect('equal')
        ax.quiver(OX, OY, OZ, OU, OV, OW, arrow_length_ratio=head_ratio)




