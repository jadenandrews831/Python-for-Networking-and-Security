from torrequest import TorRequest

with TorRequest(proxy_port=9050, ctrl_port=9051, password=None) as t:
  response = t.get('http://ipecho.net/plain')
  print(response.text)
  print(type(t.ctrl))
  t.ctrl.signal("CLEARDNSCACHE")
  t.reset_identity()
  response= t.get('http://httpbin.org/ip')
  print(response.text)