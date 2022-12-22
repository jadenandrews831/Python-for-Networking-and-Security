from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
def index():
  parameter = request.args.get('parameter', '')
  return render_template("template.html", data=parameter)

index()