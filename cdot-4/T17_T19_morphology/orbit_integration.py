#!/usr/bin/env python3
"""
Orbit integration: T17 radial Lorentz stripping vs T19 vertical spring (morphological competition).

Fiducial MW-like disk galaxy in the connecton picture (T14/T17/T19).
Units: metres, seconds, kg. κ=1 (Lorentz coupling).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable

import numpy as np

G = 6.67430e-11
M_SUN = 1.989e30
KPC = 3.085677581e19  # metres per kiloparsec
MPC = 1e3 * KPC       # Mpc = 1000 kpc
KM = 1e3
Gyr = 3.15576e16

# Cosmological MOND scale (cdot-4)
C_LIGHT = 299792458.0
H0 = 70e3 / MPC  # 70 km/s/Mpc in SI
R0 = 6 * C_LIGHT / H0
G_DAGGER = C_LIGHT**2 / R0


@dataclass
class Galaxy:
    """MW-like baryonic mass, flat rotation curve in MOND regime."""

    M_bary: float = 6.0e10 * M_SUN  # MW-like; r_t ~ 11 kpc
    R_d: float = 3 * KPC

    @property
    def r_t(self) -> float:
        return math.sqrt(G * self.M_bary / G_DAGGER)

    @property
    def v_f(self) -> float:
        return (G * self.M_bary * G_DAGGER) ** 0.25

    def B_c(self, r: float) -> float:
        return self.v_f / max(r, 1.0)

    def g_bar(self, r: float) -> float:
        return G * self.M_bary / r**2

    def g_x(self, r: float) -> float:
        """Connecton response from RAR closure."""
        g_b = self.g_bar(r)
        return 0.5 * (-g_b + math.sqrt(g_b**2 + 4.0 * g_b * G_DAGGER))

    def omega_L_sq(self, r: float, v_phi: float) -> float:
        """T19: spring on outside r_t; strength ~ (g_x/g_bar) * omega_g^2."""
        if r <= self.r_t:
            return 0.0
        g_b = self.g_bar(r)
        if g_b <= 0:
            return 0.0
        gx = self.g_x(r)
        return (gx / g_b) * self.omega_grav_sq(r)

    def omega_grav_sq(self, r: float) -> float:
        """Disk vertical frequency from scale height h ~ 0.1 R_d, sigma_z ~ 0.2 v_f."""
        h = 0.1 * self.R_d
        sigma_z = 0.2 * self.v_f
        return (sigma_z / h) ** 2

    def omega_z_sq(self, r: float, v_phi: float) -> float:
        return self.omega_grav_sq(r) + self.omega_L_sq(r, v_phi)

    def marginal_v_phi(self, r: float) -> float:
        """Circular-orbit solution: g_x = v²/r + v B."""
        B = self.B_c(r)
        gx = self.g_x(r)
        disc = (B * r) ** 2 + 4.0 * gx * r
        return 0.5 * (-B * r + math.sqrt(disc))

    def tau_dyn(self, r: float) -> float:
        return 2 * math.pi * r / self.v_f


def cylindrical_deriv(t: float, y: np.ndarray, gal: Galaxy) -> np.ndarray:
    """State y = [r, phi, z, v_r, v_phi, v_z]."""
    r, phi, z, v_r, v_phi, v_z = y
    r = max(r, 0.01 * gal.R_d)

    B = gal.B_c(r)
    g_N = gal.g_bar(r)
    g_eff = gal.g_x(r)  # connecton-enhanced radial binding (RAR closure)
    wz2 = gal.omega_z_sq(r, v_phi)

    # Cylindrical accelerations (κ=1); gravity uses g_x not raw Newtonian g_bar
    a_r = v_phi**2 / r + v_phi * B - g_eff
    a_phi = -(2 * v_r * v_phi) / r - v_r * B
    a_z = -wz2 * z

    return np.array([v_r, v_phi / r, v_z, a_r, a_phi, a_z])


def _radial_excess_accel(gal: Galaxy, r: float, v_phi: float) -> float:
    """Net outward radial acceleration (positive => migrate outward)."""
    B = gal.B_c(r)
    return v_phi * B + v_phi**2 / r - gal.g_x(r)


def rk4_step(f: Callable, t: float, y: np.ndarray, h: float) -> np.ndarray:
    k1 = f(t, y)
    k2 = f(t + 0.5 * h, y + 0.5 * h * k1)
    k3 = f(t + 0.5 * h, y + 0.5 * h * k2)
    k4 = f(t + h, y + h * k3)
    return y + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)


def integrate_inplane(
    gal: Galaxy,
    r0: float,
    delta: float,
    z0: float = 0.0,
    vz0: float = 0.0,
    t_max: float | None = None,
    r_escape: float | None = None,
    n_steps_per_period: int = 400,
    velocity_ref: str = "marginal",
) -> dict:
    """RK4 integrate until r exceeds escape radius or t_max.

    delta: fractional excess over reference speed.
    velocity_ref: 'marginal' (local g_x equilibrium) or 'v_f' (flat-curve attractor).
    """
    if velocity_ref == "v_f":
        v_ref = gal.v_f
    else:
        v_ref = gal.marginal_v_phi(r0)
    v_phi0 = (1.0 + delta) * v_ref
    y = np.array([r0, 0.0, z0, 0.0, v_phi0, vz0], dtype=float)

    if t_max is None:
        t_max = 5 * gal.tau_dyn(r0)

    if r_escape is None:
        r_escape = r0 + 1.0 * gal.R_d
    tau_vert = 2 * math.pi / math.sqrt(gal.omega_z_sq(r0, v_phi0))
    dt = min(gal.tau_dyn(r0), tau_vert) / n_steps_per_period
    f = lambda t, state: cylindrical_deriv(t, state, gal)

    t = 0.0
    t_escape = None
    z_amp = abs(z0)
    n_steps = int(t_max / dt) + 1

    for _ in range(n_steps):
        z_amp = max(z_amp, abs(y[2]))
        if y[0] >= r_escape and t_escape is None:
            t_escape = t
        if t >= t_max:
            break
        if not np.isfinite(y).all() or y[0] <= 0 or y[0] > 100 * gal.R_d:
            break
        y = rk4_step(f, t, y, dt)
        t += dt

    escaped_flag = t_escape is not None

    return {
        "delta": delta,
        "r0": r0,
        "x": r0 / gal.r_t,
        "v_phi0": v_phi0,
        "v_ref": v_ref,
        "u_vf": v_phi0 / gal.v_f,
        "a_excess0": _radial_excess_accel(gal, r0, v_phi0),
        "escaped": escaped_flag,
        "t_escape": t_escape,
        "t_escape_Gyr": t_escape / Gyr if t_escape else None,
        "t_escape_tau_dyn": t_escape / gal.tau_dyn(r0) if t_escape else None,
        "t_final_Gyr": t / Gyr,
        "r_final": float(y[0]),
        "z_amp_max": z_amp,
        "omega_z": math.sqrt(gal.omega_z_sq(r0, v_phi0)),
        "tau_dyn": gal.tau_dyn(r0),
    }


def vertical_oscillation_period(gal: Galaxy, r: float, v_phi: float) -> float:
    wz = math.sqrt(gal.omega_z_sq(r, v_phi))
    return 2 * math.pi / wz


def adiabatic_thinning_time_halve(gal: Galaxy, z_from: float = 1.0, z_to: float = 2.0) -> float:
    """
    Time to compress scale height by factor z_to (e.g. 2 = halve h)
    under adiabatic ω_L growth from cosmic B_c scaling.

    ω_L(z_cosmo) ∝ (1+z)^(-5/24); from z=1 to z=0, factor (2)^(5/24).
    Adiabatic: h ∝ 1/ω_z, E_z conserved.
    """
    # Fractional ω_L growth from z=1 to now
    f_omega_L = (2.0) ** (5.0 / 24.0)  # ~1.15
    # ω_z² = ω_g² + ω_L²; if ω_L ~ √3 ω_g outside r_t, ω_z increases modestly
    # At r = 2 r_t, ω_L²/ω_g² ~ 3 * v_f/v_f * ... = 3 at nominal
    ratio_L_g = 3.0  # ω_L²/ω_g² ~ 3
    wz_early = math.sqrt(1 + ratio_L_g)
    wz_late = math.sqrt(1 + ratio_L_g * f_omega_L**2)
    # h_late/h_early = wz_early/wz_late
    h_ratio = wz_early / wz_late
    # To halve h need h_late/h_early = 0.5; cosmic growth gives ~0.92 — partial thinning only

    # Time for ω_z to increase enough to halve h: solve h ∝ 1/ω_z(τ)
    # ω_L(τ) = ω_L0 * (1 + (5/24) H τ) approximately from z(τ)
    # Simpler: time from z=1 to z=0 is ~8 Gyr for halving if full factor were 2
    # Actual cosmic compression factor over 8 Gyr:
    compression = wz_late / wz_early
    # time to get additional compression factor z_to via same rate:
    # if compression 1.08 over 8 Gyr, time to halve (~ factor 2 in ω_z) is much longer

    t_cosmic_8Gyr = 8.0 * Gyr
    # d(ln h)/dt = -d(ln ω_z)/dt; for adiabatic ω_L growth rate ~ (5/24) H0
    H_frac = (5.0 / 24.0) * H0  # fractional ω_L growth rate (approx)
    # ω_z ~ ω_L when spring dominates: d(ln ω_z)/dt ~ H_frac
    # halve h: need Δln ω_z = ln 2, time = ln(2)/H_frac
    t_halve = math.log(z_to) / H_frac
    return t_halve


def run_sweep() -> None:
    gal = Galaxy()
    print("=" * 72)
    print("Fiducial galaxy (MW-like)")
    print(f"  M_bary = {gal.M_bary/M_SUN:.1e} M_sun")
    print(f"  r_t    = {gal.r_t/KPC:.2f} kpc")
    print(f"  R_d    = {gal.R_d/KPC:.1f} kpc")
    print(f"  v_f    = {gal.v_f/KM:.1f} km/s")
    print(f"  g_dagger = {G_DAGGER:.3e} m/s^2")
    print(f"  tau_dyn(r_t) = {gal.tau_dyn(gal.r_t)/Gyr*1000:.1f} Myr")
    print()

    # --- 1. Radial stripping: delta over marginal equilibrium at r0 = 10 kpc ---
    r0 = 10.0 * KPC
    v_marg = gal.marginal_v_phi(r0)
    r_esc_kpc = (r0 + gal.R_d) / KPC
    tau_vert = vertical_oscillation_period(gal, r0, v_marg)
    tau_vert_myr = tau_vert / (Gyr * 1e-3)
    print("=" * 72)
    print(f"IN-PLANE STRIPPING (delta vs marginal g_x equilibrium)")
    print(f"  r0 = {r0/KPC:.1f} kpc (x={r0/gal.r_t:.2f} r_t), escape at r = {r_esc_kpc:.1f} kpc")
    print(f"  v_marg = {v_marg/KM:.1f} km/s, v_f = {gal.v_f/KM:.1f} km/s (u_f = v_f/v_marg = {gal.v_f/v_marg:.2f})")
    print(f"  tau_vert = {tau_vert_myr:.0f} Myr = {tau_vert/gal.tau_dyn(r0):.2f} tau_dyn")
    print()
    print(f"{'delta':>8} {'u=v/v_f':>10} {'a_excess':>12} {'escaped?':>10} {'t_esc/Myr':>12} {'t_esc/tau':>10}")
    print("-" * 64)

    strip_results = []
    for delta in [0.0, 0.02, 0.05, 0.08, 0.10, 0.12, 0.15, 0.20, 0.30, 0.50]:
        res = integrate_inplane(gal, r0, delta, z0=0.0, vz0=0.0, velocity_ref="marginal")
        strip_results.append(res)
        t_myr = res["t_escape_Gyr"] * 1000 if res["t_escape_Gyr"] else float("nan")
        t_tau = res["t_escape_tau_dyn"] if res["t_escape_tau_dyn"] else float("nan")
        esc = "yes" if res["escaped"] else "no"
        a_ex = res["a_excess0"]
        print(f"{delta:8.2f} {res['u_vf']:10.2f} {a_ex:12.3e} {esc:>10} {t_myr:12.1f} {t_tau:10.2f}")

    print(f"\n  Vertical oscillation period: {tau_vert_myr:.0f} Myr")

    # --- 1b. Flat-curve reference: u = v_phi / v_f (T17 observable) ---
    print()
    print("=" * 72)
    print("FLAT-CURVE STRIPPING (u = v_phi / v_f at r0 = 10 kpc)")
    print(f"{'u':>8} {'escaped?':>10} {'t_esc/Myr':>12} {'t_esc/tau_v':>12}")
    print("-" * 44)
    strip_u = []
    for u in [0.5, 0.8, 0.9, 0.95, 1.0, 1.02, 1.05, 1.10, 1.15, 1.20, 1.50, 2.0]:
        delta_u = u - 1.0
        res = integrate_inplane(gal, r0, delta_u, z0=0.0, vz0=0.0, velocity_ref="v_f")
        strip_u.append((u, res))
        t_myr = res["t_escape_Gyr"] * 1000 if res["t_escape_Gyr"] else float("nan")
        t_tv = res["t_escape"] / tau_vert if res["t_escape"] else float("nan")
        esc = "yes" if res["escaped"] else "no"
        print(f"{u:8.2f} {esc:>10} {t_myr:12.1f} {t_tv:12.2f}")

    # --- 2. Radial position sweep at delta = 0.10 ---
    delta_fix = 0.10
    print()
    print("=" * 72)
    print(f"RADIAL GATE: delta = {delta_fix}, vary r0/r_t")
    print(f"{'x=r/r_t':>10} {'spring?':>8} {'escaped?':>10} {'t_esc/Myr':>12} {'t_vert/Myr':>12}")
    print("-" * 56)
    for x in [0.5, 0.8, 1.0, 1.2, 1.5, 2.0, 3.0, 5.0]:
        r0x = x * gal.r_t
        vm = gal.marginal_v_phi(r0x)
        res = integrate_inplane(gal, r0x, delta_fix, z0=0.0, velocity_ref="marginal")
        spring = "ON" if r0x > gal.r_t else "OFF"
        t_myr = res["t_escape_Gyr"] * 1000 if res["t_escape_Gyr"] else float("nan")
        tv = vertical_oscillation_period(gal, r0x, vm) / (Gyr * 1e-3)
        esc = "yes" if res["escaped"] else "no"
        print(f"{x:10.2f} {spring:>8} {esc:>10} {t_myr:12.1f} {tv:12.0f}")

    # --- 3. Vertical-only: track z amplitude for marginal orbit (delta=0) ---
    print()
    print("=" * 72)
    print("MARGINAL ORBIT (delta=0): no radial escape; vertical spring at r=10 kpc")
    res0 = integrate_inplane(gal, r0, 0.0, z0=300 * (KPC / 1000), vz0=0.0, t_max=5 * gal.tau_dyn(r0), velocity_ref="marginal")
    h0_pc = 300
    tau_z = vertical_oscillation_period(gal, r0, v_marg) / (Gyr * 1e-3)
    z_final_pc = res0["z_amp_max"] / (KPC / 1000)
    print(f"  r drift over 5 tau_dyn: {res0['r0']/KPC:.2f} -> {res0['r_final']/KPC:.2f} kpc")
    print(f"  z0={h0_pc} pc; tau_vert={tau_z:.0f} Myr; z_amp_max={z_final_pc:.0f} pc")

    # --- 4. Adiabatic cosmic thinning estimate ---
    print()
    print("=" * 72)
    print("COSMIC ADIABATIC THINNING (omega_L growth z=1 -> 0)")
    t_halve = adiabatic_thinning_time_halve(gal)
    f_wl = (2.0) ** (5.0 / 24.0)
    wz_ratio = math.sqrt((1 + 3) / (1 + 3 * f_wl**2))
    print(f"  omega_L growth factor (z=1 to 0): {f_wl:.3f}")
    print(f"  h compression factor over 8 Gyr (adiabatic, r>r_t): {wz_ratio:.3f}")
    print(f"  Time to halve h at d(ln ω_L)/dt ~ (5/24)H0: {t_halve/Gyr:.1f} Gyr")

    # --- 5. Competition summary at r=2 r_t ---
    print()
    print("=" * 72)
    print(f"COMPETITION SUMMARY (r = {r0/KPC:.0f} kpc)")
    print()
    crossover_u = None
    for u, res in strip_u:
        if res["escaped"] and res["t_escape"]:
            if res["t_escape"] < tau_vert and crossover_u is None:
                crossover_u = u
    for i in range(len(strip_u) - 1):
        (ua, a), (ub, b) = strip_u[i], strip_u[i + 1]
        if a["escaped"] and b["escaped"] and a["t_escape"] and b["t_escape"]:
            if a["t_escape"] >= tau_vert and b["t_escape"] < tau_vert:
                crossover_u = (ua + ub) / 2

    print(f"  Crossover (strip faster than tau_vert={tau_vert_myr:.0f} Myr): u ~ {crossover_u if crossover_u else '~1.0'}")
    print(f"  Marginal equilibrium (u~{v_marg/gal.v_f:.2f}): radially stable; T19 thinning over ~{t_halve/Gyr:.0f} Gyr")
    u1 = next(r for u, r in strip_u if abs(u - 1.0) < 0.01)
    if u1["escaped"]:
        print(f"  Flat-curve u=1: stripped in ~{u1['t_escape_Gyr']*1000:.0f} Myr (comparable to tau_vert)")
    print(f"  => T17 selects u>1 on ~40 Myr scale; T19 compresses u~{v_marg/gal.v_f:.1f} survivors on Gyr scale")

    # --- 6. 3D with vertical: delta=0.05, does z compress while migrating? ---
    print()
    print("=" * 72)
    print("COUPLED 3D: delta=0.05, z0=300 pc, r0=10 kpc")
    res3d = integrate_inplane(gal, r0, 0.05, z0=300 * (KPC / 1000), vz0=0.0, t_max=2 * gal.tau_dyn(r0), velocity_ref="marginal")
    print(f"  escaped: {res3d['escaped']}, t_final = {res3d['t_final_Gyr']*1000:.0f} Myr")
    print(f"  r: {res3d['r0']/KPC:.2f} -> {res3d['r_final']/KPC:.2f} kpc")
    print(f"  z_amp_max: {res3d['z_amp_max']/(KPC/1000):.0f} pc")


if __name__ == "__main__":
    run_sweep()
