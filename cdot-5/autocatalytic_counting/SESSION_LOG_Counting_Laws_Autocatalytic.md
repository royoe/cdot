# SESSION LOG — Counting Laws and the Autocatalytic Derivation

**Topic:** Finding a counting law that fits the DESI-required static-map $D_p(z)$;
fitting candidates to the clean galaxy bins; deriving the selected law from the
connecton network.
**Date:** 2026-07-04 (UTC) — continuation.
**Outcome:** Constructive — selected the exponential/autocatalytic law, corrected
a prior interpretation, produced a conditional derivation and a new falsifiable
claim. One update document + two plots.

---

## Timeline

**Prompt — "have a go at suggesting possible counting rules… fit z<1.3 first,
then decide if we need a high-z component."**
- Re-inverted on clean galaxy bins ($z<1.3$): the $z\sim1.5$ dip vanished; $n(z)$
  became monotonic but $R_\text{now}$-degenerate.
- Flipped to joint closed-form fits of $D_M$+$D_H$. Power-law fit ran away to
  $n\to\infty$; identified this as the logarithmic-distance limit
  $D_p\propto\ln(1+z)$, i.e. exponential counting $c\propto e^{R/L}$.
- Produced plots: desi_static_map.png (AP + required index) and
  desi_counting_laws.png ($D_M$,$D_H$ with log law vs $\Lambda$CDM vs volume).

**Prompt — "suggest possible counting laws."**
- Enumerated candidates with a horizon-ODE + $c(t)$-sanity filter:
  exponential $N\propto e^{R/L}$ (winner); non-uniform rising density (unphysical);
  link-counting $\propto R^6$ and all polynomials (excluded, power law);
  autocatalytic $dN/dR=N/L$ (mechanism behind the winner).
- Verified exponential law preserves finite proper age; gives $H_\text{obs}\propto(1+z)$;
  costs a finite-future $c$-singularity.

**Prompt — "attempt a derivation" (autocatalytic).**
- Checked T14/T12 commitments: connecton conservation (C2); endpoint-only
  interaction, $1/L$ per unit length (C3).
- Resolved the conservation tension: $N$ = local connectivity/degree, not total
  number → autocatalysis is reach acquisition, not creation.
- Derived $dN/dR=N/L$ via transitive reachability (new nodes join iff they link
  to already-connected nodes) → $N\propto e^{R/L}$.
- Key result: pure exponential requires a **fixed** recruitment length $L$;
  $L\propto R$ (scale-free) gives back a power law. So exponential-over-power is
  equivalent to "network recruits over a fixed length, not a fixed fraction."
- Graded honestly: conditional on (1) supercriticality, (2) the endpoint-$1/L$
  heuristic (undrived), (3) mean-field independence. $L$ unpinned ($B\approx33\,r_d$).

**Prompt — "write up."** Produced UPDATE_Autocatalytic_Counting_Law.md.

---

## Key numbers
- Log/exponential law: $B=32.94\,r_d$, $\chi^2=13.2/7$ ($\approx1.9$/dof), clean bins.
- Power laws (clean bins): $n=3\to98$, $n=2\to178$, $n=1\to552$, $n=2/3\to1104$,
  $n=1/2\to1798$. $\Lambda$CDM $\to10.5/6$.
- Worst residual: $D_H(z{=}0.934)$ at $-3.2\sigma$.

## Artifacts produced
- `UPDATE_Autocatalytic_Counting_Law.md` — proposed update for merge.
- `desi_static_map.png`, `desi_counting_laws.png` — figures.
- `SESSION_LOG_Counting_Laws_Autocatalytic.md` — this log.

## Corrections to prior session output
- The "running index $n\sim0.4$–0.7" reading in UPDATE_Static_Map_cz_Inversion is
  superseded: it was a local slope at assumed $R_\text{now}$, not a fit. Direct
  fits show constant low power laws are worse; the data select the exponential
  (growing $n_\text{eff}=R/L$). Prior arithmetic stands; interpretation updated.

## Open next steps
1. Derive $L$ from first principles (re-anchoring mean free path? Compton length?);
   not the horizon (→ scale-free → excluded).
2. Derive the endpoint-$1/L$ recruitment rate from re-anchoring kinetics (T14 gate).
3. Establish network supercriticality (or find what enforces it).
4. High-$z$: refit with QSO/Lyα + full covariance; decide running-$L$ vs second
   component above $z\sim1.3$.
5. Physical reading of the finite-future $c$-singularity at $t_*$.
