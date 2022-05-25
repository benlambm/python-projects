import os
 
# INPUT THE BASE DIRECTORY
base_directory = input("Enter full directory path: ")

# USE os.listdir() to create a list of all the files and directories in the base directory
directory_contents = os.listdir(base_directory)

# create an empty files list and an empty dirs list
files = []
dirs = []

for item in directory_contents:
    # Python if: use os.path.isfile() to see if item is a file. if so, append to the files list including its full path. NOTE: You'll need to use os.path.join() to join base_directory and item, and then give that to os.path.isfile() --> this will be necessary especially if base_directory is not equal to your current working directory. Also remember that in the full path, it's base_directory + "/" + item in UNIX systems, and base_directory + "\\" + item in Windows sytems.
    if os.path.isfile(os.path.join(base_directory, item)):
        files.append(os.path.join(base_directory, item))
    # Python elif: use os.path.isdir() to see if item is a directory if so, append to the dirs list including its full path. NOTE: You'll need to use os.path.join() to join base_directory and item, and then give that to os.path.isdir() --> this will be necessary especially if base_directory is not equal to your current working directory. Also remember that in the full path, it's base_directory + "/" + item in UNIX systems, and base_directory + "\\" + item in Windows sytems.
    elif os.path.isdir(os.path.join(base_directory, item)):
        dirs.append(os.path.join(base_directory, item))
        
# write your found files to a text file
outfile1 = open("files_found.txt", "w")
for line in files:
    outfile1.write(line + "\n")
outfile1.close()

# write your found directories to a text file
outfile2 = open("dirs_found.txt", "w")
for line in dirs:
    outfile2.write(line + "\n")
outfile2.close()

  