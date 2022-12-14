#!/usr/bin/env python3

import ftplib

def anonymouseLogin(host):
  try:
    ftp = ftplib.FTP(host)
    response = ftp.login('anonymous', 'anonymous')
    print(response)
    if '230 Anonymous access granted' in response:
      print(f'\n[*] {host} FTP Anonymous Login Succeeded.')
      print(ftp.getwelcome())
      ftp.dir()

  except Exception as e:
    print(str(e))
    print(f'\n[-] {host} FTP Anonymous Login Failed.')

host='ftp.be.debian.org'
anonymouseLogin(host)