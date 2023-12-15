import csv
c1=[]
c2=[]
c3=[]
with open("Librarie.csv","r") as csvfile:
        csv_reader=csv.reader(csvfile)
        header=next(csv_reader)
        for i in csv_reader:
            c1.append(i[0])
            c2.append(i[2])
            c3.append(i[3])

        lista=[]
        f=lambda x,y:x*y
        for j in range(4):
            p=f(int(c2[j]),float(c3[j]))
            if p<=100:
                p+=10
            lista.append((c1[j],p))
        print(lista)
        

















