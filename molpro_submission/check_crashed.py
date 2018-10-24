"""
This script checks the Molpro jobs that have run and prints the indices of those that have crashed to a file.
"""

import glob
import numpy as np

########### Things to change ################
path_to_molpro_outputs = "/Volumes/Transcend/data_sets/CN_isopentane/training_Molpro"
#############################################

def get_filename(filename):
    split_1 = filename.split("/")
    split_2 = split_1[-1].split("_")
    return int(split_2[0])

def get_energy(file):

    file.seek(0)

    ene = 0

    for line in file:
        if "!UKS STATE  1.1 Energy" in line:
            line = line.strip()
            ene = float(line[len("!UKS STATE  1.1 Energy"):].strip())

    return ene

def get_xyz(file):

    file.seek(0)

    zs_dict = {"C": 6, "H":1, "N":7}

    zs = []
    xyz = []
    for line in file:
        if "geometry={" in line:
            while True:
                line = next(file)
                if "}" in line:
                    break
                line = line.strip()
                line = line.strip(",")
                lineSplit = line.split(",")
                zs.append(zs_dict[lineSplit[0]])
                xyz_1 = []
                for j in range(1,4):
                    xyz_1.append(float(lineSplit[j]))
                xyz.append(xyz_1)

    return np.asarray(xyz), np.asarray(zs)

def get_forces(file):

    file.seek(0)

    forces = []

    for line in file:
        if "dE/dx" in line:
            line = next(file)
            line = next(file)

            while True:
                line = line.strip()
                line = line.strip(",")
                lineSplit = line.split(" ")
                filtered_line = [item for item in lineSplit if item != '']
                forces_1 = []
                for i in range(1,4):
                    forces_1.append(float(filtered_line[i]))
                forces.append(forces_1)
                line = next(file)
                if len(line) <= 3:
                    break

    return np.asarray(forces)

def extract_data(filename):
    f = open(filename, 'r')

    coordinates = []
    energies = 0
    forces = []
    filename_number = -1

    # Getting the filename
    filename_number = get_filename(filename)

    # Getting the energy
    ene = get_energy(f)

    # Getting Cartesian coordinates
    xyz, zs = get_xyz(f)

    # Getting forces
    forces = get_forces(f)

    return filename_number, xyz, zs, ene, forces

def check_data(f_n, xyz, zs, ene, forces):

    if ene == 0:
        return False

    if f_n == -1:
        return False

    if len(xyz) == 0 or len(forces) == 0 or len(zs) == 0:
        return False

    if zs.shape[0] != xyz.shape[0] or zs.shape[0] != forces.shape[0] or forces.shape[0] != xyz.shape[0]:
        return False

    if xyz.shape[-1] != 3 or forces.shape[-1] != 3:
        return False

    return True


filenames = glob.glob( path_to_molpro_outputs + "/*.out")

crashed = []

for item in filenames:
    filename_number, xyz, zs, ene, forces = extract_data(item)

    print(sum(zs))

    is_correct = check_data(filename_number, xyz, zs, ene, forces)

    if is_correct == False:
        crashed.append(filename_number)

f = open("crashed_jobs.txt", "w")

for idx in crashed:
    f.write(str(idx))
    f.write(",")

f.close()

