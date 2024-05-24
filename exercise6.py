# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:20:48 2024

@author: henningG
"""

a = 1
r = 0.5
s = 0
k = 0
grenzwert = 1/(1-r)

epsilon = 0.00001

while True:
    s += a * r**k
    k += 1
    print(s, end = " ")
    if (grenzwert - s) < epsilon:
        break
    