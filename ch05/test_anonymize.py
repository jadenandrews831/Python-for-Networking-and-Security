import requests

from anonymize import enable_proxy, disable_proxy

url='http://icanhazip.com'
def test_requests():
  print(f"requests: {requests.get(url).text}")
test_requests()
enable_proxy()
test_requests()
disable_proxy()
test_requests()