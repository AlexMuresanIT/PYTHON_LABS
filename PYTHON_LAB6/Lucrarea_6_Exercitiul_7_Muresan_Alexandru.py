import pandas as pd
import matplotlib.pyplot as plt

link = "https://data.gov.ro/dataset/4b5701ba-be6d-4c5e-958c-09d7c477552f/resource/f5b5ef46-0fa0-4752-b598-69ed0d23fe81/download/date_deschise_po_ianuarie_2022.csv"
myfile = pd.read_csv(link)

c1=myfile.iloc[:,"Judet"]
c2=myfile["TOTAL  persoane ocupate, din care:  "]

plt.bar(c1,c2,color="red")
plt.xlabel("Judete")
plt.ylabel("Valori")
plt.show()

