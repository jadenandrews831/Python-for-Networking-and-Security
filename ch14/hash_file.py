import hashlib

file_name = input('Enter file name: ')
file = open(file_name,'r')
data = file.read().encode()
print(f'-- {file_name} --')
print(hashlib.algorithms_available)
for algorithm in hashlib.algorithms_available:
  hash = hashlib.new(algorithm)
  hash.update(data)
  try:
    hex = hash.hexdigest()
  except:
    hex = hash.hexdigest(128)

  print(f'{algorithm}: {hex}')