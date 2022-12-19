import subprocess

def ping_secure(myserver):
  command = ['ping', '-c', '1', myserver]
  return command

print(ping_secure('8.8.8.8'))
