#!/usr/bin/env python3

import socket
import geoip2.database
import argparse
import json

parser = argparse.ArgumentParser(description='Get IP Geolocation info')
parser.add_argument('-host','--hostname', action='store', dest='hostname', default='python.org')

parsed_args = parser.parse_args()

hostname = parsed_args.hostname

ip_address = socket.gethostbyname(hostname)
print(f'IP address: {ip_address}')

reader = geoip2.database.Reader('/Users/jadenandrews/GeoLite2-City_20221220/GeoLite2-City.mmdb')
response = reader.city(ip_address)
if response is not None:
  print('Country: ', response.country, end='\n\n')
  print('Continent: ', response.continent, end='\n\n')
  print('Location: ', response.location, end='\n\n')
