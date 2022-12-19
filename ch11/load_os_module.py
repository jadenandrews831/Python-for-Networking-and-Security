# This program tries to highlight a vulnerability in the eval() method, which 
# executes a string of text as Python code.

import os
try:
  eval('__import__("os").system("clear")', {})
  print ("Module OS lodaded by eval")
except Exception as e:
  print(repr(e))

# This problem can be solved by defining the 'global' and 'local' parameters in the eval() call