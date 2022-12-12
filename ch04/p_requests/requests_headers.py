#!/usr/bin/env python3

import requests, json

domain = input("Enter the hostname: http://")
response = requests.get("http://"+domain)
print(response.json)
print("Status code: "+str(response.status_code))
print("Headers response: ")
for header, value in response.headers.items():
  print(f"\t{header} --> {value}")
print("Header requests: ")
for header, value in response.request.headers.items():
  print(f"\t{header} --> {value}")

