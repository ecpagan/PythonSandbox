import PyPDF2

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    print(page)
    page.rotateCounterClockwise(90)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as file2:
        writer.write(file2)
