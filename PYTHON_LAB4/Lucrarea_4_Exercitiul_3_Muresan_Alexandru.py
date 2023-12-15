class Fiinta:
    def poate_sau_nu_poate_vorbi(self,da_sau_nu):
        if da_sau_nu==1:
            return "Poate vorbi"
        else:
            return "Nu poate vorbi"

class Om(Fiinta):
    def __init__(self,da_sau_nu):
        self.da_sau_nu=da_sau_nu

class Pisica(Fiinta):
    def __init__(self,da_sau_nu):
        self.da_sau_nu=da_sau_nu

om=Om(1)
pisica=Pisica(0)
print(om.poate_sau_nu_poate_vorbi(1))
print(pisica.poate_sau_nu_poate_vorbi(0))

