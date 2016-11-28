"""
Walks recursively through a given directory path and performs
the functions in func_list. Each function takes a path as an
argument and returns a string to write to file

"""
import os


def dir_printer(dir, subdirs, files):
    return dir


def num_files_printer(dir, subdirs, files):
    return str(len(files))


def dir_walker(path, func_list, output):
    with open(output, 'w') as f:
        for directory, dirnames, filenames in os.walk(path):
            for func in func_list:
                if type(func) == str:
                    f.write(func)
                else:
                    f.write(func(directory, dirnames, filenames))


if __name__ == '__main__':

    def main():
        func_list = [
            dir_printer,
            '\t',
            num_files_printer,
            '\n',
        ]
        path = '/home/sam/test/'
        output = '/home/sam/dir_walker_output.txt'
        dir_walker(path, func_list, output)

    main()
