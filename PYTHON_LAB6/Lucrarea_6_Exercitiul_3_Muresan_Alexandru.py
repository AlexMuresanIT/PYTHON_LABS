file=open("D:\\Scoala\\an3\\PYTHON_IA\\PYTHON_LAB6\\text.txt","r")
text=file.readline()

text=text.replace('"',"")
text=text.replace(":","")
text=text.replace(",","")
text=text.replace(".","")
text=text.replace("?","")
text=text.replace("!","")
text=text.replace("(","")
text=text.replace(")","")
text=text.replace("-","")
text=text.replace("_","")
text=text.replace("=","")

cuv=text.split()

dict={}

for i in cuv:
    dict[i]=0

for i in cuv:
    dict[i]+=1
for i in dict:
    print(i,":",dict[i])

