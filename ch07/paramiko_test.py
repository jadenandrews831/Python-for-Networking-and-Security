import paramiko
import socket
import os

host = 'localhost'
username = os.environ['USER_NAME']
password = os.environ['PASSWORD']
try:
  ssh_client = paramiko.SSHClient()
  paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)
  ssh_client.load_system_host_keys()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  response = ssh_client.connect(host, port = 22, username = username, password = password)
  print('connected with host on port 22', response)
  transport = ssh_client.get_transport()
  security_options = transport.get_security_options()
  print(security_options.kex)
  print(security_options.ciphers)
except paramiko.BadAuthenticationType as e:
  print('BadAuthenticationException: '. e)
except paramiko.SSHException as sshe:
  print('SSHException: ', sshe)
except socket.error as se:
  print('Socket Error: ', se)
finally:
  print('closing connection')
  ssh_client.close()
  print('closed')

