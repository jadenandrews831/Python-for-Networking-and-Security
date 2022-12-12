from stem.control import Controller

controller = Controller.from_port(port=9051)
controller.authenticate()
entries = controller.get_network_statuses()

for entry in entries:
  print("Nickname:", entry.nickname)
  print('Fingerprint', entry.fingerprint, end="\n\n")