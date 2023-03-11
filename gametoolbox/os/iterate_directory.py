from os import listdir
from os.path import isfile, join

directory = ".."
filenames = [f for f in listdir(directory)]
for f in filenames:
    if isfile(join(directory, f)):
        print(f)
    else:
        new_directory = join(directory, f)

        filenames1 = [print(new_directory, f, sep="\\") for f in listdir(new_directory)]