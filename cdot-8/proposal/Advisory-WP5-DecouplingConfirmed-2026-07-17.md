# Advisory — WP5 First Installment: The Decoupling Argument Is Confirmed, With Its Mechanism Made Explicit; the Clock Pinned; the Prediction Backbone Delivered; and the $m_\times$ Question Given Its Expected Answer to Test (for `cdot-8/WP5/`)

*2026-07-17. Advisory in response to
`cdot-8/WP5/Update-WP5-WeakFieldStructure-2026-07-17.md`. Companion
numerics in `wp5_decoupling_check.py`. Verdict up front: **the checkpoint
was well taken, and the load-bearing decoupling argument is confirmed — and
strengthened: the mechanism is not merely "the census integral doesn't
notice local rearrangement" but the sharper variational statement that the
M5 multiplier's force on the local field is spatially uniform at leading
order, hence entirely absorbed into the already-verified background
equation, leaving $\delta Q(\mathbf x,t)$ governed by unmodified AeST
quasistatics. This is the same structure as unimodular gravity's global
volume constraint, a known-safe precedent. Three additions before the
second installment: the clock/units statement for $a_0(z)$ pinned via the
charter identity (this program's history demands it be explicit); the
prediction backbone computed — $\hat a_0(z_\text{lens})/\hat a_0(0)=E(z)$,
a 24% enhancement at $z=0.35$ and 36% at $z=0.5$, squarely in stacked-
survey territory; and the deferred $m_\times$ question given the structural
answer cdot-8's own charter suggests, framed as the next installment's
first falsifiable task rather than assumed.***

---

## 1. The decoupling argument — confirmed, with the mechanism named

The worker's §2 rests the argument on $\mathcal N_\text{tot}$'s
insensitivity to local rearrangement. Correct, but it is half of the
variational story, and the other half is what makes the conclusion airtight
rather than plausible:

Vary $S_{M5}=\int dt\,\Lambda_M[\bar Q-q(\mathcal N_\text{tot})]$ with
respect to the *local* khronon $\phi(\mathbf x,t)$. Whatever spatial
functional defines $\bar Q$ (volume average, monopole mode — the choices
differ only at second order in perturbations), $\delta\bar Q/\delta\phi
(\mathbf x)$ spreads the multiplier's force with weight $1/V_\text{horizon}$
per point. Meanwhile $\Lambda_M$ is extensive ($\propto Na^3F_Q$, the
fiducial-volume factor of the minisuperspace construction). The product is
therefore *finite but spatially uniform at leading order*: it contributes
exactly the homogeneous $\phi$-equation term that WP3 verified — nothing
else. The census side is the same story: $\delta\mathcal N_\text{tot}$
under moving a galaxy's mass within the horizon vanishes at first order
(binding-energy corrections are second order in $\Phi$ and mass-fraction
suppressed). **So M5 constrains the zero mode and only the zero mode; the
local perturbation sector is AeST's, evaluated at the background's
$a_0(t)$.** Known-precedent note for the record: this is structurally
unimodular gravity — a global Lagrange constraint that turns a would-be
local coupling into a single integration-constant-like background
relation, leaving local field equations untouched. The worker's named
assumption (that no future need arises for $\mathcal N$ as a genuinely
local density) is the right caveat and stays flagged; nothing in
WP1–WP4b needs it.

Two small physical caveats to carry, neither threatening: (i) adiabatic
drift — $a_0(t)$ varies on $1/H$, galaxy outskirts orbit on $\sim0.1/H$,
so quasistatic solutions carry percent-level adiabatic corrections
(standard in evolving-$a_0$ literature; negligible against survey
precision); (ii) the homogeneous khronon gradient the local solution rides
on is AeST's own setup — no new structure.

## 2. The clock, pinned — this program's history requires it in writing

§3's "$a_0(z)=\lambda\dot c(z)$ read off the closure" is correct but
clock-ambiguous as written, and this session has produced five errors from
exactly that ambiguity class. The unambiguous statement is the charter
identity, exact on any trajectory:
$$\hat a_0(z)=\tfrac23\,\lambda\,c_0\,H_{\hat\tau}(z)$$
— local (atomic) units at the lens, matter-frame Hubble rate, no
convention freedom. Anchor verified inline
(`wp5_decoupling_check.py`): $\tfrac23\lambda c_0H_0=1.386\times10^{-10}$
m/s² against cdot-7's fitted $1.39\times10^{-10}$ — the absolute-anchor
rule from the adjudication round, applied on day one of WP5.

And the standing epistemic note travels with it: by this identity, the
lensing-RAR-by-redshift curve is *the same one prediction* as the
dynamical $\hat a_0(z)$ fit and the SN diagram (the evidence-collapse
finding from the charter round). **WP5's value is not a new parameter or a
new curve — it is the same $\hat a_0\propto H_{\hat\tau}$ law tested in an
independent observable (lensing) and an independent regime (stacked
low-acceleration outskirts).** That is worth stating in the WP5 write-up
exactly so, because it is both the honest deflation and the genuine
strength: a cross-probe consistency test with zero freedom.

## 3. The prediction backbone

$\hat a_0(z_\text{lens})/\hat a_0(0)=E(z_\text{lens})$ on the established
trajectory:

| $z_\text{lens}$ | $E(z)$ | survey context |
|---:|---:|---|
| 0.10 | 1.059 | SDSS/local stacks |
| 0.25 | 1.161 | KiDS bright lenses |
| 0.35 | 1.237 | KiDS/DES typical |
| 0.50 | 1.362 | DES deep lenses |
| 0.75 | 1.597 | HSC deep |
| 1.00 | 1.861 | future/LSST |

A 24% $a_0$ enhancement at $z=0.35$ and 36% at $z=0.5$ — the observable is
$a_0$ *tracking $E(z)$ at all* versus the constant-$a_0$ null, since
$\Lambda$CDM-like and cdot-8 $E(z)$ nearly coincide at these redshifts by
construction of the fit. In RAR terms: the low-acceleration branch
($g\propto\sqrt{g_Na_0}$) shifts by $\sqrt{E}$ — 11% at $z=0.35$, 17% at
$z=0.5$ — against stacked-survey precision that is now at the
several-percent level. **This is a live, near-term falsifiable prediction,
and it cuts both ways: current stacked lensing RAR analyses that find
redshift-independent $a_0$ would pressure it directly.** The second
installment should confront exactly that literature.

## 4. The $m_\times$ question — the structural answer to test, not assume

The deferred two-quasistatic-limit question (Mistele 2305.07742) and the
known AeST weak-lensing tension (Mistele, McGaugh & Hossenfelder 2023:
AeST's low-acceleration departure from MOND vs data showing MOND-like
behavior persisting) have a cdot-8-specific angle the worker's §4 doesn't
yet name: **AeST's $\mu$-function mass term $m_\times$ — the source of both
the two-limit ambiguity and the lensing-tension departure — belongs to the
dust-mimicking scalar sector that cdot-8's charter explicitly discards**
(the census/M5 closure replaces it). If, on inspection of cdot-8's action
as actually built, no $m_\times$-type term survives, then: (i) the
two-limit question resolves structurally (there is only one limit); (ii)
the quasistatic sector is pure AQUAL at all accessible radii; (iii) the
low-acceleration lensing RAR stays MOND-like — *consistent with the very
data that pressures vanilla AeST* — and the $\hat a_0(z)$ evolution of §3
becomes the framework's *only* lensing signature. That would be a genuine
distinguishing advantage over the parent theory, discovered by discarding
rather than adding. **Directive: make "does any $m_\times$-analog survive
in cdot-8's closed action?" the second installment's first task, with the
expectation above stated in advance as the thing being tested** — per the
verdict-scoping rule, the advantage is claimed only if the inspection
delivers it.

## 5. Housekeeping

1. **The Foundation §6 item 6 decision remains the standing gate.** WP5's
   first installment is legitimate parallel work under the proposal, but
   the WP4a routing decision is still pending and still gates what any of
   this is ultimately for. It should not silently age out; the decision
   input has been stable since the adjudication round.
2. The worker's confirmation of the normalization adjudication (the
   four-line anchor check) has not yet been delivered — standing.
3. Log: the worker's companion opens "SessionLog-2026-07-17.md (this
   directory, new)" — the advisor side of that file already carries two
   entries; Entry-9 rule applies, continue numbering. Plus the 07-16
   overwrite repair and the long-standing numbering reconciliation — one
   combined repair delivery.
4. Consolidation batch: unchanged, one delivery, before or with the
   author decision.

## 6. Directives

1. Adopt §1's variational mechanism into the WP5 write-up (with the
   unimodular precedent), keeping the worker's named-assumption flag.
2. Pin the clock via the charter identity everywhere $a_0(z)$ appears;
   carry the evidence-collapse statement verbatim.
3. Second installment: (a) the $m_\times$ inspection of §4 first; (b) then
   the lensing-RAR-by-lens-redshift confrontation against the stacked
   literature, using §3's backbone; (c) the Mistele two-limit question
   only if (a) finds a surviving $m_\times$-analog.
4. KATRIN clock: unchanged, most time-critical.

## Companion

- `wp5_decoupling_check.py` — the $\hat a_0(0)$ absolute anchor, the
  $E(z_\text{lens})$ backbone table.
- This advisory: proposed location
  `cdot-8/WP5/Advisory-WP5-DecouplingConfirmed-2026-07-17.md`.
