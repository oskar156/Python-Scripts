#run this python file in the directory where you'd like to perform find-and-replace on the files

#from https://stackoverflow.com/questions/50037369/find-and-replace-string-from-multiple-files-in-a-folder-using-python

import glob
import ntpath
import os

output_dir = r'C:\Users\oscar\Desktop'
file_type = "*.html"
find_str = 'find'
replacement_str = 'replace'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for f in glob.glob(file_type):
    with open(f, 'r') as inputfile:
        with open('%s/%s' % (output_dir, ntpath.basename(f)), 'w') as outputfile:
            for line in inputfile:
                outputfile.write(line.replace(find_str, replacement_str))