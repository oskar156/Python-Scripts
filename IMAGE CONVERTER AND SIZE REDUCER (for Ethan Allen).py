print("PNG IMAGE SIZE REDUCER.py")
print("")

#######################################
# USER INPUT SECTION

input_image_type = "png"
#VALID OPTIONS: jpg, jpeg, png, webp

output_image_type = "png"
#VALID OPTIONS: jpg, jpeg, png, webp

output_image_quality = 70
#VALID OPTIONS: 75 for default, 0 for worst, 95 for best, or any int in 0-95 range, "keep" only valid for jpg/jpeg
#doesn't work w/png

resize_width = -1
resize_height = -1
#VALID OPTIONS: -1 for default (no change), any positive whole number
#exactly set output image size (dimensions)
#both resize_width and resize_height need to be >=1 or else it will be ignored

resize_width_relative = -1
resize_height_relative = -1
#VALID OPTIONS: 0 for default (no change), any positive number >= 1
#set output image size relative to input image size (dimensions)
#only one of resize_width_relative or resize_height_relative need to be >=1
#if one is still 0 it will be ignored, the other won't be ignored
#if both resize_width and resize_heightare >=1 then these will be ignored

resize_width_relative_method = "add"
resize_height_relative_method = "add"
#VALID OPTIONS: add, sub, mult, div

# USER INPUT SECTION END
#######################################

#https://pillow.readthedocs.io/en/stable/reference/Image.html

from PIL import Image
import os
import math

path = os.getcwd() #CURRENT DIRECTORY

print("Checking " + str(path) + "...")
print("")

i = 0
images_reduced = 0
try:
 #for every file in the current directory...
 for file in os.listdir(path):
    if file.endswith("." + input_image_type):
    	
      filename = os.fsdecode(file).lower()
      filename_no_ext = filename[:-len(input_image_type)-1]
      filename_ext = filename[-len(input_image_type):]
  
      if str(filename_ext == input_image_type):
  
        full_path_no_ext = str(path) + "\\" + str(filename_no_ext)
        full_path_ext = str(path) + "\\" + str(filename_no_ext) + "." + str(filename_ext)
        output_image_path = str(path) + "\\" + str(filename_no_ext) + "." + str(output_image_type)
        old_size = os.stat(full_path_ext).st_size
        
        print("Opening " + str(full_path_ext) + "...")
        img = Image.open(full_path_ext)
        print("Opened " + str(full_path_ext))
        
        if(output_image_path == "jpg" or output_image_path == "jpeg"):
          img = img.convert("RGB")
        elif(output_image_path == "png"):
          img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
          
        #RESIZE
        if resize_width >= 1 and resize_height >= 1:
          print("Resizing...")
          img = img.resize((math.ceil(resize_width), math.ceil(resize_height)))
          print("Resized...")
        elif resize_width_relative >= 1 or resize_height_relative >= 1:
          print("Resizing...")
          new_width = img.width
          new_height = img.height
      	
          if resize_width_relative >= 1:
            if resize_width_relative_method == "add":
              new_width = new_width + resize_width_relative
            elif resize_width_relative_method == "sub":
              new_width = new_width - resize_width_relative
            elif resize_width_relative_method == "mult":
              new_width = new_width * resize_width_relative
            elif resize_width_relative_method == "div":
              new_width = new_width / resize_width_relative
          if resize_height_relative >= 1:
            if resize_width_relative_method == "add":
              new_height = new_height + resize_width_relative
            elif resize_width_relative_method == "sub":
              new_height = new_height - resize_width_relative
            elif resize_width_relative_method == "mult":
              new_height = new_height * resize_width_relative
            elif resize_width_relative_method == "div":
              new_height = new_height / resize_width_relative
          img = img.resize((math.ceil(new_width), math.ceil(new_height)))
          print("Resized")
          
        print("Saving...")
        img.save(output_image_path, optimize=True, quality=output_image_quality)
        print("Saved")
        
        new_size = os.stat(output_image_path).st_size
        if round(new_size/1024) >= 250:
          output_image_type = 'jpg'
          old_output_image_path = output_image_path
          output_image_path = str(path) + "\\" + str(filename_no_ext) + "." + str(output_image_type)
          img.save(output_image_path, optimize=True, quality=output_image_quality)
          new_size = os.stat(output_image_path).st_size
          output_image_type = 'png'
          if os.path.isfile(old_output_image_path):
            os.remove(old_output_image_path)
          print(output_image_path)
          

        print("image " + str(images_reduced + 1) + ": " + str(filename) + " size reduced from " + str(round(old_size/1024)) + " KB to " + str(round(new_size/1024)) + " KB")
        print("")
        images_reduced = images_reduced + 1
      i = i + 1
except Exception as e:
 input(e)
print("")
print(str(images_reduced) + " images reduced")
print("")
input("Exit the Window")
