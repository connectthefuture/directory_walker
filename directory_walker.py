"""
Walks recursively through a given directory path and performs
the functions in func_list. Each function takes a path as an
argument and returns a string to write to file

"""
import os


def dir_printer(dir, subdirs, files):
    return dir


def dir_walker(path, func_list):
    for directory, dirnames, filenames in os.walk(path):
        for func in func_list:
            print(func(directory, dirnames, filenames))


if __name__ == '__main__':

    def main():
        func_list = [
            dir_printer
        ]
        path = '/home/sam/test/'
        dir_walker(path, func_list)

    main()
