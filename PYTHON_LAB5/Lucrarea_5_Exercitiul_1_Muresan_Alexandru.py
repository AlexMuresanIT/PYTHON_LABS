import time
from datetime import datetime
import calendar

EVEN=[]
def vizualizare_calendar(x):

    print()
    print("Calendarul impreuna cu evenimentele aferente au fost salvate intr-un fisier de tip txt")
    year=2022
    now=datetime.now()
    f=open("D:\\Scoala\\an3\\PYTHON_IA\\PYTHON_LAB5\\calendar.txt","w")
    f.write(str("Calendarul pe anul 2022 este: "))
    f.write(str("\n"))
    f.write(str(calendar.calendar(year)))
    f.write(str("\n"))
    f.write(str("Evenimentele din acest an sunt:"))
    f.write(str("\n"))
    for i in range(len(x)):
        f.write(str(x[i]))
    f.write(str("\n"))
    f.write(str("Calendarul a fost actualizat in data de mai jos:"))
    f.write(str("\n"))
    f.write(str(now))


def adaugare_eveniment():
    x=[]
    year=str(2022)
    month=str(input("Introdu luna:"))
    day=str(input("Introdu ziua:"))
    date1=day+" "+month+" "+year
    nume_eveniment=input("Da un nume evenimentului:")
    x.append((date1,nume_eveniment))
    return x

def stergere_eveniment(x):

        print("Evenimentele existente sunt:")
        for i in range(len(x)):
            print(x[i])
        print("Atentie! Indexul listei evenimentelor incepe de la 1!!!")
        index=int(input("Alege indexul evenimentului care vrei sa fie sters din calendar:"))
        if index<1 and index > len(x):
            print("Nu ai ales corect indexul evenimentului!!!")
        x.remove(x[index-1])
        return x

def modificare_eveniment(x):

        a=[]
        new=[]
        print("Evenimentele existente sunt:")
        for i in range(len(x)):
            print(x[i])
        print("Atentie! Indexul listei evenimentelor incepe de la 1!!!")
        index = int(input("Alege indexul evenimentului care vrei sa fie modificat:"))
        if index<1 and index > len(x):
            print("Nu ai ales corect indexul evenimentului!!!")
        year=str(2022)
        new_month=str(input("Introdu luna noua:"))
        new_day=str(input("Introdu ziua noua:"))
        date1=new_day+" "+new_month+" "+year
        new_nume_eveniment=str(input("Redenumeste noul eveniment:"))
        a.append((date1,new_nume_eveniment))
        x.remove(x[index-1])
        x.append(a)


def agenda():

    cal=True
    print("Alege o optiune:")
    print("optiunea 1: vizualizare calendar")
    print("optiunea 2: adaugare un eveniment in calendar")
    print("optiunea 3: actualizare eveniment existent")
    print("optiunea 4: stergere eveniment din calendar")
    while cal:

        optiune = int(input("Optiunea aleasa este:"))
        if optiune == 1:
            vizualizare_calendar(EVEN)
            cal=False
        if optiune == 2:
            x=adaugare_eveniment()
            EVEN.append(x)
        if optiune == 3:
            modificare_eveniment(EVEN)
        if optiune == 4:
            stergere_eveniment(EVEN)


agenda()


