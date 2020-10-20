# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:01:16 2020

@author: Admin
"""

# from GA_algorithm import GA_algorithm
# import numpy as np
# binaryMax = GA_algorithm(nGen = 1, rangeOfGen = (-4,5), 
#                            nIndividual=1000, nIterator=100, typeRandom = 0)
# print("individual optimal = ", binaryMax.optimal(lambda x : np.sum(1/np.abs(x**3+6*(x**2)+9*x-3), axis=1)))
# binaryMax.showGraphLosses()



from AlgorithmGA_LIST import GA_algorithm
import numpy as np

def funcCall(individual):
    
    finess = 0
    x = individual[0]
    finess = x**3+6*(x**2)+9*x-3
    
    return 1/finess
        
binaryMax = GA_algorithm(nGen = 1, rangeOfGen = (-4,0), 
                            nIndividual=1000, nIterator=100, typeRandom = 0)
print("individual optimal = ", binaryMax.optimal(funcCall))
binaryMax.showGraphLosses()