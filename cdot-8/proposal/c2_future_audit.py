#!/usr/bin/env python3
"""
c2_future_audit.py — 2026-07-13. Step-5 escalation: independent reproduction of
the worker's (C2, Lambda_M) audit + the FORWARD (future) test of candidate 1.

Key structural fact exploited: with iteration off, D(s; C2) = D_part(s) + C2*D_ker(s)
EXACTLY (the whole chain F -> F_Q -> pi -> P -> D is linear in F, and F is linear
in C2). So compute the two channels separately, then:
  - reproduce the worker's z=0 swing table (linear, un-iterated; iteration is a
    ~7% correction at z=0 per the confirmed round, irrelevant to the structure);
  - integrate the closure FORWARD to s=+3 (deep-MOND future, x -> ~0.02);
  - measure the forward growth exponents of D_part/E^2 and D_ker/E^2
    (asymptotic prediction: 1 and 5/6);
  - compute C2*(s) = -D_part(s)/D_ker(s): convergence to a constant means a
    unique C2 cancels the leading forward divergence; drift means none does;
  - evaluate the residual growth of D(s; C2*) to see what survives cancellation.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d
from scipy.special import zeta

KL, X0, H = 0.4355, 1.10, 0.70
T_G0, A_RAD, C0, G_N = 2.7255, 7.565723e-16, 2.99792458e8, 6.67430e-11
K_B_EV = 8.617333e-5
rho_crit = 3*(H*100*1000/3.0857e22)**2/(8*np.pi*G_N)
u_g0 = A_RAD*T_G0**4; OM_G = (u_g0/C0**2)/rho_crit
T_NU0 = (4/11)**(1/3)*T_G0; M_NU = 1.374/3; OM_CL = 0.074
F0 = 7*np.pi**4/120
ag = np.concatenate([[0], np.logspace(-3,7,400)])
Fg = np.array([quad(lambda x,A=A: x*x*np.sqrt(x*x+A*A)/(np.exp(x)+1),0,60,limit=300)[0] for A in ag])
Fi = interp1d(np.log10(ag[1:]), np.log10(Fg[1:]), kind='cubic')
def Ffd(A):
    A = np.asarray(A,float); return np.where(A<1e-3, F0, 10**Fi(np.log10(np.maximum(A,1e-3))))
REL = (7/8)*(4/11)**(4/3)
def u_nu(z):
    A = M_NU/(K_B_EV*T_NU0*(1+z)); return 3*REL*(1+z)**4*Ffd(A)/F0
om_nu0 = float(u_nu(0.0))*u_g0/C0**2/rho_crit; om_cold = OM_CL - om_nu0
def u_hat(z): return om_cold*(1+z)**3 + OM_G*(1+z)**4 + OM_G*u_nu(z)
u00 = float(u_hat(0.0))
def Ssrc(s):
    z = max(np.exp(-1.5*s)-1, -0.999999)
    return (u_hat(z)/u00)*np.exp(5*s) if z > -1 else np.nan
mu0 = X0/(1+X0)
def x_of(r,s):
    y = min(mu0*r*r*np.exp(-2*s)*float(Ssrc(s)), 1-1e-13); return y/(1-y)

# integrate BOTH directions
solb = solve_ivp(lambda s,r:[KL*x_of(r[0],s)*r[0]], (0,-9.6), [1.0],
                 rtol=1e-10, atol=1e-13, dense_output=True, max_step=0.005)
solf = solve_ivp(lambda s,r:[KL*x_of(r[0],s)*r[0]], (0, 3.2), [1.0],
                 rtol=1e-10, atol=1e-13, dense_output=True, max_step=0.005)
sb = np.linspace(-9.4, -1e-9, 9000)
sf = np.linspace(1e-9, 3.0, 3000)
s = np.concatenate([sb, sf])
r = np.concatenate([solb.sol(sb)[0], solf.sol(sf)[0]])
x = np.array([x_of(ri,si) for ri,si in zip(r,s)])
a = np.exp(1.5*s); z = 1/a-1
E = np.exp(-1.5*s)*X0/(x*r); E2 = E*E
u = np.array([float(u_hat(max(zi,-0.9999999))) for zi in z])
Om_s = E2 - u
N = np.exp(2.5*s); Q = 1/N
lnS = np.log([float(Ssrc(si)) for si in s])
bar_g = np.gradient(lnS, s) + 3*KL*x - 0.5
sdot = (2/3)*N*E
print(f"forward trajectory: x(s=3) = {x[-1]:.4f}, E(s=3) = {E[-1]:.4f}, bar_g(s=3) = {bar_g[-1]:.2e}")

# quadrature, particular (C2=0, anchored s=0) and kernel channels
integ = Q**(-2/3)*Om_s
i0 = len(sb)  # index of s=0+
I = cumulative_trapezoid(integ, s, initial=0.0); I = I - I[i0]   # int_0^s
F_part = Q**(2/3)*(-5.0*I)
F_ker  = Q**(2/3)               # C2=1 channel
def D_of(F):
    F_Q = -0.4*np.exp(2.5*s)*np.gradient(F, s)
    src_pi = 2.5*a**3*F_Q/(bar_g*sdot)
    tp = cumulative_trapezoid(src_pi, s, initial=0.0)
    src_P = tp*N*(KL*x)**2*sdot
    P = np.exp(s)*cumulative_trapezoid(src_P*np.exp(-s), s, initial=0.0)
    return tp*KL*x*N*E/(9*a**3) + P/(6*a**3)
Dp, Dk = D_of(F_part), D_of(F_ker)

# worker's swing table (linear, un-iterated)
print("\nworker's z=0 swing, reproduced (linear, iteration off; worker's были iterated):")
for C2 in (0, 10, 50, -30):
    print(f"  C2={C2:>4}: D/E^2(z=0) = {(Dp[i0]+C2*Dk[i0])/E2[i0]:+.4f}")

# forward growth exponents
mfw = s > 2.0
ep = np.polyfit(s[mfw], np.log(np.abs(Dp[mfw]/E2[mfw])), 1)[0]
ek = np.polyfit(s[mfw], np.log(np.abs(Dk[mfw]/E2[mfw])), 1)[0]
print(f"\nforward growth: d ln|D_part/E^2|/ds = {ep:.3f} (asymptotic prediction 1)")
print(f"                d ln|D_ker /E^2|/ds = {ek:.3f} (asymptotic prediction 5/6 = 0.833)")

# does a unique C2 cancel the leading divergence?
C2_star = -Dp/Dk
print("\nC2*(s) = -D_part/D_ker along the future:")
for sq in (0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0):
    i = np.argmin(abs(s-sq))
    print(f"  s={sq:.1f}: C2* = {C2_star[i]:+.4f}")
# residual with the best late-time C2
C2b = C2_star[-1]
Dres = Dp + C2b*Dk
er = np.polyfit(s[mfw], np.log(np.maximum(np.abs(Dres[mfw]/E2[mfw]),1e-30)), 1)[0]
print(f"\nresidual with C2 = C2*(s=3) = {C2b:.4f}:")
for sq in (0.0, 1.0, 2.0, 3.0):
    i = np.argmin(abs(s-sq))
    print(f"  s={sq:.1f}: D_res/E^2 = {Dres[i]/E2[i]:+.3e}")
print(f"  residual forward slope: {er:.3f}")
print(f"  and at z=0: D(C2*)/E^2 = {(Dp[i0]+C2b*Dk[i0])/E2[i0]:+.4f}")
