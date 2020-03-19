import PyPDF2
import os

os.chdir('/home/daniel/Downloads')

pdfFile = open('meetingminutes1.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)

print(reader.numPages)

page = reader.getPage(0)
print(page.extractText())


# Print entire PDF
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

pdfFile.close()
