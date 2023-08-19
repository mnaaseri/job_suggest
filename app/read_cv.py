import os
from PyPDF2 import PdfReader
import docx 


#TO DO: it's not a suggested way to handle different file extensions and should be changed
def read_cv(file_path):
    """
    Handle PDF and doc files.
    """
    _, file_extension = os.path.splitext(file_path)

    if file_extension == '.pdf':
        reader = PdfReader(file_path)
        text = []
        number_of_pages = len(reader.pages)
        for i in range(number_of_pages):
            page = reader.pages[i]
            page_text = page.extract_text()
            text.append(page_text)
            doc = "".join(text)
    elif file_extension == '.docs':
        doc = docx.Document(file_path)
    else:
        raise ValueError("Please Enter a Valid  PDF or docs")
    
    return doc 