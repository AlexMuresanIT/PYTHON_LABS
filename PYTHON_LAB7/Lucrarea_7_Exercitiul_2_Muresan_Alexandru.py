from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def x(u,v):
    return 5/4*(1-(v/2*np.pi))*np.cos(2*v)*(1+np.cos(u))+np.cos(2*v)

def y(u,v):
    return 5/4*(1-(v/2*np.pi))*np.cos(2*v)*(1+np.cos(u))+np.cos(2*v)

def z(u,v):
    return (10*v/2*np.pi)+5/4*(1-(v/2*np.pi))*np.sin(u)+15

u=np.linspace(-30,30,100)
v=np.linspace(-30,30,100)

U,V=np.meshgrid(u,v)
X=x(U,V)
Y=y(U,V)
Z=z(U,V)

ax=plt.axes(projection="3d")
ax.contour3D(X,Y,Z,100,cmap="Blues")
ax.set_title("Reprezentare grafica a functiei F(x(u,v),y(u,v),z(u,v))")
ax.set_xlabel("Axa x")
ax.set_ylabel("Axa y")
ax.set_zlabel("Axa z")
plt.show()