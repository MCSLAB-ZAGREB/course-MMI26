# Primjer iz udžbenika:
#   T. Witelski, M. Bowen, "Methods of Mathematical Modelling: Continuous
#   Systems and Differential Equations", Springer Undergraduate Mathematics
#   Series, Springer, 2015.
#   Model: poglavlje 4 "Dimensional Scaling Analysis",
#   odjeljak 4.3.1 "Projectile Motion", problem (4.9), str. 91
#   (lansiranje s površine Zemlje, Y0 = 0).
#   Perturbacijski razvoj: poglavlje 6 "Perturbation Methods",
#   odjeljak 6.4 "A Regular Expansion for a Solution of an ODE Problem",
#   str. 138-139. U knjizi je razvoj napravljen za skaliranje (4.7a), s
#   x(0) = 1, x'(0) = α; ovdje je isti postupak primijenjen na x(0) = 0,
#   x'(0) = 1.
#
# Lansiranje rakete s površine Zemlje početnom brzinom v0 vertikalno u zrak,
# u gravitacijskom polju koje slabi s visinom, opisano je bezdimenzionalnim
# modelom
#   x''(t) = -1/(1 + ε x(t))^2,
#   x(0) = 0,
#   x'(0) = 1,
# gdje je ε = v0^2/(gR) mali parametar, R = 6370 km polumjer Zemlje, a
# g = 9.81 m/s^2 ubrzanje sile teže na površini Zemlje.
# Visina je mjerena u jedinicama v0^2/g, a vrijeme u jedinicama v0/g.
#
# Za ε = 0 dobivamo model u konstantnom gravitacijskom polju, x'' = -1, s
# rješenjem x0(t) = t - t^2/2 (raketa pada natrag na tlo u t = 2).

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

plt.rcParams.update({'font.size': 12})

# Boje: svaka aproksimacija ima istu boju na svim grafovima
plava = '#4285F4'    # numeričko rješenje
zelena = '#0F9D58'   # x0 (konstantno gravitacijsko polje)
crvena = '#EA4335'   # x0 + εx1 (perturbacijsko rješenje)
zuta = '#F4B400'     # x0 + εx1 + ε^2 x2

# Parametar: za v0 = 3600 km/h = 1000 m/s je ε = v0^2/(gR) ≈ 0.016
epsilon = 0.016


# -----------------------------------------------------------------------------
# Numeričko rješenje
# -----------------------------------------------------------------------------
# Sustav prvog reda: Y = [x, v] = [x, x']
#   x' = v
#   v' = -1/(1 + ε x)^2
def sustav(t, Y, epsilon):
    x, v = Y
    return [v, -1/(1 + epsilon*x)**2]


# Događaji koje solve_ivp prati tijekom integracije (traži nultočke funkcija):
#   vrh        - brzina je nula, raketa je na najvećoj visini
#   pad_na_tlo - visina je nula pri padanju; tu zaustavljamo integraciju
def vrh(t, Y, epsilon):
    return Y[1]

def pad_na_tlo(t, Y, epsilon):
    return Y[0]
pad_na_tlo.terminal = True
pad_na_tlo.direction = -1


# DOP853 je eksplicitna Runge-Kutta metoda 8. reda. Tolerancije postavljamo
# strogo, tako da numerička pogreška bude puno manja od pogreške
# perturbacijskog razvoja koju želimo vidjeti (do ε^3 ≈ 4e-6). Uz zadane
# tolerancije (rtol = 1e-3) numeričko rješenje ne bi bilo dovoljno točno.
rj = solve_ivp(sustav, [0, 10], [0, 1], method='DOP853', args=(epsilon,),
               events=[vrh, pad_na_tlo], dense_output=True,
               rtol=1e-10, atol=1e-12)

t_vrh, x_vrh = rj.t_events[0][0], rj.y_events[0][0][0]
t_pad = rj.t_events[1][0]

# Rješenje računamo na jednolikoj mreži od lansiranja do pada
t = np.linspace(0, t_pad, 1000)
x_num = rj.sol(t)[0]


# -----------------------------------------------------------------------------
# Perturbacijsko rješenje  x(t) ~ x0(t) + ε x1(t) + ε^2 x2(t) + ...
# -----------------------------------------------------------------------------
# Razvijemo desnu stranu: -1/(1 + εx)^2 = -1 + 2εx - 3ε^2 x^2 + ...  (6.25),
# uvrstimo razvoj za x i izjednačimo članove uz iste potencije od ε:
#   O(1):    x0'' = -1,                x0(0) = 0, x0'(0) = 1
#   O(ε):    x1'' = 2 x0,              x1(0) = 0, x1'(0) = 0
#   O(ε^2):  x2'' = 2 x1 - 3 x0^2,     x2(0) = 0, x2'(0) = 0
# Svaki problem rješavamo dvostrukom integracijom, redom od x0 prema x2.
def x0(t):
    return t - t**2/2

