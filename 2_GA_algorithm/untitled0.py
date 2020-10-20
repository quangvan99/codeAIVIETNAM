# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:59:34 2020

@author: Admin
"""

import nevergrad as ng
import math
def square(x):
    return sum(x**3+6*(x**2)+9*x-3)

# optimization on x as an array of shape (2,)
optimizer = ng.optimizers.OnePlusOne(parametrization=2, budget=1000)
optimizer.suggest([-4, 5])
recommendation = optimizer.minimize(square)  # best value
print(recommendation.value)
