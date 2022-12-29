import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend
key = os.urandom(16)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()
print(encryptor)
message_encrypted = encryptor.update('a secret message'.encode())
print('Cipher Text:', str(message_encrypted))
cipher_text = message_encrypted + encryptor.finalize()
decryptor = cipher.decryptor()
print('Plain Text:', str(decryptor.update(cipher_text).decode()))