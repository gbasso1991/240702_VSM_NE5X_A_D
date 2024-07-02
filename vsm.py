#%% VSM -  Ferrosolidos (ferrotec + laurico)
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
import os
from sklearn.metrics import r2_score 
from mlognormfit import fit3

def lineal(x,m,n):
    return m*x+n
#%% 
Antes = np.loadtxt('A.txt',skiprows=12)

H_A  = Antes[:,0] #Gauss
m_A  = Antes[:,1] #emu

mass_FF_A = 52.4 #mg
vol_FF_A = mass_FF_A*1e-3 #mL  #esto venia del script de Gus
mass_Fe_A = 6.8e-3*vol_FF_A
mass_Fe3O4_A = mass_Fe_A /3/55.85*231.563

a = fit3.session(H_A, m_A,fname='NE5X_A',mass = mass_Fe3O4_A,divbymass=True)
#b = fit3.session(H_A, m_A)
a.setp('N0',3e18)
a.fit()
a.update()
a.plot()
a.print_pars()
a.save()
#%%
Despues = np.loadtxt('D.txt',skiprows=12)
H_D  = Despues[:,0] #Gauss
m_D = Despues[:,1]  #emu

mass_FF_D = 50.6 #mg
vol_FF_D = mass_FF_D*1e-3 #mL  #esto venia del script de Gus
mass_Fe_D = 6.8e-3*vol_FF_D
mass_Fe3O4_D = mass_Fe_D /3/55.85*231.563

b = fit3.session(H_D, m_D,fname='NE5X_D',mass = mass_Fe3O4_D,divbymass=True)

b.setp('N0',3e18)
b.fit()
b.update()
b.plot()
b.print_pars()
b.save()
#%%
fig,ax=plt.subplots(figsize=(7,4.66),constrained_layout=True)
ax.plot(a.X,a.Y,'o-',label='A')
ax.plot(a.X,a.Yfit,'-',label='A fit')

ax.plot(b.X,b.Y,'o-',label='D')
ax.plot(b.X,b.Yfit,'-',label='D fit')

ax.legend()
# plt.plot(f1,g1,'.-')
# plt.plot(f2,g2,'.-')
# plt.plot(f,g_ajustado,'-',c='tab:red',label=f'$\chi$ = {chi_mass_laurico:.2e} emu/gG')
plt.legend(ncol=2)
plt.grid()
plt.xlabel('H (G)')
plt.ylabel('m (emu)')
plt.title('NE5X - Antes y Despues de RF')
plt.savefig('VSM_NE5X_AD.png',dpi=300)

