import numpy as np

from src.util.ArithmeticUtil import ArithmeticUtil
from src.util.VectorUtil import VectorUtil


class AngleStatisticsManager:

    def mean_direction(self, coordinates_matrix):
        x = coordinates_matrix[:, 0]
        y = coordinates_matrix[:, 1]
        z = coordinates_matrix[:, 2]
        mean = []
        n_elements = len(x)
        r = np.math.sqrt((np.sum(x) * np.sum(x)) + (np.sum(y) * np.sum(y)) + (np.sum(z) * np.sum(z)))

        mean_x = np.sum(x) / r
        mean_y = np.sum(y) / r
        mean_z = np.sum(z) / r
        mean_longitude = 0

        if mean_y > 0 and mean_x > 0:
            mean_longitude = np.math.atan(mean_y / mean_x)

        if mean_y > 0 > mean_x:
            mean_longitude = np.math.atan(mean_y / mean_x) + np.math.pi

        if mean_y < 0 and mean_x < 0:
            mean_longitude = np.math.atan(mean_y / mean_x) + np.math.pi

        if mean_y < 0 < mean_x:
            mean_longitude = np.math.atan(mean_y / mean_x) + (2 * np.math.pi)

        mean_longitude = ArithmeticUtil.to_sexagesimal_3d(mean_longitude)
        mean_colatitud = np.math.acos(mean_z)
        mean_colatitud = ArithmeticUtil.to_sexagesimal_3d(mean_colatitud)

        mean.append(mean_longitude)
        mean.append(mean_colatitud)
        return mean

    def mean_module(self, coordinates_matrix):
        x = coordinates_matrix[:, 0]
        y = coordinates_matrix[:, 1]
        z = coordinates_matrix[:, 2]
        n_elements = len(x)
        r = np.math.sqrt((np.sum(x) * np.sum(x)) + (np.sum(y) * np.sum(y)) + (np.sum(z) * np.sum(z)))

        mean_module = r / n_elements

        return mean_module

    def real_mod_to_unit_mod(self, coordinates_matrix):
        x = coordinates_matrix[:, 0]
        y = coordinates_matrix[:, 1]
        z = coordinates_matrix[:, 2]
        n_elements = len(x)
        polar_values = VectorUtil.vector_to_polar(coordinates_matrix)
        module = [1] * n_elements
        colatitud = polar_values[:, 1]
        longitude = polar_values[:, 2]

        u_vector = [module, colatitud, longitude]
        unit_incr = VectorUtil.vectors_to_rectangular(u_vector)

        return unit_incr

    def concentration_parameter(self, coordinates_matrix):
        x = coordinates_matrix[:, 0]
        y = coordinates_matrix[:, 1]
        z = coordinates_matrix[:, 2]
        n_elements = len(x)
        mean_module = self.mean_module(coordinates_matrix)
        parameter = (n_elements - 1) / float((n_elements * (1 - mean_module)))

        return parameter


    # sphericalErr < - SphericalStandardError3D(unit_incr)