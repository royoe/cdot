# Advisory — WP6 Checkpoint Verified: the Cassini Table and the PPN Degeneracy Both Confirmed to the Digit; Two Structural Additions — the Screening Completion Is Not Derivable from the Quadrature Even in Principle, and Requirement (v) and the PPN Singularity Are One Design Fact Seen Twice (for `cdot-8/WP6/`)

*2026-07-18. Advisory in response to §4–§6 of
`Update-WP6-TensorSpeedStructure-2026-07-18.md`. Verification in
`wp6_verification.py`. All findings inherit Gate 1(b)'s
provisional-structural-failure caveat on the cosmological background.
Verdict up front: **both sections are accepted with independent
verification — §4's three-row Saturn table reproduces exactly (2825×,
2.48×10⁻³, ~0), including the constant-anomaly asymptote that makes the
naked-simple kill clean, and §5's degeneracy is confirmed symbolically
($\alpha_1=-4c_1$ finite, $c_{123}=0$ identically, $\alpha_2$ divergent).
Sub-task 1 closes as scoped; sub-task 2's staging is endorsed. Two
additions change how the remaining work should be framed: the worker's
flagged "further derivation" of the screening completion from cdot-8's
own machinery should not be attempted, because it is impossible in
principle — the background quadrature has zero support on the
$\mathcal Y$-sector — which sharpens what the program's
"zero-adjustable-elements" claim does and does not cover; and the PPN
singularity is not merely explained by AeST's design, it is the same
fact as requirement (v), which reframes the $\alpha_1/\alpha_2$
derivation's starting point.***

---

## 1. §4 accepted — verified, with the scope statement it earns

The table verifies to the digit, and the analytic structure behind the
first row is confirmed: for the naked simple function,
$u=y+1-1/y+\dots$, so the anomaly $a_0(u-y)\to a_0$ — a *constant*
$1.13\times10^{-10}$ m/s² at Saturn regardless of $g_\text{bar}$, which
is exactly why T22's exclusion is clean rather than marginal. The
model-independent conclusion (any fast-tail completion passes by 2+
orders of magnitude) stands, and the worker's refusal to invent a
$(\lambda_s,p)$ ansatz to extract a fake precision bound is the right
call. Two additions:

- **Do not attempt the flagged "further derivation" — it cannot exist.**
  The worker's §4 closes by flagging, as separate future work, deriving
  the actual screening completion "from cdot-8's own quadrature/M5
  machinery, the way $F(Q)$ was derived." That derivation is impossible
  in principle, not merely hard: the quadrature is built against the
  homogeneous background, where $\mathcal Y\equiv0$ identically — the
  invoice has *zero support* on the $\mathcal Y$-sector, at every order.
  cdot-8's background machinery can never determine the high-gradient
  completion, only the $Q$-sector. **Scope statement for the charter,
  stated now so the headline claim stays honest: "zero adjustable
  elements" is a $Q$-sector claim. The $\mathcal Y$-sector — MOND
  interpolation shape and its high-gradient completion — remains
  AeST-inherited functional freedom, constrained by data (galaxy-regime
  fits from below, Cassini-class bounds from above), exactly as in the
  parent theory.** This is a limitation shared with every relativistic
  MOND completion, not a cdot-8 defect; but the program should say it
  itself before a referee does.
- **The two roles of $\mu$ decouple in cdot-8 — refining this morning's
  exposure flag.** In cdot-7, one function served both the cosmological
  closure and the galaxy quasistatic limit (the AQUAL economy). In
  cdot-8's chassis these are *formally distinct objects*: the closure's
  $\mu_\text{simple}$ enters through the fitted $E(z)$ history → the
  invoice → $F(Q)$ (the $Q$-sector), while the galaxy/solar-system
  interpolation is the $\mathcal Y$-sector. A Cassini-safe
  $\mathcal Y$-sector completion therefore does **not** by itself force
  the 24–41% background refit — that exposure bites only if the program
  retains the cdot-7-style single-$\mu$ identification. The
  magnitude-coincidence flag for the post-WP7 revisit stands, restated
  conditionally: *if* the unification (one $\mu$, the $a_0=\lambda\dot c$
  economy) is kept as a principle, the Cassini-forced swap propagates to
  the closure at the tens-of-percent scale and is first in the options
  queue; if the sectors are allowed to differ, the swap is free locally
  and the $\theta_*$ candidate list loses its externally-forced member.
  That choice — economy versus freedom — is itself Gate-1-revisit
  material, and should be put to the author there, not decided by
  default.

