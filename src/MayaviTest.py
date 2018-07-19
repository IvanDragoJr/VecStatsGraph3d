#!/usr/bin/env python

from src.FileManager import FileManager

from src.Vectors3D import Vectors3D


fileManager = FileManager()

fileManager.loadData()
data = fileManager.loadData3D(fileManager.get_vectorsMatrix())
vectors3D = Vectors3D()
vectors3D.plotVectors3D(data)
# vectors3D.test_quiver3d(fileManager.simpleLoad())
