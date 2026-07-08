import numpy as np

# --- constants ---
G, c0 = 6.674e-11, 2.9979e8
H0_70 = 70*1000/3.0857e22          # s^-1
a0_emp = 1.2e-10                   # m/s^2 (SPARC)
Obh2   = 0.0224
rho_b  = Obh2 * 1.8795e-26         # kg/m^3, H0-independent
kl     = 0.307                     # joint-fit kappa*lambda
lam_a0 = 1.5*a0_emp/(c0*H0_70)     # a0-anchored lambda (exact identity)
print(f"lambda (a0-anchored, H0=70) = {lam_a0:.4f}   kappa = {kl/lam_a0:.3f}")

xs  = 3/(4*kl); mus = xs/(1+xs)
def state(eps0):
    mu0 = mus*(1+eps0)**2
    x0  = mu0/(1-mu0)
    return x0, mu0

# Omega-form (needs lambda + H0 conventions) and F-form (H0-free)
def Omega(eps0, lam, kap):        # = (8/9) kap lam^2 x0^2 mu0
    x0,mu0 = state(eps0);  return (8/9)*kap*lam*lam*x0*x0*mu0
def F(eps0, kap, a0=a0_emp):      # rho0/rho_b = (3/4pi) kap mu0 x0^2 a0^2/(G c^2 rho_b)
    x0,mu0 = state(eps0);  return (3/(4*np.pi))*kap*mu0*x0*x0*a0*a0/(G*c0*c0*rho_b)

print("\nReconciliation of the three published numbers:")
print(f"  seed analysis   0.134 : kappa=1 convention (lam=kl), eps0=-0.0678 -> "
      f"{Omega(-0.0678, kl, 1.0):.4f}")
print(f"  consolidator    0.115 : a0-anchored lam, eps0=-0.0678            -> "
      f"{Omega(-0.0678, lam_a0, kl/lam_a0):.4f}")
print(f"  this session    0.104 : a0-anchored lam, proxy eps0=-0.0752      -> "
      f"{Omega(-0.0752, lam_a0, kl/lam_a0):.4f}")

print("\nH0-free F-form (rho_closure/rho_baryon), a0-anchored:")
for e0,tag in [(-0.0678,'joint-fit central'),(-0.073,'seed-implied'),(-0.0752,'proxy')]:
    print(f"  eps0={e0:+.4f} ({tag:>17}): F = {F(e0, kl/lam_a0):.2f}")

print("\nSensitivity of F (joint-fit eps0):")
Fc = F(-0.0678, kl/lam_a0)
print(f"  a0 +/-20% (F ~ a0 linearly, since kappa ~ 1/a0 at fixed kl): "
      f"{F(-0.0678, kl/(1.5*0.94e-10/(c0*H0_70)), 0.94e-10):.2f} .. "
      f"{F(-0.0678, kl/(1.5*1.46e-10/(c0*H0_70)), 1.46e-10):.2f}")
print(f"  eps0 variants: +/-{100*(Fc-F(-0.0752,kl/lam_a0))/Fc/2:.0f}% -> minor")
# neutrino escape line
print(f"\n  Escape needs F <= (Ob+Onu_max)/Ob = {(0.049+0.0296)/0.049:.2f}"
      f"   (KATRIN-limit Sum m_nu = 1.35 eV)")
