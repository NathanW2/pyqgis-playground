import PyQt4.uic
from qgis.core import QgsVectorLayer, QgsMapLayerRegistry
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Window(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)

		PyQt4.uic.loadUi('canvas.ui', self)

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
	app = QApplication([])
	window = Window()
	window.loadLayer("C:\\dev\\python\\qgis-sandbox\\composition\\Cadastre.shp", "cadastre")
	# window.loadLayer("../data/Roads.shp", "roads")
	window.show()
	app.exec_()
