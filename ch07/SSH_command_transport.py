import paramiko
import getpass

def run_ssh_command(hostname, user, passwd, cmd):
  transport = paramiko.Transport(hostname)
  try:
    transport.start_client()
  except Exception as e:
    print(e)
  try:
    transport.auth_password(username=user, password=passwd)
  except Exception as e:
    print(e)
  if transport.is_authenticated():
    print(transport.getpeername())
    channel = transport.open_session()
    channel.exec_command(cmd)
    response = channel.recv(1024)
    print(f'Command {cmd}({user})-->{response.decode()}')

if __name__ == '__main__':
  hostname = input('Enter the target hostname: ')
  usrname = input("Enter username: ")
  passwd = getpass.getpass(prompt='Enter password: ')
  command = input("Enter command: ")
  run_ssh_command(hostname, usrname, passwd, command)