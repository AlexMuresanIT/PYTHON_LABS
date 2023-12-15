import pandas as pd
from pandas import ExcelWriter
from openpyxl import Workbook


def convert(s):
    new = ""
    for x in s:
        new += x
    return new

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "ID"
sheet["B1"] = "Autor"
sheet["C1"] = "Citat"


with open('proba.txt') as f:
    lines = f.readlines()

p=0
for i in range(2,27):
    sheet["A"+str(i)]=p
    p=p+1

autori=[]
p=2
for i in lines:
    for j in range(0,len(i)):
        autor=[]
        if i[j]=="-" and i[j+1]==" ":
            for k in range(j+2,len(i)-1):
                autor.append(i[k])
            a1=convert(autor)
            sheet["B"+str(p)]=a1
            p=p+1

p=2
for i in lines:
    citat=[]
    for j in range(0,len(i)):
        if i[j]=="-" and i[j-1]==" " and i[j+1]==" ":
            break
        else:
            citat.append(i[j])
    a2=convert(citat)
    sheet["C" + str(p)] = a2
    p = p + 1

workbook.save(filename="Citate.xlsx")

