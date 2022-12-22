from flask import Flask, redirect, Response

app = Flask(__name__)
valid_locations = ['www.packtpub.com', 'valid_url']
@app.route('/redirect/<url>')
def reidrect_url(url):
  sanitizedLocation = getSanitizedLocation(url)
  print(sanitizedLocation)
  return redirect('http://"+sanitizedLocation, code=302')

def getSanitizedlocation(location):
  if (location is valid_locations):
    return location
  else:
    return 'check url'

if __name__ == '__main__':
  app.run(debug=True)

  
 