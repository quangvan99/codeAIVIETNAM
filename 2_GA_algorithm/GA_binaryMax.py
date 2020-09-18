from GA_algorithm import GA_algorithm
import numpy as np
binaryMax = GA_algorithm(nGen = 6, rangeOfGen = (0,1), 
                           nIndividual=10, nIterator=100, typeRandom = 1)
print("individual optimal = ", binaryMax.optimal(lambda x : np.sum(x, axis=1)))
binaryMax.showGraphLosses()



