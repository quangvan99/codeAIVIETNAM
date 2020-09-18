# from AlgorithmGA_LIST import GA_algorithm

# def load_data():
#     # kết nối với file
#     file = open('advertising.csv','r')
#     # readlines giúp việc đọc file theo từng dòng , mỗi dòng là 1 chuỗi
#     lines = file.readlines()
        
#     features = []
#     prices   = []
#     for i in range(1, 201): 
#         strings = lines[i].split(',')
#         feature = [float(s.strip()) for s in strings[:len(strings)-1]]
#         feature.append(1.0) # for bias
#         features.append(feature)
#         prices.append(float(strings[-1]))
#     # Đóng kết nối với file
#     file.close()
    
#     return features, prices
# # load data
# features, yTruth = load_data()


# #============  SỬA Ở ĐÂY  ================
# # Đánh giá loss, error của giá trị dự đoán so với giá trị thật (MIN)
# def funcCall(individual):
#     predicts = []
#     for feature in features:
#         predicts.append(sum(gen*x for (gen,x)in zip(individual, feature)))
    
#     finess = sum(abs(predict-y) for (predict,y) in zip(predicts,yTruth))
    
#     return 1/(1 + finess) # Đảo lại thành max để khớp với hàm sorted
# #=========================================
        
# gaInstance = GA_algorithm(nGen = 4, rangeOfGen = (0,100), nIndividual=100, nIterator=100)
# print("individual optimal = ", gaInstance.optimal(funcCall))
# gaInstance.showGraphLosses()
from GA_algorithm import GA_algorithm
import numpy as np

data = np.genfromtxt('advertising.csv', delimiter=',', skip_header=1)

features, yTruth = data[:,:-1], data[:,-1:]
features = np.append(features, np.ones((len(data),1)), axis=1)

def funcCall(population):
    
    
    return 1/(1 + finess)
        
gaInstance = GA_algorithm(nGen = 4, rangeOfGen = (0,100), nIndividual=100, nIterator=100)
print("individual optimal = ", gaInstance.optimal(funcCall))
gaInstance.showGraphLosses()
