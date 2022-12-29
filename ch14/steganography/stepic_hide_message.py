from PIL import Image

import stepic

image = Image.open('python.png').convert('RGBA')
image2 = stepic.encode(image, 'This is the hidden message'.encode())
image2.save('python_secrets_1.png', 'PNG')
image2 = Image.open('python_secrets_1.png')
data = stepic.decode(image2)
print('Decoded data:', data)