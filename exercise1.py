# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:43:32 2024

@author: s_henningg20
"""

def cagr_berechnung(AK,EK,t):
    AK_abs = abs(AK)
    t_abs = abs(t)
    CAGR = (EK/AK_abs)**(1/t_abs)-1 #test
    return CAGR 
print(cagr_berechnung(100, 700, 30))

AK = 120
t = 30
cagr = cagr_berechnung(100, 700, 30)

EK = AK * (1+cagr)**t

print(EK)


