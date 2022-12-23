import requests
import os

key = os.environ['IPSTACK_API']

def geoip(domain):
  headers = {
    'Content-Type': 'application/json'
  }
  response = requests.get(f'http://api.ipstack.com/{domain}?access_key={key}', headers=headers)
  return response.text

print(geoip('python.org'))