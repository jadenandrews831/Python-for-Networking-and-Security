from PIL import Image
from PIL.ExifTags import TAGS

for i, j in Image.open('images/IMG_1110.JPG')._getexif().items():
  print(f'{TAGS.get(i)} = {j}')