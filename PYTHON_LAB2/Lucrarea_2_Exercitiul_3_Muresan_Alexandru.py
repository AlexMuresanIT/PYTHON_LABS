f=open("ex3.txt","r")
message=f.read()
print(message)

def contorPp(sir):
    numar_p=0
    numar_P=0
    for x in message:
        if x == "P":
            numar_P+=1
        if x == "p":
            numar_p+=1

    return numar_p ,numar_P


print("Numarul de aparitii al literelor 'p' si 'P' este: ",contorPp(message))
f.close()