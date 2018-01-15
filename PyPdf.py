import PyPDF2

file = open('cv.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(file)
print(pdfreader.getNumPages())
pageObject = pdfreader.getPage(0)
print(pageObject.extractText())

