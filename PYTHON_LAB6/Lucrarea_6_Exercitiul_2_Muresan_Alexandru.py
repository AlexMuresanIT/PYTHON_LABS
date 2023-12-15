secventa_ADN=input("Da-ti secventa ADN pentru verificare: ")
esantioane=["GTA","GGG","GAC"]

def ADN():

    ct_es=0
    for i in esantioane:
        for j in range(len(secventa_ADN)):
            if i[0]==secventa_ADN[j]:
                if i[1]==secventa_ADN[j+1]:
                    if i[2]==secventa_ADN[j+2]:
                        ct_es+=1

    if ct_es>=3:
        print("Suspectul trebuie investigat mai departe!")
    else:
        print("Suspectul nu trebuie investigat mai departe!")

ADN()




