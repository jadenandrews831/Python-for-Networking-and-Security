import dns.reversename
import threading

hosts = ['oreilly.com', 'yahoo.com', 'google.com', 'microsoft.com']

def resolveDNS(host):
  print(host)
  try:
    ip = dns.reversename.to_address(host)
  except Exception as e:
    print(f'Error: {e}')
  else:
    for i in list(ip):
      print(i)

threads = []
for host in hosts:
  t = threading.Thread(target=resolveDNS, args=(host,))
  threads.append(t)


for thread in threads:
  thread.start()
  thread.join()

