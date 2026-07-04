# SESSION LOG — Fork A: BH-Confined Mass as D_p Symmetry Breaker

**Topic:** Testing whether a time-varying black-hole-confined mass fraction
$f_\text{BH}(z)$ can break the horizon-count $D_p(z)$ rigidity exposed by the
BAO Alcock–Paczynski test, without invoking a dark sector.
**Date:** 2026-07-04 (UTC) — continuation of the same day's BAO session.
**Outcome:** Constructive — decisive NEGATIVE result. One update document produced.

---

## Timeline

**2026-07-04T~08:0x UTC — User prompt (Fork context)**
> So, the connecton background that drives cdot cannot be sourced just by the
> horizon. It must evolve significantly as the universe ages. We don't have much
> to play with as long as we do not go the dark matter / dark energy route, but
> we do have PBHs and BHs in general. If connectons do not escape BHs, they can
> be pure sinks. And if the ratio of matter confined to BHs changes with time,
> we do have a candidate for breaking the symmetry.

**Response (critical framing).** Read T14 (connecton properties, sea dynamics,
holographic saturation). Flagged the collision: "BHs are connecton sinks"
contradicts T14's *conserved in number, never destroyed* premise, which several
results lean on (counting-Mach bookkeeping; T12's photon-exclusion). Laid out
three forks: A — sink the *counted matter*, not the connectons (BH-confined
mass excluded from the count, connecton number still conserved); B — genuine
sink, drop conservation, pay the T12/T14 cost; C — source/sink balance replaces
holographic saturation (loses the ρ_bg=(π/6)ρ_crit win). Recommended Fork A.
Defined the make-or-break test: is the observed $f_\text{BH}(z)$ large enough
and the right shape to bend $F_\text{AP}$ onto DESI? Asked which population
should carry $f_\text{BH}(z)$.

**2026-07-04T~08:2x UTC — User prompt (Fork A endorsement)**
> I'm OK with testing Fork A first. Connectons were originally conceived as
> pilot wave entities, and if a connection cannot be made to matter inside a
> black hole, because the advancing wave cannot return, then a connecton cannot
> connect to matter inside a black hole. This Fork might allow us to restore the
> original vision of connectons.

**Response (execution).** Noted the pilot-wave framing strengthens Fork A: the
BH-interior exclusion follows from the definition of a (two-way) connection, not
an added rule. Retrieved observed cosmic BH mass density evolution (Soltán
argument; SMBH mass functions). Computed:

- **Magnitude:** $\rho_\text{SMBH}(0)\sim4.5\times10^5\,M_\odot/\text{Mpc}^3$
  → $f_\text{BH}\sim10^{-5}$ of matter, $\sim7\times10^{-5}$ of baryons.
- **Required swing:** inverting the AP residual (companion update),
  $|\Delta f_\text{BH}|\sim3\times10^{-2}$ near $z\sim1$, with a sign flip by
  $z=2.33$. Linear-response gain $dF/F\approx-(2\text{–}6)\Delta f$.
- **Available swing:** SMBH/AGN $\Delta f\sim10^{-5}$ (shortfall ~2600×);
  + all stellar remnants $\sim3\times10^{-4}$ (shortfall ~90×);
  PBHs large fraction but genesis-formed → $\Delta f\approx0$ (no clock).

**Conclusion.** Fork A fails by 2–4 orders of magnitude. Structural dilemma:
the large-fraction population (PBH) is time-constant; the time-varying
population (accretion) is a negligible fraction. The only escape (a dominant
late-forming BH population) is the dark sector renamed. The $D_H=dD_p/dz$ lock
survives; remaining model-internal routes narrowed to (a) relax the shared-$c$
assumption, or (b) accept the negative structural conclusion.

---

## Artifacts produced
- `UPDATE_ForkA_BH_Confined_Mass_NEGATIVE.md` — proposed update for merge.
- `SESSION_LOG_ForkA_BH_Confined_Mass.md` — this log.

## Data sources
- Soltán-argument SMBH mass density and evolution: arXiv:1604.05333,
  2011ApJ...742...33L, arXiv:1602.05711, arXiv:2411.03184 (z=6 growth).
- Cosmic density normalisations: standard ($\Omega_m=0.31$, $\Omega_b=0.0486$,
  $h=0.7$).

## Open next steps
1. Decide between the two surviving routes (relax shared-$c$ vs accept the
   negative conclusion). Route (a) requires a second field entering the distance
   ruler but not the redshift — assess whether any such field is admissible
   without becoming a dark-sector fluid.
2. If pursued, re-express the CMB first-peak self-similarity (T16 §C) under any
   shared-$c$ relaxation, since that argument also assumes one $c$.
