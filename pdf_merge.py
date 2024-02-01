import PyPDF2

pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']
output_path = 'merged_file.pdf'
pdf_writer = PyPDF2.PdfFileWriter()
for pdf_file in pdf_files:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page)
with open(output_path, 'wb') as puff:
    pdf_writer.write(puff)