def x1(t):
    return t**3/3 - t**4/12

def x2(t):
    return -t**4/4 + 11*t**5/60 - 11*t**6/360


x_p0 = x0(t)
x_p1 = x_p0 + epsilon*x1(t)
x_p2 = x_p1 + epsilon**2*x2(t)


# -----------------------------------------------------------------------------
# Usporedba
# -----------------------------------------------------------------------------
# Najveća visina može se izračunati i točno, iz zakona očuvanja energije:
#   x_max = 1/(2 - ε)
print(f'Vrijeme leta:   {t_pad:.6f}   (konstantno polje: 2)')
print(f'Najveća visina: {x_vrh:.6f}   (točno: 1/(2 - ε) = {1/(2 - epsilon):.6f},'
      f' konstantno polje: 0.5)')
print('Najveća pogreška u odnosu na numeričko rješenje:')
for naziv, x_p in [('x0', x_p0), ('x0 + εx1', x_p1),
                   ('x0 + εx1 + ε^2 x2', x_p2)]:
    print(f'  {naziv:20s} {np.max(np.abs(x_num - x_p)):.1e}')


# -----------------------------------------------------------------------------
# Grafovi
# -----------------------------------------------------------------------------
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5.5))

# 1) Rješenja: promjenjivo polje (numerički) i dvije aproksimacije
ax1.plot(t, x_num, color=plava, linewidth=2,
         label='numeričko (promjenjivo polje)')
ax1.plot(t, x_p0, color=zelena, linewidth=2,
         label=r'$x_0$ (konstantno polje)')
ax1.plot(t, x_p1, color=crvena, linewidth=2, linestyle='--',
         label=r'$x_0 + \varepsilon x_1$')
ax1.set_title('Visina rakete')
ax1.set_ylim(0, 0.6)
ax1.legend(loc='lower center')

# 2) Veličina pojedinih članova perturbacijskog reda (logaritamska skala):
#    svaki je otprilike ε puta manji od prethodnog.
#    Točku t = 0 izostavljamo jer su tamo svi članovi 0 (log(0) nije definiran).
ax2.semilogy(t[1:], np.abs(x0(t))[1:], color=zelena, linewidth=2,
             label=r'$|x_0|$')
ax2.semilogy(t[1:], np.abs(epsilon*x1(t))[1:], color=crvena, linewidth=2,
             label=r'$|\varepsilon x_1|$')
ax2.semilogy(t[1:], np.abs(epsilon**2*x2(t))[1:], color=zuta, linewidth=2,
             label=r'$|\varepsilon^2 x_2|$')
ax2.set_title('Članovi perturbacijskog reda')
ax2.set_ylim(1e-12, 1)
ax2.legend(loc='lower right')

# 3) Pogreška aproksimacija (logaritamska skala): redom je O(ε), O(ε^2) i
#    O(ε^3), tj. svaki novi član reda je smanjuje.
ax3.semilogy(t[1:], np.abs(x_num - x_p0)[1:], color=zelena, linewidth=2,
             label=r'$|x - x_0|$')
ax3.semilogy(t[1:], np.abs(x_num - x_p1)[1:], color=crvena, linewidth=2,
             label=r'$|x - (x_0 + \varepsilon x_1)|$')
ax3.semilogy(t[1:], np.abs(x_num - x_p2)[1:], color=zuta, linewidth=2,
             label=r'$|x - (x_0 + \varepsilon x_1 + \varepsilon^2 x_2)|$')
ax3.set_title('Pogreška u odnosu na numeričko rješenje')
ax3.set_ylim(1e-12, 1)
ax3.legend(loc='lower right')

for ax in (ax1, ax2, ax3):
    ax.set_xlabel('vrijeme t')
    ax.set_xlim(0, t_pad)
    ax.grid(linestyle=':', color='#c8c7c2')
ax1.set_ylabel('visina x')

fig.suptitle(rf"Lansiranje rakete: $x'' = -1/(1 + \varepsilon x)^2$, "
             rf"$x(0) = 0$, $x'(0) = 1$, $\varepsilon = {epsilon:g}$")
fig.tight_layout()
plt.show()
