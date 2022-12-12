import requests, json

response = requests.get("http://httpbin.org/get", timeout=5)
print("HTTP Status Code: " + str(response.status_code))
print(response.headers)
if response.status_code == 200:
  results = response.json()
  for result in results.items():
    print(result)
  print("Headers response: ")
  for header, value in response.headers.items():
    print('\t', end="")
    print(f"{header} --> {value}")
  print("Headers request: ")
  for header, value in response.request.headers.items():
    print('\t', end="")
    print(f"{header} --> {value}")
  print("Server:"+response.headers['server'])
else:
  print(f'Error code {response.status_code}')