#!/usr/bin/env python3

import nmap
import argparse

def callbackFTP(host, result):
  try:
    script = result['scan']['host']['tcp'][21]['script']
    print("Command line"+result['nmap']['command_line'])
    for key, value in script.items():
      print(f'Script {key} --> {value}')
  except KeyError:
    pass

class NmapScannerAsync:
  def __init__(self):
    self.portScanner = nmap.PortScanner()
    self.portScannerAsync = nmap.PortScannerAsync()

  def scanning(self):
    while self.portScannerAsync.still_scanning():
      print('Scanning >>>')
      self.portScannerAsync.wait(10)

  def nmapScanAsync(self, hostname, port):
    try:
      print("Checking port "+ port +" ..........")
      self.portScanner.scan(hostname, port)
      self.state = self.portScanner[hostname]['tcp'][int(port)]['state']
      print(" [+] "+hostname+" tcp/"+port+" "+self.state)
      # Checking FTP service
      if (port == '21') and self.portScanner[hostname]['tcp'][int(port)]['state'] == 'open':
        print("Checking ftp port with nmap scripts......")

        print('Checking ftp-anon.nse .....')
        self.portScannerAsync.scan(hostname, arguments='-A -sV -p21 --script ftp-anon.nse', callback=callbackFTP)
        self.scanning()

        print('Checking ftp-bounce.nse .....')
        self.portScannerAsync.scan(hostname, arguments="-A -sSV -p21 --script ftp-bounce.nse", callback=callbackFTP)
        self.scanning()

        print('Checking ftp-libopie.nse .....')
        self.portScannerAsync.scan(hostname, arguments="-A -sSV -p21 --script ftp-libopie.nse", callback=callbackFTP)
        self.scanning()

        print('Checking ftp-proftpd-backdoor.nse .....')
        self.portScannerAsync.scan(hostname, arguments="-A -sSV -p21 --script ftp-proftpd-backdoor.nse", callback=callbackFTP)
        self.scanning()

    except Exception as e:
      print(f"Error to connect with {hostname} for port scanning {e}")


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Nmap Scanner ASYNC")
  parser.add_argument('--host', dest='host', help='target host', required=True)
  parsed_args = parser.parse_args()

  host = parsed_args.host

  NmapScannerAsync().nmapScanAsync(host, '21')