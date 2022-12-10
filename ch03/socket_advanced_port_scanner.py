#!/usr/bin/env python3
import optparse

from socket import *
from threading import *

def socketScan(host, port):
  try:
    socket_connect = socket(AF_INET, SOCK_STREAM)
    socket_connect.settimeout(5)
    result = socket_connect.connect((host, port))
    print(f'[+] {port:d}/tcp open')
  except Exception as exception:
    print(f'[-] {port:d}/tcp closed')
    print(f'[-] Reason: {exception}/tcp closed')
  finally:
    socket_connect.close()

def portScanning(host, ports):
  try:
    ip = gethostbyname(host)
    print(f'[+] Scan Results for: {ip}')
  except:
    print(f"[-] Cannot resolve '{host}': Unknown host")
    return
  for port in ports:
    t = Thread(target=socketScan, args=(ip, int(port)))
    t.start()

def main():
  parser = optparse.OptionParser('socket_portScan '+ '-H <Host> -P <Port>')
  parser.add_option('-H', dest='host', type='string', help='specify host')
  parser.add_option('-P', dest='port', type='string', help='specify port[s] separated by comma')
  options, args = parser.parse_args()
  host = options.host
  ports = str(options.port).split(',')
  if (host == None) | (ports[0] == None):
    print(parser.usage)
    exit(0)
  portScanning(host, ports)

if __name__ == '__main__':
  main()