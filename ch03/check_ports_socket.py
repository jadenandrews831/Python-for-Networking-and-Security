import socket, sys

def checkPortsSocket(ip, portlist):
  try:
    for port in portlist:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(5)
      err = s.connect_ex((ip, port))
      if err == 0:
        print(f'Port {port}: \t Open', err)
      else:
        print(f'Port {port}: \t Closed', err)
      s.close()
  except socket.error as e:
    print(f'Connection error: {e}')
    sys.exit()

def main():
  ip_port = ip, ports = 'localhost', [23,26,80,8080,443]
  checkPortsSocket(*ip_port)

if __name__ == '__main__':
  main()