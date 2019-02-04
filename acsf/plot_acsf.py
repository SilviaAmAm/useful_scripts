import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
sns.set_style("white")
sns.set_context("poster")

def fc(r, rc):
    if r <= rc:
        cut = 0.5 * (np.cos(np.pi * r/rc) + 1)
    else:
        cut = 0
    return cut

# old_params = {"radial_rs": np.arange(0, 10, 0.5),"angular_rs": np.arange(0, 10, 0.5), "theta_s": np.arange(0, 3.14, 0.25)}
# rcut = 10.0
# nRs2 = len(old_params["radial_rs"])
# eta = 1.0
# R_s = old_params["radial_rs"]


rcut = 5.0
nRs2 = 6
eta = 4
R_s = np.linspace(0, rcut, nRs2)


R_ij = np.linspace(0, 5, 500)

all_G = []
for i in range(len(R_s)):
    G = []
    for rij in R_ij:
        g = np.exp(-eta * (rij - R_s[i])**2) #* fc(rij, rcut)
        G.append(g)
    all_G.append(G)

fig, ax = plt.subplots(figsize=(9,9))
for item in all_G:
    ax.plot(R_ij, item)
ax.set_xlabel("Distance (Å)")
ax.set_ylabel("Radial basis function value")
plt.savefig("/Users/walfits/Desktop/good_eta.png", dpi=200)
# plt.show()