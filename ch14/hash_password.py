import hashlib
import getpass

password = getpass.getpass('Password: ')
hash_password = hashlib.sha512(password.encode())
print("The hash password is: ")
print(hash_password.hexdigest())

