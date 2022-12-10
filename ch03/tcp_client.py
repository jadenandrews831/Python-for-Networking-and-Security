import socket

host = 'localhost'
port = 9998

try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((host, port))
  print(f'Connected to host {host} in port: {port}')
  message = sock.recv(1024)
  print("Message received from the server:", message)
  while True:
    message = input("Enter your message > ")
    sock.send(message.encode())
    if message == 'quit':
      break
    msg = sock.recv(1024)
    print(msg.decode())
except socket.errno as error:
  print("Socket error ", error)
finally:
  sock.close()
