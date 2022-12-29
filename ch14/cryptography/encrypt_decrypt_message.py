from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)
print('Key', str(cipher_suite))
message = 'Secret message'.encode('utf8')
cipher_text = cipher_suite.encrypt(message)
plain_text = cipher_suite.decrypt(cipher_text)
print('Cipher Text:', cipher_text)
print('Plain Text:', plain_text)

