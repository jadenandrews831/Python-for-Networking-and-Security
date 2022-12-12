import time, socks, socket
import requests
from stem import Signal
from stem.control import Controller
numIPs = 5
with Controller.from_port(port=9051) as controller:
  controller.authenticate()
  socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
  socket.socket = socks.socksocket
  for i in range(0, numIPs):
    response = requests.get('http://icanhazip.com').text
    print(f"New IP Address: {response}")
    controller.signal(Signal.NEWNYM)
    if controller.is_newnym_available() == False:
      print(f"Waiting time for Tor to change IP: {controller.get_newnym_wait()}")
      time.sleep(controller.get_newnym_wait())
    