"""
This script takes a vr trajectory and makes a numpy data set containing the xyz, the zs, the energies and the forces.
"""

import numpy as np



def extract_data(input_file, output_dir):
    """
    This function takes in a path to a file which contains a joined VR trajectory with xyz, energies and forces and extracts the information. It the saves it to a npz file.
    """
    elements = {"H": 1, "C": 6, "N": 7}

    f = open(input_file, 'r')

    energies = []
    coordinates = []
    tot_forces = []
    tot_zs = []

    for line in f:
        n_atoms = int(line)
        line = next(f)
        line = line.strip()
        line = line.split(" ")
        energy = float(line[2])

        xyz = np.zeros((n_atoms, 3))
        forces = np.zeros((n_atoms, 3))
        zs = np.zeros((n_atoms,))

        for i in range(n_atoms):
            line = next(f)
            line = line.strip()
            line = line.split("\t")
            zs[i] = elements[line[0]]
            xyz[i] = [float(item) for item in line[1:4]]
            forces[i] = [float(item) for item in line[4:]]

        energies.append(energy)
        coordinates.append(xyz)
        tot_forces.append(forces)
        tot_zs.append(zs)

    energies = np.asarray(energies)
    coordinates = np.asarray(coordinates)
    tot_zs = np.asarray(tot_zs)
    tot_forces = np.asarray(tot_forces)

    return coordinates, tot_zs, energies, tot_forces


if __name__ == "__main__":

    input_file = "/Volumes/Transcend/data_sets/CN_isobutane_model/training_traj/combinedTraj.xyz"
    output_directory = "."

    coord, zs, ene, forces = extract_data(input_file, output_directory)

    print(coord.shape, zs.shape, ene.shape, forces.shape)

    np.savez("CN_isopentane_forces.npz", coord, zs, ene, forces)
