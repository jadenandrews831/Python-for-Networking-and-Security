#!/usr/bin/env python3

import urllib.request

from urllib.request import Request

url='http://python.org'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'

def chrome_user_agent():
  opener = urllib.request.build_opener()
  opener.addheaders = [('User-agent', USER_AGENT)]
  urllib.request.install_opener(opener)
  response = urllib.request.urlopen(url)
  print("Repsonse headers")
  print("-"*20)
  for header, value in response.getheaders():
    print(header+':'+value)

  request = Request(url)
  request.add_header('User-agent', USER_AGENT)
  print("\nRequest headers")
  print('-'*20)
  for header, value in request.header_items():
    print(header+':'+value)

if __name__ == "__main__":
  chrome_user_agent()