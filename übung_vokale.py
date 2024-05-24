# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:12:18 2024

@author: henningG
"""
def vokon_zählen(text):
    vokale_liste = 'aeiou'
    
    vokal_count = 0
    konsonant_count = 0
    
    for vokal in text:
        if vokal.isalpha():
            if vokal in vokale_liste:
                vokal_count += 1
            else:
                konsonant_count += 1
    
    print(f"Es gibt {vokal_count} Vokale und {konsonant_count} Konsonanten")
    
vokon_zählen("%&/9, hi Berlin")
    
