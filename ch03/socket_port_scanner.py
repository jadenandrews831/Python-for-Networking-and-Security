import socket
import sys
import errno

from datetime import datetime

remoteServer = input('Enter a remote host to scan: ')
remoteServerIP = socket.gethostbyname(remoteServer)
print("Please enter the range of ports you would like to scan on the machine:")
startPort = input("\tEnter a start port: ")
endPort = input("\tEnter an end port: ")
print("Pleasae wait, scanning remote host:", remoteServerIP)
time_init = datetime.now()
try:
  for port in range(int(startPort), int(endPort)+1):
    print(f"Checking port {port} ...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((remoteServerIP, port))
    if result == 0:
      print(f"Port {port}: Open")
    else:
      print(f"Port {port}: Close")
      print(f'Reason: {errno.errorcode[result]}')
    sock.close()
except socket.error:
  print("couldn't connect to server")
  sys.exit()

time_finish = datetime.now()
total = time_finish - time_init
print(f'Port Scanning Completed in: {total}')