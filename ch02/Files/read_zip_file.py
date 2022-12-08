#!/usr/bin/env python3

import zipfile

def list_files_in_zip(filename):
  with zipfile.ZipFile(filename) as z:
    for zipinfo in z.infolist():
      yield zipinfo.filename

for filename in list_files_in_zip("files.zip"):
  print(filename)