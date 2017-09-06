# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 12:10:29 2017

@author: Nagasudhir
"""
import xmlFileNetworkParser as networkParser
import json

# parse network as a dictionary
network = networkParser.parseNetworkFromXMLFile("Urtdsm communcation.xml")

# dump the json file to network.json
f = open('network.json', 'w')
f.write(json.dumps(network, indent=4))
f.close()

print network