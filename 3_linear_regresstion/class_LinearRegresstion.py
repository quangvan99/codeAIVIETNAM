# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 08:46:47 2020

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt

class LinearRegresstion:
    """
        propety: 
            path: path of file contain data
            rate: leanring rate
            epochs = 100: Number of loop
            miniBatchSize = None: size of mini Data
        method:
            run(): run LinearRegresstion
            showLossGraph: show graph of losses
                
    """
    
    def __init__(self, data, rate, epochs = 100, miniBatchSize = None):
        self.data, self.coefficient = self.getNomal(data[:].copy())
        self.features = self.data[:, :-1]
        self.y = self.data[:, -1:]
        self.rate = rate
        self.epochs = epochs
        self.w = np.random.rand(self.features.shape[1], self.y.shape[1])
        self.b = np.random.rand(1)
        self.nData = self.features.shape[0]
        self.miniBatchSize = miniBatchSize
        self.losses = []

    def getNomal(self, data):
        maxi = np.max(data, axis = 0)
        mini = np.min(data, axis = 0)
        avg = np.mean(data, axis = 0)
        return (data-avg) / (maxi-mini), (maxi, mini, avg)
    def getDataPredict(self):
        data = self.features.dot(self.w) + self.b
        maxi, mini, avg = self.coefficient
        return data*(maxi - mini) + avg
    
    def run(self):
        if (self.miniBatchSize == None):
            self.miniBatchSize = self.nData
            
        for epoch in range(self.epochs):

                iIndex = np.random.randint(0, self.nData, size=(self.miniBatchSize,))
                xi = self.features[iIndex]
                yi = self.y[iIndex]
                
                predict = self.features[iIndex].dot(self.w) + self.b
                
                loss = 1/2 * (predict - yi)**2
                loss_grd = (predict - yi)/self.miniBatchSize

                self.losses.append(loss.mean())
                self.w -= self.rate * xi.T.dot(loss_grd)
                self.b -= self.rate * np.sum(loss_grd)
        
        return self.w, self.b, self.losses
    def showLossGraph(self):
        plt.plot(self.losses, 'r')
        plt.show()