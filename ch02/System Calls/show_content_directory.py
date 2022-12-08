import os
pwd = os.getcwd()
print(pwd)
list_directory = os.listdir(pwd)  # lists the contents of the given directory
for directory in list_directory:
  print("[+] ",directory)
print('-'*20)
walk_directory = os.walk(pwd)
for content in walk_directory:
  for c in content:
    print("[+] ",c)
  print('+'*10)