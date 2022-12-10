import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(100)
s.connect(('localhost', int(input("Port: "))))
s.send(b'Hello from the TCP Client (waves)')
print(s.recv(4096).decode())