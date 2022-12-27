import sqlite3
import datetime
import argparse

def fixDate(timestamp):
  # Chrome stores timestamps in the number of microseconds since Jan 1 1601
  # To convert, we create a datetime object for Jan 1 1601...
  epoch_start = datetime.datetime(1601, 1, 1)

  # Then, we create an object for the number of microseconds in the timestamp
  delta = datetime.timedelta(microseconds=int(timestamp))

  # and return the sum of the two
  return epoch_start + delta

def getMetadataHistoryFile(locationHistoryFile):
  sql_connect = sqlite3.connect(locationHistoryFile)
  for row in sql_connect.execute('SELECT target_path, referrer, start_time, end_time, received_bytes FROM downloads;'):
    print("Downloads: ", row[0])
    print(f'\tFrom: {str(row[1])}')
    print(f'\tStarted: {fixDate(str(row[2]))}')
    print(f'\tFinished: {fixDate(str(row[3]))}')
    print(f'\tSize: {str(row[4])}')
    print()

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Chrome Downloads CLI')
  parser.add_argument('-l --location', dest='location', help='location of History database', required=True)
  parsed_args = parser.parse_args()

  getMetadataHistoryFile(parsed_args.location)