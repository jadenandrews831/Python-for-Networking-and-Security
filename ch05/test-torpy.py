from torpy.http.requests import TorRequests

with TorRequests() as tor_requests:
  print("building circuit...")
  with tor_requests.get_session() as session:
    print(session.get("http://httpbin.org/ip").json())
  print('renewing circuit...')
  with tor_requests.get_session() as session:
    print(session.get("http://httpbin.org/ip").json())
  
  response = session.get('http://check.torproject.org') # Ahmia -> Search Engine for Hidden Services
  print('\n', '#'*20, sep="")
  for key,value in response.headers.items():
    print(key,':',value)
