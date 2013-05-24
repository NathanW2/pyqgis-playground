from qgis.core import *
from qgis.gui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import QApplication
from PyQt4.QtXml import *
import sys
import xml.etree.ElementTree as ET

app = QgsApplication([], True)
QgsApplication.initQgis()

project = "composer.qgs"
template = "template.qpt"

QgsProject.instance().setFileName(project)
QgsProject.instance().read()

doc = QDomDocument()
doc.setContent(QFile(project), False)

templateDOM = QDomDocument()
templateDOM.setContent(QFile(template), False)

layers = doc.elementsByTagName("maplayer")
layerset = []

for x in xrange(layers.count()):
	layerDOM = layers.at(x)
 	layer = QgsVectorLayer()
 	layer.readXML(layerDOM)
 	QgsMapLayerRegistry.instance().addMapLayer(layer)
 	layerset.append(layer.id())

newlayers = []
for layer in reversed(layerset):
	newlayers.append(layer)

myMapRenderer = QgsMapRenderer()
mLBL = QgsPalLabeling()
myMapRenderer.setLabelingEngine(mLBL)
myMapRenderer.setLayerSet(newlayers)
myMapRenderer.setProjectionsEnabled(False)

comp = QgsComposition(myMapRenderer)
comp.loadFromTemplate(templateDOM,{'Name':"Water", 'Tag':'FooBar'})
comp.exportAsPDF("composer.pdf")
QgsApplication.exitQgis()