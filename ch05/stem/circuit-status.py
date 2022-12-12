from stem.control import Controller

controller = Controller.from_port(port=9051)
controller.authenticate()
entries = controller.get_network_statuses()
print(controller.get_info('circuit-status'))
