#!/usr/bin/env python3

import requests, re

url = input("Enter url > ")
var = requests.get(url).text

print("Images: ")
print("#"*20)
for image in re.findall("<img (.*)>", var):
  for images in image.split():
    if re.findall('src=(.*)', images):
      image = images.replace("src=\"","")
      print('\t', end="")
      if(image.startswith("http")):
        print(image)
      else:
        print(url+image)
print("#"*20)
print("Links: ")
print("#"*20)
for link, name in re.findall("<a (.*)>(.*)</a>", var):
  for a in link.split():
    if re.findall("href=(.*)",a):
      url_image = a[0:-1].replace('href="',"")
      print('\t', end="")
      if(url_image.startswith("http")):
        print(url_image)
      else:
        print(url+url_image)
