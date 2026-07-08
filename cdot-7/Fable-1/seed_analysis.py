#!/usr/bin/env python3
"""
seed_analysis.py — cdot-7, Fable-2 session 2026-07-07, entry 2
Attack on the eps0 seed (Foundation §6 item 2). Companion to
Update-Epsilon0Seed-2026-07-07.md; reproduces every number quoted there.

Contents:
  (a) exact scaling-symmetry verification (matter-era closure), incl. nonlinear regime
  (b) radiation forced-response: adiabatic floor coefficient -m/(2m+3); positive
      switch-on excitation (sign proof that the seed is not post-equality)
  (c) two-component (matter+radiation) background closure integrated through the
      framework's equality (z_eq ~ 1600): confirms radiation-era fixed point
      x_rad = 3/(2*kl) = 2*x_star, R ~ c^{3/2}, and the analytic floor at 10<z<200
  (d) invariants: tuning number |eps_hom(z_eq)| ~ 6.5e-13; floor table
  (e) closure density Omega = 0.134 (factor 2.7 over baryons); N_h ~ 2e80;
      over-excitation bounds on the closure's coupling to horizon-scale dM/M
Joint-fit inputs: kappa*lambda = 0.307, eps0 = -0.0678 (Update-JointFit-2026-07-07).
"""
import numpy as np
from scipy.integrate import solve_ivp

LT=0.307; EPS0=-0.0678   # joint-fit values
xs=3/(4*LT); mus=xs/(1+xs); nus=1/(1+xs); m=3/(2*nus)
xinv=lambda mu: mu/(1-mu)
print(f"x*={xs:.3f} nu*={nus:.4f} m=3/(2nu*)={m:.3f}  1/nu*={1/nus:.3f}")

# (a) SCALING SYMMETRY: trajectories with different eps0 must be c-translates
def eps_of_a(eps0, a_arr):
    r0=1+eps0
    rhs=lambda a,Y:[LT*xinv(min(mus*Y[0]**2/a**1.5,1-1e-13))*Y[0]/a]
    sol=solve_ivp(rhs,[1,min(a_arr)*0.98],[r0],dense_output=True,rtol=1e-11,atol=1e-13)
    return sol.sol(a_arr)[0]/a_arr**0.75-1
a=np.geomspace(0.05,1,60)
e1=eps_of_a(-0.0678,a); e2=eps_of_a(-0.0678*10**(-m*0.3),a)  # sigma=10^0.3
shift=np.interp(np.log(a)-0.3*np.log(10),np.log(a),np.log(-e1))
err=np.max(np.abs(np.log(-e2)-shift)[8:-8])
print(f"(a) scaling symmetry: max |ln eps| mismatch after c-translation = {err:.2e}  (0 = exact)")

# (b) RADIATION FORCING, linear: deps/du = m*eps + (m/2)*eta0*exp(-1.5u)
eta0=6.3e-4
sol=solve_ivp(lambda u,y:[m*y[0]+(m/2)*eta0*np.exp(-1.5*u)],[0,4],[-(m/(2*m+3))*eta0],
              rtol=1e-12,atol=1e-18,dense_output=True)
track=-(m/(2*m+3))*eta0*np.exp(-1.5*np.array([1.,2.,3.]))
num=sol.sol([1.,2.,3.])[0]
print(f"(b) adiabatic coefficient -m/(2m+3) = {-m/(2*m+3):.4f}; track-follow err {np.max(np.abs(num/track-1)):.1e}")
sol0=solve_ivp(lambda u,y:[m*y[0]+(m/2)*eta0*np.exp(-1.5*u)],[0,2],[0.0],rtol=1e-12,atol=1e-18)
pred=(m/(2*m+3))*eta0*(np.exp(m*2)-np.exp(-1.5*2))
print(f"    switch-on from rest after 2 e-folds: {sol0.y[0,-1]:+.3e} vs analytic {pred:+.3e} (POSITIVE)")

# (c) FULL two-component closure, backward through equality
def rhs2(a,Y):
    r=Y[0]
    src=1+eta0*(a**-1.5-1)
    mu=min(mus*r*r/a**1.5*src,1-1e-13)
    return [LT*xinv(mu)*r/a]
