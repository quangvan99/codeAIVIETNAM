# # -*- coding: utf-8 -*-
# """
# Created on Wed Sep  9 16:34:56 2020

# @author: Admin
# """
# from AlgorithmGA_LIST import GA_algorithm

# def load_data():
#     map = []
#     file = open('data_route.txt', 'r')
#     lines = file.readlines()
    
#     for line in lines:
#         line = line.split(',')
#         nums = []
#         for num in line:
#              nums.append(int(num))
#         map.append(nums)
        
#     file.close()
#     return map

# map = load_data()

# def funcCost(individual):
#     n = len(individual)
    
#     if len(set(individual)) != n:
#         return 1/1000000
    
#     cost = 0
#     for i in range(n-1):
#         cost += (map[individual[i] - 1][individual[i+1] - 1])
#     cost += map[individual[-1] - 1][individual[0] - 1]   

#     return 1/cost

# travelOpimal = GA_algorithm(5, (1,5), 100, 20, 1)
# travelOpimal.optimal(funcCost)
# travelOpimal.showGraphLosses()
# print(travelOpimal.getOptimal)
# print(1/funcCost(travelOpimal.getOptimal))
from GA_algorithm import GA_algorithm
import numpy as np

data = np.genfromtxt('data_route.txt', delimiter=',')

def funcCost(population):
    cost = np.sum(data[population[:,0:-1] - 1,population[:,1:] - 1], axis=1)
    cost += data[population[:,-1] - 1,population[:,0] - 1]
    idx = [len(np.unique(i)) != len(i) for i in population]
    cost[idx] = 100000

    return 1/cost

travelOpimal = GA_algorithm(5, (1,5), 1000, 20, 1)
travelOpimal.optimal(funcCost)
travelOpimal.showGraphLosses()
a = travelOpimal.getOptimal
cost = np.sum(data[a[0:-1] - 1,a[1:] - 1])
cost += data[a[-1] - 1,a[0] - 1]
print(a)
print(cost)