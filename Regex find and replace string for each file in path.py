#run this python file in the directory where you'd like to perform find-and-replace on the files

#from https://stackoverflow.com/questions/50037369/find-and-replace-string-from-multiple-files-in-a-folder-using-python
#from https://stackoverflow.com/questions/11475885/python-replace-regex

import glob
import ntpath
import os
import re

output_dir = r'C:\Users\oscar\Desktop'
file_type = "*.html"
find_regex_exp = 'find'
replacement_str = 'replace'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for f in glob.glob(file_type):
    with open(f, 'r') as inputfile:
        with open('%s/%s' % (output_dir, ntpath.basename(f)), 'w') as outputfile:
            for line in inputfile:
                outputfile.write(re.sub(find_regex_exp, replacement_str, line))

print("Exit the Window")