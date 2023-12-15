import matplotlib.pyplot as plt
import numpy as np
def g(x):
    try:
        return (1/x+1)+(3/x)-(2/x-1)
    except ZeroDivisionError:
        return 0

def f(x):
    return x**3-3*x

def y():
    Y=np.arange(-100,100,0.1)
    Y=f(Y)
    return Y

def plotare(Y):

    X=np.arange(-100,100,0.1)
    plt.plot(X,Y,color="red")
    plt.ylabel("y=f(x)")
    plt.xlabel("x")
    plt.show()

Y=[]
Y=y()
plotare(Y)
