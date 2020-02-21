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

#Generell formel
Bhhs1 = 3*R*(ThetaE/T)**2*(np.e**(ThetaE/T))/((np.e**(ThetaE/T)-1)**2)
#dBbd = [sp.diff(Bhhs, x), sp.diff(Bhhs, I), sp.diff(Bhhs, R), sp.diff(Bhhs, a)]

Te, Ce, xe = np.loadtxt('Tabell 2_1.txt', unpack=True, delimiter = ', ')
Ce = Ce*4.184


te = 1/Te
ye = np.log(Ce)
a0e, a1e, y1e, Dye = lineaer_regresjon(te,ye)
print('a1 = ', a1e, 'a0 = ', a0e)


#posisjonen eksperimentielt#Målte B-verdier
Tb = np.linspace(2, Te[-1]+10, 200) #posisjon for en beregnet kurve #ikke start på 1 eller mindre
Cb = [Bhhs1.subs([(T, Tbi), (ThetaE, 1325)]) for Tbi in Tb]
Tb = np.array(Tb).astype(np.float64)
Cb = np.array(Cb).astype(np.float64)

tb = 1/Tb
yb = np.log(Cb)
a0b, a1b, y1b, Dyb = lineaer_regresjon(tb,yb)



# Plotter

plt.figure(2)
plt.plot(Tb, Cb, label='Beregnet kurve', alpha=0.5)
plt.errorbar(Te, Ce, fmt='r.', label='Måledata')
plt.title('Tabell 2_1')
plt.xlabel('$T$ [K]')
plt.ylabel('$C$ [(J/(mol K)]')
plt.legend(loc='upper left');
#plt.savefig('Helmholtzspole_a=2R_v3.pdf')



plt.show()
plt.close()


