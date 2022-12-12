from stem import Signal

from stem.control import Controller

with Controller.from_port(port=9051) as controller:
  controller.authenticate()
  print('Success!!')
  controller.signal(Signal.NEWNYM)    # Signals for a new identity
  print('New Tor connection processed')