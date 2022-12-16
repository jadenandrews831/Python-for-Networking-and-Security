import optparse
import nmap
import csv

class NmapScannerCSV:
  def __init__(self):
    self.portScanner = nmap.PortScanner()
  def nmapScanCSV(self, host, ports):
    try:
      print("Checking ports ", str(ports) + '.'*10)
      self.portScanner.scan(host, arguments='-n -p'+ports)
      print(f"[*] Executing command: {self.portScanner.command_line()}")
      print(self.portScanner.csv())
      print("Summary for host", host)
      with open('csv_file.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(['Host', 'Protocol', 'Port', 'State'])
        for x in self.portScanner.csv().split('\n')[1:-1]:
          splited_line = x.split(';')
          host = splited_line[0]
          protocol = splited_line[5]
          port = splited_line[4]
          state = splited_line[6]
          print("Protocol:",protocol,"Port:",csv_writer.writerow([host, protocol, port, state]))
    except Exception as e:
      print(f"Error to connect with {host} for port scanning {e}")

def main():
  parser = optparse.OptionParser('usage%prog'+'--host <target host> --ports <target port>')
  parser.add_option('--host', dest='host', type='string', help='Please, specify the target host.')
  parser.add_option('--ports', dest='ports', type='string', help='Please, specify the target port(s) separated by comma.')
  options, args = parser.parse_args()
  if (options.host == None) or (options.ports == None):
    print('[-] You must specify a target host and a target port(s)')
    exit(0)
  host = options.host
  ports = options.ports
  NmapScannerCSV().nmapScanCSV(host,ports)

if __name__ == '__main__':
  main()