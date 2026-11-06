# Primjer iz udžbenika:
#   T. Witelski, M. Bowen, "Methods of Mathematical Modelling: Continuous
#   Systems and Differential Equations", Springer Undergraduate Mathematics
#   Series, Springer, 2015.
#   Poglavlje 7 "Boundary Layer Theory",
#   odjeljak 7.1 "Observing Boundary Layer Structure in Solutions",
#   problem (7.1), str. 148.
#   Perturbacijsko rješenje izvedeno je u odjeljku 7.2 (jednadžbe 7.6-7.20).
#
# Rubni sloj u problemu
#   mali_p*y'' + 2y' + y = 0,  x iz (0, 1)
#   y(0) = 0,  y(1) = 1
# gdje je mali_p = ε mali pozitivni parametar (0 < ε << 1).
#
# Budući da ε množi najvišu derivaciju, rješenje se naglo mijenja u tankom
# sloju širine reda ε uz x = 0 (rubni sloj). Izvan sloja je blizu rješenja
# reduciranog problema 2y' + y = 0.
#
# Numeričko rješenje: scipy.integrate.solve_bvp (kolokacija s adaptivnom
# mrežom). Jednadžbu zapisujemo kao sustav prvog reda zamjenom u = y':
#   y' = u
#   u' = -(2u + y)/mali_p
#
# Uspoređujemo ga s perturbacijskim (složenim asimptotskim) rješenjem
#   y_pert(x) = e^((1-x)/2) - e^(1/2) e^(-2x/ε)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

# Parametar modela
mali_p = 0.001


# Desna strana sustava; Y[0] = y, Y[1] = u = y' (po retcima, za sve točke mreže)
def desna_strana(x, Y):
    y, u = Y
    return np.vstack((u, -(2*u + y)/mali_p))


# Rubni uvjeti u obliku reziduala koji moraju biti nula: y(0) = 0, y(1) = 1
def rubni_uvjeti(Ya, Yb):
    return np.array([Ya[0], Yb[0] - 1])


# Početna mreža i početna aproksimacija (y = 0, y' = 0).
# Gruba mreža je dovoljna: solve_bvp sam progušćuje mrežu gdje treba.
x = np.linspace(0, 1, 101)
Y_poc = np.zeros((2, x.size))

rjesenje = solve_bvp(desna_strana, rubni_uvjeti, x, Y_poc,
                     tol=1e-6, max_nodes=100000)
if not rjesenje.success:
    raise RuntimeError(rjesenje.message)

print(f'Broj čvorova konačne mreže: {rjesenje.x.size}, '
      f'od toga u [0, {5*mali_p:g}]: {np.sum(rjesenje.x < 5*mali_p)}')


# Perturbacijsko rješenje = vanjsko + unutarnje - zajednički dio:
#   vanjsko   (ε = 0, uvjet y(1) = 1):            e^((1-x)/2)              (7.8)
#   unutarnje (X = x/ε, uvjet y(0) = 0):          e^(1/2) (1 - e^(-2x/ε))  (7.11)
#   zajednički dio (preklapanje):                 e^(1/2)                  (7.15)
# Složeno rješenje je (7.20) u udžbeniku; pogreška mu je reda veličine ε.
def y_pert(x):
    return np.exp((1 - x)/2) - np.exp(0.5)*np.exp(-2*x/mali_p)


x_plot = np.linspace(0, 1, 5000)
y_num = rjesenje.sol(x_plot)[0]     # sol(x) vraća [y, y'], uzimamo y
print(f'Najveća razlika |y_num - y_pert| = '
      f'{np.max(np.abs(y_num - y_pert(x_plot))):.1e}  (očekujemo red ε = {mali_p:g})')


# Crtanje: lijevo cijela domena, desno uvećani rubni sloj [0, 10ε]
boja_num = '#4285F4'    # plava  - numeričko rješenje
boja_pert = '#EA4335'   # crvena - perturbacijsko rješenje
x_sloj = 10*mali_p      # na x = 10ε je e^(-2x/ε) = e^(-20), sloj je iščeznuo


def nacrtaj(ax, x):
    ax.plot(x, rjesenje.sol(x)[0], color=boja_num, linewidth=2,
            label='Numeričko rješenje (solve_bvp)')
    ax.plot(x, y_pert(x), color=boja_pert, linewidth=2, linestyle='--',
            label='Perturbacijsko rješenje')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(linestyle=':', color='#c8c7c2')
    ax.legend(loc='lower right')


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

nacrtaj(ax1, x_plot)
ax1.axvspan(0, x_sloj, color='#e8e8e8')     # sivo: područje uvećano desno
ax1.set_title('Cijela domena')

nacrtaj(ax2, np.linspace(0, x_sloj, 1000))
ax2.set_xlim(0, x_sloj)
ax2.set_title(f'Rubni sloj, uvećano na [0, {x_sloj:g}]')

fig.suptitle(rf"Rubni sloj u lijevom rubu domene: "
             rf"$\varepsilon y'' + 2y' + y = 0$, $\varepsilon = {mali_p:g}$")
fig.tight_layout()
plt.show()
