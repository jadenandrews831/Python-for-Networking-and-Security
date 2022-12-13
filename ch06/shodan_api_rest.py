#!/usr/bin/env python3

import shodan
import requests
import os

SHODAN_API_KEY=os.environ['SHODAN_API_KEY']
api = shodan.Shodan(SHODAN_API_KEY)
domain = 'www.python.org'
dnsResolve = f'https://api.shodan.io/dns/resolve?hostnames={domain}&key={SHODAN_API_KEY}'
try:
  print(f'Getting url: {dnsResolve}')
  response = requests.get(dnsResolve)
  hostIP = response.json()[domain]
  host = api.host(hostIP)
  print(f"IP: {host['ip_str']}")
  print(f"Organization: {host.get('org', 'n/a')}")
  print(f"Operating System: {host.get('os', 'n/a')}")
except shodan.APIError as e:
  print(f"Error: {e}")