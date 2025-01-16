#ADD EACH FOLDER IN PATH TO THEIR OWN ZIP ARCHIVE


### USER INPUT START ###

#LEAVE THIS BLANK TO GET THE PATH WHERE THE SCRIPT IS LOCATED
path_with_all_the_folders = r''

### USER INPUT END ###


import os
import shutil

if path_with_all_the_folders == "":
  path_with_all_the_folders = os.getcwd() #CURRENT DIRECTORY

i = 0

for item in os.listdir(path_with_all_the_folders):

    current_path = os.path.join(path_with_all_the_folders, item)
    if os.path.isdir(current_path):
        
        print(current_path + " ... ", end="", flush=True)
        shutil.make_archive(current_path, 'zip', current_path)
        print("archived as " + str(current_path) + ".zip")

i = i + 1

print(str(i) + " .zip files created from folders in " + str(path_with_all_the_folders))
input("Script is finished, you can exit the window.")
