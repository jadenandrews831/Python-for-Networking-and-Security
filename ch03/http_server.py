import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 8080))
mySocket.listen(5)

while True:
  print('Waiting for connections')
  s, addr = mySocket.accept()
  print('HTTP request received: ')
  print(s.recv(1024))
  s.send(b'HTTP/1.1 200 OK\r\n\r\n <html><body><h1>Hello World!</h1></body></html>\r\n')
  s.close()


