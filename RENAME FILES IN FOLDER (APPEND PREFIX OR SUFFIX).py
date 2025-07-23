import os

prefix = 'GPPO'
suffix = ''

path = os.getcwd() #CURRENT DIRECTORY
script_file_path = __file__

i = 0
for file in os.listdir(path):
  if file != script_file_path:
    og_file_name = os.path.basename(file)
    new_file_name = str(prefix) + str(og_file_name) + str(suffix)
    os.rename(os.path.join(path, og_file_name), os.path.join(path, new_file_name))
    print(str(i + 1) + ": " + str(os.path.join(path, og_file_name)) + " renamed to " + str(os.path.join(path, new_file_name)))
    i = i + 1
  
