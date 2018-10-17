from VecStatsGraph.manager.FileManager import FileManager
from VecStatsGraph.manager.graphs.ModuleAngleGraph import ModuleAngleGraph
from VecStatsGraph.manager.ModuleStatisticsManager import ModuleStatisticsManager

fileManager = FileManager()
fileManager.read_file()
dat = fileManager.load_data(fileManager.get_vectorsMatrix())