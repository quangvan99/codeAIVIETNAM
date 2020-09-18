# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:02:44 2020

@author: Admin
"""
import numpy as np
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
    
    def getIndividual(self):
        if self.typeRandom:
            return np.random.randint(self.rangeOfGen[0],self.rangeOfGen[1]+1, self.nGen)
        return np.random.uniform(self.rangeOfGen[0],self.rangeOfGen[1], self.nGen)
    
    # Khởi tạo quần thể BỘ THAM SỐ
    def getPopulation(self):
        return np.array([self.getIndividual() for _ in range(self.nIndividual)])
    
    # Chọn 1 BỘ THAM SỐ
    def selectionIndiviual(self, population, funcCost):
        cost = funcCost(population)
        index = np.random.choice(np.arange(self.nIndividual), 
                                 self.nIndividual,
                                 p = cost/cost.sum())
        return population[index]

    # Chéo 2 BỘ THAM SỐ
    def crossIndividual(self, individual1, individual2):
        prob= np.random.random(size = self.nGen) < self.rateCross
        
        individual1[prob], individual2[prob] = individual2[prob], individual1[prob].copy()
        
        return individual1, individual2
    
    # Đột biến 1 BỘ THAM SỐ
    def mutateIndividual(self, individual):
        prob= np.random.random(size = self.nGen) < self.rateMutate
        individual[prob] = self.getIndividual()[prob]
        return individual
    
    # tối ưu BỘ THAM SỐ từ việc chạy lại nhiều lần
    def optimal(self, funcCost):
        population = self.getPopulation()
        for _ in range(self.nIterator):
            population = self.selectionIndiviual(population, funcCost)
            
            for i in range(self.nIndividual//2 - 2):
                
                in1 = population[np.random.randint(0,self.nIndividual)]
                in2 = population[np.random.randint(0,self.nIndividual)]
                
                in1,in2 = self.crossIndividual(in1.copy(),in2.copy())
                
                in1 = self.mutateIndividual(in1)
                in2 = self.mutateIndividual(in2)
                
                population[i*2] = in1
                population[i*2+1] = in2
            
            indexMax = funcCost(population).argsort()[-2:]
            population[-2] = population[indexMax[0]]
            population[-1] = population[indexMax[1]]
            self.losses.append(1/(funcCost(population).sum()+1))
        self.getOptimal = population[-1]
        
        return self.getOptimal
    #=========================================
    
    # Quan sát đồ thị
    def showGraphLosses(self):
        if (self.losses == []):
            print("you need run optimal Function!!")
            return
        
        plt.plot(self.losses)
        plt.show()