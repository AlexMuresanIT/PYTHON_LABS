import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

file=pd.read_excel("D:\\Scoala\\an3\\PYTHON_IA\\PYTHON_LAB6\\Perspective_criza_e.xlsx")

prima_col=file["Marcaj de timp"]
ora=[]

for i in prima_col:
    ora.append(datetime.datetime.strftime(i,("%H")))
print(len(ora))


X=np.arange(0,20,1)
plt.plot(X,ora,color="blue")
plt.xlabel("Numar in lista")
plt.ylabel("Ora exacta")
plt.show()