#!/usr/bin/env python3

import shodan
import re
import os

servers = []
SHODAN_API_KEY = os.environ['SHODAN_API_KEY']
shodanApi = shodan.Shodan(SHODAN_API_KEY)
results = shodanApi.search("port: 21 Anonymous user logged in")
print(f"hosts number: {len(results['matches'])}")
for result in results['matches']:
  if result['ip_str'] is not None:
    # servers.append((result, result['ip_str']))
    servers.append(result['ip_str'])
for server in servers:
  # print(server, end="#"*20+'\n\n')
  print(server)