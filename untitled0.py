# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:07:31 2024

@author: henningG
"""

def vokon_zählen(wort):
    vokale = "aeiou"
    
    vokale_count = 0
    konsonanten_count = 0
    
    for vokal in wort.lower():
        if vokal.isalpha():
            if vokal in vokale:
                vokale_count += 1
        else:
                konsonanten_count += 1
    print(f" Es gibt: {vokale_count} Vokale und {konsonanten_count} Konsonanten")
    
vokon_zählen("Hallo, Berlin")    

    
    
        