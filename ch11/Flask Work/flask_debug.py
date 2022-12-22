from flask import Flask

app = Flask(__name__)
class MyException(Exception):
  status_code = 400
  def __init__(self, message, status_code):
    Exception.__init_(self)

@app.route('/showException')
def main():
  raise MyException('MyException', status_code=500)

if __name__ == '__main__':
  app.run(debug=True) # insecure

  # If we run the 'showException' url, when debug mode is activated, we will
  # see a trace of the exception.