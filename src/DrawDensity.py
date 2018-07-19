import numpy as np
from scipy import stats
from mayavi import mlab
import multiprocessing
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from src.FileManager import FileManager


soa = np.array([[0, 0, 0, 15, 0, 0], [0, 0, 0, 0, 15, 0],
                [0, 0, 0, 0, 0, 15]])

OX, OY, OZ, OU, OV, OW = zip(*soa)
# fig2 = plt.figure()
# ax = fig2.add_subplot(111, projection='3d')


#density fields
fileManager = FileManager()
fileManager.loadData()
dat = fileManager.loadData3D(fileManager.get_vectorsMatrix());

mu, sigma = 0, 0.1
x = np.array([row[3] for row in dat])
y = np.array([row[4] for row in dat])
z = np.array([row[5] for row in dat])

xyz = np.vstack([x, y, z])
density = stats.gaussian_kde(xyz)(xyz)

idx = density.argsort()
x, y, z, density = x[idx], y[idx], z[idx], density[idx]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=density)


#surface over density fields
# x_surf=np.arange(0, 1, 0.01)                # generate a mesh
# y_surf=np.arange(0, 1, 0.01)
# x_surf, y_surf = np.meshgrid(x_surf, y_surf)
# z_surf = np.sqrt(x_surf+y_surf)             # ex. function, which depends on x and y
# ax.plot_surface(x_surf, y_surf, z_surf, cmap=cm.hot)

#Wireframe
# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
# wire_z = np.linspace(-2, 2, 100)
# wire_r = wire_z**2 + 1
# wire_x = wire_r * np.sin(theta)
# wire_y = wire_r * np.cos(theta)
# ax.plot(wire_x, wire_y, wire_z, label='parametric curve')

#Sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x_sphere = 15 * np.outer(np.cos(u), np.sin(v))
y_sphere = 15 * np.outer(np.sin(u), np.sin(v))
z_sphere = 15 * np.outer(np.ones(np.size(u)), np.cos(v))
# elev = 10.0
# rot = 80.0 / 180 * np.pi
ax.plot_surface(x_sphere, y_sphere, z_sphere, rstride=4, cstride=4, color='none', linewidth=0, alpha=0.1)
ax.set_aspect('equal')
ax.axis()
ax.quiver(OX, OY, OZ, OU, OV, OW, arrow_length_ratio=0.1)

plt.hold(True)

plt.axis('off')
plt.show()

