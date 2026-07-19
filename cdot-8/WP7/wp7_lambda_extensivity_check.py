#!/usr/bin/env python3
"""
Checking (before using it) the advisory's "Lambda_M extensive over the
fiducial ball" step (Advisory-WP7-QDefinitionAdjudicated §3): does the
minisuperspace a^3 in Lambda_M = N a^3 F_Q/(16 pi Gtilde) actually track
the SAME volume as N_tot's own (4pi/3) R_h(t)^3 ball (WP2 §1)?

If R_h(t)/a(t) is NOT constant, then a^3 and R_h^3 are two genuinely
different volume conventions, and "Lambda_M density = Lambda_M/(ball
volume)" needs an EXPLICIT convention choice to convert the minisuperspace
a^3 into the ball's own (4pi/3)R_h^3 -- not something that falls out
automatically. This has NOT been checked anywhere in the WP7 record so far.

Method: reuse the exact trajectory machinery already validated in
wp7_structure.py (E(s)=H/H0 from the solved closure ODE), integrate
R_h(s) via its own defining relation dot(R_h) = c(t):
    dR_h/ds = c(t)/H(s),  c(t) = c0 (a/a0)^(2/3) = c0 e^{(2/3)s}
(since s = ln(a/a0), dt = ds/H). Compare d ln R_h/ds to 1 (=d ln a/ds).
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d

# --- exact trajectory machinery from wp7_structure.py (unchanged) ---
KL, X0, H = 0.4355, 1.10, 0.70
T_G0, A_RAD, C0, G_N = 2.7255, 7.565723e-16, 2.99792458e8, 6.67430e-11
K_B_EV = 8.617333e-5
rho_crit = 3*(H*100*1000/3.0857e22)**2/(8*np.pi*G_N)
OM_G = ((A_RAD*T_G0**4)/C0**2)/rho_crit
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
om_nu0 = float(u_nu(0.0))*(A_RAD*T_G0**4)/C0**2/rho_crit; om_cold = OM_CL - om_nu0
def u_hat(z): return om_cold*(1+z)**3 + OM_G*(1+z)**4 + OM_G*u_nu(z)
u00 = float(u_hat(0.0))
def Ssrc(s):
    z = np.exp(-1.5*s)-1
    return (u_hat(z)/u00)*np.exp(5*s)
mu0 = X0/(1+X0)
def x_of(r,s):
    y = min(mu0*r*r*np.exp(-2*s)*float(Ssrc(s)), 1-1e-13); return y/(1-y)
sol = solve_ivp(lambda s,r:[KL*x_of(r[0],s)*r[0]], (0,-11), [1.0],
                rtol=1e-10, atol=1e-13, dense_output=True, max_step=0.005)
s = np.linspace(-10.8, -1e-6, 16000)
r = sol.sol(s)[0]
x = np.array([x_of(ri,si) for ri,si in zip(r,s)])
E2 = (np.exp(-1.5*s)*X0/(x*r))**2
E = np.sqrt(E2)
z_arr = np.exp(-1.5*s)-1

# --- R_h(s): integrate dR_h/ds = c0 e^(2/3 s) / (H0 E(s)) forward from
# the deep-past end of the solved range (past-regularity anchor, same
# convention as every other trajectory integral in this program) ---
# units: R_h in c0/H0 (Hubble-radius-today units)
integrand = np.exp((2.0/3.0)*s) / E
Rh_over_c0H0 = cumulative_trapezoid(integrand, s, initial=0.0)  # R_h(s) - R_h(s_min)

# a(s)/a0 = e^s ; check d ln R_h/ds vs 1 (=d ln a/ds)
dlnRh_ds = np.gradient(np.log(np.maximum(Rh_over_c0H0, 1e-30)), s)

print("=== Does a^3 track R_h^3 (the 'extensive over the ball' assumption)? ===")
print(f"{'z':>10} {'d ln R_h/ds':>14} {'d ln a/ds (=1)':>16} {'R_h/[c0/H0 * e^s]':>20}")
for zt in [1e6, 1e4, 9640.0, 1090.0, 30.0, 1.0, 0.0]:
    i = np.argmin(np.abs(z_arr - zt))
    ratio = Rh_over_c0H0[i] / np.exp(s[i])
    print(f"{zt:>10.0f} {dlnRh_ds[i]:>14.4f} {1.0:>16.1f} {ratio:>20.4e}")

print("""
READING: d ln R_h/ds is NOT identically 1 and R_h/[e^s] is NOT constant
across these epochs -- R_h(t) (the horizon comoving radius, built from
integrating c(t) per WP2's own Rdot_h=c(t) relation) and a(t) (the FRW
scale factor) evolve at genuinely DIFFERENT rates. They agree only
asymptotically in special eras (where E(s) itself is a clean power law
in e^s), not as a general identity.

CONSEQUENCE FOR THE ACCEPTED ADVISORY: Lambda_M = N a^3 F_Q/(16 pi Gtilde)
is built from the MINISUPERSPACE fiducial-cell a^3 (WP3's own
Update-WP3-ActionLevelAttempt, confirmed: a^3 there is the bare FRW
scale-factor cube, d/dt(a^3 F_Q)=0 the free conservation law -- no R_h
anywhere in that derivation). N_tot's own ball, by contrast, is built
directly from R_h(t) (WP2 §1). These are NOT the same volume convention,
and nothing in the accepted advisory (or anywhere upstream) states or
derives the conversion factor between them. The advisory's step
"Lambda_M extensive over the ball, so Lambda_M/(V_ball) = F_Q-density"
silently IDENTIFIES a^3 with (4pi/3)R_h(t)^3 (up to a constant) --
plausible as a MODELING CONVENTION (treat the M5 sector's own minisuper-
space cell as coinciding with the horizon ball, consistent with M5 being
"one constraint per slice" tied to the SAME horizon census throughout),
but it is a CHOICE, not a derived fact -- and the two volumes' differing
growth RATES (checked above) mean the choice is not even asymptotically
harmless in general, only in eras where R_h/a happens to be slowly
varying.
""")
