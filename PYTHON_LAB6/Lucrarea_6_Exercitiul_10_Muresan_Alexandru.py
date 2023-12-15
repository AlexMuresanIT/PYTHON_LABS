import matplotlib.pyplot as plt
import numpy as np

def Z(x,y):
    return np.prod([y,y])-np.prod([x,x])

def domeniu():
    X=np.arange(-100,100,1)
    Y=np.arange(-20,20,0.2)
    G=Z(X,Y)
    return X,Y,G

def plotare(X,Y,G):
    plt.plot(X,Y,G,color="red")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

X,Y,G=domeniu()
plotare(X,Y,G)
