
import numpy as np
def alegere():
    OP=["a","b","c"]
    a=np.random.choice(OP)
    b=input("Alege o varianta")
    if a==b:
        print("AI CASTIGAT!!")
        print("Alegera calculatorului este: ",a)
        print("Alegerea ta este: ",b)
    else:
        print("AI PIERDUT!")
        print("Alegera calculatorului este: ", a)
        print("Alegerea ta este: ", b)

alegere()
