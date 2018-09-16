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

    @staticmethod
    def module_variance(dat):
        """ TEST SMALL ERROR
        """
        m_arit = ArithmeticUtil.arithmetic_mean(dat)
        n = ArithmeticUtil.number_of_elements(dat)
        return np.math.fsum(((dat - m_arit) ** 2)) / (n - 1)

    @staticmethod
    def module_standard_deviation(dat):
        """ TEST SMALL ERROR
                """
        m_arit = ArithmeticUtil.arithmetic_mean(dat)
        n = ArithmeticUtil.number_of_elements(dat)
        return np.math.sqrt((np.math.fsum((dat - m_arit) ** 2)) / (n - 1))

    @staticmethod
    def module_population_variance(dat):
        """ TEST SMALL ERROR
        """
        m_arit = ArithmeticUtil.arithmetic_mean(dat)
        n = ArithmeticUtil.number_of_elements(dat)
        return sum(((dat - m_arit) ** 2)) / n

    @staticmethod
    def module_population_standard_deviation(dat):
        """ TEST SMALL ERROR
        """
        m_arit = ArithmeticUtil.arithmetic_mean(dat)
        n = ArithmeticUtil.number_of_elements(dat)
        return np.math.sqrt((np.math.fsum((dat - m_arit)**2))/n)

    @staticmethod
    def skewness_module_coefficient(dat):
        """ TEST SMALL ERROR
        """
        n = ArithmeticUtil.number_of_elements(dat)
        mean = ArithmeticUtil.arithmetic_mean(dat)
        s = ArithmeticUtil.module_standard_deviation(dat)
        return (n / float(((n - 1) * (n - 2)))) * np.math.fsum(((dat - mean) / s) ** 3)


    @staticmethod
    def kurtois_module_coefficient(dat):
        """ TEST STRANGE ERROR
        """
        dat = [1, 2, 3, 4, 5, 6, 5, 4, 30, 2, 1]

        n = ArithmeticUtil.number_of_elements(dat)
        mean = ArithmeticUtil.arithmetic_mean(dat)
        s = ArithmeticUtil.module_standard_deviation(dat)

        a = (n * (n+1)) / float(((n - 1) * (n - 2) * (n - 3)))
        b = sum(((dat - mean) / float(s))**4)
        c = (3 * (n-1)**2) / float(((n-2) * (n-3)))
        return ((a *
                 b) -
                c)


