#!/usr/bin/env python3

from ftplib import FTP

ftp_client=FTP('ftp.be.debian.org')
ftp_client.login()
ftp_client.cwd('/www.kernel.org/pub/linux/kernel/v5.x')
ftp_client.voidcmd('TYPE I')
datasock, estsize = ftp_client.ntransfercmd('RETR ChangeLog-5.0')
transbytes=0
with open('ChangeLog-5.0', 'wb') as f:
  while True:
    buffer=datasock.recv(2048)
    if not len(buffer):
      break
    f.write(buffer)
    transbytes+=len(buffer)
    print("Bytes received", transbytes, "Total", (estsize, 100.*float(transbytes)/float(estsize)),str('%'))
datasock.close()
ftp_client.quit()  