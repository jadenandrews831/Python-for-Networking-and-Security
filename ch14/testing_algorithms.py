import hashlib

for algorithm in hashlib.algorithms_guaranteed:
  print(algorithm)
  h = hashlib.new(algorithm)
  h.update('password'.encode())
  try:
    print(h.hexdigest())
  except:
    print(h.hexdigest(128))
  print()

