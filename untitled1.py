# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:43:32 2024

@author: s_henningg20
"""

def cagr_berechnung(AK,EK,t):
    AK_abs = abs(AK)
    t_abs = abs(t)
    CAGR = (EK/AK_abs)**(1/t)-1 #test
    return CAGR 


