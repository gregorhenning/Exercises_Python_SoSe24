# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 14:37:41 2024

@author: s_henningg20
"""

def steigung_funktion(x1,y1,x2,y2):
        if (x2-x1) == 0:
            print("Die Steigung ist nicht definiert")
        else:
            print((y2-y1)/(x2-x1))
                
            