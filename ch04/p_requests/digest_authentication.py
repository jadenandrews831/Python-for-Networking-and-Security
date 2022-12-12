#!/usr/bin/env python3

import requests

from requests.auth import HTTPDigestAuth
from getpass import getpass

user=input("Get username: ")
passwd = getpass()

url = 'http://httpbin.org/digest-auth/auth/user/pass'
response = requests.get(url, auth=HTTPDigestAuth(user, passwd))
print("Headers request : ")
for header, value in response.request.headers.items():
  print(f"{header} --> {value}")
print("Response.status_code: ", str(response.status_code), str(response.reason))
if response.status_code == 200:
  print('Login successful :'+str(response.json()))
  print("Headers response: ")
  for header, value in response.headers.items():
    print(f"{header} --> {value}")
