import os
for root, directories, files in os.walk(".", topdown=False):
  for file_entry in files:
    print('[+] ', os.path.join(root, file_entry))
  for name in directories:
    print('[++] ', name)

  print(root, directories, files, sep="\n")