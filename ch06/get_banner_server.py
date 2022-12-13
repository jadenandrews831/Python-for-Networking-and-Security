import socket
import argparse
import re

parser = argparse.ArgumentParser(description='Get banner server')
# Main Arguments
parser.add_argument('-t --target', dest='target', help='target IP', required=True)
parser.add_argument('-p', '--port', dest='port', type=int, help='port', required=True)
parsed_args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((parsed_args.target, parsed_args.port))
sock.settimeout(2)
query = f'GET / HTTP/1.1\nHost: {parsed_args.target}\n\n'
http_get = query.encode()
data = ''
with open('vulnbanners.txt') as file:
  vulnbanners = file.readlines()
  try:
    sock.sendall(http_get)
    data = sock.recvfrom(4096)
    data = data[0]
    # print(data)
    headers = data.splitlines()
    for header in headers:
      try:
        if re.search('Server:', str(header)):
          print(f"{'*'*5}{header.decode()}{'*'*5}")
        else:
          print(header.decode())
      except:
        pass
    for vulnbanner in vulnbanners:
      if vulnbanner.strip() in str(data.strip().decode()):
        print('Found server vulnerable! ', vulnbanner)
        print(f'Target: {parsed_args.target}')
        print(f'Port: {parsed_args.port}')
  except socket.error:
    print('Socket error', socket.errno)
  finally:
    sock.close()
