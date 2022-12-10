import socket

try:
  result = socket.gethostbyaddr('8.8.8.8')
  print('The host name is: ', result[0])
  print("Ip addresses: ")
  for item in result[2]:
    print("", item)
except socket.error as e:
  print("error for resolving ip addresses:", e)