import numpy as np
from scipy import stats


class ArithmeticUtil:

    @staticmethod
    def arithmetic_mean(data):
        return np.sum(data) / len(data)

    @staticmethod
    def mean_direction(x, y, z):
        mean = []
        n_elements = len(x)

        R = np.math.sqrt((np.sum(x) * np.sum(x)) + (np.sum(y) * np.sum(y)) + (np.sum(z) * np.sum(z)))

        meanX = np.sum(x) / R
        meanY = np.sum(y) / R
        meanZ = np.sum(z) / R

        meanLongitud = 0

        if meanY > 0 and meanX > 0:
            meanLongitud = np.math.atan(meanY / meanX)

        if meanY > 0 and meanX < 0:
            meanLongitud = np.math.atan(meanY / meanX) + np.math.pi

        if meanY < 0 and meanX < 0:
            meanLongitud = np.math.atan(meanY / meanX) + np.math.pi

        if meanY < 0 and meanX > 0:
            meanLongitud = np.math.atan(meanY / meanX) + (2 * np.math.pi)

        meanLongitud = ArithmeticUtil.to_sexagesimal_3d(meanLongitud)
        meanColatitud = np.math.acos(meanZ)
        meanColatitud = ArithmeticUtil.to_sexagesimal_3d(meanColatitud)

        mean.append(meanLongitud)
        mean.append(meanColatitud)
        return mean

    @staticmethod
    def to_sexagesimal_3d(radians):
        grades = []
        if isinstance(radians, list):
            for item in radians:
                grades.append(180 * item / np.math.pi)
            return grades

        else:
            return radians * 180 / np.math.pi

    @staticmethod
    def to_radian(grades):
        radians = (grades / 180 * np.math.pi)
        return radians

    @staticmethod
    def number_of_elements(dat):
        return len(dat)

    @staticmethod
    def max_value(dat):
        return max(dat)

    @staticmethod
    def min_value(dat):
        return min(dat)

    @staticmethod
    def range(dat):
        element_range = ArithmeticUtil.max_value(dat) - ArithmeticUtil.min_value(dat)
        if element_range < 0:
            element_range = element_range * -1

        return element_range

    @staticmethod
    def module_sum(dat):
        return np.math.fsum(dat)

    @staticmethod
    def standard_error(dat):
        """ TESTED
        """
        return stats.sem(dat)


