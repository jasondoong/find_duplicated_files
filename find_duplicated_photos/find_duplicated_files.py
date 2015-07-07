import filecmp

__author__ = 'jason'

import itertools
import os

__author__ = 'jason'

def list_all_files(folder_path):
    print('reading all files in %s' % folder_path)
    # stort in tuple (file_name, folder_path)
    all_files = [(file_name, root) for root, dirs, files in os.walk(folder_path) for file_name in files]
    return all_files



def group_by_file_name(all_files):
    print('grouping by file name')
    file_name_group = []
    for k, g in itertools.groupby(all_files, key=lambda x: x[0]):
        tmp = list(g).copy()
        file_name = tmp[0][0]

        folders = []
        for x in tmp:
            folders.append(x[1])

        file_name_group.append((file_name, folders))
    return file_name_group

def find_files_with_the_same_name(all_files):

    # sorted by file name
    print('sorting all files')
    all_files = sorted(all_files, key=lambda x: x[0])

    # group by file_name.  [file name: folder1, folder1, ...]
    file_name_group = group_by_file_name(all_files)

    # remove files which only appear in one place
    print('remove files which only appear in one place')
    file_name_group = [f for f in file_name_group if len(f[1]) > 1]

    return file_name_group

def find_duplicated_file_pairs(file_group):
    print('Comparing files which have the same name in different folders.')
    duplicated_file_pairs = []
    for x in file_group:
        file_name = x[0]
        for x in itertools.combinations(x[1], 2):
            file1 = os.path.join(x[0], file_name)
            file2 = os.path.join(x[1], file_name)
            if filecmp.cmp(file1, file2):
                duplicated_file_pairs.append((file1, file2))
    return duplicated_file_pairs

#find all duplicated files in given folder. output: [path1, path2)]
def find(folder):

    # list all files.  [(file_name, folder path)]
    all_files = list_all_files(folder)

    # find files with the same name. output: [(file name, [folder1, folder2, ...])]
    file_name_group = find_files_with_the_same_name(all_files)

    # find duplicated files. output: [path1, path2)]
    out = find_duplicated_file_pairs(file_name_group)
    return out