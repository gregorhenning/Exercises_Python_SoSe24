# -*- coding: utf-8 -*-
"""
Created on Fri May 24 12:32:40 2024

@author: henningG
"""


def buchstaben_ändern(string, buchstabe):
    vokale = "aeiou"
    

    def buchstabe_ersetzen(x, y, z):
        x_list = list(x.lower())
        
        for i in range(len(x_list)):
        
            if x_list[i] == y:
                x_list[i] = z
            
        return "".join(x_list)
    
    for v in vokale:
            print(buchstabe_ersetzen( x = string, y = buchstabe, z = v), end = " ")

buchstaben_ändern("Banana", "a")