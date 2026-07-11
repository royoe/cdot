# Update — The Counting Law: Planck-Unit Census (Foundation.md §2.1/§2.3; §6 items 4, 5, 9)

*Session: 2026-07-11. Status: proposed — for cross-check and merge, not yet applied.
Companion files: `SessionLog-2026-07-11.md` (full prompt-by-prompt record),
`census_closure.py` (every number below independently re-runnable in one pass),
`census_trajectory.svg`/`.png` (figure).*

**Merge dependency, stated up front:** this update *amends* the still-unmerged
`Update-RadiationEraClosure-2026-07-10.md`. It should be merged together with it, or
after it, never instead of it — Part A below is written as amendments to that update's
proposed §2.3 text. It also independently re-verifies every headline number of the
07-10 update from a from-scratch reimplementation (the original `radiation_closure.py`
was not consulted; it is not in the project knowledge), so the merge can treat those
numbers as now double-checked rather than single-sourced.

**Note on sourcing:** this session worked from `project_knowledge_search` retrieval
plus a full linear read of `Update-RadiationEraClosure-2026-07-10.md`. Section numbers
follow the same convention as that update and need the same final placement check.

---

## What this update covers

The 2026-07-10 session's radiation-era extension rested on a counting law the author
correctly identified as under-justified: matter is counted by rest mass, photons by
$u_\gamma/c^2$, with the $\eta=1$ (no-pressure) prefactor argued only from AQUAL's
scope. This session (1) surveyed the space of plausible counting laws, (2) found that
one reformulation — the **Planck-unit census** — converts three separate ad hoc
choices into a single principle already load-bearing elsewhere in the framework,
(3) found the census *forces* the missing neutrino third term (07-10 update, item
5(b)) with zero additional freedom, (4) built and integrated that term, materially
revising the recombination-era numbers, and (5) resolved the $z_{\nu,\text{nr}}$
convention question. Background-history only, as before: the perturbation sector
(item 6) is untouched.

---

## Part 0 — The counting-law survey (why the census, and what died)

The freedom is narrower than it first appears. Under the standing assumptions every
species' coordinate number density is conserved, so **any pure count within the horizon
scales as $R_h^3$** — species can never be distinguished by counting alone. The entire
radiation-era structure lives in the **per-entity weight** $w_i(c)$ in
$M_h=\sum_i N_i w_i$; a crossover exists iff the photon/matter weight ratio grows into
the past. The candidates, assessed:

- **Rest mass only (photons weigh zero).** No crossover, no $z_\text{eq}$ analog, the
  closure sits on the matter fixed point forever. Incompatible with the correspondence
  to standard radiation-era history the 07-10 session established. Dead.
- **Unweighted number, entropy, or mode counts.** Constant dimensionless weight per
  photon ⇒ census $\propto R_h^3$ with no species-dependent $c$-scaling ⇒ no crossover;
  and photons outnumber baryons by $\sim1.6\times10^9$, making the matter-era successes
  accidental. Dead.
- **Energy census vs. mass-equivalent census.** The $c^2$ is common to all species: once
  made dimensionless the two are identical. Recorded as a robustness result — the only
  genuine residual freedom is the pressure prefactor.
- **Tolman weighting** ($\rho+3p/c^2$; photons at $2u/c^2$, $\eta=2$). The one live
  alternative; native to relativistic field equations this framework has declined to
  build (item 7). Changes only $\rho_{\gamma,0}$'s normalization, never the exponents or
  fixed points. Kept as an explicit systematic, exactly as the 07-10 update carries it.
- **Pair/connection counts** (cdot-4's connecton direction, $\propto N^2$). Incompatible
  with the current closure without a ground-up rebuild; noted, not pursued.

## Part A — Proposed changes to `Foundation.md`

### A.1 — Restate §2.1's counting law as the Planck-unit census

Propose replacing §2.1's "Machian by number" statement (and the 07-10 update's §2.3
opening) with a single counting principle:

