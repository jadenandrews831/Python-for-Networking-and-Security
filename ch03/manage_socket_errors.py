import socket, sys

host = 'domain/ip_address'
port = 80

try: 
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print(s)
  s.settimeout(5)
except socket.error as e:
  print(f"socket create error: {e}")
  sys.exit(1)

try:
  s.connect((host, port))
  print(s)
except socket.timeout as e:
  print(f"Timeout {e}")
  sys.exit(1)
except socket.gaierror as e:
  print(f"connection error to the server {e}")
  sys.exit(1)
except socket.error as e:
  print(f"Connection error: {e}")
  sys.exit(1)

