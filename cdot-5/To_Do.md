*Note (2026-07-05): the cosmological sector (premise 2 and the CMB) is closed — see
`T24_The_Cosmological_Sector_Closed.md`. Items below that depend on the counting law
specifically (redshift drift, chronometer-vs-BAO split, the CMB $\beta$-test) are
routed to topics now flagged closed rather than live; the local-physics items (Tolman,
$\mu=m_p/m_e$, the old-object age test, cosmic dipole) are unaffected, since they use
only premises 1/3/4 or local physics, not the specific counting law.*

# To-Do — Standing Observational Test List

*Not a topic document. This is the project's running checklist of tests flagged, in
cdot-4's `T23_The_Failed_Tests.md` Part III ("The Deferred Test Battery"), as **not yet
run** — and never revisited after cdot-4 closed. Each item below was checked against
the counting-law change; where a test's formula depended on it, the formula is redone
here (or in the topic it was routed to) rather than carried over stale. Items with a
natural home in an existing topic document are routed there as an Open Item, with the
updated derivation, and only indexed here. Items with no natural single-topic home stay
here in full.*

---

## Already Run (for context, not pending)

- **The effective radial expansion rate / Alcock–Paczyński test.** cdot-4's battery
  called this "the sharpest currently-available geometric test" before it was actually
  run. It was — and failed decisively (T23, $\chi^2=93.9$/6 points, zero parameters),
  directly motivating the premise-2 replacement that produced cdot-5's connectivity
  law. Not pending; recorded so the history isn't lost.

---

## Routed to Topics (updated derivation there, indexed here)

| Test | Old (cdot-4) claim | New (cdot-5) status | Topic |
|---|---|---|---|
| **Redshift drift (Sandage–Loeb)** | $\dot z=H_0^\text{obs}(1+z)[1-(1+z)^{1/6}]$, always negative | **$\dot z\equiv0$ identically, at every redshift** — an exact null result, not a small negative number. Sharper and easier to falsify than the old claim. | T3, §"Redshift Drift" |
| **Cosmic chronometers vs. BAO split** | Predicted split $(1+z)^{1/2}$ | Same exponent survives (from $H_\tau(z)/H_\tau(0)=(1+z)^{1/2}$ vs. $H_\text{obs}(z)/H_\text{obs}(0)=(1+z)$, both already in T3) — but *which* clock a real chronometer measurement recovers is still the open half of the question. | T3, Open Questions |
| **CMB temperature–redshift relation ($\beta$ test)** | Claimed $T(z)=T_0(1+z)$ exactly, via an absorber-transition-frequency argument | Live tension with T16's own new $R_\text{rec}$ derivation ($T_\text{eff}(t)\propto c(t)$, an emission-epoch quantity) — not the same quantity as what an absorber at intermediate $z$ would measure; **not reconciled**. | T16, Open Questions |
| **Bullet Cluster (1E 0657-56)** | Needs PBH-dominated cluster potentials; conflicts with baryon-only RAR (T15) | Structural tension restated with a concrete observational target; not quantified. | T16, Open Questions |
| **BBN D/H** | Calculation undone | Still undone; gated on the pre-percolation $c(t)$ history (T13's own top prerequisite) — T21's weak/nuclear scalings ($\Gamma_\text{weak}\propto c^4$, deuteron binding $\propto c^2$) are ready whenever that history exists. | T13, Open Questions |
| **$\mu=m_p/m_e$ invariance** | Passes automatically, never recorded | Recorded — trivial, exact, present-value physics (both masses invariant, premise 3). | T7, new section |
| **Cosmic dipole / preferred-frame test** (Secrest et al. quasar dipole) | "A rare place the model could outperform $\Lambda$CDM"; not followed up | Tied explicitly to T22's own $\alpha_1,\alpha_2$ discussion; still not quantified. | T22, Open Item 7 |
| **The old-object two-sided test** | Any object $>14.5$ Gyr falsifies $\Lambda$CDM; cdot-4 ceiling was $21$ Gyr | Ceiling is now **$27.9$ Gyr** — an even larger margin; distinct from T20's white-dwarf ceiling (which bounds how *young*, not how old). No candidate object identified. | T1, Open Questions |
| **Tolman surface-brightness / duality** | Filed as "non-discriminating" — assumed to pass automatically via Etherington reciprocity | **Reclassified: genuinely discriminating.** Etherington does not hold here (T16/Core §4); using the model's own $D_A\equiv D_p$, $D_L=(1+z)D_p$ gives $\text{SB}\propto(1+z)^{-2}$, **not** $\Lambda$CDM's $(1+z)^{-4}$ — a real, testable, half-the-exponent prediction. | T4, new section |

---

## No Natural Topic Home — Still Fully Open

- **Growth of structure** ($f\sigma_8$, redshift-space distortions, cluster mass
  function counts). Flagged in cdot-4's battery as "entirely unworked, possibly fatal,
  possibly a discovery channel." No T-document in cdot-4 or cdot-5 addresses structure
  growth at all — there is currently no model-native prediction for how density
  perturbations evolve under either the static-$a$ premise or connectivity counting.
  This is arguably the largest genuine gap in the program: $\Lambda$CDM's growth-of-
  structure fit is one of its most stringent tests, and this model has no
  corresponding calculation to even fail. If this ever grows into a real derivation,
  it should probably become its own topic document rather than living here.

- **FRB dispersion measures (Macquart relation).** The observed DM–$z$ relation for
  fast radio bursts is sensitive to the cosmic baryon density and its distribution
  along the line of sight. Not evaluated under either counting law. Plausibly belongs
  with T13 (baryon density) or a future distance-probe topic once someone works out
  what this model predicts for the intergalactic electron column density as a function
  of $z$ — not attempted.

---

## Explicitly Non-Discriminating — Don't Re-Derive These

Flagged in cdot-4's battery specifically so future sessions don't waste time on them.
Tolman/duality was pulled out of this bucket above (it turned out to be discriminating
after all, once Etherington was correctly dropped) — these two remain genuinely inert:

- **SN light-curve time dilation.** Any standard redshift mechanism predicts
  observed-duration $\propto(1+z)$; matches data; does not distinguish this model from
  $\Lambda$CDM.
- **Laboratory $\dot c$-drift searches.** The real drift rate ($H_0^\text{hor}\sim
  10^{-18}$/s) is far below any achievable laboratory clock/interferometer sensitivity.

---

## Notes for Whoever Picks This Up Next

- This list is a **snapshot of cdot-4's 2026-07-02 test battery**, checked against the
  cdot-5 counting-law change on 2026-07-04. It is not a survey of every conceivable
  test — it's specifically the items that were proposed once and then dropped. New
  tests proposed during the cdot-5 review (e.g. T16's own $z_\text{rec}$ rescan, T20's
  pre-percolation-branch dependency) live as Open Items in their own topics, not here,
  since they were never part of the original deferred battery.
- When an item above gets a real, quantitative answer (not just a formula update), move
  its row from "Routed to Topics" to a "Resolved" section here, or just let the topic
  document's own Open Questions reflect it and delete the row — whichever the next
  session finds less redundant.
