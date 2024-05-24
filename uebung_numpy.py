# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:01:42 2024

@author: henningG
"""

#import numpy as np

#array_example = np.arange(1,13)

#new_array = np.reshape(array_example, (4,3), order = 'F')

#print(new_array)

import numpy as np
a = np.arange(1, 13)
b = np.reshape(a, (4,3))

print(b[2:3, 1:6])
#print(b)


