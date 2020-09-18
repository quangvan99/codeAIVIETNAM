# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 16:38:42 2020

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

data = np.genfromtxt("irispetal.csv", delimiter=',', skip_header=1)

def softmax(z):
    exp_z = np.exp(z)
    return exp_z/np.sum(exp_z, axis=1, keepdims=True)

def cross_entropy(y, predict):
    return -np.log(predict[range(len(y)), y])

class SoftmaxRegresstion:
    def __init__(self, data, rate, miniBatchSize = None, epochs = 1000):
        data = data[:].copy()
        self.features = data[:, :-1]
        self.y = data[:, -1].astype(np.int64)
        self.rate = rate
        self.epochs = epochs
        self.nData = len(data)
        self.miniBatchSize = miniBatchSize
        self.nClass = len(np.unique(self.y))
        self.w = np.random.randn(self.features.shape[1], self.nClass)
        self.b = np.random.randn(self.nClass, )
        self.losses = []
        self.accuracy = []
                      
    def run(self):
        if self.miniBatchSize == None:
            self.miniBatchSize = self.nData
        maxWB = 0
        for epoch in range(self.epochs):
            iFillter = np.random.randint(0, self.nData, 
                                         size=(self.miniBatchSize,))
            xFillter = self.features[iFillter]
            yFillter = self.y[iFillter]
            
            predict = softmax(xFillter.dot(self.w) + self.b)
            self.losses.append(cross_entropy(yFillter, predict).mean())
            self.accuracy.append(np.sum(np.argmax(predict, axis=1) == yFillter))
            loss_grd = predict
            loss_grd[range(self.miniBatchSize), yFillter] -= 1
            loss_grd /= self.miniBatchSize
            
            self.w -= self.rate * xFillter.T.dot(loss_grd)
            self.b -= self.rate * np.sum(loss_grd, axis=0)
            
        def showGraph(self):
            plt.figure(figsize=(10, 6))
            plt.scatter(self.features[self.y == 0][:, 0], self.features[self.y == 0][:, 1], color='b', label='0')
            plt.scatter(self.features[self.y == 1][:, 0], self.features[self.y == 1][:, 1], color='r', label='1')
            plt.scatter(self.features[self.y == 2][:, 0], self.features[self.y == 2][:, 1], color='g', label='2')
            plt.legend()
            h = 0.01
            x_min, x_max = self.features[:, 0].min() - 1, self.features[:, 0].max() + 1
            y_min, y_max = self.features[:, 1].min() - 1, self.features[:, 1].max() + 1
            xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
            Z = np.dot(np.c_[xx.ravel(), yy.ravel()], self.w) + self.b
            Z = np.argmax(Z, axis=1)
            Z = Z.reshape(xx.shape)
            fig = plt.figure()
            plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral, alpha=0.8)
            plt.scatter(self.features[:, 0], self.features[:, 1], c=self.y, s=40, cmap=plt.cm.Spectral)
            plt.xlim(xx.min(), xx.max())
            plt.ylim(yy.min(), yy.max())
        
a = SoftmaxRegresstion(data, 0.1, 30)
a.run()
plt.plot(a.accuracy)
plt.show()