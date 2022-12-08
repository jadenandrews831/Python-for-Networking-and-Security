try:
  f = open('newfile.txt', 'wt')
  for i in range(10):
    f.write("line #"+str(i+1)+'\n')
  f.close()
except IOError as error:
  print("I/O error occurred: ", str(error.errno))

