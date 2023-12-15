import random

#Ex 5
print("Ex 5:")
lista=["HTML","Python","JavaScript","Ruby"]
rezultat=list(filter(lambda x:x=="Python",lista))
print(rezultat)
print()

#Ex 6
print("Ex 6:")
square_list=[i**2 for i in range(1,11)]
rezultat=list(filter(lambda x:x>=30 and x<=70,square_list))
print(rezultat)
print()

#Ex 7
print("Ex 7")
list1=[]
list=[i for i in range(1,16)]
for i in list:
    if i%3==0 or i%5==0:
       list1.append(i)
print(list1)
print()

#Ex 8
print("Ex 8")
A="IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
print("Sirul inainte de eliminare: ")
print(A)
A_new=""
for i in A:
    if i =="X":
       A_new=A.replace(i,"")
    else:
        A_new+=i
print("Sirul rezultat:")
print(A_new)
print()

#Ex 9
print("Ex 9")
def aruncare_zar():
    list=[1,2,3,4,5,6]
    return random.choice(list)

a1=aruncare_zar()
a2=aruncare_zar()
s=a1+a2

nr=int(input("Introdu un numar cuprins intre 1 si 12:"))
if nr>=s:
    print("BRAVO! Ai castigat!")
else:
    print("SCUZE! Ai pierdut!")




