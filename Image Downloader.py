print("Image Downloader")
print("")

#############################################
#USER INPUT SECTION

#enter a list of urls to download media from ["url1", "url2", etc...]"
urls = [""] 
	
#add/remove extensions to try and download
extensions = ['jpg', 'png', 'gif', 'webp', 'mp4']


exe_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver_path = r'E:\BROWSER AUTOMATION\geckodriver.exe'
#############################################


if urls == [] or urls == [""]:
  input("urls variable is empty, please open this script in a text editor and add a comma seperted list of urls")
  exit()
  
#############################
### Set Up for Firefox
#############################
print("Set Up for Firefox")
print("")

import os 
import time 
from datetime import datetime
import requests

#selenium
from selenium import webdriver 
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By #for selenium’s find_element
from selenium.webdriver.common.keys import Keys #send CTRL, DEL, etc... to an element

#https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html
from selenium.webdriver import ActionChains #	automate low level interactions such as mouse movements, mouse button actions, key press, and context menu interactions.

from selenium.webdriver.support.ui import WebDriverWait #help check webpage loaded
from selenium.webdriver.support import expected_conditions as EC

#copy/paste interaction
try:
  import pyperclip as pc
except Exception as e:
  print('Unable to import pyperclip, which may be needed for some actions like importing large blocks of text quickly (eg importing HTML code into CleanSender).')
  print(e)

#windows keystroke automation
try:
  import win32api
  import win32com.client
except Exception as e:
  print('Unable to import win32api, which may be needed for some actions like interacting with the file-upload popup (eg importing contact lists into iPost).')
  print(e)

#set up options and service
options = Options()
options.binary_location = exe_path

service = Service(driver_path)

#opens an instance of the browser
driver = webdriver.Firefox(service=service, options=options)
script_path = os.path.dirname(os.path.realpath(__file__))

###################################################

files_output = 0
url_index = 0

for url in urls:
  print("-----------------------------------------------------------------")
  print("URL " + str(url_index + 1) + ": " + str(url))
  driver.get(url)
  time.sleep(2)

  #scroll down to load all images
  try:
    scroll_height = .1
    while scroll_height < 9.9:
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scroll_height)
      scroll_height += .01
  except Exception as e:
    print(e)
    print("UNABLE TO SCROLL! - some images may not load")

  for extension in extensions:

    print("searching for " + str(extension) + "...")
    files = []
    try:
      files = driver.find_elements(By.XPATH, "//*[contains(@src, '" + str(extension) + "')]")
    except Exception as e:
      print(e)
      print("UNABLE TO FIND ELEMENTS! - skipped")

    print("found " + str(len(files)) + " " + str(extension))
    print("")
	
    for element in files:
  	
      print("File: " + str(files_output + 1))

      src_attribute = element.get_attribute("src")
      print(src_attribute)
    
      #extract image name
      substring_start_index = str(src_attribute).rfind('/')
      substring_end_index = str(src_attribute).rfind('.') #we dont' want the extension
      file_name = str(src_attribute)[substring_start_index:substring_end_index]
      file_name = file_name[1:] #remove /)
      #print(file_name)
     
      #timestamp
      timestamp_object = datetime.now()
      yr = timestamp_object.year
      mo = timestamp_object.month
      dy = timestamp_object.day
      hr = timestamp_object.hour
      minute = timestamp_object.minute
      sec = timestamp_object.second
      
      timestamp = str(timestamp_object.year)
      
      if mo < 10:
        timestamp = timestamp + "0"
      timestamp = timestamp + str(mo)
      
      if dy < 10:
        timestamp = timestamp + "0"
      timestamp = timestamp + str(dy)

      timestamp = timestamp + "_"
      if hr < 10:
        timestamp = timestamp + "0"
      timestamp = timestamp + str(hr)
      
      if minute < 10:
        timestamp = timestamp + "0"
      timestamp = timestamp + str(minute)

      if sec < 10:
        timestamp = timestamp + "0"
      timestamp = timestamp + str(sec)
            
      output_path = r'' + str(script_path) + '\\' + str(url_index + 1) + "_" + str(files_output + 1) + "_" + str(timestamp) + "_" + str(file_name) + "." + str(extension)
      
      file_request = None
      try:
        file_request = requests.get(src_attribute)
      except Exception as e:
        print(e)
        print("REQUEST ERROR")

      #time.sleep(5)
      
      try:
        with open(output_path, 'wb') as outfile:
          outfile.write(file_request.content)
        print(output_path)
        files_output = files_output + 1
        print("")
      except Exception as e:
        print(e)
        print("OUTFILE ERROR")

  print("")
  url_index = url_index + 1
print("")
print(str(files_output)  + " files output.")
