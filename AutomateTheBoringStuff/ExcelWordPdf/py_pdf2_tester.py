import PyPDF2

pdf_path = r''

pdf_file = open(pdf_path, 'rb')
reader = PyPDF2.PdfFileReader(pdf_path)

page = reader.getPage(0)
text = page.extractText()

for page_num in range(reader.numPages):
    print(reader.getPage(page_num))

pdf_file.close()
