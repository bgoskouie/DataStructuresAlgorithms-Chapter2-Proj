# Problem Statement:
Finding Files
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing, which can be downloaded here:

./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
Python's os module will be useful—in particular, you may want to use the following resources:

os.path.isdir(path)

os.path.isfile(path)

os.listdir(directory)

os.path.join(...)

Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().

# Solution explanation:
This is a recursion problem.
The entry point function is `find_files` which sets up the variables and does the initial setups and then it calls the `find_files_recur` function.
The `find_files_recur` function calls itself if the path it is called with is a directory. It gets called for all the subdirectories of the path it is called with.
If there are n deep directories and m items in each one the time analysis is of O(m * n) as we are running for loop on the all the directory elements and we keep doing it as deep as it can go (n times).


# Time and Space Analyses:
- Overall
    - SPACE:  sizeof(list) + sizeof(path) * n,     sizeof(path) is a string of 100 chars (100 bytes)
    - TIME:   O(n * m),      if n directories and each has m child
