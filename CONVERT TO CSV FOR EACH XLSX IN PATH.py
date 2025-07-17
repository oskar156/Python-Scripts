#PRINT EACH ITEM IN PATH


### USER INPUT START ###

#LEAVE THIS BLANK TO GET THE PATH WHERE THE SCRIPT IS LOCATED
main_path = r''

### USER INPUT END ###


import os
from pathlib import Path
import pandas as pd

if main_path == "":
  main_path = os.getcwd() #CURRENT DIRECTORY

i = 0

for item in os.listdir(main_path):
  
  item_full_path = os.path.join(main_path, item)
  root, extension = os.path.splitext(item_full_path)

  if extension == ".xlsx":
    read_file = pd.read_excel(item_full_path)
    read_file.to_csv(root + ".csv", index=None, header=True)
    print(str(item_full_path) + " exported to " + str(root) + ".csv")
    print("")

input("Script is finished, you can exit the window.")
