import PyPDF2 
import os


# pdf to word.txt converter
pdfs=[]
n=int(input('enter the number of PDFs you want to work on'))
for i in range(n):
    name=input(f'enter the pdf no.{i+1} ')
    pdfs.append(name)
for pdf in pdfs:
    with open(pdf,'rb') as temp:
        reader=PyPDF2.PdfReader(temp)
        text_content=""
        for page in reader.pages:
            text_content+=page.extract_text() or '' #ye short circuit he JS ka ki agar phla true hua means agar text hua pdf ke uss page me to wo text extract krke de dega varna or hone ke karan jab empty page aayega to "" dega in place of None taki code loop break na ho
    with open(f'word_{os.path.splitext(pdf)[0]}.txt','w',encoding='utf-8') as f:
        f.write(text_content)
    print('your pdf to text conversion is done')
