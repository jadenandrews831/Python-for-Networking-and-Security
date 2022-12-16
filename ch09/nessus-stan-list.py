#!/usr/bin/env python3

from nessrest import ness6rest
import argparse
import os

nessus_url = 'https://localhost:8834'
parser = argparse.ArgumentParser(description='Nessus Scan List')
parser.add_argument('-a --accesskey', dest='accesskey', help='Access Key for Nessus', default=os.environ['NESSUS_A'])
parser.add_argument('-s --secretkey', dest='secretkey', help='Secret Key for Nessus', default=os.environ['NESSUS_B'])
parsed_args = parser.parse_args()

akey = parsed_args.accesskey
skey = parsed_args.secretkey

scan = ness6rest.Scanner(url=nessus_url, api_akey=akey, api_skey=skey, insecure=True)

print(scan.scan_list())
scans = scan.scan_list()['scans']

for detail_scan in scans:
  print(scan.scan_details(detail_scan['name']))