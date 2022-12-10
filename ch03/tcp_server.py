import socket
import threading

SERVER_IP = 'localhost'
SERVER_PORT = 9998

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((SERVER_IP, SERVER_PORT))
serv.listen(5)
print(f"[*] Server Listening on {SERVER_IP}:{SERVER_PORT}")
while True:
  print('hi')
  client, addr = serv.accept()
  client.send("I am the server accepting connections...".encode())
  print(f'[*] Accepted connection from {addr[0]}:{addr[1]}')
  def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"[*] Received request : {request} from client {client_socket.getpeername()}")
    client_socket.send(b'ACK')
  while True:
    handle_client(client)
  client_socket.close()
  serv.close()
