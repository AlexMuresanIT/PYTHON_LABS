#contorizare numar de biti ai unui numar intreg pozitiv
def nr_biti(numar):
    if type(numar)!=int:
        return "Numarul introdus nu este intreg"
    if numar<=0:
        return "Numarul introdus trebuie sa fie pozitiv"
    binar=bin(numar)
    return len(binar)-2

numar=1234
print(nr_biti(numar))