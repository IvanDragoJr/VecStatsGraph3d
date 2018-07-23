

# load data from file
from src.FileManager import FileManager
from src.graphs.DrawDensity import DrawDensity

fileManager = FileManager()
fileManager.loadData()
dat = fileManager.loadData3D(fileManager.get_vectorsMatrix())
draw_density = DrawDensity()

draw_density.draw_density_graph(dat)