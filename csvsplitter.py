# -*- coding: utf-8 -*-
"""
This script takes two parameters, the script name and the csv file name.
It then splits the csv file into an array
"""
import numpy as np
from sys import argv

script, filename = argv

txt = open(filename)

csvarray = []

for row in txt:
    
    row1 = row.strip('\n')
    
    csvarray.append(row1.split(","))


print csvarray
