#PRINT EACH ITEM IN PATH


### USER INPUT START ###

#LEAVE THIS BLANK TO GET THE PATH WHERE THE SCRIPT IS LOCATED
main_path = r''

#if 1, then it shows the full path of the item C:/folders/folders/item.ext
#if 2, then it shows the item.ext
#if 3, then it shows the item
print_style = 3

### USER INPUT END ###


import os
from pathlib import Path

if main_path == "":
  main_path = os.getcwd() #CURRENT DIRECTORY

i = 0

for item in os.listdir(main_path):

  item_full_path = os.path.join(main_path, item)
  path = ""

  if print_style == 1:
    path = item_full_path
  elif print_style == 2:
    path = os.path.basename(item_full_path)
  elif print_style == 3:
    path = Path(os.path.basename(item_full_path)).stem
  
  print(path)
  i = i + 1

print("")
print(str(i) + " items in " + str(main_path))
print("")
input("Script is finished, you can exit the window.")
