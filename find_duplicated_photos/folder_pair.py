import os
import itertools

__author__ = 'jason'


def group_by_folder_pair(pairs):
    # transfer to [(folder1, folder2): file_name] format
    tmp = []
    for x in pairs:
        dir1 = os.path.dirname(x[0])
        dir2 = os.path.dirname(x[1])
        file_name = os.path.basename(x[0])
        tmp.append((set([dir1, dir2]), file_name))

    # group by (folder1, folder2):  [(folder1, folder2): file1, file2, file3, ...]
    print("grouping by folder path")
    group = []
    for k, g in itertools.groupby(tmp, key=lambda x: x[0]):
        tmp = list(g).copy()
        path_set = tmp[0][0]

        files = [x[1] for x in tmp]

        group.append((path_set, files))

    return group

# find two folder with most duplicated files. input: [(path1, path2)]  output: (folder1, folder2), [file1, file2, file3, ...]
def most_duplicated(file_pairs):

    # group by (folder1, folder2):  [(folder1, folder2), [file1, file2, file3, ...]]
    group = group_by_folder_pair(file_pairs)  # sort by number of files, descending

    # sorting by number of files, descending
    print("Sorting by number of files, descending")
    sorted_group = sorted(group, key=lambda x: len(x[1]), reverse=True)

    return sorted_group[0]