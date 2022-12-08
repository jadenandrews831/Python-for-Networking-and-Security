#!/usr/bin/env python3

import subprocess
import sys
import argparse

parser = argparse.ArgumentParser(description="Ping Scan Network")
parser.add_argument("-network", dest="network", help="NetWork segment[For example 192.168.56]", required=True)
parser.add_argument("-machines", dest="machines", help="Machines number", type=int, required=True)
parsed_args = parser.parse_args()
for ip in range(1, parsed_args.machines+1):
  ipAddress = parsed_args.network +'.'+str(ip)
  print("Scanning %s " %(ipAddress) )
  if sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
    output = subprocess.Popen(["ping", '-c 1', ipAddress], stdout=subprocess.PIPE).communicate()[0]
  elif sys.platform.startswith('win'):
    output = subprocess.Popen(['ping', ipAddress], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
  output = output.decode('utf-8')
  print("Output", output)
  if "Lost = 0" in output or "bytes from " in output:
    print("the Ip Address %s has responded with a ECHO_REPLY!" % ipAddress)