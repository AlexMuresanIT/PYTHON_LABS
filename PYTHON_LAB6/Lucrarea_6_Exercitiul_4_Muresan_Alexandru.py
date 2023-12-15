class A:
    def __init__(self,x,y,z,u,w):
        self.x=x
        self.y=y
        self.z=z
        self.u=u
        self.w=w

    def f(self):
        if (type(self.x)==int ) and (type(self.y)==str) and (type(self.z)==float) \
            and (type(self.u)==list) and (type(self.w)==bool):
            return [self.x,self.y,self.z,self.u,self.w]
        else:
            return "Eroare tip date"

    def suma(self):
        if type(self.u)==list:
            return sum(self.u)
        else:
            return "Elementul 'u' trebuie sa fie o lista"



a1=A(21,"Alex",10.5,[10,5,15],False)
print(a1.f())
print("Suma elementelor din lista este: ",a1.suma())