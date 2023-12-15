from cryptography.fernet import Fernet

def obtinere_cheie():
    key=Fernet.generate_key()
    return key

def decriptare(text,key):

    fernet=Fernet(key)
    encrypted=fernet.decrypt(text)
    print(encrypted)

key=obtinere_cheie()
mesaj="gAAAAABiIfYm7AjgizG1mn8Cd_JJuy2GRSkmbBohwkute-pR7Yu9BOZwwunsc4bvXRtDvHBQnaT3NtxdvDkuzBbHtqSqsM8THsrMnuPOAhMtdM4MWHBiTOQ="
b=bytes(mesaj,"utf-8")
b=mesaj.encode("utf-8")
print("Mesajul decriptat este: ")
decriptare(b,key)

