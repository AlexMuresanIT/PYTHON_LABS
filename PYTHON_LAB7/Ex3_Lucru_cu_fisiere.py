from docx2python import docx2python


doc_result=docx2python("D:\\Scoala\\an3\\PYTHON_IA\\PYTHON_LAB7\\Raport_Stiintific_Tehnic.docx")
#print(doc_result)
#separate components of the document
#print(doc_result.body)

#get the text from the file
#print(doc_result.body[0])

#get the image
#print(doc_result.body[1])

#get the table text
#print(doc_result.body[2])

#get all the text in a single string
text=doc_result.text
#print(text)

#get the headers
headers=doc_result.header
#print(headers)

#get the footers
footer=doc_result.footer
print(footer)