a_eq=(1+1/eta0)**(-2/3.)
s2=solve_ivp(rhs2,[1,2e-4],[1+EPS0],dense_output=True,rtol=1e-11,atol=1e-14)
print(f"(c) two-component backward: a_eq={a_eq:.2e} (z_eq={1/eta0:.0f})")
print(f"{'a':>9} {'z':>9} {'x':>7} {'R/a^1.5':>9} {'eps_vs_matterFP':>15}")
for aa in [0.1, 4*a_eq, a_eq, a_eq/4, a_eq/30]:
    r=s2.sol(aa)[0]; src=1+eta0*(aa**-1.5-1)
    x=xinv(min(mus*r*r/aa**1.5*src,1-1e-13))
    print(f"{aa:9.2e} {aa**-1.5-1:9.0f} {x:7.3f} {r/aa**1.5:9.3g} {r/aa**0.75-1:+15.4f}")
print(f"    radiation-era predictions: x_rad=3/(2lt)={3/(2*LT):.3f}, R prop c^(3/2) (R/a^1.5 -> const)")

# (d) invariants
zeq=1/eta0
T=abs(EPS0)*(1+zeq)**(-1/nus)
floor0=(m/(2*m+3))*eta0
print(f"\n(d) tuning invariant |eps(z_eq)| = {T:.1e}")
print(f"    radiation floor: eps_floor(z) = -{floor0:.1e}*(1+z); crossover with hom mode at "
      f"z={(abs(EPS0)/floor0)**(1/(1/nus+1))-1:.2f}")
for zz in [1.44,10,100]:
    print(f"    z={zz:>6}: floor {-floor0*(1+zz):+.2e}   hom {EPS0*(1+zz)**(-1/nus):+.2e}")

# (e) closure density + N_h + over-excitation bounds
H0=2.268e-18; c0=3e8; G=6.674e-11
r0=1+EPS0; mu0=mus*r0**2; x0=xinv(mu0)
Rh0=1.5/(LT*x0)*(c0/H0)          # Rh0*H0/c0 = 1.5/(lt*x0); r0 already in H0 def
rho=3*mu0*c0**2/(4*np.pi*G*Rh0**2)
rhoc=3*H0**2/(8*np.pi*G)
print(f"(e) closure density: Omega_closure = {rho/rhoc:.3f} (vs baryons 0.049 -> factor {rho/rhoc/0.049:.1f})")
print(f"    N_h ~ {4/3*np.pi*Rh0**3*rho/1.67e-27:.1e} nucleon-equivalents")
for zz in [2,10,100,int(zeq)]:
    print(f"    over-excitation bound |g*dM/M|(z={zz}) < {abs(EPS0)*(1+zz)**(-1/nus):.1e}")
import numpy as np
from scipy.integrate import solve_ivp
LT=0.307; xs=3/(4*LT); mus=xs/(1+xs); xinv=lambda mu: mu/(1-mu)

def traj(eps0, a_span):
    rhs=lambda a,Y:[LT*xinv(min(mus*Y[0]**2/a**1.5,1-1e-13))*Y[0]/a]
    return solve_ivp(rhs,a_span,[1+eps0],dense_output=True,rtol=1e-12,atol=1e-14)

# Exact symmetry check: trajectory B with eps0_B = eps_A(1/sigma) must satisfy
# eps_B(a) = eps_A(a/sigma) for ALL a, including the nonlinear regime.
sig=1.5
A=traj(-0.0678,[1,0.05])
epsA=lambda a: A.sol(a)[0]/a**0.75-1
B=traj(epsA(1/sig),[1,0.05])
epsB=lambda a: B.sol(a)[0]/a**0.75-1
aa=np.geomspace(0.08,1.0,40)
lhs=np.array([epsB(x) for x in aa])
rhs=np.array([epsA(x/sig) for x in aa])
print("scaling-symmetry check (nonlinear, exact construction):")
print(f"  max relative mismatch eps_B(a) vs eps_A(a/sigma): {np.max(np.abs(lhs/rhs-1)):.2e}")
# forward continuation into the deeply nonlinear regime
Af=traj(-0.0678,[1,0.05]); Bf_sol=solve_ivp(lambda a,Y:[LT*xinv(min(mus*Y[0]**2/a**1.5,1-1e-13))*Y[0]/a],
        [1,sig],[1+epsA(1/sig)],dense_output=True,rtol=1e-12,atol=1e-14)
eB_at_sig=Bf_sol.sol(sig)[0]/sig**0.75-1
print(f"  eps_B(sigma) = {eB_at_sig:+.5f}  vs eps_A(1) = {-0.0678:+.5f}  (must match)")
