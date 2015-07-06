import os
import shlex
import subprocess

__author__ = 'jason'

def execute(cmd):
    args = shlex.split(cmd)
    p = subprocess.Popen(args)
    return p

def remove_files(folder, files):
    for f in files:
        path = os.path.join(folder, f)
        print("remove file: %s" % path)
        os.remove(path)

def ask(x):
    [dir1, dir2] = list(x[0])
    files = x[1]
    # open corresponding folder
    execute('nautilus "%s"' % dir1)
    execute('nautilus "%s"' % dir2)
    print("files: " + str(files))
    print("there are %d files duplicated in folders:" % len(files))
    print("(A) " + dir1)
    print("(B) " + dir2)
    choice = input("in which folder do you want to delete these duplicated files?[skip]")
    if choice.lower() == 'a':
        print('remove files in %s' % dir1)
        remove_files(dir1, files)
    elif choice.lower() == 'b':
        print('remove files in %s' % dir2)
        remove_files(dir2, files)
    else:
        print("Program doesn't remove any files.")