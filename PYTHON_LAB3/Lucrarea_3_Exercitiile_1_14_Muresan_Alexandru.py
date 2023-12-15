#ex 1
def ret_true(a):
    if type(a)==float and round(a)==a  or type(a)==int:
        return True
    else:
        return False

print("Valoarea introdusa este de tipul int sau float ",ret_true(5.0))

#ex2
j=1
for i in [j*0.5 for j in range(10)]:
    print(i,"->",j)

#ex3
def suma(number):
    sum=0
    if number<0:
        return "Numarul trebuie sa fie pozitiv"
    else:
        for i in str(number):
            sum+=int(i)
    return sum

number = 5234
print("Suma cifrelor numarului ",number," este: ",suma(number))

#ex4
def fact(n):
    prod=1
    for i in range(1,n+1):
        prod*=i
    return prod

number = 6
print("Factorialul numarului ",number," este: ",fact(number))

#ex5
def text_invers(text):
    rev=""
    for i in text:
        rev=i+rev
    return rev

text="UTCN"
print("Inversul textului ",text," este: ",text_invers(text))

#ex6
def no_vowels(text):
    new_text=""
    for x in text.lower():
        for i in "aeiou":
            if x==i:
                x=""
        new_text=new_text+x
    return new_text


text="abecedar"
print("Cuvantul rezultat fara vocale este: ",no_vowels(text))

#ex7
#algoritm pentru a verifica daca un numar este prim
def is_prime(x):
    if x<2:
        return False
    else:
        for n in range(2,x-1):
            if x%n==0:
                return False
            return True

print("Verifica daca numarul este prim: ",is_prime(231))

#ex8
def scor(text):
    sum=0
    punctaj = {"a":2,"b":4,"c":8,"d":5,"e":3,"f":1,"g":7,"h":4,"i":5,"j":5,"k":4,"l":1,"m":2,"n":4,"o":5,"p":3,"q":9,"r":10,"s":6,"t":4,"u":5,"v":9,"w":5,"x":2,"y":1,"z":5}
    for i in text.lower():
        sum+=punctaj[i]
    return sum

print("Suma literelor din cuvant este: ",scor("Robotica"))

#ex9
def inlocuire(text,cuv):
    rez=" "
    stars="*"*len(cuv)
    cuvinte=text.split()
    ct=0
    for i in cuvinte:
        if i==cuv:
            cuvinte[ct]=stars
        ct+=1
    rez=" ".join(cuvinte)
    return rez

print(inlocuire("Alex este student la Robotica","este"))

#ex10
def contor(lista,elem):
    ct=0
    for i in lista:
        if i==elem:
            ct+=1

    return ct

a=[1,2,3,1,4,1,1,5,6,1]
elem=1
print("Elementul",elem," apare de ",contor(a,elem)," ori")

#ex11
def par(lista):
    nou=[]
    for i in lista:
        if i%2==0:
            nou.append(i)
    return nou

a=[2,3,2,5,4,6,7,7]
print("Lista rezultata dupa eliminarea numerelor impare este: ",par(a))

#ex12
def prod_int(lista):
    prod=1
    for i in lista:
        if type(i)==int:
            prod*=i
    return prod

a=[2,2.1,"x",4,"Alex","Muresan",5.5]
print("Produsul numerelor intregi din lista este: ",prod_int(a))

#ex13
def no_identics(lista):
    lista=sorted(lista)
    nx=[]
    dict={}
    for i in range(0,len(lista)):
        dict[lista[i]]=0

    for i in range(0, len(lista)):
        dict[lista[i]]+=1

    for i in range(0,len(lista)):
        if dict[lista[i]]==1:
            nx.append(lista[i])
    return nx

print(no_identics([1,2,1,4,1,3,4,4]))
# 1 1 1 2 3 3 4

#ex14
import numpy as np
def mediana(lista):
    if len(lista)%2==0:
        ct=0
        sum=0
        for i in range(0,len(lista)):
            sum+=lista[i]
            ct+=1
        return float(sum/ct)
    else:
        med=np.median(lista)
        return float(med)

a=[1,2,3,4]
print("Mediana listei este: ",mediana(a))
























