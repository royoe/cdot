# Decision Gates Standing Before the Author — 2026-07-18

*Prepared at the author's request ("prepare all appropriate decision
gates"), following WP5's closure. This document collects every open
question in cdot-8 right now that is a genuine author/scope call rather
than something resolvable by further technical work — with context,
options, and a recommendation where I have one, but no gate is decided
here. Housekeeping items (consolidation batch, log repairs, WP4b
confirmation) are listed separately at the end since they are owed
deliveries, not decisions.*

---

## Gate 1 — Foundation §6 item 6: the verdict on WP4a's 27% acoustic-scale miss

**The oldest and most consequential open gate.** First raised
2026-07-16, restated as "the standing gate" in every subsequent WP4b and
WP5 round since, and explicitly never narrowed by any advisor or by me —
by design, since this is a scientific-strategy call, not a numerics
question.

**What's settled, not in dispute:** cdot-8's own recombination-era sound
horizon gives $100\theta_*=1.326$ against Planck's $1.04109\pm0.00030$ —
a clean, methodologically-resolved 27% overshoot (distance convention,
$z_*$, and provenance all independently audited). The miss localizes
almost entirely to cdot-8's own fitted $E(z)$ in the crossover era
(z*-to-few$\times10^4$), not to the census baryon density $\Omega_b$ —
which is, separately, *validated* by this same work (within 3% of
Planck's independent BBN value). BBN itself (WP4b) passes at leading
order after a long, twice-reversed dispute that ultimately confirmed the
pass. So the combined WP4a+WP4b picture is specific: a **crossover-era-only
failure**, bracketed by genuine passes on both sides (BBN below, SN
diagram above).

**The three readings, unchanged since first framed:**
- **(a) Soft miss, proceed.** Treat 27% as a known, bounded, crossover-
  era tension to revisit once WP7 (full perturbation/CMB machinery) is
  built — a single-number confrontation at recombination may look
  different once the actual power spectrum, not just the peak-spacing
  scale, is computed. Consistent with WP5 (just closed) and WP6
  proceeding as legitimate parallel structural work.
- **(b) Provisional structural failure.** Keep working (WP5/WP6/WP7 all
  still valuable and mostly independent of this number), but formally
  flag cdot-8's cosmological-background sector as *not yet viable as
  stated*, pending either a fix or a reformulated M5/census closure.
  Downgrades the confidence with which any WP4a-adjacent claim
  (crossover-era $E(z)$, and everything built on it — including WP5's
  own $E(z_\text{lens})$ backbone) is stated.
- **(c) Decisive kill.** Treat the 27% miss as falsifying the census/M5
  closure as currently constructed, halting new WP5/6/7 work pending a
  redesign.

**Why I don't hold a preference between them, stated plainly:** the
numerics don't decide this — 27% is neither "obviously fine" (it's a
precision-cosmology-era measurement, not a rough estimate) nor "obviously
fatal" (nothing else in the framework has broken, and the miss is
cleanly localized to one term, not diffuse). This is a judgment about how
much slack a still-developing covariant completion earns before its
headline cosmological number must match Planck, and that's the author's
call to make, not something I or the advisor should narrow further by
technical argument alone.

**One new piece of context since this gate was last stated (worth
weighing, not decisive):** WP5's $E(z)$ backbone — built from the same
crossover-era $E(z)$ that WP4a flags — independently cross-validates
against cdot-7's own pre-existing, SN+RAR+MIGHTEE+MUSE-DARK-fitted
$a_0(z)$ trajectory to 1–5% across $0<z<1$. That's a different regime
(low-to-moderate $z$, galaxy-lensing-relevant) than WP4a's recombination-
era comparison, so it doesn't resolve the gate — but it's evidence that
whatever is wrong at $z^*$ doesn't obviously propagate to where WP5 needs
$E(z)$ to be right.

**My recommendation, offered but not pressed:** (a), with (b)'s downgrade
language attached — i.e., proceed, but every WP5/WP6 deliverable from
here should carry an explicit note that it inherits an unresolved,
crossover-era cosmological tension until WP7 either resolves or hardens
it. This keeps the parallel structural work (which has been genuinely
productive and largely orthogonal to the $E(z)$-at-$z^*$ number) moving
without quietly laundering the tension into a false "all clear."

---

## Gate 2 — WP5b scope: pursue the binned lensing-redshift confrontation, or close WP5 as delivered?

**New this round.** WP5's structural deliverable (the M5/local-decoupling
argument, the recovered AQUAL equation, the $m_\text{eff}$/condensate-mass
resolution, the lensing-RAR prediction backbone) is complete and
independently verified at every step. The one remaining piece — an actual
data confrontation — turned out to be blocked not by theory but by the
literature: **neither of the two natural anchor papers (Brouwer et al.
2021, KiDS-1000; Mistele et al. 2024) bins its lens sample by redshift**;
both pool $z=0.1$–$0.5$ into a single measurement, and both carry
uncertainty floors (a $\approx26\%$ stellar-mass-to-acceleration
conversion band; an unresolved missing-baryons degeneracy) that are
common-mode with, and larger than, cdot-8's predicted 12–16% signal at
their mean redshift. **I checked this myself against both primary
sources** — one advisory characterization (a specific severity quote
attributed to Brouwer et al.) didn't survive that check and has been
corrected in the record, but the underlying conclusion (pooled data can't
decide this) holds up independently of that one quote.

