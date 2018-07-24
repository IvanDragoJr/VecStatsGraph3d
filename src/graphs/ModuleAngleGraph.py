import numpy as np
import matplotlib.pyplot as plt

from src.util.ArithmeticUtil import ArithmeticUtil
from src.util.DrawUtil import DrawUtil


class ModuleAngleGraph:

    @staticmethod
    def draw_module_angle_distrib(dat):
        module = np.array([row[0] for row in dat])
        x = np.array([row[3] for row in dat])
        y = np.array([row[4] for row in dat])
        z = np.array([row[5] for row in dat])

        R = np.math.sqrt((np.sum(x) * np.sum(x)) + (np.sum(y) * np.sum(y)) + (np.sum(z) * np.sum(z)))

        meanX = np.sum(x) / R
        meanY = np.sum(y) / R
        meanZ = np.sum(z) / R

        meanModule = ArithmeticUtil.arithmetic_mean(module)
        meanDirection = ArithmeticUtil.mean_direction(x, y, z)

        if meanDirection[0] < 0:
            meanDirection[0] = meanDirection[0] + 180

        if meanX < 0:
            meanDirection[1] = meanDirection[1] + 180

        if meanDirection[1] < 0:
            meanDirection[1] = meanDirection[1] + 360

        Ax = meanModule * np.math.sin(ArithmeticUtil.to_radian(meanDirection[0])) * \
             np.math.cos(ArithmeticUtil.to_radian(meanDirection[1]))

        Ay = meanModule * np.math.sin(ArithmeticUtil.to_radian(meanDirection[0])) * \
             np.math.sin(ArithmeticUtil.to_radian(meanDirection[1]))

        Az = meanModule * np.math.cos(ArithmeticUtil.to_radian(meanDirection[0]))

        # define 3d plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        DrawUtil.draw_sphere(module[0], 0.08, 0, ax)
        DrawUtil.draw_axis_vectors(module[0], 0.1, ax)

        ax.quiver(0, 0, 0, x, y, z, arrow_length_ratio=0.01)
        plt.show()
