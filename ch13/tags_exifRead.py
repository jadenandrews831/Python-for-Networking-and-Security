import exifread

file = open('images/IMG_1110.jpg', 'rb')
tags = exifread.process_file(file)
for tag, value in tags.items():
  print(f'Key: {tag}, value {value}')

