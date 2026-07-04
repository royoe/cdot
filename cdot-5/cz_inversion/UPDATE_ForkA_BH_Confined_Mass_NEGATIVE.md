# UPDATE — Fork A Test: BH-Confined Mass as the D_p Symmetry Breaker (NEGATIVE)

*Status: proposed update, for cross-check and merge. Session 2026-07-04 (cont.).*
*Targets: T14 (connecton conservation premise), T12 (premise-2 fork), T16 (PBH program), Core §4/§4a.*
*Depends on: UPDATE_BAO_Alcock-Paczynski_Shape_Test.md (same session).*

---

## Summary

Motivated by the BAO AP failure (the $D_H=dD_p/dz$ lock), we tested whether a
**time-varying black-hole-confined mass fraction** $f_\text{BH}(z)$ could break
the rigidity of the horizon-count $D_p(z)$ **without** invoking a dark-energy or
dark-matter fluid. The proposal (Fork A): connectons cannot connect to matter
inside a black-hole horizon (the pilot-wave "advancing + returning" handshake
cannot complete across the horizon), so BH-confined mass drops out of the count
that sets $c$, while total connecton number remains conserved (preserving T14's
conservation premise). Effective premise 2 becomes
$$c \propto M_\text{count}(R) = M_u(R)\,[1 - f_\text{BH}] \propto R^3\,[1-f_\text{BH}(z)].$$

**Result: the mechanism fails by 2–4 orders of magnitude.** It is a physical
dilemma, not a tuning miss, and it rules out a class of "BH-sink" fixes.

---

## The conceptual merit (why it was worth testing)

- **Principled exclusion.** In the pilot-wave reading of connectons, a
  connection is a two-way relation. A BH interior is exactly where the return
  leg cannot propagate out, so BH-confined matter is excluded from the count by
  the *definition* of a connection — not by an added rule. This is the cleanest
  available symmetry breaker consistent with the relational principle.
- **Preserves T14 conservation.** Fork A sinks the *sources* (counted mass),
  not the connectons themselves; total connecton number is still globally
  conserved. It therefore does **not** collide with T14's "conserved in number"
  premise or T12's photon-exclusion argument. (Forks B and C, which make BHs
  genuine connecton sinks, do collide and were not pursued.)
- **Uses only known physics.** No new fluid; $f_\text{BH}(z)$ is an observable.

---

## The quantitative test

Redshift is unchanged ($1+z=(c_0/c_\text{emit})^2$; the count-normalisation
constant cancels), giving
$$\left(\frac{R_\text{emit}}{R_\text{now}}\right)^3
= (1+z)^{-1/2}\,\frac{1-f_\text{BH}(0)}{1-f_\text{BH}(z)},$$
and $D_p=R_\text{now}-R_\text{emit}$, $D_H=dD_p/dz$, $F_\text{AP}=D_p/D_H$
(parameter-free, as established in the companion update).

**Required swing (inverting the AP residual).** The baseline (volume-law,
$f_\text{BH}=0$) over-predicts $F_\text{AP}$ by up to $9.3\%$ near $z\approx0.93$
and under-predicts by $\sim1.8\%$ at $z=2.33$ (an S-shaped residual). The
linear response is $dF_\text{AP}/F_\text{AP}\approx -(2\text{–}6)\times
\Delta(f_e-f_0)$. Removing the residual therefore requires
$$|\Delta f_\text{BH}| \sim 3\times10^{-2}\ \text{(of the counted mass), concentrated near }z\sim1,\text{ with a sign flip by }z\sim2.3.$$

**Available swing (observed BH budget).**

| Population | $f_\text{BH}$ (of matter) | $\Delta f_\text{BH}$ over $z=2.3\to0$ | shortfall vs required |
|---|---:|---:|---:|
| SMBH/AGN (Soltán; $\rho_\text{BH}(0)\!\sim\!4.5\times10^5\,M_\odot/\text{Mpc}^3$) | $\sim1\times10^{-5}$ | $\sim1\times10^{-5}$ | $\sim2600\times$ |
| + all stellar-remnant BHs (maximal) | $\sim\text{few}\times10^{-4}$ | $\sim3\times10^{-4}$ | $\sim90\times$ |
| PBHs ($\Omega_\text{PBH}\sim0.25$) | $\sim0.8$ | $\approx0$ (genesis-formed) | no time variation |

(Cosmic densities used: $\rho_\text{crit}(0)=1.36\times10^{11}\,M_\odot/\text{Mpc}^3$,
$\rho_m=4.2\times10^{10}$, $\rho_b=6.6\times10^{9}$.)

---

## Why it fails — a structural dilemma

The two requirements are carried by different populations that cannot both
deliver:

1. **Large confined fraction** (needed to move the $c$-sourcing integral)
   → PBHs. But PBHs form at genesis, so they are BH-confined at *all* $z$:
   their $f_\text{BH}$ is nearly constant, and a constant $f_\text{BH}$ merely
   renormalises $k$ in $c=kR^3$ — it cannot bend the AP **shape**.
2. **Large time-variation** over $z<2.3$ → accretion-built SMBHs. But these are
   a $\sim10^{-5}$ sliver of the counted mass.

The large-fraction population is time-constant; the time-varying population is a
negligible fraction. The only escape is a hidden, dominant, **late-forming** BH
population — which is the dark sector by another name, and is excluded by the
project's own no-dark-sector constraint (and by BH-abundance observations).

---

## Consequences for the model

- **Fork A is closed** as a route to break the $D_p$ rigidity using the real BH
  budget. Record in T12 (premise-2 fork) and T16 (PBH program): PBHs cannot
  double as the BAO symmetry breaker, because their genesis origin makes
  $f_\text{BH}$ time-constant.
- **The $D_H=dD_p/dz$ lock survives intact.** Any surviving fix must introduce a
  degree of freedom that (i) varies at the few-percent level over $z<2.3$ and
  (ii) enters the distance ruler *independently* of the horizon-growth integral.
  BH-confined mass supplies neither at the needed magnitude.
- **Narrowed options.** Two model-internal routes remain:
  (a) **relax the shared-$c$ assumption** — the lock arises because both
  $D_p=\int c\,dt$ and $1+z=(c_0/c)^2$ use the *same* $c(t)$; a second field
  entering one but not the other would break it (but this is precisely the
  extra degree of freedom the model has resisted);
  (b) **accept the structural conclusion** that a single-$c(t)$ static
  cosmology cannot match the BAO AP shape without a dark sector — a strong
  negative result about the program as a whole.

---

## Caveats

- $f_\text{BH}$ magnitudes are order-of-magnitude (Soltán $\rho_\text{BH}(0)$,
  standard radiative efficiency $\epsilon\sim0.1$); a factor-few revision does
  not close a $\sim90$–$2600\times$ gap.
- Linear-response sensitivity was used to size the required $\Delta f_\text{BH}$;
  the conclusion is a magnitude statement and is insensitive to the exact shape
  of $f_\text{BH}(z)$ given the budget ceiling.
- The negative result is specific to *BH-confined mass* as the clock. It does
  not by itself refute Fork B/C (genuine connecton sinks) — but those carry the
  T14/T12 conservation costs flagged in-session and were not tested.
