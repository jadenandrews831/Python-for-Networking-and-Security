#!/usr/bin/env python3

import shodan
import argparse
import socket
import sys
import os

SHODAN_API_KEY=os.environ['SHODAN_API_KEY']
api=shodan.Shodan(SHODAN_API_KEY)

parser = argparse.ArgumentParser(description='Shodan Search')
parser.add_argument('-t', '--target', dest='target', help='target IP / domain', required=None)
parser.add_argument('-s', '--search', dest='search', help='search', required=None)

parsed_args = parser.parse_args()
if len(sys.argv)>1 and sys.argv[1] in ('--search', '-s'):
  try:
    results = api.search(parsed_args.search)
    print(f"Results: {results['total']}")
    for result in results:
      print(f"IP: {result['ip_str']}")
      print(result['data'])
  except shodan.APIError as exception:
    print(f'Error: {exception}')

if len(sys.argv)>1 and sys.argv[1] in ('--target', '-t'):
  try:
    hostname = socket.gethostbyname(parsed_args.target)
    results = api.host(hostname)
    print(f"""
            IP: {results['ip_str']}
            Organization: {results.get('org', 'n/a')}
            Operating System: {results.get('os', 'n/a')}
            """)
    for item in results['data']:
      print(f"Port: {item['port']} Banner: {item['data']}")
  except shodan.APIError as e:
    print(f"Error: {e}")