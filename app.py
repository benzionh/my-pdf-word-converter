import pdfkit
import docx

def convert_word_to_pdf(word_file_path, pdf_file_path):
    doc = docx.Document(word_file_path)
    pdfkit.from_file(word_file_path, pdf_file_path)
    print(f"Successfully converted {word_file_path} to {pdf_file_path}")

if __name__ == '__main__':
    word_file_path = 'document.docx'
    pdf_file_path = 'document.pdf'
    convert_word_to_pdf(word_file_path, pdf_file_path)