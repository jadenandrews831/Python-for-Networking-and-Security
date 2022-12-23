#!/usr/bin/env python3

import socket
import argparse
import json

from geolite2 import geolite2

parser = argparse.ArgumentParser(description='Get IP Geolocation info')
parser.add_argument('-host', '--hostname', action='store', dest='hostname', default='python.org')
parsed_args = parser.parse_args()

hostname = parsed_args.hostname
ip_address = socket.gethostbyname(hostname)
print(f'IP Address: {ip_address}')
reader = geolite2.reader()
response = reader.get(ip_address)
print(json.dumps(response, indent=4))
print('Continent: ', json.dumps(response['continent']['names']['en'], indent=4))
print('Latitude: ', json.dumps(response['location']['latitude'], indent=4))
print('Longitude: ', json.dumps(response['location']['longitude'], indent=4))
print('Time Zone: ', json.dumps(response['location']['time_zone'], indent=4))
