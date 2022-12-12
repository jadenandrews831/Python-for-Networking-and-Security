import requests

res = requests.get('http://www.google.com')
print(res.content)