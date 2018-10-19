"""
This script takes some files from the directory with all the molpro input files and submits some of them to the queue.
"""

import glob
import os
import sys

###### Things to change #############
path_to_molpro_inputs = "/Volumes/Transcend/useful_scripts/molpro_submission/cn_isopentane_molpro_inputs_dft"
indices_to_run = list(range(int(sys.argv[1]),int(sys.argv[2])))
#####################################

filenames = glob.glob(path_to_molpro_inputs + "/*.com")

filenames_to_run = []
for file in filenames:
    the_name = file.split("/")[-1]
    the_idx = int(the_name.split("_")[0])
    if the_idx in indices_to_run:
        filenames_to_run.append(file)

for file in filenames_to_run:
    temp_submit_script = open("submit.sh", "w")
    submit_script = open("template_submit.sh", "r")

    file_name_with_extension = file.split("/")[-1]

    for line in submit_script:
        if "b3lyp_tzvp_u" in line:
            index_end = line.find("b3lyp_tzvp_u")
            index_start = index_end - 8
            line = line.replace(line[index_start:index_end], file_name_with_extension[:8])
        temp_submit_script.write(line)

    temp_submit_script.close()
    submit_script.close()

    os.system("qsub submit.sh")


os.system("python gather_results.py")

