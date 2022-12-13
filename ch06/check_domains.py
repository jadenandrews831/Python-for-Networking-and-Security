#!/usr/bin/env python3

import argparse
import dns.name

def main(domain1, domain2):
  domain1 = dns.name.from_text(domain1)
  domain2 = dns.name.from_text(domain2)
  print('domain1 is subdomain of domain2: ', domain1.is_subdomain(domain2))
  print('domain2 is subdomain of domain1: ', domain2.is_subdomain(domain1))

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Check 2 domains with dnsPython')
  parser.add_argument('-d1 --domain1', action='store', dest='domain1', default='python.org')
  parser.add_argument('-d2 --domain2', action='store', dest='domain2', default='docs.python.org')
  given_args = parser.parse_args()
  domain1 = given_args.domain1
  domain2 = given_args.domain2
  main(domain1, domain2)