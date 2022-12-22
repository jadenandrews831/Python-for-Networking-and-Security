import sys

from python_registry.Registry import Registry

reg = Registry.Registry(sys.argv[1])
print("Analyzing SOFTWARE in Windows registry...")
try:
  key = reg.open('Microsoft\\Windows\\CurrentVersion\\Run')
  print(f"Las modifiedL {key.timestamp()} [UTC]")
  for value in key.values():
    print(f'Name: {value.name()}, Value path: {value.value()}')
except Registry.RegistryKeyNotFoundException as e:
  print("Exception", e)


