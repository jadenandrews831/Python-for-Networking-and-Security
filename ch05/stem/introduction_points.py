from stem.control import Controller

with Controller.from_port(port=9051) as controller:
  controller.authenticate()
  desc = controller.get_hidden_service_descriptor('ciadotgov4sjwlzihbbgxnqg3xiyrg7so2r2o3lt5wz5ypk4sxyjstad') # <-- CIA onion site:
  for point in desc.introduction_points():
    print(f"\t{point.address}:{point.port} => {point.identifier}")  # <-- does not work with v3 onion sites so far...
