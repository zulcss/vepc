#!/usr/bin/python

import json
import xmltodict

with open('vepc.conf', 'rv') as f:
    d = xmltodict.parse(f, xml_attribs=True)
    data = json.dumps(d, indent=4)
print data
