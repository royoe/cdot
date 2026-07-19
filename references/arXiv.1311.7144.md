# Yagi, Blas, Barausse & Yunes (2014) — "Strong Binary Pulsar Constraints on Lorentz Violation in Gravity"

**Citation:** K. Yagi, D. Blas, E. Barausse, N. Yunes, Phys. Rev. D 89, 084067 (2014); arXiv:1311.7144.
**Source stored:** `arXiv.1311.7144/paper.tex` (+ `.bbl`, many figure PDFs).

## What this is, for cdot-8

The definitive binary-pulsar constraint paper for Einstein-æther and
khronometric gravity — WP6 sub-task 3's primary literature anchor for
adapting pulsar-timing bounds to AeST/cdot-8's aether sector.

## Aspects load-bearing for cdot-8

- **The core physical concept: "sensitivities"** $\sigma_A,\sigma_A'$ —
  strong-field parameters measuring how a neutron star's binding energy
  responds to its motion relative to the æther, computed by numerically
  solving the modified stellar-structure equations for realistic
  equations of state, at $O(v)$ in the star's velocity relative to the
  æther. **This is a genuinely massive numerical-relativity undertaking**
  (solving interior+exterior PDEs, matching, across multiple EOSs) —
  far beyond a derivation exercise; explicitly out of scope to replicate
  from scratch in this program without dedicated tooling.
- Dipole radiation power is proportional to the *difference* of
  sensitivities between the two binary components — the dominant
  beyond-GR effect in generic Einstein-æther/khronometric theory,
  constrained by binary pulsar orbital-decay measurements (PSR
  J1141-6545, J0348+0432, J0737-3039 used in this paper).
- Confirms the same $(c_1,c_2,c_3,c_4)$ basis and the "Foster's
  constraint on $c_\pm$ is only valid in the small-coupling regime" —
  i.e., prior weak-coupling estimates (like the naive æther-only
  $\alpha_1=-4K_B$-type formula WP6 derived) are explicitly flagged, in
  this literature, as approximations that break down once sensitivities
  (strong-field, non-perturbative-in-coupling effects) are included
  properly.
- Notes that PSR J1738+0333 specifically constrains the **strong-field
  PPN preferred-frame parameters** directly — the route Vaglio et al.
  2026 (arXiv:2605.01436) develops further and uses for its own,
  more recent, single-pulsar bound.

## Status in cdot-8's record

Read for its formalism and scope, not yet applied numerically — the
sensitivity calculation itself is flagged as requiring dedicated,
substantial future work (comparable in scope to Foster-Jacobson's own
PPN derivation, but for strong-field neutron-star structure rather than
weak-field PPN). See `arXiv.2605.01436.md` for the discrepancy found
while cross-checking mode-speed formulas between this literature family
and Foster-Jacobson's — not yet resolved.
