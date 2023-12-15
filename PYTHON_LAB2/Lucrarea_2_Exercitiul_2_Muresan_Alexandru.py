text = input("Introdu textul:")
ct_Python=0
ct_spaces=0
ct_char=0
ct_cuv=0
string=""

for x in text:
    if x != " ":
        ct_char+=1
    if x == " ":
        ct_spaces+=1
        ct_char+=1
        ct_cuv+=1
    if x =="P":
        string = x
    if x=="y":
        string = string+x
    if x == "t":
         string = string+x
    if x=="h":
        string = string+x
    if x == "o":
         string = string +x
    if x == "n":
        string = string+x
    if string == "Python":
        ct_Python+=1
        string = ""


print("Numarul de spatii: " ,ct_spaces)
print("Numarul de caractere: " ,ct_char)
print("Numarul de cuvinte 'Python': ",ct_Python)
print("Numarul de cuvinte: ",ct_cuv)


