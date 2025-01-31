#ADD EACH file IN PATH TO THEIR OWN ZIP ARCHIVE


### USER INPUT START ###

#LEAVE THIS BLANK TO GET THE PATH WHERE THE SCRIPT IS LOCATED
path_with_all_the_files = r'' #no dash at the end

### USER INPUT END ###


import os
import shutil
from pathlib import Path

if path_with_all_the_files == "":
  path_with_all_the_files = os.getcwd() #CURRENT DIRECTORY

i = 0

for item in os.listdir(path_with_all_the_files):

  current_path = os.path.join(path_with_all_the_files, item)
  file_name_no_ext = Path(item).stem

  if not os.path.isdir(current_path):
        
    print(current_path + " ... ", end="", flush=True)
    shutil.make_archive(path_with_all_the_files + "\\" + file_name_no_ext, 'zip', path_with_all_the_files, item)
    print("archived as " + str(current_path) + ".zip")

    i = i + 1

print("")
print(str(i) + " .zip files created from folders in " + str(path_with_all_the_folders))
print("")
input("Script is finished, you can exit the window.")
