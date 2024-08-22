import os

search = '[Company]'
replace = '(Company)'

path = os.getcwd() #CURRENT DIRECTORY

i = 0
for file in os.listdir(path):
  og_file_name = os.path.basename(file)
  new_file_name = og_file_name.replace(search, replace)
  os.rename(os.path.join(path, og_file_name), os.path.join(path, new_file_name))
  print(str(i + 1) + ": " + str(os.path.join(path, og_file_name)) + " renamed to " + str(os.path.join(path, new_file_name)))
  i = i + 1
  