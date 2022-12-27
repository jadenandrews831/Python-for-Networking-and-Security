import sqlite3
import os

def getDownloads(downloadDB):
  try:
    connection = sqlite3.connect(downloadDB)
    cursor = connection.cursor()
    cursor.execute('SELECT name, source, datetime(endTime/1000000,\'unixepoch\') FROM moz_downloads;')
    print('\n[*] --- Files Downloaded --- ')
    for row in cursor:
      print(f'[+] File: {str(row[0])} from source: {str(row[1])} at: {str(row[2])}')
  except Exception as e:
    print(f'\n[*] Error reading moz_downlaods database, {e}')

def getCookies(cookiesDB):
  try:
    connection = sqlite3.connect(cookiesDB)
    cursor = connection.cursor()
    cursor.execute('SELECT host, name, value FROM moz_cookies')
    print('\n[*] -- Found Cookies --')
    for row in cursor: 
      print(f'[+] Host: {str(row[0])}, Cookies: {str(row[1])}, Value: {str(row[2])}')

  except Exception as e:
    print(f'\n[*] Error reading moz_cookies database, {e}')

def getHistory(placesDB):
  try:
    connection = sqlite3.connect(placesDB)
    cursor = connection.cursor()
    cursor.execute('SELECT url, datetime(visit_date/1000000, \'unixepoch\') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id;')
    print('\n[*] -- Found History --')
    for row in cursor:
      print(f'[+] {str(row[1])} - Visited: {str(row[0])}')

  except Exception as e:
    print(f'\n[*] Error reading moz_places, moz_historyvisits databases, {e}')

if __name__ == '__main__':
  db = 'downloads.sqlite', 'cookies.sqlite', 'places.sqlite'
  funcs = getDownloads, getCookies, getHistory
  for f, d in zip(funcs, db):
    f(d)