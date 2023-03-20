import os
from functools import reduce
from gametoolbox.utility.print_pretty import print_dict


def get_directory_structure(rootdir, file_extensions: [str] = None):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    output = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        print(files)
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        # print(subdir)
        parent = reduce(dict.get, folders[:-1], output)
        parent[folders[-1]] = subdir
    return output[rootdir]

def main():
    x = get_directory_structure("..")
    # print_dict(x, indent=4)


if __name__=="__main__":
    main()