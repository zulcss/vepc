#!/usr/bin/python

import json

import datadiff
import xmltodict

with open('/root/master.conf', 'rb') as f:
    d = xmltodict.parse(f, xml_attribs=True)
    master = json.dumps(d, indent=4)
with open('/root/vepc.conf', 'rb') as f:
    d = xmltodict.parse(f, xml_attribs=True)
    slave = json.dumps(d, indent=4)

print datadiff.diff(master, slave, fromfile="golden-configuration", tofile="vepc.conf")
