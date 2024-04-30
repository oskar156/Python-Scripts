print("DELETE COLUMNS FROM CSV.py")
print("")

###################################################################
# USER INPUT SECTION, UPDATE AS NEEDED

delete_columns = ["PRIORITY"] 
#examples:
#["PRIORITY"]
#["UNIQUE_ID"]
#["COLUMN_A", "COLUMN_B"]



#USUALLY LEAVE THESE AS IS
quoted = True
qualifier = '"'
extension = "csv"
seperator = ","
seperator_description = "comma"

# USER INPUT SECTION END
###################################################################

input("This script will delete columns: " + str(delete_columns) + " from every .csv file in the same folder.\nPress Enter to continue...\nExit the script to Cancel...")



###################################################################
# SET UP
###################################################################
import collections
from collections import defaultdict
import pandas as pd
import os
import csv
import re

path = os.getcwd() #CURRENT DIRECTORY

###################################################################
# FIND .csv files in folder
###################################################################

i = 0
files_imported = 0
tables_imported_to_sql = 0

try:
	
 #for every file in the current directory...
 for file in os.listdir(path):

   #open file to import
   filename = os.fsdecode(file)
  
   #if the file does not start with split_file_prefix and it does end with the .extension...
   if filename.endswith("." + str(extension)):  
    
     print(str(filename))

     #get path and name w/o extension
     full_path = str(path) + "\\" + str(filename)
     filename_no_ext = os.path.splitext(os.path.basename(filename))[0]

     type = defaultdict(lambda: str)
     print("reading file...")
     df = pd.read_csv(str(full_path), dtype=type, keep_default_na=False, sep=seperator, quotechar=qualifier, encoding='latin-1')
     print("deleting column(s)...")
     df = df.drop(columns=delete_columns)
     print("exporting updated file...")
     if quoted == True:
       df.to_csv(str(full_path), sep=seperator, quotechar=qualifier, encoding='latin-1', index=False, header=True, mode='w', quoting = csv.QUOTE_ALL)
     else:
       df.to_csv(str(full_path), sep=seperator, quotechar=qualifier, encoding='latin-1', index=False, header=True, mode='w')
     print("")
     i = i + 1
except Exception as e:
  input(e)

input("Exit the Window")




