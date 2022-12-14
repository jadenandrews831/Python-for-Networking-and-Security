import pysftp
import getpass

host = 'localhost'
port = 22

def sftp_getfiles(user, pss, host=host, port=port):
  with pysftp.Connection(host=host, port=port, username=user, password=pss) as sftp:
    print("Connection successfully established with server...")
    sftp.cwd('/')
    list_directory = sftp.listdir_attr()
    for directory in list_directory:
      print(directory.filename, directory)

if __name__ == '__main__':
  host = input("Enter the target hostname: ")
  port = input("Enter the target port: ")
  user = input("Enter username: ")
  pss = getpass.getpass(prompt='Enter password: ')
  sftp_getfiles(user, pss, host, port)
