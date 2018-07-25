"""
This script takes as input the the combined trajectory file that was made using the "join_vr_traj.py" script and splits
it into files xyz files that can be read by molpro.

Warning: Molpro xyz files are not the same format as VMD xyz format. To make xyz files compatible with VMD, see the script.
"""

import os

def pad_filename(filenumber, n_of_zeros=5):
    """
    This function creates a filename number. If one has 20000 data samples, the first file should be called 00000.xyz
    and not 0.xyz. This function deals with this problem.

    :param filenumber: number of the data sample. In the example above it's "0" (int)
    :param n_of_zeros: Total number of characters that the number could have (int)
    :return: number of the file with added zeros. (string)
    """
    padding = "0"
    str_file_n = str(filenumber)
    n = n_of_zeros - len(str_file_n)
    file_idx = n * padding + str_file_n
    return file_idx

input_file = open("/Volumes/Transcend/data_sets/CN_squalane_model/test_traj/test_traj_2018-02-20_03-43-05-pm.xyz", 'r')
path_to_results = "/Users/walfits/Desktop/Test/"

counter = 0

# Creating a directory for the results if it doesn't exist already
if not os.path.exists(path_to_results):
    os.makedirs(path_to_results)

for line in input_file:
    # Creating the filename of each xyz
    file_ind = pad_filename(counter)
    f_name = path_to_results + str(file_ind) + ".xyz"
    f = open(f_name, "w")

    n_atoms = int(line.strip())

    line = next(input_file)

    # To make xyz files compatible with VMD, uncomment these lines
    # f.write(str(n_atoms)+"\n")
    # f.write("\n")

    for i in range(n_atoms):
        line = next(input_file)

        line_strip = line.strip()
        line_split = line_strip.split("\t")

        for j in range(4):
            f.write(line_split[j])
            f.write("\t")
        f.write("\n")

    f.close()
    counter += 1



