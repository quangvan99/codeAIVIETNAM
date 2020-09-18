# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 16:04:57 2020

@author: Admin
"""

import random

# pi = 4*Nc/Nr
coor = [0,0]
Nc = 1
Nr = 1000000

for i in range(Nr):
    coor = [random.uniform(-1,1), random.uniform(-1,1)]
    # coor = [random.random()*2-1, random.random()*2-1]

    if (coor[0]*coor[0] + coor[1]*coor[1] < 1):
        Nc += 1

print("pi = ", 4*Nc/Nr)
            