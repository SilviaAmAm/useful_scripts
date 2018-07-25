"""This script can be used to rename files in a folder that are numbered such as 1.xyz, 20.xyz and should be renamed to 01.xyz, 20.xyz..."""

import os
import glob


files = glob.glob('/Volumes/Transcend/data_sets/dftb/*.xyz')
# files = glob.glob('/Users/walfits/Desktop/test_dir/*.xyz')
padding = "0"

for file in files:
    file_name = file.split("/")[-1]
    file_idx = file_name.split(".")[0]
    n = 5 - len(file_idx)
    new_idx = n * padding + file_idx

    os.rename(file, '/Volumes/Transcend/data_sets/dftb/{}.xyz'.format(new_idx))
    # os.rename(file, '/Users/walfits/Desktop/test_dir/{}.xyz'.format(new_idx))
