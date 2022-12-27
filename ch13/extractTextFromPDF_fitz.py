#!/usr/bin/env python3

import fitz

pdf_document = 'pdf/JadenAndrewsResume12122022.pdf'
doc = fitz.open(pdf_document)
print(f'number of pages: {doc.page_count}')
page_number = input('Enter page number: ')
page = doc.load_page(int(page_number)-1)
page_text = page.get_text('text')
print(page_text)


