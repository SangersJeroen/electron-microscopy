from math import gamma
from turtle import speed
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['figure.dpi'] = 180
mpl.rcParams['font.family'] = ["Baskerville"]
mpl.rcParams['font.size'] = 12

electronv_joule = 1.6e-19
electron_mass   = 9.1e-31
speed_const     = 3e8
planck          = 6.6e-34
mcsq            = 511e3


volts = np.linspace(70,310,310-70+1) *1e3
energy = electronv_joule*volts

lambda_cla = planck/(np.sqrt(2*electron_mass*energy)) * 1e12 #pm

lambda_rel = speed_const*planck /np.sqrt(energy**2 + \
    2*energy*electron_mass*speed_const**2) * 1e12 #pm

lambda_200 = lambda_rel[volts==200000][0]


plt.plot(volts*1e-3, lambda_rel, label="relativistically", color='red')
plt.plot(volts*1e-3, lambda_cla, label='classically', color='blue')
plt.xlabel(r"Acceleration Voltage $V_{acc}$ [$kV$]")
plt.ylabel(r"de Broglie wavelength $\lambda$ [$pm$]")
plt.hlines(lambda_200,volts[volts==200000]*1e-3, 150, linestyle='--', color='red')
plt.vlines(200, 0, lambda_200, color='red', linestyle='--')
plt.text(80, 2.5, r"$\lambda_{200kV}=$"+'{:.2f}'.format(lambda_200)+r" $pm$")
plt.ylim([1.8,4.6])
plt.legend(frameon=False)
plt.gcf().set_size_inches(8,5)
plt.savefig('problem1.pdf')
plt.show()
