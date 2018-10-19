import os

def write_molpro_input(xyz, zs, filename, directory, header, footer):
    """
    This function creates a Molpr input file in a specified directory.

    :param xyz: numpy array of cartesian coordinates of shape (n_atoms, 3)
    :param zs: numpy array of nuclear charges of shape (n_atoms,)
    :param filename: string with the name of the file to create
    :param directory: string with the path of the directory
    :param header: the header for the calculation
    :param footer: the footer for the calculation
    :return: none
    """
    path_file_name = directory + filename
    f = open(path_file_name, "w")

    f.write(header)

    # Writing the geometry to file
    zs_to_name = {6:"C",1:"H",7:"N"}
    n_atoms = xyz.shape[0]
    for i in range(n_atoms):
        f.write(zs_to_name[zs[i]])
        f.write("\t")
        for j in range(3):
            f.write(str(xyz[i][j]))
            f.write("\t")
        f.write("\n")

    f.write(footer)

    f.close()

def n_electrons(zs, charge):
    """
    Takes in a raw geometry and works out the number of electrons, accounting for overall charge

    :param zs: numpy array for the nuclear charge of each atom. shape (n_atoms,)
    :param charge: total charge of the compound (int)
    :return: the total number of electrons
    """

    neutral_electrons = sum(zs)
    total_charge = neutral_electrons - charge
    return total_charge

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




