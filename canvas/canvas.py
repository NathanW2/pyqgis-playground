import PyQt4.uic
from qgis.core import QgsVectorLayer, QgsMapLayerRegistry, QgsApplication
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os.path
import sys

basepath = os.path.dirname(__file__)
datapath = os.path.abspath(os.path.join(basepath, "..", "data"))


class Window(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)
		PyQt4.uic.loadUi(os.path.join(basepath,'canvas.ui'), self)
		self.canvas.setCanvasColor(Qt.white)
		self.canvas.enableAntiAliasing(True)

	def loadLayer(self, path, name):
		layer = QgsVectorLayer(path, name, 'ogr')
		if not layer.isValid():
  			raise IOError, "Failed to open the layer"
		self.canvas.setExtent(layer.extent())
		QgsMapLayerRegistry.instance().addMapLayer(layer)
		layers = self.canvas.mapRenderer().layerSet()
		layers.append(layer.id())
		self.canvas.mapRenderer().setLayerSet(layers)


if __name__ == "__main__":
	app = QgsApplication([], True)
	QgsApplication.initQgis()
	window = Window()
	window.loadLayer(os.path.join(datapath, "Cadastre.shp"), "cadastre")
	window.loadLayer(os.path.join(datapath, "Roads.shp"), "Roads")
	window.show()
	app.exec_()
	QgsApplication.exitQgis()
