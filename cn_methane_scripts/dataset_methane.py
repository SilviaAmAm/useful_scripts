import numpy as np
import h5py

path = "/Volumes/Transcend/data_sets/CN_methane/SilviaAmAm-trainingdata-d5c9661aad24.zip.download/SilviaAmAm-trainingdata-d5c9661aad24/per-user-trajectories/CH4+CN/pruning/dataSets/pbe_b3lyp_partQ.csv"

f = open(path, "r")

xyz = []
ene = []

for line in f:
    clean_line = line.strip()
    if "C1x" in clean_line:
        continue
    else:
        split_line = clean_line.split(",")
        xyz_mol = []
        for i in range(1,22):
            xyz_mol.append(float(split_line[i]))
        xyz_mol = np.reshape(xyz_mol, (7, 3))
        xyz.append(xyz_mol)
        ene.append(float(split_line[-1]))

f.close()
xyz = np.asarray(xyz)
ene = np.asarray(ene)
zs = [6, 1, 1, 1, 1, 6, 7]
zs = np.tile(zs, reps=[len(ene), 1])

f = h5py.File("methane_cn_dft.hdf5", "w")

f.create_dataset("xyz", xyz.shape, data=xyz)
f.create_dataset("ene", ene.shape, data=ene)
f.create_dataset("zs", zs.shape, data=zs)

f.close()

