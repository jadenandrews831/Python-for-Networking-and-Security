#!/usr/bin/env python3

import shodan
import os

SHODAN_API_KEY=os.environ['SHODAN_API_KEY']
shodan = shodan.Shodan(SHODAN_API_KEY)
try:
  resultados = shodan.search('nginx')
  print(f"results: {resultados.items()}")
except Exception as e:
  print(str(e))
  