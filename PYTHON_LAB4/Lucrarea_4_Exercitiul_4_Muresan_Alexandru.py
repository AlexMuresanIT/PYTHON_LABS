class Human:
    def __init__(self,nume,varsta,sex,culoare_ochi,greutate,inaltime):
        self.nume=nume
        self.varsta=varsta
        self.sex=sex
        self.culoare_ochi=culoare_ochi
        self.greutate=greutate
        self.inaltime=inaltime

    def caracteristici(self):
        print("Numele: ",self.nume)
        print("Varsta: ",self.varsta)
        print("Sex: ",self.sex)
        print("Culoare ochi: ",self.culoare_ochi)
        print("Greutate: ",self.greutate," kg")
        print("Inaltime: ",self.inaltime," cm")

person1=Human("Adrian Vasile",22,"M","Caprui",78,176)
person2=Human("Daniela Popescu",25,"S","Albatru",67,168)
person1.caracteristici()
print()
person2.caracteristici()
