#Exercitiul 1
import math

print("Exercitiul 1:")
class robotica:
    pass
r=robotica()
r.tip="ROBOTICA"
print(r.tip)

print()
#Exercitiul 2
print("Exercitiul 2:")
IR=type("inginer",(),{}) ()
IR.a="Inginer"
IR.b=" robotician"
print(IR.a+IR.b)

IR.x=10
IR.y=20
print(IR.x+IR.y)

print()
#Exercitiul 3
print("Exercitiul 3:")
class student:
    def __init__(self,an_studii,nume):
        self.an_studii=an_studii
        self.nume=nume

s=student(1,"Popescu Mihai")
print("Anul de studiu este:",s.an_studii,"si numele este: ",s.nume)
s.an_studii=2
print("Studentul",s.nume,"a trecut din anul 1 in anul",s.an_studii,"de studii")

print()
#Exercitiul 4
print("Exercitiul 4:")
s1=student(4,"Mihai Dorel")
print("Studentul",s1.nume,"a incheiat studiile si nu mai are rost sa apara in evidentele acelui student, va ramane doar numele")
delattr(s,"an_studii") #stergerea unui atribut

s2=student(2,"Adela Popescu")
print("Studentul",s2.nume,"s-a retras de la studii si trebuie sters din evidente")
del s2 #stergrea unui obiect

print()
#Exercitiul 5
print("Exercitiul 5: ")
s=student("absolvent","alex")
delattr(s,"an_studii")
setattr(s,"stare","absolvent")
print(s.stare)

print()
#Exercitiul 6
print("Exercitiul 6:")
s1=student(3,"Andrei")
s2=student(1,"Marius")
print(type(s1) is type(s2))


print()
#Exercitiul 7
print("Exercitiul 7:")
s1=student(1,"Mihai")
s2=s1
print(s2.nume,s2.an_studii)

print()
#Exercitiul 8
print("Exercitiul 8:")

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def norm(self):
        n=math.sqrt(self.x**2+self.y**2)
        return n

p1=Point(2,3)
print(p1.__dict__)
print(dir(p1))

print()
#Exercitiul 9
print("Exercitiul 9:")

class robotica:
    pass

r=robotica()
r.tip_robot="Colaborativ"
r.producator_robot="ABB"

print()
#Exercitiul 10
print("Exercitiul 10")
class student1:
    def __init__(self, an_studii, nume):
        self.an_studii = an_studii
        self.nume = nume

class student2:
    def __init__(persoana, an_studii, nume):
        persoana.an_studii = an_studii
        persoana.nume = nume

s1=student1(1,"Mihai")
print(s1.nume,s1.an_studii)

s2=student2(1,"Mihai")
print(s2.nume,s2.an_studii)

print()
#Exercitiul 11
print("Exercitiul 11:")
class Student:
    def __init__(self,universitate,an_studii,nume):
        self.universitate="UTCN"
        self.an_studii=an_studii
        self.nume=nume

s1=Student("UBB",3,"Mihai")
print(s1.universitate,s1.an_studii,s1.nume)

print()
#Exercitiul 12
print("Exercitiul 12:")

class student:
    universitate=""
    def __init__(self,an_studii,nume):
        self.an_studii=an_studii
        self.nume=nume

print()
#Exercitiul 13
print("Exercitiul 13:")

class Student():
    def __init__(self,*args,**kwargs):
        pass

print()
#Exercitiul 14
print("Exercitiul 14:")

class student1:
    def __init__(self,n):
        self._nume=[]
        for i in range(0, n):
            s = input("Introdu un nume: ")
            self._nume.append(s)

        def __call__(self, t):
            self._date = []
            for k in range(0, t):
                s = input("Introdu un nume: ")
                self._date.append(s)

#p=student1(1)
#print(p._nume)
#p(2)

print()
#Exercitiul 16
print("Exercitiul 16:")

class Incrementare:
     def __init__(self,start,end):
         self.start=start
         self.end=end

     def __iter__(self):
         return self

     def __next__(self):
         if self.start>self.end:
             raise StopIteration
         else:
             self.start+=1
             return self.start-1

a=0
b=5
c=Incrementare(a,b)
obj=iter(c)

try:
    while True:
        print(next(obj))
except:
    print("GAME OVER")

print()





