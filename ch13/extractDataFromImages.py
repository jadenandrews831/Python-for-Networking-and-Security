import os

from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_metadata(path):
  exifData = {}
  image = Image.open(path)
  if hasattr(image, '_getexif'):
    exifinfo = image._getexif()
    if exifinfo:
      for tag, value in exifinfo.items():
        decoded = TAGS.get(tag, tag)
        exifData[decoded] = value
  decode_gps_info(exifData)
  return exifData  

def decode_gps_info(exif):
  gpsinfo = {}
  if 'GPSInfo' in exif:
    Nsec = exif['GPSInfo'][2][2]
    Nmin = exif['GPSInfo'][2][1]
    Ndeg = exif['GPSInfo'][2][0]
    Wsec = exif['GPSInfo'][4][2]
    Wmin = exif['GPSInfo'][4][1] 
    Wdeg = exif['GPSInfo'][4][0]
    Nmult = 1 if exif['GPSInfo'] == 'N' else -1
    Wmult = 1 if exif['GPSInfo'] == 'E' else -1
    latitude = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
    longitude = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
    exif['GPSInfo'] = {'Latitude': latitude, 'Longitude': longitude}

def printMetadata():
  for dirpath, dirnames, files in os.walk('images'):
    for name in files:
      print(f'[+] Metadata for file: {dirpath+os.path.sep+name}')
      try:
        exifData = {}
        exif = get_exif_metadata(dirpath+os.path.sep+name)
        for metadata in exif: 
          print(f'Metadata: {metadata} - Value: {exif[metadata]}')
      except:
        import sys, traceback
        traceback.print_exc(file=sys.stdout)
      finally:
        print()

if __name__ == '__main__':
  printMetadata()