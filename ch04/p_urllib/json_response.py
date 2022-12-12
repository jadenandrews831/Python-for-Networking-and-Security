#!/usr/bin/env python3

import urllib.request
import json

url='http://httpbin.org/get'

with urllib.request.urlopen(url) as response:
  data_json = json.loads(response.read().decode())
  print(data_json)