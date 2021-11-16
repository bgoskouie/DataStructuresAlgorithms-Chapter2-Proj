# Finding Files
# For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

# Here is an example of a test directory listing, which can be downloaded here:

# ./testdir
# ./testdir/subdir1
# ./testdir/subdir1/a.c
# ./testdir/subdir1/a.h
# ./testdir/subdir2
# ./testdir/subdir2/.gitkeep
# ./testdir/subdir3
# ./testdir/subdir3/subsubdir1
# ./testdir/subdir3/subsubdir1/b.c
# ./testdir/subdir3/subsubdir1/b.h
# ./testdir/subdir4
# ./testdir/subdir4/.gitkeep
# ./testdir/subdir5
# ./testdir/subdir5/a.c
# ./testdir/subdir5/a.h
# ./testdir/t1.c
# ./testdir/t1.h
# Python's os module will be useful—in particular, you may want to use the following resources:

# os.path.isdir(path)

# os.path.isfile(path)

# os.listdir(directory)

# os.path.join(...)

# Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().

# Here is some code for the function to get you started:

## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os
# Let us print the files in the directory in which you are running this script
# print (os.listdir("."))
# Let us check if this file is indeed a file!
# print (os.path.isfile("./ex.py"))
# Does the file end with .py?
# print ("./ex.py".endswith(".py"))

#--------------TIME AND SPACE COMPLEXITY ANALYSES----------
# SPACE:  O(n)
# TIME:   O(n)
# Details:
# space: sizeof(list) + sizeof(path) * n,     sizeof(path) is a string of 100 chars (100 bytes)
# TIME: if n directories and each has n child


class FilesFinder(object):
    def __init__(self, suffix, path):
        self.out = self.find_files(suffix, path)

    def __str__(self):
        out = ""
        if len(self.out) > 0:
            out += "Paths are as follows:\n"
            for item in self.out:
                out += item + "\n"
        else:
            out += "No paths found to print!\n"
        return out

    def find_files(self, suffix, path):
        """
        Find all files beneath path with file name suffix.

        Note that a path may contain further subdirectories
        and those subdirectories may also contain further subdirectories.

        There are no limit to the depth of the subdirectories can be.

        Args:
          suffix(str): suffix if the file name to be found
          path(str): path of the file system

        Returns:
           a list of paths
        """
        def find_files_recur(found_files, suffix, itemfullpath):
            # discard the filename and extension (if any)
            # dirpath = os.path.split(path)[0]
            dirpath = itemfullpath
            if os.path.isfile(itemfullpath):
                dirpath = os.path.dirname(itemfullpath)
            if not os.path.isdir(dirpath):
                print(f"Directory \"{dirpath}\" is invalid!")
                return
            dircontent = os.listdir(dirpath)
            for item in dircontent:
                itemfullpath = os.path.join(dirpath, item)
                if os.path.isfile(itemfullpath):
                    split = item.split(".")
                    if len(split) > 1:  # name has extendion
                        if split[-1] == suffix:
                            found_files.append(itemfullpath.replace("\\", "/"))
                if os.path.isdir(itemfullpath):
                    find_files_recur(found_files, suffix, itemfullpath)

        found_files = list()
        find_files_recur(found_files, suffix, path)
        return found_files



if __name__ == "__main__":
    parent_dir = os.getcwd()
    valid_dir = os.path.join("2-finding-files-test-dir", "testdir")
    invalid_dir = "testdir_non_existant"
    empty_dir = ""
    valid_path = os.path.join(parent_dir, valid_dir)
    invalid_path = os.path.join(parent_dir, invalid_dir)
    empty_path = empty_dir
    print("--------------------Starting Test 1--------------------")
    ff1 = FilesFinder("h", valid_path)
    print(ff1)
    print("--------------------Starting Test 2--------------------")
    ff2 = FilesFinder("h", invalid_path)
    print(ff2)
    print("--------------------Starting Test 3--------------------")
    ff3 = FilesFinder("h", empty_path)
    print(ff3)
