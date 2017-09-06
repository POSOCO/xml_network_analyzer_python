# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 12:10:29 2017

@author: Nagasudhir
"""
def parseNetworkFromXMLFile(filename):
    
    # Variable initializations
    numPMUsAttributeStr = "NoofPMUs"
    bandWidthRequiredAttributeStr = "BandwidthReqd"
    ssNodes = []
    ssLinks = []

    # getting the xml data
    xmlData = open(filename, 'r').read()
    
    # getting the xml tree
    import xml.etree.ElementTree as ET
    xml = ET.fromstring(xmlData)
    
    # parsing the elements using object tag
    for el in xml.getiterator('object'):
        elementId = el.attrib["id"]
        elementLabel = el.attrib["label"]
        elementNumPMUs = el.attrib[numPMUsAttributeStr]
        elementBandWidthRequired = el.attrib[bandWidthRequiredAttributeStr]
        nodeMxCell = el.getiterator('mxCell')[0]
        nodeStyleStrings = nodeMxCell.attrib["style"].split(";")    
        nodeStyles = {}
        for k in range(0,len(nodeStyleStrings)-1):
            attribVal = nodeStyleStrings[k].split("=")
            if len(attribVal) < 2:
                nodeStyles[nodeStyleStrings[k].split("=")[0]] = None
            else:
                nodeStyles[nodeStyleStrings[k].split("=")[0]] = nodeStyleStrings[k].split("=")[1]
        if "ellipse" in nodeStyles.keys():
            elementType = "node"
            ssNode = {}
            ssNode['id'] = elementId
            ssNode['label'] = elementLabel
            ssNode['num_pmu'] = elementNumPMUs
            ssNode['bandwidth_req'] = elementBandWidthRequired
            ssNode['element_type'] = elementType
            ssNodes.append(ssNode)
            
    # parsing the elements and links using mxCell tag
    for el in xml.getiterator('mxCell'):
        if set(["id", "value", "style"]).issubset(set(el.keys())):
            elementId = el.attrib["id"]
            elementValue = el.attrib["value"]
            elementStyleStrings = el.attrib["style"].split(";")
            elementStyles = {};
            for k in range(0, len(elementStyleStrings)-1):
                attribVal = elementStyleStrings[k].split("=")
                if len(attribVal) < 2:
                    elementStyles[elementStyleStrings[k].split("=")[0]] = None
                else:
                    elementStyles[elementStyleStrings[k].split("=")[0]] = elementStyleStrings[k].split("=")[1]
            if "ellipse" in elementStyles.keys():
                ssNodes.append({"id": elementId, "label": elementValue, "element_type": "node"})
            elif "edgeStyle" in elementStyles.keys():
                ssLinks.append({"bandwidth": elementValue,"sourceId": el.attrib["value"], "targetId": el.attrib["target"], "id": elementId, "element_type": "link"})
    
    # creating the network object
    network = {}
    network['nodes'] = ssNodes
    network['links'] = ssLinks
    return network
    # print network