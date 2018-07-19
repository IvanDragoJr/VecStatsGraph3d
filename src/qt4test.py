import sys
from PyQt4 import QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


import random

from mpl_toolkits.mplot3d import Axes3D

from src.FileManager import FileManager


class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        fileManager = FileManager()

        fileManager.loadData()
        data = fileManager.loadData3D(fileManager.get_vectorsMatrix())

        # Just some button connected to `plot` method
        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.plotTest(data))

        # set the layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def plot(self):
        ''' plot some random stuff '''
        # random data
        data = [random.random() for i in range(10)]

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.clear()

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()

    def plotTest(self, data):
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
        ax.set_xlim([minXAxis, maxXAxis])
        ax.set_ylim([minYAxis, maxYAxis])
        ax.set_zlim([minZAxis, maxZAxis])

        ax.plot(data, '*-')
        self.canvas.draw()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
