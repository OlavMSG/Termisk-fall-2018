#Dette skriptet gjør en Linær regresjon, med usikkerhet
#skrevet av Olav Milian Schmitt Gran

import matplotlib.pyplot as plt
import numpy as np
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

def func1(x, y):
    t1 = 339.87 + x
    t2 = 391.64 + y
    #Les inn fil
    t1e, M1e = np.loadtxt('Maalinger uten Al.txt', unpack = True,  delimiter =' ')
    #x-verdier eksprimentell
    #y-verdier eksprimetell

    #a0, a1, yb, Dy
    M1a0, M1a1, M1b, DM1 = lineaer_regresjon(t1e, M1e)

    #Les inn fil 2
    t2e, M2e = np.loadtxt('Maalinger med Al.txt', unpack = True,  delimiter =' ')
    #x-verdier eksprimentell
    #y-verdier eksprimetell
    M2e = M2e
    #a0, a1, yb, Dy
    M2a0, M2a1, M2b, DM2 = lineaer_regresjon(t2e, M2e)

    #for plotting
    tb = np.linspace(min(t1e), max(t2e), 100)
    M1b = M1a0 + M1a1 * tb
    M2b = M2a0 + M2a1 *tb
    #Regner ut DeltaM og dDeltaM
    Mat1 = M1a0 + M1a1*t1
    Mat2 = M1a0 + M1a1*t2

    Mbt1 = M2a0 + M2a1*t1
    Mbt2 = M2a0 + M2a1*t2

    DeltaM1 = Mat1-Mbt1
    DeltaM2 = Mat2-Mbt2

    DeltaM = 1/2*(DeltaM1+DeltaM2)
    print('DeltaM = ',DeltaM)
    delDeltaM = 1/2*(DeltaM1-DeltaM2)
    print('dDelta = ', delDeltaM)

    # Plotter
    plt.figure(1)                # første figure
    plt.plot(t1e, M1e, 'rx', label='(t1i,m1i)', alpha=0.5)              # plottter xe mot ye i røde kryss
    plt.plot(tb, M1b, 'r-',label='m1 = m1a0 +m1a1*t', alpha=0.5)               # plotter xe mot yb med blå linje
    plt.plot(t2e, M2e, 'bx', label='(t2i,m2i)', alpha=0.5)              # plottter xe mot ye i røde kryss
    plt.plot(tb, M2b,'b-', label='m2 = m2a0 +m2a1*t', alpha=0.5)               # plotter xe mot yb med blå linje
    plt.axvline(x=t1, color='k', label='t1', linestyle='--')
    plt.axvline(x=t2, color='k', label='t2', linestyle='-.')
    plt.ylim([0, 1.1*np.max(M1b)])
    plt.xlabel('$t [s]$')
    plt.ylabel('$m [g]$')
    plt.title('Delta m')
    plt.legend(loc='lower left')
    #plt.savefig('Delta_m.pdf') # lagrer plot som pdf

    """plt.figure(2) # andre figur
    plt.plot(xe, Dy, 'rx', label='(xi,Dyi)', alpha=0.5)              # plottter xe mot Dy i røde kryss
    plt.plot(xe, yb - yb)
    plt.ylim([1.1*np.min(Dy), 1.1*np.max(Dy)])
    plt.xlabel('$x$')
    plt.ylabel('$Dy$')
    plt.title('x mot Dy')
    plt.legend(loc='upper left');
    plt.savefig('lengdeDM.pdf')"""

    plt.show()

    return DeltaM, delDeltaM

