import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', int(input("Port: "))))
s.listen(10)

while True:
  sock, cli_addr = s.accept()
  msg = sock.recv(1024)
  print(f'[+] Recieved from {cli_addr[0]}/{cli_addr[1]}: \n{msg.decode()}')
  sock.send(b'Recieved Message.')
  sock.close()

