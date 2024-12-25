"""
Created on Mar 5, 2020
@author: Tammy DiPrima
Creates new directories with the names given as command line arguments in the current working directory.
https://stackoverflow.com/questions/992737/safe-rm-rf-function-in-shell-script
https://stackoverflow.com/questions/373156/what-is-the-safest-way-to-empty-a-directory-in-nix
"""

import os
import sys


# function to create directories
def create_dirs(dirs):
    cwd = os.getcwd()  # get current working directory

    # create respective directories in current working directory based on command line argument(s) provided
    for dirName in dirs:
        dir_full_path = os.path.join(cwd, dirName)
        os.makedirs(dir_full_path)


# main
def main():
    create_dirs(sys.argv[1:])


if __name__ == '__main__':
    main()
