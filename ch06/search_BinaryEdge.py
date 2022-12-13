from pybinaryedge import BinaryEdge

import os

key=os.environ['Binary_Edge_API_KEY']
binaryEdge = BinaryEdge(key)
search_domain = 'www.python.org'
results = binaryEdge.host_search(search_domain)
for ip in results['events']:
  print(f"{ip['target']['ip']}")