def main():
  try:
    with open('test.txt', 'w') as f:
      f.write("this is a test file")
  except IOError as e:
    print("Exception caught: Unable to write to  file ", e)
  except Exception as e:
    print("Another error occurred ", e)
  else:
    print("File written successfully")
  
if __name__ == '__main__':
  main()