> **The counting law: Planck-unit census.** The Machian source is a genuinely
> dimensionless count: every entity within the horizon contributes its instantaneous
> coordinate energy measured in the instantaneous Planck unit,
> $$\mathcal{N}(t)\;=\;\sum_{i\,\in\,R_h}\frac{E_i(t)}{E_P(t)},\qquad
> M_h(t)\;=\;\mathcal{N}(t)\,m_P(t),$$
> with $E_P=\sqrt{\hbar c^5/G}\propto c^{5/2}$, $m_P=\sqrt{\hbar c/G}\propto c^{1/2}$.
>
> **This is not a new dynamical assumption — it is arithmetically identical to the
> counting already in use, term by term.** For a massive particle,
> $E_i/E_P=m_ic^2/E_P=m_i/m_P=\sqrt{\alpha_{G,i}}$, which is **epoch-invariant by
> premise 3** — so the matter census literally reduces to counting massive particles,
> which is why "just counting mass" has worked in every late-time result: premise 3 is
> exactly the condition under which mass-counting and pure counting coincide. For a
> photon, $E_\gamma/E_P=\hbar kc/E_P\propto c^{-3/2}=(1{+}z)$ relative to matter's
> constant weight, reproducing §2.3's $\rho_\gamma^\text{eff}\propto c^{-1}$ exactly.
> The same symmetry principle that uniquely fixed $s=+\tfrac12$ (§3.4) therefore fixes
> the counting law: **the counting law is the Machian face of Planck-unit invariance**
> (§6 item 4 now carries both debts as one).
>
> Three consequences follow at zero further cost. (i) The $\eta=1$ sourcing prefactor
> becomes principled rather than scope-argued: a census of what exists has no pressure
> term — $\rho+3p/c^2$ is a property of a gravitational *field equation*, not of an
> inventory. §2.3's scope argument survives as a backstop. (ii) Kinetic energies count.
> Negligible for cold matter (fractional correction $\sim10^{-7}$ for relic neutrinos
> today), decisive for the neutrino sector (§2.3 amendment below). (iii) The census is
> **continuous through any locally energy-conserving conversion**: at the instant of
> $e^+e^-\!\to\gamma\gamma$ or nuclear burning, $\sum E_i/E_P$ is unchanged — only the
> *subsequent evolution law* of the converted quanta changes (their weight-evolution
> differs by species). This replaces the per-species number-conservation assumption
> (item 9 and its 07-10 photon companion, both known false at transitions) with the
> weaker pair: census continuity at conversions + kinematic evolution between them.
> Species transitions become computable re-weighting kinks, not breakdowns of the
> premise. *(The continuity statement itself assumes coordinate-frame local energy
> conservation at an instant — plausible given premise 3, but an assumption; flagged
> for item 10's energy-continuity check, not smuggled in.)*

### A.2 — Amend the (pending) §2.3: the neutrino third term, forced

Propose appending to the 07-10 update's §2.3, replacing its item-5(b) placeholder:

> **The neutrino term is forced by the census, with zero free functions.** Premise 1's
> spatial translation invariance conserves each relic neutrino's coordinate wavenumber
> $k$ (the same Noether argument as §3.3's photons); premise 3 gives
> $m_\nu(t)\propto c^{1/2}$. The census weight per neutrino is therefore
> $$w_\nu=\frac{1}{c^2}\sqrt{\big(m_\nu(t)c(t)^2\big)^2+\big(\hbar k\,c(t)\big)^2},$$
> interpolating between census-radiation ($\propto c^{-1}$, deep past) and
> census-matter ($\propto c^{+1/2}$, today) with the transition where
> $\hbar k\approx m_\nu c$. **Translated to local units via the standard dictionary,
> this is exactly the relativistic Fermi–Dirac energy density of massive relic
> neutrinos** ($\hat p\propto(1{+}z)$, $\hat m$ const, frozen occupation) — i.e.
> precisely the "genuine relativistic Fermi–Dirac term" the 07-10 update flagged as
> the needed fix but did not attempt. Verified numerically: with the four-term fit's
> own $\Sigma m_\nu=1.374$ eV (three quasi-degenerate states at $0.458$ eV),
> $$\Omega_\nu^\text{census}(t_0)=0.0298,\qquad
> \Omega_b+\Omega_\nu^\text{census}=0.0740,$$
> matching the closure's demanded $\Omega_\text{closure}=0.074$ to $0.1\%$ — the
> census's own exact-FD neutrino budget closes the four-term fit's mass census without
> adjustment (the naive $\Sigma m_\nu/93.14h^2$ formula differs by $1\%$; the census
> value is the exact one).
>
> **Revised numbers (supersede the two-fluid values of this subsection).** With the
> three-component census source (cold matter $\Omega_\text{closure}-\Omega_\nu$,
> photons, exact-FD neutrinos), integrated through $z=10^6$ exactly as before:
> - Below $z\approx190$ the census and two-fluid trajectories agree to $<1\%$; at
>   $z\le10$ they are identical to 4 digits — **every late-time result, including the
>   four-term fit itself, is untouched.** Both fixed points ($1.72$, $3.44$) are
>   exactly unchanged (neutrinos asymptote to census-radiation in the deep past).
> - The crossover moves down: at the primary convention the radiation-like and
>   matter-like census components cross at $z\approx1080$ — essentially *at*
>   recombination (ratio $1.02$ at $z=1100$) — versus the two-fluid $z_\text{eq}
>   \approx1466$. The effective source exponent $n_\text{eff}=d\ln\rho/d\ln c$ sweeps
>   $+\tfrac12\to-1$ with its midpoint at $z\approx870$.
> - **$x(z_\text{recomb}{=}1100)=2.61$ at the primary convention** ($[2.32,2.61]$
>   across all four $\Omega_\text{closure}$ conventions; $2.67$ under standard $\mu$)
>   — a systematic $\sim{+}10\%$ upward revision of the two-fluid $[2.14,2.37]$, now
>   $\sim50\%$ above the matter-only $1.72$. Any recombination-era treatment should
>   use the census value.
> - At $z=1100$ the neutrinos are genuinely mid-transition: $40\%$ of their census
>   energy is kinetic — confirming, and now resolving exactly, the 07-10 flag that
>   "the two-fluid split is incomplete precisely where it matters most."
>
> **The $z_{\nu,\text{nr}}$ marker, resolved as a convention question.** The 07-10
> update's $z\approx2733$ is the $T_\nu=m_\nu$ convention (reproduced here exactly:
> $2731$), *not* — as this session initially suspected before checking — a
> $\Sigma m_\nu$-vs-per-state slip. Other standard markers: $\langle p\rangle=m_\nu c$
> gives $z\approx866$; the census-native center (kinetic census $=$ rest census) sits
> between, at $z\approx1445$. The census makes the choice moot: the exact smooth FD
> weight replaces every threshold marker, and the markers survive only as descriptors
> of where along it recombination falls (answer: inside the transition).

### A.3 — §6 item list amendments (relative to the 07-10 update's own amendments)

> 4. **Justify Planck-unit invariance** — *now also carries the counting law*: the
>    Machian census (§2.1) and premise 3 are two faces of the same symmetry; a
>    mechanism for one is a mechanism for both. A single debt where there were two.
> 5. (b) **Resolved at the background level** by the census neutrino term (§2.3):
>    exact FD interpolation, zero free parameters, numerically integrated. Residuals
>    renamed: (b′) $N_\text{eff}=3$ was used, not $3.044$ (sub-percent on
>    $u_\nu$; noted, not propagated); (b″) the census's $\Omega_b+\Omega_\nu=0.074$
>    closure-budget match should be folded into any rerun of the four-term fit rather
>    than only checked post hoc. Items (a) and (c) as amended below / unchanged.
>    (a) **Reframed, materially weakened as a debt**: per-species number conservation
>    is replaced by census continuity at energy-conserving conversions + kinematic
>    evolution between them (§2.1). $e^+e^-$/QCD become computable re-weighting kinks.
>    What remains: the instantaneous coordinate-energy-conservation assumption
>    (cross-linked to item 10), and actually computing those kinks in census form.
> 9. Same reframing as 5(a); the item's scope narrows to the homogeneity of the
>    census density, no longer per-species number conservation itself.
> 10. Add: the census-continuity assumption of §2.1 is exactly the kind of statement
>     this item's internal energy-continuity check should adjudicate.

---

## Part B — Proposed new `ResearchNotes.md` section

> ## §17. The Counting Law: from ad hoc weights to the Planck-unit census
>
> Prompted by the author's direct challenge to §16's counting law ("The counting law
> seems like an arbitrary choice… I would have preferred a more better justified
> counting law"), with the premise restated: $c$ is set Machianly by a count of all
> that exists within the local causality horizon; the question is what to count when
> mass and energy themselves vary with $c$.
>
> **§17.1 Locating the freedom.** All conserved-number counts scale as $R_h^3$; the
> counting law is really the per-entity weight function, and the radiation era lives
> entirely in the weights' $c$-scaling. Candidate survey as in Part 0 above: rest-mass-
> only, unweighted-number, entropy, and mode counts all die (no crossover, and the
> latter three are photon-dominated by $10^9$ at all epochs); energy- and
> mass-equivalent censuses coincide once dimensionless; Tolman weighting survives as
> the $\eta=2$ systematic only.
>
> **§17.2 The census and its equivalences.** $\mathcal N=\sum E_i/E_P$,
> $M_h=\mathcal N m_P$. Checked three ways: (i) algebraically term-by-term equal to
> §16's adopted law ($Nm+N_\gamma\hbar\langle k\rangle/c$); (ii) the full two-fluid
> pipeline was reimplemented from the documented equations alone and reproduces every
> §16 number — fixed points $1.7222/3.4443$ (ratio exactly 2), $z_\text{eq}$ per
> convention ($1465/2060/2278/2654$ at $\eta{=}1$; $732$–$1327$ at $\eta{=}2$),
> $x(1100)\in[2.14,2.37]$ at $\eta{=}1$ and $2.68$ max at $\eta{=}2$, deep-past
> settling at $3.44$ — §16's numbers are now independently double-checked, not
> single-sourced; (iii) matter's census weight $\sqrt{\alpha_G}$ is epoch-invariant by
> premise 3, closing the loop with §7's LLR$\Leftrightarrow\alpha_G$ identity: **the
> counting law, the $s=\tfrac12$ derivation, and LLR safety are one dimensionless
> statement.**
>
> **§17.3 What the census newly commits to (its falsifiable surplus over a
> rationalization).** (i) $\eta=1$ is forced, not chosen — an inventory has no
> pressure; (ii) kinetic energies count; (iii) the neutrino term is the exact
> relativistic FD energy density with conserved coordinate $k$ and $m\propto c^{1/2}$
> — derivation: premise 1 Noether conserves $\hbar k$ for massive modes exactly as for
> photons; census weight $\sqrt{(mc^2)^2+(\hbar kc)^2}/c^2$; dictionary check: local
> momenta redshift as $(1{+}z)$, local mass constant, occupation frozen ⇒ standard
> massive-neutrino $\hat\rho_\nu(z)$, hitting both known limits
> ($(1{+}z)^4$/$(1{+}z)^3$) and everything between; (iv) census continuity through
> energy-conserving conversions, replacing per-species number conservation.
>
> **§17.4 Numerics (all in `census_closure.py`, one pass).** Constants: $h=0.7$
> (reproduces §16's $\Omega_\gamma=5.047\times10^{-5}$, verified via
> $z_\text{eq}=1465$), $\Omega_b h^2=0.02166$ (CPS18, as in the four-term fit),
> $T_{\gamma,0}=2.7255$ K, $\Sigma m_\nu=1.374$ eV. FD census integral
> $F(a)=\int x^2\sqrt{x^2+a^2}/(e^x{+}1)\,dx$ validated at both limits
> ($F(0)=7\pi^4/120$ to 7 digits; $F(a)/a\to\tfrac32\zeta(3)$ to 7 digits).
> Results: $\Omega_\nu^\text{census}(0)=0.0298$;
> $\Omega_b+\Omega_\nu^\text{census}=0.0740$ vs. the closure's $0.074$ ($0.1\%$);
> three-component trajectory: identical to two-fluid to 4 digits at $z\le10$,
> $<1\%$ different below $z\approx190$, then systematically higher —
> $x(1100)=2.605$ primary / $[2.32,2.61]$ across conventions / $2.666$ standard $\mu$;
> radiation-like$=$matter-like at $z\approx1080$; $n_\text{eff}$ midpoint $z\approx
> 870$; $x(10^6)=3.443$ (radiation fixed point recovered identically). Neutrino
> kinetic census fraction at $z=1100$: $40\%$.
>
> **§17.5 Caveats, stated as sharply as the wins.** (i) The census **post-dicts** the
> two-fluid law; its evidential weight rests entirely on the surplus commitments of
> §17.3 — judge it there. (ii) $\eta=2$ still lurks: if a relativistic completion
> (item 7) is ever built it may force Tolman weights; the two-fluid $\eta=2$ envelope
> ($x(1100)$ up to $2.68$) remains the standing systematic. A census-native $\eta=2$
> run was deliberately not built — doubling "what exists" is incoherent in inventory
> language, which is the point, but also means the systematic is only carried in
> two-fluid form. (iii) Census continuity assumes instantaneous coordinate-frame
> energy conservation at conversions — an assumption, now explicitly on item 10's
> desk. (iv) Field and gravitational binding energies are not counted; negligible
> now, not obviously so near genesis. (v) The census answers *what to count*, not
> *why a count sources* $c^2=\kappa g_hR_h$ — the closure-form question (§8) is
> untouched. (vi) An initial suspicion this session voiced — that §16's $z_{\nu,
> \text{nr}}\approx2733$ was a $\Sigma m_\nu$-for-per-state slip — was **wrong**: it
> is the $T_\nu=m_\nu$ convention with the correct per-state mass (reproduced:
> $2731$). Recorded so the false alarm isn't re-raised; the real correction is that
> the physically weighted transition center sits at $z\approx870$–$1445$ depending on
> weighting, i.e. recombination falls *inside* the transition, which the exact census
> term now handles rather than marks.
>
> **Ledger.** Derived and cross-checked at least two independent ways: the census
> $\equiv$ adopted-law identity (algebra + full pipeline reproduction of every §16
> number); the matter census weight's epoch-invariance (premise 3 + §7 identity); the
> neutrino term's two limits (dictionary + direct FD). Derived once, numerically
> verified: the three-component trajectory and all revised $x$/$z_\text{eq}$ values;
> the $\Omega_b+\Omega_\nu=0.074$ budget match. Argued from principle, not derived:
> that a census is the right *kind* of object to source the closure ($\eta=1$'s
> forcing is internal to the census reading). Estimated/noted only: $N_\text{eff}=
> 3.044$ refinement, $e^+e^-$/QCD census-form kinks (now well-posed, still
> uncomputed). Not attempted: anything in the perturbation sector.

---

## Files in this delivery

- `Update-CountingLaw-PlanckCensus-2026-07-11.md` — this document.
- `SessionLog-2026-07-11.md` — full prompt-by-prompt record, two entries, timestamped.
- `census_closure.py` — Part 1 (independent §16 verification) and Part 2 (census +
  neutrino term) in one pass; `python3 census_closure.py` reproduces every number.
- `census_trajectory.svg` / `.png` — $x(z)$, two-fluid vs. census, both fixed points,
  recombination and the neutrino-transition marker indicated.
