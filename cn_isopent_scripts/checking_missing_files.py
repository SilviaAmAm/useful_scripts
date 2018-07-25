"This script checks why there were more energies than xyz files in /Volumes/Transcend/data_sets/CN_isobutane_model/geoms_2/training."

import glob
import os
import numpy as np

def list_files(dir, key):
    """
    This function walks through a directory and makes a list of the files that have a name containing a particular string
    :dir: path to the directory to explore
    :key: string to look for in file names
    :return: list of files containing "key" in their filename
    """

    r = []  # List of files to be joined together
    subdirs = [x[0] for x in os.walk(dir)]
    for subdir in subdirs:
        files = next(os.walk(subdir))[2]

        for file in files:
            isTrajectory = file.find(key)
            if isTrajectory >= 0:
                r.append(subdir + "/" + file)
    return r

def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]


files_xyz = list_files("/Volumes/Transcend/data_sets/CN_isobutane_model/geoms_2/training", ".xyz")

files_prop = np.loadtxt("/Volumes/Transcend/data_sets/CN_isobutane_model/geoms_2/training/prop_Ha_training.txt", usecols=0, dtype='str')

print("There are %s xyz files and %s energies." % (len(files_xyz), len(files_prop)))

# Checking for missing files
for item in files_prop:

    filename = "/Volumes/Transcend/data_sets/CN_isobutane_model/geoms_2/training/" + item

    if not filename in files_xyz:
        print("File %s is missing the xyz coordinates.")

# Checking for duplicates
unique_ene = np.unique(files_prop)

if len(unique_ene) < len(files_prop):
    print("There is a duplicate energy.")

    for item_1 in files_prop:
        counter = 0
        for item_2 in files_prop:
            if item_1 == item_2:
                counter += 1
                if counter > 1:
                    print("Item %s is a duplicate." % (item_1))
