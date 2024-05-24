# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:13:01 2024

@author: henningG
"""

import numpy as np

array_example = np.eye(5,5)

array_example[3:, :2] = 2
array_example[0:2, 3:5] = 3
print(array_example)