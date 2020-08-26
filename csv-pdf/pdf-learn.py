import PyPDF2

# we need read binary mode to read  pdf => "rb"
f = open("Working_Business_Proposal.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)

page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
print(page_one_text)


pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page_one)

pdf_output = open("Some_BrandNew_Doc.pdf", "wb")
pdf_writer.write(pdf_output)

# pdf_writer = PyPDF2.PdfFileWriter()

# for i in range(2):
#     page = pdf_reader.getPage(i)
#     pdf_writer.addPage(page)

# pdf_output = open("Some_BrandNew_Doc.pdf", "wb")
# pdf_writer.write(pdf_output)

pdf_output.close()
f.close()
