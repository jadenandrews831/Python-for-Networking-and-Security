import time, requests, json

from stem import Signal
from stem.control import Controller

def get_tor_session():
  session = requests.session()
  session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}
  return session

def main():
  while True:
    time.sleep(5)
    print('Rotating IP: ')
    with Controller.from_port(port=9051) as controller:
      controller.authenticate()
      controller.signal(Signal.NEWNYM)
    session = get_tor_session()
    print(json.loads(session.get('http://httpbin.org/ip').text))

if __name__ == "__main__":
  main()

