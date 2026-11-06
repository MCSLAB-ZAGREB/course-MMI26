import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# ============================================================
# Physical parameters
# ============================================================

q = 40_000.0          # imposed heat flux [W/m^2]

rho = 1000.0          # [kg/m^3]
cp = 4180.0           # [J/(kg K)]
k = 0.60              # [W/(m K)]

alpha = k / (rho * cp)

T0 = 20.0             # initial temperature [deg C]
T_boil = 100.0        # boiling temperature [deg C]

H = 0.15              # water depth [m]

print(f"alpha = {alpha:.4e} m^2/s")


# ============================================================
# Analytical semi-infinite solution
# ============================================================

def exact_temperature(z, t):
    """
    Semi-infinite solution:
        T_t = alpha T_zz
        -k T_z(0,t) = q
        T(z,0) = T0
        T -> T0 as z -> infinity
    """

    z = np.asarray(z, dtype=float)

    if t == 0:
        return np.full_like(z, T0)

    eta = z / (2.0 * np.sqrt(alpha * t))

    delta_T = (
        2.0 * q / k
        * np.sqrt(alpha * t / np.pi)
        * np.exp(-eta**2)
        -
        q * z / k
        * erfc(eta)
    )

    return T0 + delta_T


# Exact boiling time at z = 0
t_boil_exact = (
    np.pi / alpha
    * (k * (T_boil - T0) / (2.0 * q))**2
)

print(f"Exact semi-infinite boiling time: {t_boil_exact:.6f} s")


# ============================================================
# Finite-difference grid
# ============================================================

N = 600                 # number of intervals
dz = H / N

z = np.linspace(0.0, H, N + 1)

# Explicit stability parameter
r = 0.4

dt = r * dz**2 / alpha

print(f"dz = {dz:.6e} m")
print(f"dt = {dt:.6e} s")
print(f"alpha*dt/dz^2 = {alpha*dt/dz**2:.3f}")


# ============================================================
# Initial condition
# ============================================================

T = np.full(N + 1, T0)


# ============================================================
# Times at which we want to save solutions
# ============================================================

save_times = [
    1.0,
    4.0,
    t_boil_exact,
    12.0
]

solutions = {}

t = 0.0
next_save = 0

t_end = max(save_times)


# ============================================================
# Explicit finite-difference time integration
# ============================================================

while t < t_end:

    # Adjust last step if necessary
    current_dt = min(dt, t_end - t)

    r_current = alpha * current_dt / dz**2

    T_new = T.copy()

    # --------------------------------------------------------
    # Interior points
    # --------------------------------------------------------

    T_new[1:-1] = (
        T[1:-1]
        + r_current
        * (T[2:] - 2.0*T[1:-1] + T[:-2])
    )

    # --------------------------------------------------------
    # Bottom boundary z = 0
    #
    # -k T_z = q
    #
    # Ghost point:
    # T_-1 = T_1 + 2 dz q/k
    # --------------------------------------------------------

    T_new[0] = (
        T[0]
        + r_current
        * (
            2.0*(T[1] - T[0])
            + 2.0*dz*q/k
        )
    )

    # --------------------------------------------------------
    # Top boundary z = H
    #
    # T_z(H,t) = 0
    # --------------------------------------------------------

    T_new[-1] = (
        T[-1]
        + r_current
        * 2.0*(T[-2] - T[-1])
    )

    t_old = t
    t += current_dt
    T = T_new

    # Save requested times approximately
    while (
        next_save < len(save_times)
        and t >= save_times[next_save]
    ):
        solutions[save_times[next_save]] = T.copy()
        next_save += 1


# ============================================================
# Compare numerical and analytical profiles
# ============================================================

# We only plot first 10 mm because the thermal layer is tiny
z_plot_max = 0.010

mask = z <= z_plot_max

for ts in save_times:

    T_num = solutions[ts]
    T_exact = exact_temperature(z, ts)

    plt.figure(figsize=(7, 5))

    plt.plot(
        1000*z[mask],
        T_num[mask],
        label="finite difference"
    )

    plt.plot(
        1000*z[mask],
        T_exact[mask],
        "--",
        label="semi-infinite exact"
    )

    plt.xlabel("z [mm]")
    plt.ylabel("T [deg C]")
    plt.title(f"t = {ts:.3f} s")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

    error_inf = np.max(
        np.abs(T_num[mask] - T_exact[mask])
    )

    print(
        f"t = {ts:8.4f} s : "
        f"max error in first 10 mm = {error_inf:.4e} K"
    )


# ============================================================
# Numerical boiling time
# ============================================================

T = np.full(N + 1, T0)

t = 0.0

previous_T_bottom = T[0]
previous_t = t

while T[0] < T_boil:

    previous_T_bottom = T[0]
    previous_t = t

    T_new = T.copy()

    T_new[1:-1] = (
        T[1:-1]
        + r
        * (T[2:] - 2.0*T[1:-1] + T[:-2])
    )

    T_new[0] = (
        T[0]
        + r
        * (
            2.0*(T[1] - T[0])
            + 2.0*dz*q/k
        )
    )

    T_new[-1] = (
        T[-1]
        + r
        * 2.0*(T[-2] - T[-1])
    )

    T = T_new
    t += dt


# Linear interpolation between the last two time levels
theta = (
    T_boil - previous_T_bottom
) / (
    T[0] - previous_T_bottom
)

t_boil_num = (
    previous_t
    + theta * dt
)

print()
print(f"Numerical boiling time = {t_boil_num:.6f} s")
print(f"Exact boiling time     = {t_boil_exact:.6f} s")

relative_error = abs(
    t_boil_num - t_boil_exact
) / t_boil_exact

print(
    f"Relative error = {100*relative_error:.4f} %"
)