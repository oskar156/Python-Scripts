print("PNG IMAGE SIZE REDUCER.py")
print("")

from PIL import Image
import os

path = os.getcwd() #CURRENT DIRECTORY

print("Checking " + str(path) + "...")
print("")

i = 0
images_reduced = 0

#for every file in the current directory...
for file in os.listdir(path):

  #open file to import
  filename = os.fsdecode(file)

  if str(filename[-4:]).lower() == '.png':

    full_path = str(path) + "\\" + str(filename)

    old_size = os.stat(full_path).st_size

    img = Image.open(full_path)
    img = img.convert("RGB")
    input(full_path[:-4] + ".jpg")
    img.save(full_path[:-4] + ".jpg", optimize=True, quality=85)

    new_size = os.stat(full_path[:-4] + ".jpg").st_size

    print("image " + str(images_reduced + 1) + ": " + str(filename) + " size reduced from " + str(round(old_size/1024)) + " KB to " + str(round(new_size/1024)) + " KB")

    images_reduced = images_reduced + 1
  i = i + 1

print("")
print(str(images_reduced) + " images reduced")
print("")
input("Exit the Window")