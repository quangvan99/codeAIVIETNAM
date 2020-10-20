# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:02:44 2020

@author: Admin
"""
import random
import matplotlib.pyplot as plt

class GA_algorithm():
    '''
    return:
        class aims find parameter optimal for problem
    
    Parameter: 
        nGen is quantum parameter
        rangeOfGen is values parameter can get
        nIndividual is quantum individual
        nIterator: loop for optimal
        typeRandom: 1 is int and 0 is float
    '''
    def __init__(self, nGen, rangeOfGen, nIndividual, nIterator, typeRandom = 0, 
                 rateCross=0.9, rateMutate=0.05, elitism = 2):
        self.nGen = nGen
        self.rangeOfGen = rangeOfGen
        self.nIndividual = nIndividual
        self.nIterator = nIterator
        self.rateCross = rateCross
        self.rateMutate = rateMutate
        self.elitism = elitism
        self.nIterator = nIterator
        self.getOptimal = None
        self.losses = []
        self.typeRandom = typeRandom
        
    # Khởi tạo random từng THAM SỐ   
    def initGen(self):
        if self.typeRandom:
            return random.randint(self.rangeOfGen[0], self.rangeOfGen[1])
        return random.uniform(self.rangeOfGen[0], self.rangeOfGen[1])
    
    # Khởi tạo BỘ THAM SỐ
    def initIndividual(self):
        return [self.initGen() for _ in range(self.nGen)]
    
    # Khởi tạo quần thể BỘ THAM SỐ
    def getPopulation(self):
        return [self.initIndividual() for _ in range(self.nIndividual)]
    
    # Chọn 1 BỘ THAM SỐ từ quần thể đã sắp xếp
    def selectionIndiviual(self, sort_population):
        return sort_population[max(random.randint(0, self.nIndividual-1), 
                                    random.randint(0,self.nIndividual-1))]
    #======== funcCost mặc định =======
    def funcCost(self, individual):
        return sum(individual)
    # Chéo 2 BỘ THAM SỐ
    def crossIndividual(self, individual1, individual2):
        for i in range(self.nGen):
            if (random.random() < self.rateCross):
                individual1[i], individual2[i] = individual2[i], individual1[i]
        return individual1, individual2
    
    # Đột biến 1 BỘ THAM SỐ
    def mutateIndividual(self, individual):
        for i in range(self.nGen):
            if (random.random() < self.rateMutate):
                individual[i] = self.initGen()
        return individual
    
    # Tạo 1 quần thể mới sau khi lai tạo
    def newIndividual(self, sort_population):
        newPopulation = []
        while len(newPopulation) < self.nIndividual-self.elitism :
            individual1 = self.selectionIndiviual(sort_population)
            individual2 = self.selectionIndiviual(sort_population)
            
            individual1, individual2 = self.crossIndividual(individual1[:], 
                                                            individual2[:])
            individual1 = self.mutateIndividual(individual1)
            individual2 = self.mutateIndividual(individual2)
            newPopulation.append(individual1)
            newPopulation.append(individual2)
            
        for x in sort_population[-self.elitism:]:
            newPopulation.append(x)
            
        return newPopulation
    
    # tối ưu BỘ THAM SỐ từ việc chạy lại nhiều lần
    def optimal(self, funcCall = None):
        sort_population = [i.copy() for i in self.getPopulation()]
        if funcCall == None:
            funcCall = self.funcCost
        for _ in range(self.nIterator):
            newPopulation = sorted(sort_population, key=funcCall)
            sort_population = self.newIndividual(newPopulation)  
            self.losses.append(1/funcCall(sort_population[-1]))
        self.getOptimal = sort_population[-1]
        return funcCall(self.getOptimal)
    #=========================================
    
    # Quan sát đồ thị
    def showGraphLosses(self):
        if (self.losses == []):
            print("you need run optimal Function!!")
            return
        
        plt.plot(self.losses)
        plt.show()