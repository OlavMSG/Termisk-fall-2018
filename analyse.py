#skrevet av Olav Milian Schmitt Gran

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from LinejaerRegresjon_for_Delta_m import func1

x = 0 #Normalt 0
y = 0 #Normalt 0

DeltaM, dDeltaM = func1(x, y)
DeltaM = DeltaM*1e-3
dDeltaM = dDeltaM*1e-3
L = 2.0e5
T_0 = 297.15
DeltaT_0 = 1
T_f = 77
R = 8.3144598
n = 6.069/26.981538

T0, ThetaE = sp.symbols('T0 ThetaE')
DM = sp.symbols('DM')

#Generell formel
fDeltaQ1 = 3*n*R*(T0*(ThetaE/T0)/(np.e**(ThetaE/T0)-1)-T_f*(ThetaE/T_f)/(np.e**(ThetaE/T_f)-1))
fDeltaQ2 = L*DM
N = 100
M = 277
K = 310
ThetaElist = np.linspace(M+1, K+1, (K-M)*N)

#ThetaE
DeltaQ1 = [fDeltaQ1.subs([(T0, T_0),(ThetaE, ThetaEi)]) for ThetaEi in ThetaElist]
DeltaQ1 = np.array(DeltaQ1).astype(np.float64)
DeltaQ2 = fDeltaQ2.subs([(DM, DeltaM)])

F = np.abs(DeltaQ1-DeltaQ2)

F_min = np.argmin(F)
F_min = F_min / N + M
print('ThetaE = ', F_min)

#DDThetaE_dm

DeltaQ1 = [fDeltaQ1.subs([(T0, T_0),(ThetaE, ThetaEi)]) for ThetaEi in ThetaElist]
DeltaQ1 = np.array(DeltaQ1).astype(np.float64)
DeltaQ2 = fDeltaQ2.subs([(DM, DeltaM+dDeltaM)])

F = np.abs(DeltaQ1-DeltaQ2)

F_T0pdDM = np.argmin(F)

F_T0pdDM = F_T0pdDM / N + M
print(F_T0pdDM)

DeltaQ1 = [fDeltaQ1.subs([(T0, T_0),(ThetaE, ThetaEi)]) for ThetaEi in ThetaElist]
DeltaQ1 = np.array(DeltaQ1).astype(np.float64)
DeltaQ2 = fDeltaQ2.subs([(DM, DeltaM-dDeltaM)])

F = np.abs(DeltaQ1-DeltaQ2)

F_T0ndDM = np.argmin(F)

F_T0ndDM = F_T0ndDM / N + M
print(F_T0ndDM)

DDThetaE_dm = 1/2 * (F_T0pdDM - F_T0ndDM)

print(DDThetaE_dm)

#DDThetaE_dT

DeltaQ1 = [fDeltaQ1.subs([(T0, T_0 + DeltaT_0),(ThetaE, ThetaEi)]) for ThetaEi in ThetaElist]
DeltaQ1 = np.array(DeltaQ1).astype(np.float64)
DeltaQ2 = fDeltaQ2.subs([(DM, DeltaM)])

F = np.abs(DeltaQ1-DeltaQ2)

F_T0pdDT = np.argmin(F)

F_T0pdDT = F_T0pdDT / N + M
print(F_T0pdDT)

DeltaQ1 = [fDeltaQ1.subs([(T0, T_0 - DeltaT_0),(ThetaE, ThetaEi)]) for ThetaEi in ThetaElist]
DeltaQ1 = np.array(DeltaQ1).astype(np.float64)
DeltaQ2 = fDeltaQ2.subs([(DM, DeltaM)])

F = np.abs(DeltaQ1-DeltaQ2)

F_T0ndDT = np.argmin(F)

F_T0ndDT = F_T0ndDT / N + M
print(F_T0ndDT)

DDThetaE_dT = 1/2 * (F_T0pdDT - F_T0ndDT)

print(DDThetaE_dT)

#DThetaE

DThetaE =np.sqrt(DDThetaE_dm**2 + DDThetaE_dT**2)
print('DThetaE =', DThetaE)
