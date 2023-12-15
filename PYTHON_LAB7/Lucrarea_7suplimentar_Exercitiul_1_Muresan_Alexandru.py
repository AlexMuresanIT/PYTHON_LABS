from docx2python import docx2python

cuv={}
cuv_cheie=["tehnic","tehnologie","inovare","cercetare"]

doc_result=docx2python("D:\\Scoala\\an3\\PYTHON_IA\\PYTHON_LAB7\\Raport_Stiintific_Tehnic.docx")
text=doc_result.text

text=text.replace("-"," ")
text=text.replace("…"," ")
text=text.replace("_"," ")
text=text.replace("png"," ")
text=text.replace("media/image1"," ")
text=text.replace("media/image2"," ")
text=text.replace("."," ")


text=text.split()

print("Numarul de cuvinte din text este: ",len(text))

for i in text:
    cuv[i]=0
for i in text:
    cuv[i]+=1
print("Cuvintele utizilate si nr de aparitii sunt: ")
for i in cuv:
    print(i,":",cuv[i])

cuv_t_a=[]
for i in text:
    if (i[len(i)-1]=="a" or i[len(i)-1]=="c") and (i[0]=="t" or i[0]=="T"):
        cuv_t_a.append(i)
print(cuv_t_a)








