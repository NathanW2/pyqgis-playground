import PyQt4.uic
from qgis.core import QgsVectorLayer, QgsMapLayerRegistry, QgsApplication, QgsPalLabeling
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os.path
import sys
from projectparser import ProjectParser

basepath = os.path.dirname(__file__)
datapath = os.path.abspath(os.path.join(basepath, "..", "data"))

class Window(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        PyQt4.uic.loadUi(os.path.join(basepath, 'canvas.ui'), self)
        self.canvas.setCanvasColor(Qt.white)
        self.canvas.enableAntiAliasing(True)
        pal = QgsPalLabeling()
        self.canvas.mapRenderer().setLabelingEngine(pal)

    def loadLayer(self, layer):
        self.canvas.setExtent(layer.extent())
        QgsMapLayerRegistry.instance().addMapLayer(layer)
        layers = self.canvas.mapRenderer().layerSet()
        layers.append(layer.id())
        self.canvas.mapRenderer().setLayerSet(layers)

    def loadproject(self, filename):
        parser = ProjectParser.fromFile(filename)
        for layerid, visible, layer in parser.layers():
            self.loadLayer(layer)

if __name__ == "__main__":
    print "HELLO WORLD"
    projectfile = sys.argv[1]
    print projectfile
    app = QgsApplication(sys.argv, True)
    QgsApplication.initQgis()
    window = Window()
    QDir.setCurrent(os.path.dirname(projectfile))
    window.loadproject(projectfile)
    window.show()
    app.exec_()
    QgsApplication.exitQgis()
