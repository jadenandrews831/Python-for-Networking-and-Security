import os
import pickle
import yaml

user_input = input()
with open(user_input, 'rb') as file:
  contents = pickle.load(file)  # insecure 
with open(user_input) as exploit_file:
  contents = yaml.load(exploit_file)  #insecure


# From a security pov, the beast practice at this point is to never load data from an untrusted input source.
