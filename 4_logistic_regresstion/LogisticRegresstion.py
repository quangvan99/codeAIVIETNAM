import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("irispetal.csv", delimiter=',', skip_header=1)

def signmod(z):
    result = 1/(1+np.exp(-z))
    result[result<=0] = 0
    result[result>=1] = 1
    return result

def crossentropy(y, predict):
    return -y*np.log(predict) - (1-y)*np.log(1-predict)

def loss_grd_z(y, predict):
    return predict - y

def oneHoding(predict):
    predict[predict<0.5] = 0
    predict[predict>=0.5] = 1
    return predict

class LogisticRegression:
    
    def __init__(self, data, rate, miniBatchSize = None, epochs = 100):
        data = data[:].copy()
        self.features = data[:, 0:-1]
        self.y = data[:, -1:]
        self.rate = rate
        self.epochs = epochs
        self.nData = self.features.shape[0]
        self.miniBatchSize = miniBatchSize
        self.w = np.random.rand(self.features.shape[1], self.y.shape[1])
        self.b = np.random.rand(1)
        self.losses = []
        self.accuracy = []
        
    def nomal(self, features):
        mini = np.min(features)
        maxi = np.max(features)
        meani = np.mean(features)
        return (features - meani)/(maxi - mini), (maxi, mini, meani)
    
    def run(self):
        if (self.miniBatchSize == None):
            self.miniBatchSize = self.nData
            
        for epoch in range(self.epochs):
            iFillter = np.random.randint(0, self.nData, 
                                         size=(self.miniBatchSize,))
            xFillter = self.features[iFillter]
            yFillter = self.y[iFillter]
            
            predict = signmod(xFillter.dot(self.w) + self.b)
            
            loss = crossentropy(yFillter, predict)
            self.losses.append(loss.mean())
            
            self.accuracy.append((oneHoding(predict.copy()) == yFillter).mean())
            
            grd_z = loss_grd_z(yFillter, predict)/self.nData

            self.w -= self.rate*xFillter.T.dot(grd_z)
            self.b -= self.rate*np.sum(grd_z)
        return oneHoding(self.features.dot(self.w) + self.b)
    def showLossGraph(self, f):
        plt.plot(f, 'r')
        plt.show()
        
ls = LogisticRegression(data, 1, 64)
a = ls.run()
ls.showLossGraph(ls.accuracy)