## 2. §5 accepted — verified symbolically, and unified

The mapping ($c_2=c_4=0$, $c_3=-c_1$), the finite $\alpha_1=-4c_1$, and
the $\alpha_2$ divergence at $c_{123}=0$ all confirm
(`wp6_verification.py`), and $\alpha_1=-4c_1$ matches the known
post-GW170817 æ-theory form $-4c_{14}$ at $c_4=0$ — a consistency check
with the wider literature the worker didn't claim but gets for free. The
addition that reframes the remaining derivation:

**The same Maxwell-only kinetic choice produces $c_{13}=0$ — the exact
tensor-speed-equals-$c$ condition — and $c_{123}=0$ — the vanished aether
spin-0 mode that blows up the PPN formula.** Requirement (v) and the PPN
singularity are one design fact seen from two sides: AeST bought
$c_\text{gw}=c_\gamma$ *exactly and in all situations* by stripping the
aether of every non-Maxwell structure, and the price is that the aether
carries no scalar dynamics — which is why $\phi$ exists, why the
$Q_0$-coupling exists, and why the post-GW170817 æ-theory viable region
(which keeps $c_2\neq0$ to retain a healthy spin-0 mode) never contains
AeST's corner. Consequences for the derivation:

- **$\gamma=1$ is already in hand** — the $\Psi=\Phi$ import (WP5 §1) is
  precisely the statement that the static PPN sector is GR's; the
  remaining work is genuinely only the preferred-frame sector.
- **The staged path**: (i) boost the established quasistatic system
  (Mistele Eq. 1 with the screened scalar) to a source moving at $w$
  relative to the aether frame at 1PN — the $\alpha_1$-generating
  vector-potential sector; (ii) the $\alpha_2$-generating anisotropic
  terms next; (iii) the condensate is suppressed at Gpc$^{-1}$
  (WP5's $\mu_\text{eff}$), so the calculation carries the
  $\chi=\varphi+Q_0\alpha$ mixing but not condensate contamination.
  Pre-registered expectation, stated loosely on purpose: $\alpha_1$ of
  the $-4c_{14}$ form *completed* by $\phi$-sector terms in $(K_B,Q_0)$;
  $\alpha_2$ finite once the outsourced scalar is included, since the
  full theory's spectrum is healthy (SZ stability paper) and the
  divergence is the restricted formula's, not the theory's.
- The worker's symmetric-stakes framing (false pass and false kill both
  unacceptable; stage the work) is endorsed as written — this is WP3-class
  derivation and should be checkpointed like WP3 was.

## 3. Housekeeping

KATRIN preamble synced ✓ (§6 now carries the registered content).
Sub-task 3 remains gated on sub-task 2, correctly. Still owed, unchanged:
Brouwer version statement, WP4b file sighting, consolidation batch (now
also carrying: the $\mathcal Y$-sector scope statement of §1 — which
touches charter language and should reach the author's eyes explicitly —
the single-$\mu$ economy-versus-freedom question for the Gate-1 revisit,
and the one-fact-two-faces PPN note), log repairs.

## Companion

- `wp6_verification.py` — the three-row Saturn reproduction, the
  constant-anomaly asymptote, the symbolic PPN check, the
  $c_{13}=c_{123}=0$ unification.
- This advisory: proposed location
  `cdot-8/WP6/Advisory-WP6-CheckpointVerified-2026-07-18.md`.
