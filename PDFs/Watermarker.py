import PyPDF2

input_file = "./super.pdf"
output_file = "./watermarked.pdf"
watermark_file = "./wtr.pdf"

with open(input_file, "rb") as file_handle_input:
    # read content of the original file
    pdf = PyPDF2.PdfFileReader(file_handle_input)

    with open(watermark_file, "rb") as file_handle_watermark:
        # read content of the watermark
        watermark = PyPDF2.PdfFileReader(file_handle_watermark)

        # create a pdf writer object for the output file
        pdf_writer = PyPDF2.PdfFileWriter()

        for i in range(pdf.getNumPages()):
            # get first page of the original PDF
            current_page = pdf.getPage(i)

            # get first page of the watermark PDF
            watermarked_page = watermark.getPage(0)

            # merge the two pages
            current_page.mergePage(watermarked_page)

            # add page
            pdf_writer.addPage(current_page)

            with open(output_file, "wb") as file_handle_output:
                # write the watermarked file to the new file
                pdf_writer.write(file_handle_output)
