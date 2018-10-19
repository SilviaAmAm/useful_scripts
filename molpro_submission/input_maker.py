"""
This script takes a hdf5 that contains the geometries of some configurations and generates the molpro input files for
each one of them in a new directory.
"""

import h5py
import os
import utils
import numpy as np

####### Things to modify ##########
file_hdf5 = "/Volumes/Transcend/data_sets/CN_isopentane_pm6/cn_isopentane_pm6.hdf5"
molpro_dir_name = "cn_isopentane_molpro_inputs_dft/"
###################################

# Reading in the hdf5 data

data = h5py.File(file_hdf5, "r")

xyz = np.array(data.get("xyz"))
zs = np.array(data.get("zs"), dtype=np.int32)
traj_idx = np.array(data.get("traj_idx"), dtype=np.int32)

# Generating a new molpro directory
os.mkdir(molpro_dir_name)

# The Molpro input file header and footer
header = "memory,500,m\ngeomtyp=xyz\nnosym\nnoorient\ngdirect\ngeometry={\n"
footer = "}\nbasis={ default,tzvp }\n{uks,b3lyp,direct;wf,55,1,1}\nforce\n{ibba,bonds=1}"

# The loop to create each input file
n_files = xyz.shape[0]
for n in range(n_files):

    filenumber = utils.pad_filename(n)
    file_name = filenumber + "_" + str(traj_idx[n]) + "_b3lyp_tzvp_u.com"

    utils.write_molpro_input(xyz[n], zs[n], file_name, molpro_dir_name, header, footer)

    if n == 5:
        break







