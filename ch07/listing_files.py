#!/usr/bin/env python3

from ftplib import FTP

ftp_client=FTP("ftp.be.debian.org")
print("Server:")
print(ftp_client.getwelcome())
print(ftp_client.login())
print("Files and directories in the root directory:")
ftp_client.dir()
ftp_client.cwd('/www.kernel.org/pub/linux/kernel/')
files = ftp_client.nlst()
files.sort()
print(f"{len(files)} files in /www.kernel.org/pub/linux/kernel directory:")
for file in files:
  print(file)
ftp_client.quit()
