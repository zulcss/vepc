#!/usr/bin/python

import json
import sys

import xlrd

workbook = xlrd.open_workbook(sys.argv[1])
worksheet = workbook.sheet_by_index(0)

data = []
keys = [v.value for v in worksheet.row(0)]
for row_number in range(worksheet.nrows):
    if row_number == 0:
        continue
    row_data = {}
    for col_number, cell in enumerate(worksheet.row(row_number)):
        row_data[keys[col_number]] = cell.value
    data.append(row_data)
