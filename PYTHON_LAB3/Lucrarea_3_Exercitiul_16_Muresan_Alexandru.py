from cryptography.fernet import Fernet

key=Fernet.generate_key()
print("Cheia este: ",key)

#am salvat cheia intr-un fisier
f=open("D:\\Scoala\\an3\\PYTHON_IA\\PYTHON_LAB3\\cheia.txt","wb")
f.write(key)
f.close()

#criptare
mesaj="Alex este student la Robotica"
b=bytes(mesaj,"utf-8")
b=mesaj.encode("utf-8")

fernet=Fernet(key)
encrypted=fernet.encrypt(b)
print("Mesajul criptat este salvat in fisierul 'mesaj_criptat' ")
with open("D:\\Scoala\\an3\\PYTHON_IA\\PYTHON_LAB3\\mesaj_criptat.txt","wb") as f:
    f.write(encrypted)

#decriptare
with open("D:\\Scoala\\an3\\PYTHON_IA\\PYTHON_LAB3\\mesaj_criptat.txt","rb") as f:
    data=f.read()
fernet=Fernet(key)
encrypted=fernet.decrypt(data)
print("Mesajul decriptat este: ",encrypted)










