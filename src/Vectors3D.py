import numpy

from mayavi import mlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Vectors3D:

    def test_quiver3d(self, data):
        soa = []
        x = []
        y =[]
        z =[]
        u =[]
        v =[]
        w =[]
        # x, y, z, u, v, w = data
        for vector in data:
            x.append(vector[0])
            y.append(vector[1])
            z.append(vector[2])
            u.append(vector[3])
            v.append(vector[4])
            w.append(vector[5])

            # a, b, c = numpy.mgrid[vector[1], vector[2], vector[3]]

        # obj = mlab.quiver3d(a, b, c, e, f, g, line_width=1, scale_factor=0.2)

        mlab.quiver3d(x, y, z, u, v, w)
        mlab.axes()
        mlab.outline()
        mlab.show()


        def test_quiver3d2(self, data):

            mlab.show()

    def plotVectors3D(self, data):
        soa = []
        for vector in data:
            soa.append([vector[1],
                        vector[2],
                        vector[3],
                        vector[4],
                        vector[5],
                        vector[6]]
                       )

        X, Y, Z, U, V, W = zip(*soa)

        minXAxis = min(X) if min(X) < min(U) else min(U)
        minYAxis = min(Y) if min(Y) < min(V) else min(V)
        minZAxis = min(Z) if min(Z) < min(W) else min(W)

        maxXAxis = max(X) if max(X) > max(U) else max(U)
        maxYAxis = max(Y) if max(Y) > max(V) else max(V)
        maxZAxis = max(Z) if max(Z) > max(W) else max(W)
        fig = plt.figure()

        ax = fig.add_subplot(111, projection='3d')
        # ax.scatter(X, Y, Z, c='r', marker='o')
        ax.quiver(X, Y, Z, U, V, W, arrow_length_ratio=0.02)
        # ax.quiver([0,1,2], [1,2,3], [2,3,4], [9,8,7], [8,7,6], [7,6,5], arrow_length_ratio=0.02)
        ax.set_xlim([minXAxis, maxXAxis])
        ax.set_ylim([minYAxis, maxYAxis])
        ax.set_zlim([minZAxis, maxZAxis])
        Axes3D.mouse_init(ax, rotate_btn=1, zoom_btn=3)
        plt.savefig('/home/pedro/Desktop/splunk/cosa', format='eps', dpi=1000)
        fig.savefig('/home/pedro/Desktop/splunk/myimage.svg', format='svg', dpi=1200)

        beingsaved = plt.figure()


        beingsaved.savefig('/home/pedro/Desktop/splunk/myimage.svg', format='eps', dpi=1000)

        plt.show()

        # for i in range(0, 360, 45):
        #     ax.view_init(None, i)
        #     plt.show()
