from cryptography.fernet import Fernet

def generate_key():
  key = Fernet.generate_key()
  with open('secret.key', 'wb') as f:
    f.write(key)

def  load_key():
  return open('secret.key', 'rb').read()

def encrypt_message(message):
  key = load_key()
  encoded_message = message.encode()
  fernet = Fernet(key)
  return fernet.encrypt(encoded_message)

def decrypt_message(message):
  key = load_key()
  fernet = Fernet(key)
  decoded_message = fernet.decrypt(message).decode()
  return decoded_message

if __name__ == '__main__':
  generate_key()
  message_encrypted = encrypt_message('Encrypt this message')
  message_decrypted = decrypt_message(message_encrypted)
  print('Message Encrypted:', message_encrypted)
  print('Message Decrypted:', message_decrypted)