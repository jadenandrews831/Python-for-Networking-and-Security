import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8080))
s.send(b'GET / HTTP/1.1\r\n\r\nHost: localhost\r\n')
while True:
  r = s.recv(1024)
  if not r:
    break
  print("Response from localhost:\n", r.decode())