import numpy as np
from matplotlib import pyplot as plt
import sympy as sp
from regresjon import lineaer_regresjon

# Initialiserer pen visning av uttrykkene
sp.init_printing()

# Plotteparametre for C% fC% store, tydelige plott som utnytter tilgjengelig skjermareal
fontsize = 20
newparams = {'axes.titlesize': fontsize, 'axes.labelsize': fontsize,
             'lines.linewidth': 2, 'lines.markersize': 7,
             'figure.figsize': (16, 7), 'ytick.labelsize': fontsize,
             'xtick.labelsize': fontsize, 'legend.fontsize': fontsize,
             'legend.handlelength': 1.5}
plt.rcParams.update(newparams)

R = 8.3144598
T, ThetaE = sp.symbols('T ThetaE')

# Generell formel
Bhhs1 = 3 * R * (ThetaE / T) ** 2 * (np.e ** (ThetaE / T)) / ((np.e ** (ThetaE / T) - 1) ** 2)
# dBbd = [sp.diff(Bhhs, x), sp.diff(Bhhs, I), sp.diff(Bhhs, R), sp.diff(Bhhs, a)]

Te, Ce = np.loadtxt('Chase.txt', unpack=True, delimiter=' , ')
Ce = Ce*5/7

# posisjonen eksperimentielt#Målte B-verdier
Tb = np.linspace(2, Te[-1] + 100, 200)  # posisjon for en beregnet kurve #ikke start på 1 eller mindre
Cb = [Bhhs1.subs([(T, Tbi), (ThetaE, 300)]) for Tbi in Tb]
Tb = np.array(Tb).astype(np.float64)
Cb = np.array(Cb).astype(np.float64)

# y_kurve = [C_Vm]

plt.errorbar(Te, Ce, fmt='r.')
plt.plot(Tb, Cb)
plt.title('Chase')
plt.xlabel('T (K)')
plt.ylabel('C_Vm (J/(K mol))')
plt.savefig('Chase')
plt.show()