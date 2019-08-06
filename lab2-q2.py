# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 22:58:52 2019

@author: Gautam
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#a.	source IP addresses and destination IP addresses
dataset = pd.read_csv('lab 2.csv') 
x=  dataset.iloc[:,2]
y=  dataset.iloc[:,3]

print(x)
print(y)
# b. source port numbers and destination port numbers

z=dataset.iloc[:,4]
print(z)
# c. c.	http request and response messages.
e=dataset.iloc[:,6]
print(e)