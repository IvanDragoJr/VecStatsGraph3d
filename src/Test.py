
# load data from file
from src.graphs.DensityGraph import DensityGraph
from src.manager.FileManager import FileManager
from src.graphs.ModuleAngleGraph import ModuleAngleGraph
from src.util.ArithmeticUtil import ArithmeticUtil

fileManager = FileManager()
fileManager.load_data()
dat = fileManager.loadData3D(fileManager.get_vectorsMatrix())

# DensityGraph.draw_density_graph(dat)
# ModuleAngleGraph.draw_module_angle_distrib(dat)
ArithmeticUtil.kurtois_module_coefficient(fileManager.getColumnAsArray(0, dat))
