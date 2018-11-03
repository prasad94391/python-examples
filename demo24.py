#print("no of char's=",len(open("durga.txt").read()))


from docx import Document

document = Document()
document.save('test.docx')