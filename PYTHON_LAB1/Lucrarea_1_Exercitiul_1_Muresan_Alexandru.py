from datetime import datetime

option=input("Alegeti o valoare ").upper()
acum=datetime.now()

if option == "V1":
        print("Ai ales optiunea: ", option)
        print(acum.hour, ".", acum.minute, ".", acum.second)
elif option=="V2":
        print("Ai ales optiunea: ", option)
        print(acum.hour,".",acum.minute,".",acum.second)
elif option == "V3":
        print("Ai ales optiunea: ", option)
        print(acum.hour,".",acum.minute,".",acum.second)
elif option == "V4":
        print("Ai ales optiunea: ", option)
        print(acum.hour,".",acum.minute,".",acum.second)
else:
        print("Nu ai ales o varianta corecta. Alege o alta varianta")










