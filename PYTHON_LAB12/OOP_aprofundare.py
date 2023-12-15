"""import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url=input("Enter - ")
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,"html.parser")

tags=soup("a")
for tag in tags:
    print(tag.get("href",None))

class Obiect():
    x=0
    def __init__(self):
        print("Sunt construita!")

    def functie(self):
        self.x=self.x+1
        print("Pana acuma",self.x)

    def __del__(self):
        print("Sunt destructurata!")

y=Obiect()
y.functie()
y.functie()
y=42
print(y)

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

p=Point(10,20)
print(p.x,"",p.y)
p.x=100
print(p.x,"",p.y)

import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def norm(self):
        n=math.sqrt(self.x**2+self.y**2)
        return n

    def __eq__(self, other):
        return (self.x==other.x) and (self.y == other.y)

class Rect(Point):

    def area(self):
        Area=(self.norm()+self.norm())**2
        return Area

p1=Point(20,30)
print(p1.x,p1.y,p1.norm())

r1=Rect(10,20)
print(r1.area())
print(r1.norm())

class Parent:
    parentAttr=100
    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAttr(self,attr):
        self.parentAttr=attr
        return self.parentAttr

    def getAttr(self):
        print("Parent attribute: ",self.parentAttr)

class Child(Parent):

    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print("Calling child method")

c=Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

class Parent:
    def call(self):
        print("Calling parent method")

class Child(Parent):
    def call(self):
        print("Calling child method")

c=Child()
c.call()

class JustCounter:
    __secretCount=0
    def count(self):
        self.__secretCount+=1
        print(self.__secretCount)

counter=JustCounter()
counter.count()
counter.count()
print(counter._JustCounter__secretCount)"""

class A(object):
    def __init__(self,items=None):
        if items is None:
            self.items=[]
        else:
            self.items=items
        print(self.items)

class C(list):
    def get_len(self):
        return len(self)

c=C((10,10,121))
print(c.get_len())




