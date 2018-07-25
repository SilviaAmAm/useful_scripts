import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from shutil import copyfile

name_test = np.loadtxt("/Volumes/Transcend/data_sets/CN_isobutane_model/geoms_2/test/properties_kjmol.txt", usecols=[0], dtype='str')
name_train = np.loadtxt("/Volumes/Transcend/data_sets/CN_isobutane_model/geoms_2/training/prop_kjmol_training.txt", usecols=[0], dtype='str')

ene_test_kj = np.loadtxt("/Volumes/Transcend/data_sets/CN_isobutane_model/geoms_2/test/properties_kjmol.txt", usecols=[1])
ene_train_kj = np.loadtxt("/Volumes/Transcend/data_sets/CN_isobutane_model/geoms_2/training/prop_kjmol_training.txt", usecols=[1])
ene_test_ha = np.loadtxt("/Volumes/Transcend/data_sets/CN_isobutane_model/geoms_2/test/properties_Ha.txt", usecols=[1])
ene_train_ha = np.loadtxt("/Volumes/Transcend/data_sets/CN_isobutane_model/geoms_2/training/prop_Ha_training.txt", usecols=[1])

pruned_training_dir = "/Volumes/Transcend/data_sets/CN_isobutane_model/pruned_cn_isobutane/training/"
raw_training_dir = "/Volumes/Transcend/data_sets/CN_isobutane_model/geoms_2/training/"

prop_file_kj = open("/Volumes/Transcend/data_sets/CN_isobutane_model/pruned_cn_isobutane/training/properties_kjmol.txt", "w")
prop_file_Ha = open("/Volumes/Transcend/data_sets/CN_isobutane_model/pruned_cn_isobutane/training/properties_Ha.txt", "w")



for name, ene_kj, ene_ha in zip(name_train, ene_train_kj, ene_train_ha):
    if ene_kj < 500.0:
        # Copying xyz
        # src = raw_training_dir + name
        # dst = pruned_training_dir + name
        # copyfile(src, dst)

        # Updating prop file
        prop_file_kj.write("name" + "\t" + str(ene_kj) + "\n")
        prop_file_Ha.write("name" + "\t" + str(ene_ha) + "\n")

prop_file_Ha.close()
prop_file_kj.close()

new_train_ene = np.loadtxt("/Volumes/Transcend/data_sets/CN_isobutane_model/pruned_cn_isobutane/training/properties_kjmol.txt", usecols=[1])
new_train_Ha = np.loadtxt("/Volumes/Transcend/data_sets/CN_isobutane_model/pruned_cn_isobutane/training/properties_Ha.txt", usecols=[1])
x = range(len(new_train_ene))

print(len(new_train_ene))
print(len(new_train_Ha))

plt.scatter(x, new_train_ene, alpha=0.6)
plt.ylabel("Energy (kJ/mol)")
plt.xlabel("Time step")
plt.savefig("cn_isopent_pruned.png", dpi=200)
plt.show()
