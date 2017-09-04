"""
Spyder Editor
"""
xmlData = open('Urtdsm communcation.xml', 'r').read()

import xml.etree.ElementTree as ET
xml = ET.fromstring(xmlData)

for table in xml.getiterator('object'):
    for child in table:
        print child.tag, child.text

