import os

from PyPDF2 import PdfReader    # used to be PdfFileReader

def get_metadata():
  for dirpath, dirnames, files in os.walk('pdf'):
    for data in files:
      ext = data.lower().rsplit('.', 1)[-1]
      if ext in ['pdf']:
        print(f'[--- Metadata: {dirpath+os.path.sep+data}')
        print('-'*50)
        pdfReader = PdfReader(open(dirpath+os.path.sep+data, 'rb'))
        info = pdfReader.metadata     # used to be getDocumetnInfo()
        for metaItem in info:
          print(f'[+] {metaItem.strip("/")}: {info[metaItem]}')
        pages = len(pdfReader.pages)    # used to be getNumPages()
        print(f'[+] Pages: {pages}')
        layout = pdfReader.page_layout    # used to be getpageLayout()
        print(f'[+] Layout: {str(layout)}\n')
        xmpinfo = pdfReader.xmp_metadata    # used to be .getXmpMetadata()
        if hasattr(xmpinfo, 'dc_contributor'): print(f'[+] Contributor: {xmpinfo.dc_contributor}')
        if hasattr(xmpinfo, 'dc_identifier'): print(f'[+] Identifier: {xmpinfo.dc_identifier}')
        if hasattr(xmpinfo, 'dc_date'): print(f'[+] Date: {xmpinfo.dc_date}')
        if hasattr(xmpinfo, 'dc_source'): print(f'[+] Source: {xmpinfo.dc_source}')
        if hasattr(xmpinfo, 'dc_subject'): print(f'[+] Subject: {xmpinfo.dc_subject}')
        if hasattr(xmpinfo, 'xmp_modify_date'): print(f'[+] ModifyDate: {xmpinfo.xmp_modify_date}')   # used to be .xmp_modifyDate()
        if hasattr(xmpinfo, 'xmp_metadata_date'): print(f'[+] MetadataDate: {xmpinfo.xmp_metadata_date}')
        if hasattr(xmpinfo, 'xmpmm_document_id'): print(f'[+] DocumentId: {xmpinfo.xmpmm_document_id}')
        if hasattr(xmpinfo, 'xmpmm+instanecId'): print(f'[+] InstanceId: {xmpinfo.xmpmm_instance_id}')
        if hasattr(xmpinfo, 'pdf_keywords'): print(f'[+] PDF-Keywords: {xmpinfo.pdf_keywords}')
        if hasattr(xmpinfo, 'pdf_pdfversion'): print(f'[+] PDF-Version: {xmpinfo.pdf_pdfversion}')
        if hasattr(xmpinfo, 'dc_publisher'): 
          for publisher in xmpinfo.dc_publisher:
            if publisher:
              print(f'[+] Publisher:\t {publisher}')
        print(f'{pdfReader.size} Bytes')
        print()

if __name__ == '__main__':
  get_metadata()

