import requests

logins = []
with open('Logins.txt', 'r') as file:
  for line in file:
    login = line[:-1]
    logins.append(login)
domain = "http://testphp.vulnweb.com"
for login in logins:
  print(f"Checking ... {domain}{login}")
  response = requests.get(domain+login)
  if response.status_code == 200:
    print(f"Login resource detected: {login}")