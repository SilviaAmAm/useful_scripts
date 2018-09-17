import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def fc(r, rc):
    if r <= rc:
        cut = 0.5 * (np.cos(np.pi * r/rc) + 1)
    else:
        cut = 0
    return cut

old_params = {"radial_rs": np.arange(0, 10, 0.5),"angular_rs": np.arange(0, 10, 0.5), "theta_s": np.arange(0, 3.14, 0.25)}

# rcut = 5.0
# nRs2 = 15
# eta = 30.8065
# R_s = np.linspace(0, rcut, nRs2)

rcut = 10.0
nRs2 = len(old_params["radial_rs"])
eta = 1.0
R_s = old_params["radial_rs"]

R_ij = np.linspace(0, 5, 500)

all_G = []
for i in range(len(R_s)):
    G = []
    for rij in R_ij:
        g = np.exp(-eta * (rij - R_s[i])**2) * fc(rij, rcut)
        G.append(g)
    all_G.append(G)

for item in all_G:
    plt.plot(R_ij, item)
plt.xlabel("Distance (Å)")
plt.ylabel("Two body term")
plt.savefig("2body_acsf_oldparams.png", dpi=200)
plt.show()