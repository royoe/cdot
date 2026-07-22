# Skordis & Złośnik (2020) — "A new relativistic theory for Modified Newtonian Dynamics"

**Citation:** C. Skordis & T. Złośnik, Phys. Rev. Lett. 127, 161302 (2021); arXiv:2007.00082.
**Source stored:** `arXiv.2007.00082/newRMONDLett.tex` (+ `.bbl`, figure PDFs).

## What this is, for cdot-8

This is **the AeST founding paper** — the chassis cdot-8 is built on
(Aether-Scalar-Tensor theory). cdot-8 adopts AeST's field content
(tensor $g_{\mu\nu}$ + unit-timelike aether vector $A_\mu$ + scalar
$\phi$) and its quasistatic/GW structure, explicitly *not* its native
cosmology (AeST's own CMB fit relies on the scalar mimicking dark matter
— cdot-8 replaces that with the census/M5-closure mechanism instead).

## Aspects load-bearing for cdot-8

- **Design requirements list**, including **requirement (v): propagate
  tensor-mode gravitational waves at the speed of light** — confirmed
  in-text this session (WP6): "the tensor mode speed equals the speed of
  light in all situations." This is *why* AeST exists as a post-GW170817
  successor to TeVeS ("TeVeS has been shown to be incompatible with the
  LIGO-Virgo observations for any choice of parameters"). Directly
  underwrites WP6's tensor-speed import.
- Confirms GW170817/GRB170817A's observational bound on $c_\text{gw}$
  and that TeVeS fails it — the historical motivation for AeST's
  $\{g_{\mu\nu},A_\mu\}$ field content (as opposed to TeVeS's disformal
  construction).
- States AeST reproduces CMB and matter power spectra (the native-scalar
  dark-matter-mimicking mechanism cdot-8 explicitly discards per its own
  charter — see `cdot-8/proposal/Proposal-cdot8-CovariantCompletion-2026-07-11.md`).
- **The paper's own linear cosmological perturbation system** (Newtonian
  gauge, the effective density contrast $\delta$/velocity divergence
  $\theta$ built from $\chi,\mathcal E_\alpha$, the nonstandard pressure
  contrast $\Pi$, and $\mathcal E_\alpha$'s own evolution equation) — **now
  WP7's primary imported machinery** (`cdot-8/WP7/Update-WP7-PerturbationStructure-2026-07-18.md`).
  Key reported finding: for a wide range of AeST's own (native $K(Q)$)
  parameters, $c_\text{ad}^2,w$ are small enough that $\Pi\to0$ and the
  system reduces to dustlike evolution with the vector field decoupling
  — explicitly a property of AeST's *native* cosmology, not yet checked
  for cdot-8's own census/quadrature-determined $F(Q)$.
- **Verified directly against `newRMONDLett.tex` (secondary advisor,
  WP7 Stage 2, 2026-07-20)**: (i) $\mathcal K(\bar{\mathcal Q})\equiv
  -\tfrac12\mathcal F(0,\bar{\mathcal Q})$ (line 355) — confirms the
  toy/background function is *minus one-half* the full action's
  $\mathcal F$, not $\mathcal F$ itself; (ii) the toy action's
  $1/(8\pi\tilde G)$ prefactor vs. the full action's $1/(16\pi\tilde G)$
  (eqs. `sculpted_FRW_action`/the $S=\int d^4x\sqrt{-g}/(16\pi\tilde
  G)[\ldots]$ action) — the two together are exactly what compensates
  the factor of 2 in (i); (iii) $\mathcal K_2$ is the coefficient of
  $(\bar{\mathcal Q}-\mathcal Q_0)^2$ in $\mathcal K$'s own expansion
  (`Kcal_expansion`), giving $\mathcal K_2=-\tfrac14\mathcal
  F_{QQ}(\mathcal Q_0)$ exactly; (iv) the $\mathcal E_\alpha$ evolution
  equation's coefficient is written as $d\mathcal K/d\mathcal Q$
  (verbatim), i.e. $-\tfrac12\mathcal F_Q$(background) — **not** the
  bulk-current $\mathcal F_Q$ used elsewhere in cdot-8's own field
  equation. This directly confirms (rather than merely
  self-consistency-checks) the distinction WP7 §30's units contract
  relies on. Full equation: $\mathcal K_B(\dot{\mathcal E}_\alpha+H
  \mathcal E_\alpha)=\tfrac{d\mathcal K}{d\mathcal Q}\chi-(2-\mathcal
  K_B)\big[\tfrac{\dot{\bar\phi}}{1+w}\Pi+(H+\dot{\bar\phi})\chi-3c_
  \text{ad}^2H\dot{\bar\phi}\alpha\big]$ (matches
  `Update-WP7-PerturbationStructure-2026-07-18.md` §25's quote exactly,
  parenthesization included).
- Cites an in-preparation companion (Skordis, Ilic & Złośnik) for the
  detailed cosmology and parameter dependence — searched, not found
  published/indexed as of this session; the founding paper's own
  compact system (above) is what WP7 has to build on.
- Establishes AeST has **no disformal metric** — matter couples minimally
  to $g$ alone (a deliberate anti-TeVeS design choice), corrected into
  cdot-8's own WP1 dictionary (K5/M3 wording fix from "$\hat g$" to
  plain "$g$").

## Status in cdot-8's record

Cited/verified across WP0 (initial literature pass), WP1 (dictionary),
WP6 (tensor-speed import, requirement (v) quote), and now WP7 (the
imported linear perturbation system, §25 onward; the $\mathcal K$-vs-
$\mathcal F$ normalization distinction underlying Stage 2's units
contract, verified directly against source, 2026-07-20). No known
dispute; treated as a primary, trusted source throughout.
