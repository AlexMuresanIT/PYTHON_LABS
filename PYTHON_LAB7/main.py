from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


def functie(x,y):
    return np.sin(np.sqrt(x**2+y**2))

x=np.linspace(-6,6,30)
y=np.linspace(-6,6,30)

X,Y=np.meshgrid(x,y)
Z=functie(X,Y)


ax=plt.axes(projection="3d")
ax.contour3D(X,Y,Z,50,cmap="spring")
ax.set_title("Grafic 3D")
ax.set_xlabel("Axa x")
ax.set_ylabel("Axa y")
ax.set_zlabel("Axa z")
plt.show()
