from Crypto.Cipher import AES

# key has to be 16, 24, or 32 bytes long
key='secret-key-12345'.encode('utf8')

# Initial Vector
iv = 'This is an IV-12'.encode('utf8')
encrypt_AES = AES.new(key, AES.MODE_CBC, iv)

# Fill with spaces the user until 32 characters
message = ('This is the secret message'+(' '*6)).encode('utf8')
print(len(message))
ciphertext = encrypt_AES.encrypt(message)
print('Cipher text:', ciphertext)
decrypt_AES = AES.new(key, AES.MODE_CBC, iv)
message_decrypted = decrypt_AES.decrypt(ciphertext)
print("Decrypted Message:", message_decrypted.strip().decode('utf8'))