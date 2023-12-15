from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def F(x,y):
    return np.sqrt(x**2+y**2)*np.sinc(np.sqrt(x**2+y**2))

x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)

X,Y=np.meshgrid(x,y)
Z=F(X,Y)


ax=plt.axes(projection="3d")
ax.contour3D(X,Y,Z,80,cmap="Blues")
ax.set_title("Vizualizare functia F=np.sqrt(x**2+y**2)*np.sinc(np.sqrt(x**2+y**2))")
ax.set_xlabel("Axa x")
ax.set_ylabel("Axa y")
ax.set_zlabel("Axa z")
plt.show()