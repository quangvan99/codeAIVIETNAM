from GA_algorithm import GA_algorithm
import numpy as np

#============  SỬA Ở ĐÂY  ================
# Đánh giá loss, error của giá trị dự đoán so với giá trị thật (MIN)
def funcCall(population):
    fitness = np.sum(population*population, axis=1)
    
    return 1/(1 + fitness) # Đảo lại thành min để khớp với hàm sorted
#=========================================

minSphere = GA_algorithm(nGen = 4, rangeOfGen = (0,100), nIndividual=100, nIterator=100)
print("individual optimal = ", minSphere.optimal(funcCall))
minSphere.showGraphLosses()

