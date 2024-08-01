print("EXPORT SQL SERVER to QUOTED CSV.py")
print("")

###################################################################
# USER INPUT SECTION, UPDATE AS NEEDED

server = "SQL04" #example: SQL04
database = "TEMP_OK" #example: TEMP_OK

#There are 2 ways to search for tables to export...
# IF OPTION 1 IS FILLED OUT, OPTION 1 WILL BE USED
# IF OPTION 1 IS KEPT = [], OPTION 2 WILL BE USED

#--------------------------------------------------------
# OPTION 1 - SEARCH BY LIST:
#format as a list of strings ["table1", "table2", "etc..."]
list_of_table_names = ["GPPO247328_2-FACEBOOK FILE"]
#	"TABLENAME_INTERNAL_RAW"  #-OG RAW FILE
#	"TABLENAME-RAW-FILE"      #-RAW-FILE
#	"TABLENAME-FACEBOOK FILE" #-FINAL FILE
#]
#--------------------------------------------------------

#--------------------------------------------------------
# OPTION 2 - SEARCH BY REGEX:
#REGEX TEMPLATE TO GET ALL OF AN ORDER'S TABLES IF THEY'RE USING dash - or underscore _
#just copy it between the quotes after table_name_re = and replace order numbers as needed
#GPPO243510[-_](1$|1[-_])
table_name_re = ""
#--------------------------------------------------------





#USUALLY LEAVE THESE AS IS
order_by = ['PRIORITY']
order_by_asc = [True]
quoted = True

qualifier = '"'
extension = "csv"
seperator = ","
seperator_description = "comma"

# USER INPUT SECTION END
###################################################################





###################################################################
# SET UP
###################################################################
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import inspect
import collections
from collections import defaultdict
import pandas as pd
import os
import csv
import re


###################################################################
# EXPORT
###################################################################
path = os.getcwd() #CURRENT DIRECTORY

i = 0
tables_exported_from_sql = 0

try:
 #for every table we found in the last step / for every table the user entered...
 for table_name in list_of_table_names:

  print("table " + str(i + 1) + ": " + str(table_name))

  try:
     if len(order_by) > 0:
      print("reading export csv to sort...")
      type = defaultdict(lambda: str)
      df = pd.read_csv(str(path) + "\\" + str(table_name) + "." + str(extension), dtype=type, keep_default_na=False, sep=seperator, quotechar=qualifier, encoding='latin-1')
      
      print("sorting...")
      df = df.sort_values(by=order_by, ascending=order_by_asc)
      print("writing sorted values...")
      if quoted == True:
        df.to_csv(str(path) + "\\" + str(table_name) + "." + str(extension), sep=seperator, quotechar=qualifier, encoding='utf-8', index=False, header=True, mode='w', quoting = csv.QUOTE_ALL)
      else:
        df.to_csv(str(path) + "\\" + str(table_name) + "." + str(extension), sep=seperator, quotechar=qualifier, encoding='utf-8', index=False, header=True, mode='w')
      print("done sorting.")
     print("")
  except Exception as e:
     print("ERROR")
     input(e)
  i = i + 1
  tables_exported_from_sql = tables_exported_from_sql + 1

except Exception as e:
 print(row)
 input(e)
###################################################################
# FINAL MESSAGE
###################################################################
try:
  print(str(tables_exported_from_sql) + " " + str(seperator_description) + "-delimited " + str(extension) + " files exported to " + str(path))
  print("")
except Exception as e:
  input(e)
input("Exit the Window")
