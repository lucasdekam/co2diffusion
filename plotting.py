import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'font.size': 12})

# COLORS & formats
china = [x/255 for x in (214, 46, 28)]
purpur = [x/255 for x in (109, 29, 179)]
radish = [x/255 for x in (201, 95, 83)]
forest = [x/255 for x in (16, 97, 6)]
spring = [x/255 for x in (29, 184, 71)]
polar = [x/255 for x in (110, 110, 110)]
lapis = [x/255 for x in (52, 58, 235)]
end = [x/255 for x in (159, 10, 196)]
fmtcycle = ['-', '--', ':', '-.']

# Load data in list
data = []
data.append(np.load('concentrationdata_5e-03.npy'))
data.append(np.load('concentrationdata_3e-03.npy'))
data.append(np.load('concentrationdata_5e-04.npy'))
data.append(np.load('concentrationdata_5e-05.npy'))
# data.append(np.load('concentrationdata_5e-06.npy'))

legendlist = [r'-5', r'-2.5', r'-0.5','-0.05']

# CO2 concentration
plt.figure(1, figsize=(4,4))
for i in range(0, len(data)):
    plt.plot(data[i][:,0], data[i][:,1], fmtcycle[i], color=lapis)
    plt.xlim([0, data[i][-1,0]])
    plt.xlabel(r'$x \; \mathrm{(\mu m)}$')
    plt.ylabel(r'$\mathrm{[CO_2 \; (aq)]} \; \mathrm{(mM)}$')
plt.legend(legendlist)
plt.subplots_adjust(top=0.93,
    bottom=0.2,
    left=0.215,
    right=0.95,
    hspace=0.2,
    wspace=0.2)

# pH
plt.figure(2, figsize=(4,4))
for i in range(0, len(data)):
    plt.plot(data[i][:,0], data[i][:,4], fmtcycle[i], color=china)
    plt.xlim([0, data[i][-1,0]])
    plt.xlabel(r'$x \; \mathrm{(\mu m)}$')
    plt.ylabel(r'$\mathrm{pH}$')
plt.legend(legendlist)
plt.subplots_adjust(top=0.93,
    bottom=0.2,
    left=0.215,
    right=0.95,
    hspace=0.2,
    wspace=0.2)

# HCO3-
plt.figure(3, figsize=(4,4))
for i in range(0, len(data)):
    plt.plot(data[i][:,0], data[i][:,2], fmtcycle[i], color=spring)
    plt.xlim([0, data[i][-1,0]])
    plt.xlabel(r'$x \; \mathrm{(\mu m)}$')
    plt.ylabel(r'$\mathrm{[HCO_3^-]} \; \mathrm{(mM)}$')
plt.legend(legendlist)
plt.subplots_adjust(top=0.93,
    bottom=0.2,
    left=0.215,
    right=0.95,
    hspace=0.2,
    wspace=0.2)

# CO3 2-
plt.figure(4, figsize=(4,4))
for i in range(0, len(data)):
    plt.plot(data[i][:,0], data[i][:,3], fmtcycle[i], color=end)
    plt.xlim([0, data[i][-1,0]])
    plt.xlabel(r'$x \; \mathrm{(\mu m)}$')
    plt.ylabel(r'$\mathrm{[CO_3^{2-}]} \; \mathrm{(mM)}$')
plt.legend(legendlist)
plt.subplots_adjust(top=0.93,
    bottom=0.2,
    left=0.215,
    right=0.95,
    hspace=0.2,
    wspace=0.2)

plt.show()
