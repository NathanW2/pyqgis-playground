import PyQt4.uic
from qgis.core import QgsVectorLayer, QgsMapLayerRegistry, QgsApplication, QgsPalLabeling, QgsProject
from qgis.gui import QgsMapCanvasLayer
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
        QgsProject.instance().readProject.connect(self.readProject)

    def readProject(self, doc):
        nodes = doc.elementsByTagName("mapcanvas")
        node = nodes.at(0)
        self.canvas.mapRenderer().readXML(node)
        layers = QgsMapLayerRegistry.instance().mapLayers()

        def makelayer(layerid, visible):
            layer = layers[layerid]
            return QgsMapCanvasLayer(layer, visible)

        layerset = [makelayer(layerid, visible) for layerid, visible in self.parser.layers()]
        self.canvas.setLayerSet(layerset)

    def loadproject(self, filename):
        self.parser = ProjectParser.fromFile(filename)
        QgsProject.instance().read(QFileInfo(filename))

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
