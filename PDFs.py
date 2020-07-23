import PyPDF2 as PDF

with open('./PDFs/dummy.pdf', 'rb') as file:
    print(file)  # <_io.TextIOWrapper name='./PDFs/dummy.pdf' mode='r' encoding='cp1252'>
    reader = PDF.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PDF.PdfFileWriter()
    writer.addPage(page)

    with open('./PDFs/titled.pdf', 'wb') as new_file:
        writer.write(new_file)
