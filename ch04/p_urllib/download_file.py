#!/usr/bin/env python3

import urllib.request
import subprocess
import os

def del_img():
  files = os.listdir()
  if 'python.png' in files:
    subprocess.run(['rm', '-f', 'python.png'])
  if 'python1.png' in files:
    subprocess.run(['rm', '-f', 'python1.png'])

del_img()
print('starting download...')
url="https://www.python.org/static/img/python-logo.png"
urllib.request.urlretrieve(url, "python.png")
with urllib.request.urlopen(url) as response:
  print("Status:", response.status)
  print("Downloading python1.png")
  with open("python1.png", 'wb') as image:
    image.write(response.read())

