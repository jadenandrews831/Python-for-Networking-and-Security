import os
import yaml

user_input = input()

with open(user_input) as file:
  content = yaml.safe_load(file)    #s ecure


