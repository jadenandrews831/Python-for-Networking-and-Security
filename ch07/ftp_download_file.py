#!/usr/bin/env python3

import ftplib

FTP_SERVER_URL = 'ftp.be.debian.org'
DOWNLOAD_DIR_PATH = '/www.kernel.org/pub/linux/kernel/v5.x'
DOWNLOAD_FILE_NAME = 'ChangeLog-5.0'

def ftp_file_download(server, username):
  ftp_client = ftplib.FTP(server, username)
  ftp_client.cwd(DOWNLOAD_DIR_PATH)
  ftp_client.dir()

  try:
    with open(DOWNLOAD_FILE_NAME, 'wb') as file_handler:
      ftp_cmd = f'RETR {DOWNLOAD_FILE_NAME}'
      ftp_client.retrbinary(ftp_cmd, file_handler.write)
      ftp_client.quit()
  except Exception as e:
    print(f'File could not be downloaded: {e}')

if __name__ == '__main__':
  ftp_file_download(server=FTP_SERVER_URL, username='anonymous')
