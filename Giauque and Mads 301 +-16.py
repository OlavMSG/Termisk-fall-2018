#skrevet av Olav Milian Schmitt Gran

import numpy as np
from matplotlib import pyplot as plt
import sympy as sp

from regresjon import lineaer_regresjon
"""For pen plotting"""
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

"""Kode"""

R = 8.3144598
T, ThetaE = sp.symbols('T ThetaE')

#Generell formel
Bhhs1 = 3*R*(ThetaE/T)**2*(np.e**(ThetaE/T))/((np.e**(ThetaE/T)-1)**2)
#dBbd = [sp.diff(Bhhs, x), sp.diff(Bhhs, I), sp.diff(Bhhs, R), sp.diff(Bhhs, a)]

Te, Ce = np.loadtxt('Giauque and Mads.txt', unpack=True, delimiter = ' , ')
Ce = Ce*4.184


#posisjonen eksperimentielt#Målte B-verdier
Tb = np.linspace(5, Te[-1]+20, 200) #posisjon for en beregnet kurve #ikke start på 1 eller mindre
Cb = [Bhhs1.subs([(T, Tbi), (ThetaE, 300)]) for Tbi in Tb]
Cbforrev = [Bhhs1.subs([(T, Tei), (ThetaE, 300)]) for Tei in Te]
Cbp = [Bhhs1.subs([(T, Tbi), (ThetaE, 300+16)]) for Tbi in Tb]
Cbn = [Bhhs1.subs([(T, Tbi), (ThetaE, 300-16)]) for Tbi in Tb]
Tb = np.array(Tb).astype(np.float64)
Cb = np.array(Cb).astype(np.float64)
Cbforrev = np.array(Cbforrev).astype(np.float64)
Cbp = np.array(Cbp).astype(np.float64)
Cbn = np.array(Cbn).astype(np.float64)

#Relativt
revCe = (Cbforrev-Ce)/Cbforrev
revCbp = (Cb-Cbp)/Cb
revCbn = (Cb-Cbn)/Cb


#y_kurve = [C_Vm]
plt.figure(1)
plt.plot(Te, Ce, 'rx', label = 'Data G og M')
plt.plot(Tb, Cb, label = 'Beregnet, Theta_E = 301')
plt.fill_between(Tb, Cbn, Cbp,
                    label='Usikkerhet i beregnet ', alpha=0.5)
plt.title('Giauque and Meads, Theta_E = 301+-16')
plt.xlabel('T [K]')
plt.ylabel('C_Vm [J/(K mol)]')
plt.legend(loc='upper left')
plt.savefig('Aluminium_theta_E=301_16.pdf')

plt.figure(2)
plt.plot(Te, revCe, 'rx', label = 'Avvik i prosent')
plt.plot(Tb, Cb-Cb, label = 'Avvik = 0')
plt.fill_between(Tb, revCbn, revCbp,
                    label='Relativ usikkerhet i beregnet ', alpha=0.5)
plt.title('Relavtiv usikkerhet Giauque and Meads, Theta_E = 301+-16')
plt.xlabel('T [K]')
plt.ylabel('Avvik [%]')
plt.ylim(1.1*min(revCbn), 1.5*max(revCbp))
plt.legend(loc='lower right')
#plt.savefig('Relativ_usikkerhet_Aluminium_theta_E=301_16_2.pdf') # lagrer plot som pdf

plt.show()