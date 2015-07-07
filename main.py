import sys

import ask_user
import find_duplicated_files
import folder_pair

__author__ = 'jason'


if(len(sys.argv)==2):
    folder = sys.argv[1]
else:
    sys.exit("Usage: python3 main.py [folder path]")

#find all duplicated files in given folder. output: [path1, path2)]
pairs = find_duplicated_files.find(folder)

#exit if no duplicated files
if len(pairs)==0:
    print("No duplicated files!")
    sys.exit(0)

# find two folder with most duplicated files. output: (folder1, folder2), [file1, file2, file3, ...]
x = folder_pair.most_duplicated(pairs)

# ask user which to delete?
ask_user.ask(x)

