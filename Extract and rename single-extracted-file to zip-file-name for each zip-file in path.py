#run this python file in the directory where you'd like to extract the zip-files and rename the file within to the name of the zip-file
#only use this with zip-files that have a single file within

import glob
import os
import zipfile

folder_path = os.getcwd()

#iteratre over files in a folder
for file in os.listdir(folder_path):

  #if it's a zip file...
  if file.endswith(".zip"):

    #extract file
    file_name = str(file)
    path = os.path.join(str(folder_path), str(file))

    z = zipfile.ZipFile(os.path.join(str(folder_path), str(file_name)))
    z.extractall(folder_path)

    #rename file
    files_in_path = os.listdir(folder_path)
    latest_file = max(files_in_path, key=os.path.getctime)
    
    latest_file_split = os.path.splitext(latest_file)
    file_split = os.path.splitext(file)
    new_name = os.path.join(folder_path, (file_split[0] + latest_file_split[1]))

    os.rename(latest_file, new_name)

    print("Extracted " + str(file_name) + " and renamed to " + str(new_name))

print("Exit the Window")