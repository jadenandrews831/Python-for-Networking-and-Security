#!/usr/bin/env python3

import PyPDF2

pdfFile = open('pdf/JadenAndrewsResume12122022.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFile)
page_number = input('Enter a page number> ')
pageObj = pdfReader.pages[int(page_number) - 1]   # used to be .getPage()
text_pdf = str(pageObj.extract_text())    # used ot be .extractText()
print(text_pdf)