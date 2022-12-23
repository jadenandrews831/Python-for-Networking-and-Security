import requests
import os

key = os.environ['IPSTACK_API']

class IPtoGeo(object):
  def __init__(self, ip):
    self.latitude = ''
    self.longitude = ''
    self.country = ''
    self.city = ''
    self.time_zone = ''
    self.ip = ip
    self.get_location()

  def get_location(self):
    req = f'http://api.ipstack.com/{self.ip}?access_key={key}'
    json_request = requests.get(req).json()
    if 'country_name' in json_request.keys():
      self.country = json_request['country_name']

    if 'country_code' in json_request.keys():
      self._country_code = json_request['country_code']

    if 'time_zone' in json_request.keys():
      self.time_zone = json_request['time_zone']

    if 'city' in json_request.keys():
      self.city = json_request['city']

    if 'latitude' in json_request.keys():
      self.latitude = json_request['latitude']

    if 'longitude' in json_request.keys():
      self.longitude = json_request['longitude']

if __name__ == '__main__':
  ip = IPtoGeo('8.8.8.8')
  print(ip.__dict__)