from PyQt4.QtXml import QDomDocument
from qgis.core import QgsVectorLayer, QgsRasterLayer

def iternodes(nodes):
    for index in xrange(nodes.length()):
        yield nodes.at(index).toElement()

class ProjectParser(object):
    def __init__(self, xmldoc):
        self.doc = xmldoc
        self._maplayers = None

    @classmethod
    def fromFile(cls, filename):
        print filename
        xml = open(filename).read()
        doc = QDomDocument()
        doc.setContent(xml)
        return cls(doc)

    def _createLayer(self, node):
        type = node.attribute('type')
        if type == "vector":
            layer = QgsVectorLayer()
        elif type == "raster":
            layer = QgsRasterLayer()
        else:
            return None
        layer.readLayerXML(node)
        print layer.id(), layer.isValid()
        return layer.id(), layer

    def _getLayers(self, node):
        if not self._maplayers:
            self._maplayers = dict(self.maplayers())

        filelist = node.elementsByTagName("legendlayerfile")
        layerid = filelist.at(0).toElement().attribute('layerid')
        print layerid
        visible = node.attribute('visible')
        return layerid, visible, self._maplayers[layerid]
    
    def maplayers(self):
        layernodes = self.doc.elementsByTagName("maplayer")
        return (self._createLayer(elm) for elm in iternodes(layernodes))
        
    def layers(self):
        legendnodes = self.doc.elementsByTagName("legendlayer")
        return (self._getLayers(elm) for elm in iternodes(legendnodes))


