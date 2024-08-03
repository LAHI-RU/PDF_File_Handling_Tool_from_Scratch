import PyPDF2
import os

def merge_pdfs(input_folder, output_pdf):
    # Remove the existing merged PDF file if it exists
    if os.path.exists(output_pdf):
        os.remove(output_pdf)

    # Get a list of PDF files in the input folder
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]

    # Sort the list of PDF files (optional)
    pdf_files.sort()

    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Loop through each PDF file and merge it into the output PDF
    for pdf_file in pdf_files:
        with open(os.path.join(input_folder, pdf_file), 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

    # Write the merged PDF to the output file
    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

# Example usage:
input_folder = 'pdf_files'  # Path to the folder containing PDF files to merge
output_pdf = 'pdf_files/merged.pdf'   # Output PDF file name (relative path)

merge_pdfs(input_folder, output_pdf)