What *would* decide it: a differential test — the ratio of fitted
$a_0$ between two lens-redshift bins *within one survey, one pipeline*,
which cancels the absolute zero-point and $M/L$ degeneracies that sink
the pooled comparison. Design work (not data analysis) is done and
checked: KiDS-alone bin splits are directional at best ($\sim1\sigma$);
a decisive ($3$–$5\sigma$) test needs lens bins out to $z\sim0.6$–$1.0$,
which only DES/HSC-deep, LSST, or Euclid depth provides.

**The options:**
- **(a) Close WP5 here.** The pre-registered prediction + the
  demonstrated literature gap + the test design (with its full
  systematics budget) is a complete, falsifiable, honestly-scoped
  deliverable — registered *before* any binned analysis exists, which is
  a genuinely strong position (a real prediction the field could go test,
  not a post-hoc fit). Proceed to WP6.
- **(b) Open WP5b as an in-program work package**: acquire and reprocess
  the actual KiDS/DES/HSC lens catalogs, build the redshift-binned RAR
  measurement directly. This is *new observational data-analysis work* —
  different in kind from everything WP0–WP5 have done so far (all
  first-principles derivation and confrontation against already-published
  numbers), with its own data-access, calibration, and systematics-
  modeling burden.
- **(c) Flag it as a separate, external proposal** (e.g., for a
  collaborator with existing KiDS/DES pipeline access) rather than
  something this program does internally — the design and prediction are
  cdot-8's contribution; the reanalysis is a different skill set.

**My recommendation, offered but not pressed:** (a) now, with (c) noted
as the natural home for the follow-through — the design is genuinely
valuable as a stated, falsifiable prediction regardless of who eventually
tests it, and reprocessing survey catalogs is a substantial undertaking
that doesn't obviously belong inside this program's own charter (which
has, so far, been theory-and-confrontation-against-existing-numbers, not
primary data reduction). But this is a scope-and-resourcing call, not a
physics one, and legitimately yours to make.

---

## Housekeeping — owed, not decisions, listed so they don't keep aging silently

- **WP4b adjudication confirmation**: I believe I already delivered the
  concession the advisor is waiting on
  (`WP4b/Update-WP4b-RebuttalWithdrawn-2026-07-17.md`), but the
  proposal-side session log still lists it as pending as of the last
  advisory round. Worth an explicit one-line confirmation back to the
  advisor loop so this stops being carried as open.
- **Errata/consolidation batch**: several rounds now (WP3's six advisor
  errors, WP4b's two, WP5's "advisor error #6" and the Brouwer misquote
  caught this round, the K6 pattern-library additions) have accumulated
  without a single consolidated delivery. Not urgent, but growing.
- **Log repairs**: the 07-16 WP4b session-log overwrite (already
  rewritten from memory), a numbering reconciliation between per-WP logs
  and the shared proposal-side log, and an "Entry-9" note on the 07-17
  proposal log — small, mechanical, not yet done.
- **KATRIN clock**: repeatedly flagged across many rounds as "the
  program's most time-critical item," without a specific pending action
  attached in what I have on record. If there's a concrete deadline or
  decision tied to this, it isn't reflected in my current context —
  worth the author confirming what (if anything) is actually pending
  here, since I don't want to either silently drop it or invent an action
  for it.

---

## Resolutions (author, 2026-07-18)

**Gate 1 — (b), provisional structural failure.** Not a kill. cdot-8's
cosmological-background sector (the census/M5 closure, and specifically
the crossover-era $E(z)$ WP4a's $\theta_*$ miss traces to) is **not yet
viable as stated** — real options for resolving the discrepancy need to
be investigated, not assumed away or accepted as a tolerable footnote.
**But**: the author's explicit sequencing instruction is to complete the
analysis through WP7 *first*, on the current radiation-era assumptions,
and only revisit those assumptions afterward. So: proceed with WP6 and
WP7 as planned, but every deliverable from here carries the (b)-level
caveat (inherits an unresolved, not-yet-viable cosmological-background
tension) rather than an all-clear — consistent with the recommendation
offered above, now the confirmed instruction, not just a suggestion.
Radiation-era-assumption revisiting is explicitly deferred until after
WP7, not dropped.

**Gate 2 — (a), close WP5 as delivered.** No WP5b. The explicit goal
going forward for this line of work is establishing clear, falsifiable
predictions for *future* observational results, not reprocessing existing
survey catalogs in-program. WP5's pre-registered prediction + literature
gap + differential test design stands as the complete deliverable.
Proceed to WP6.
