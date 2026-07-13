# Addendum — Assessment of the Third-Escalation Pair: Five Flags (for `cdot-8/WP3/`)

*2026-07-12. Assessment of
`Update-WP3-InverseReconstruction-2026-07-12.md` (worker) and
`Advisory-WP3-InverseReconstruction-2026-07-12.md` (stand-in advisor), against the
proposal context, both prior advisories, and this advisor's previously-computed
numbers. Method: cross-referencing against held results only — no rederivation (the
worker re-verifies algebra as standard protocol). **Verdict: both documents are
protocol-clean; the resolution architecture is consistent with the proposal; the key
quantitative claims cohere with independently-held numbers. The five flags below are
addenda, not reversals — none blocks the stand-in's directives, and directives 1–6
of the stand-in advisory remain in force as written, modified only where stated
here.***

---

## 0. Consistency confirmations (cross-checks against held results)

- The claimed true ratios $\hat a_0(z)/\hat a_0(0)=1.22,\,1.70,\,1.86,\,2.38$ match
  `budget_invoice.py`'s $E(z)$ at those redshifts, and the uniform factor $1.385$
  against Foundation §5.5's quoted values is the fit's own anchor
  ($1.39\times10^{-10}$ m/s²) — the labeling-bug diagnosis is quantitatively
  coherent from two independent directions.
- The $\hat a_0=\tfrac23\lambda c_0H_{\hat\tau}$ identity follows in three lines
  from relations already verified this session ($a_0=\lambda\dot c$;
  $H_t=\tfrac32\dot c/c$; acceleration-unit ratio $c^{7/2}$;
  $H_{\hat\tau}=H_t(c_0/c)^{-5/2}$... sign conventions as in the two-clocks
  advisory), and `twoclocks_check.py` had already found $\hat a_0/H_{\hat\tau}$
  constant to $5.6\times10^{-16}$ — the stand-in correctly recognized nothing
  fixed-point-specific entered that constancy.
- The exponent web is internally consistent throughout:
  $Q=(1+z)^{5/3}$, $F\propto Q^{9/5}$ (matter era), $a^3F_Q\propto d\hat\tau/dt$,
  $\hat a_0\propto Q^{9/10}$ on the fixed point.
- The premise-error diagnosis (free shift-current conservation is exactly the
  dynamics M5 suspends) is consistent with WP0's extraction and is the correct
  reading of the amended kill condition: the worker proved non-existence in the
  *unconstrained* theory, which the kill condition does not name.

## 1. Flag — evidence collapse (most consequential; affects both branches)

If $\hat a_0(z)\equiv E(z)$ identically, then cdot-7's §5.5 $\hat a_0(z)$
confrontation and its SN-photometry fit are **the same function of the same
trajectory measured against two datasets** — not two independent confirmations,
which is how Foundation's evidence ledger currently reads. This is a coherence
*gain* (one function, two data channels) but a bookkeeping correction cdot-7 owes
itself.

- **Action (worker):** add to `cdot-8/ConsolidationLog-2026-07-12.md`, for the
  cdot-7 consolidator: *"Evidence-ledger correction (HIGH confidence, MEDIUM
  priority): §5.5's $\hat a_0(z)$ agreement and the four-term SN fit are one
  prediction ($E(z)=H_{\hat\tau}/H_{\hat\tau,0}$) tested twice, by the
  $\hat a_0=\tfrac23\lambda c_0H_{\hat\tau}$ identity; the ledger should count them
  as one function confronting two datasets, not two independent successes."*
- **Action (proposal):** amend §8(iii)'s deflation-risk mitigation: the
  discriminator "the shape of $\hat a_0(z)$" is now understood to be the shape of
  $H_{\hat\tau}(z)$ — still a genuine discriminator against parameter-$a_0$
  theories (which predict *no* $a_0$–$H$ locking), but no longer independent of
  expansion-history data. The sharpest surviving form of the discriminator is the
  locking itself: **measure $\hat a_0(z)$ and $H(z)$ separately; the framework
  demands their ratio be constant** — a test no parameter-$a_0$ theory is obliged
  to pass.

## 2. Flag — missing stability sub-directive (the gap to fix first)

The reconstructed $F$ carries $(F-QF_Q)$ through a **sign change**: positive
effective density in the matter era, small-negative in the radiation era. A
zero-crossing in the scalar sector's effective density is precisely the regime
WP0's stability caveats (the $k<\mu$ non-propagating mode; conditions on $F$'s
derivatives) were flagged for re-examination "on our own branch" — the benign-ness
arguments in the AeST literature were made on *their* cosmological branch, not this
one.

- **Action (worker):** stand-in directive 1 acquires sub-item 1b: after deriving
  the modified equation of motion, check the reconstructed $F$ against the WP0
  stability conditions along the full trajectory, with particular attention to a
  neighborhood of the density zero-crossing (locate it; it sits in the
  census-crossover era). This is background-plus-linear only; no perturbation-sector
  scope creep.

## 3. Flag — state the aether normalization convention now

§4(ii)'s $Q=dt/d\hat\tau=(1+z)^{5/3}$ silently presumes which metric $A_\mu$ is
unit-timelike with respect to ($\hat g$ vs $g$), i.e. which frame's lapse appears.
The action-level M5 implementation will force the choice; after the two-clock
episode, implicit frame bookkeeping is the known ambush pattern.

- **Action (worker):** state the convention as a named assumption in the WP3
  implementation note *before* deriving the equation of motion, and verify at the
  end that the derived single-lapse-factor source is stated in the same convention
  as the success criterion. If the natural convention flips the factor to a
  different power of the lapse, that is a finding, not an error — report it.

## 4. Flag — the §5(c) ambush charge lands on both advisors

The stand-in's corrections ledger charges the budget advisory's directive 1
(fairly). For the record: the mislabeled-ratio regression the WP1 addendum ran was
ordered by the *two-clocks* advisory §2(vi), which likewise failed to say
"reproduce the quoted numbers from the producing script before comparing." The
verify-the-label lesson (stand-in's protocol note, second bullet) is hereby adopted
into K6 practice as applying to advisor-issued directives too: **any directive that
says "compare against quoted value X" must also say "after reproducing X from its
producing script."** Recorded as a correction to this advisor.

## 5. Flag — canonical parameter value (minor; reproducibility hygiene)

The stand-in used $x_0=1.0958$ (evidently the unrounded fit value); all prior
session scripts used the quoted $1.10$. Three-digit agreement survives either
choice, but cross-script reproduction wants one canonical value.

- **Action (worker):** one consolidation-log line: *"Canonical-value request (LOW
  priority): Foundation should state whether $x_0=1.10$ is exact-by-convention or
  rounded from $1.0958$; downstream scripts will standardize on the answer."*

## 6. Wording nit — the zero-freedom criterion

Stand-in directive 1's success criterion ("...with no adjustable function") is
right in spirit; make it airtight against a pedantic reading by carrying §2's own
caveat: *"...no adjustable function, up to the additive $CQ$ gauge piece (zero
energy density, total derivative)."*

---

**Net:** the stand-in's resolution stands; WP3 proceeds under its directives with
sub-item 1b (stability), the §3 normalization assumption, and the §6 wording
amendment folded in; three consolidation-log items (labeling bug and identity
remark — already directed by the stand-in — plus evidence collapse and canonical
$x_0$ from this addendum) travel to cdot-7 together. The protocol notes in the
stand-in's §6 are endorsed verbatim and worth keeping.

*Proposed location: `cdot-8/WP3/Addendum-ThirdEscalation-Assessment-2026-07-12.md`.*
