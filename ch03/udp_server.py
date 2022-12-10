import socket, sys

host = 'localhost'
port = 6789

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))
print(f"[*] Server UDP Listening on {host};{port}")
while True:
  data, address = sock.recvfrom(4096)
  sock.sendto("I am the server accepting connections".encode(), address)
  data = data.strip()
  print(f"Message {data} received from {address}")
  try:
    response = f"Hi {sys.platform}"
  except Exception as e:
    response = f"{sys.exc_info()[0]}"
  print("Response: ", response)
  sock.sendto(response.encode(), address)
  sock.close()
