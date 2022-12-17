import sys
import requests

from bs4 import BeautifulSoup, SoupStrainer

xsspayloads = []
with open('XSS-attack-vectors.txt', 'r') as file:
  xsspayloads = file.readlines()
  xsspayloads = [line[:-1] for line in xsspayloads]
print(xsspayloads)
URL = 'http://testphp.vulnweb.com/search.php?test=query'
data = {}
response = requests.get(URL)
for payload in xsspayloads:
  for field in BeautifulSoup(response.text, 'html.parser', parse_only=SoupStrainer('input')):
    print(field)
    if field.has_attr('name'):
      if field['name'].lower() == 'submit':
        data[field['name']] = 'submit'
      else:
        data[field['name']] = payload
  response = requests.post(URL, data=data)
  if payload in response.text:
    print('Payload ' + payload + 'returned in the response') 

# print('\n'+'*'*20+'\n'+response.text)