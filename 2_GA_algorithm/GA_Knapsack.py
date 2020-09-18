# from AlgorithmGA_LIST import GA_algorithm

# weights = [1, 2, 5, 7, 10, 12, 15, 23, 32, 33, 35, 37]  # can nang cac vat
# prices =  [1, 3, 6, 7, 12, 15, 25, 32, 44, 45, 47, 50]  # gia tri cua cac vat tuong ung
# maxWeight = 70


# def funcCost(individual):
#     cost = 0
#     weight = 0
#     for i in range(len(individual)):
#         if individual[i]:
#             weight += weights[i]
#             if (weight > maxWeight):
#                 return 1/1000000
#             cost += prices[i]
                    
#     return cost

# travelOpimal = GA_algorithm(12, (0,1), 1000, 20, 1)
# travelOpimal.optimal(funcCost)
# travelOpimal.showGraphLosses()
# print(travelOpimal.getOptimal)
# print(funcCost(travelOpimal.getOptimal))
from GA_algorithm import GA_algorithm
import numpy as np

weights = np.array([1, 2, 5, 7, 10, 12, 15, 23, 32, 33, 35, 37])  # can nang cac vat
prices =  np.array([1, 3, 6, 7, 12, 15, 25, 32, 44, 45, 47, 50])  # gia tri cua cac vat tuong ung
maxWeight = 70


def funcCost(population):
    weight = np.sum(population*weights, axis = 1)
    price = np.sum(population*prices, axis = 1)
    for i in range(len(population)):
        if weight[i] > maxWeight:
            price[i] = 1/100000 
                    
    return price

travelOpimal = GA_algorithm(12, (0,1), 2000, 10, 1)
travelOpimal.optimal(funcCost)
travelOpimal.showGraphLosses()
print(travelOpimal.getOptimal)
print(np.sum(travelOpimal.getOptimal*prices))