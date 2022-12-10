import socket

host = 'localhost'
port = 6789

address = host, port

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
  message = input("enter your message > ")
  if message == "quit":
    break
  sock.sendto(message.encode(), address)
  response, addr = sock.recvfrom(4096)
  print(f"Response from the server => {response}")
  sock.close()

  