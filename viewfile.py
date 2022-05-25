import os
import os.path


def displayFiles(path_name):
    if os.path.isfile(path_name):
        file_handle = open(path_name, 'r')
        return path_name + '\n' + file_handle.read()
    else:
        files = os.listdir(path_name)
        for file in files:
            return displayFiles(path_name + file)


def main():
    print(displayFiles("C:\\Users\\blamb\\PycharmProjects\\pythonProject\\"))


main()
