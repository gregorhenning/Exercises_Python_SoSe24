# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:40:21 2024

@author: henningG
"""


def spar_funktion(AK,SR,i,lz):
    
    kapital = AK
    sparsumme = []
    
    for k in range(1, lz+1):
        kapital = (kapital)*(1+i)+SR
        kapital = round(kapital,2)
        sparsumme.append(kapital)
    
    return sparsumme

print(spar_funktion(10000,1000,0.01,10))
    

        
        
    