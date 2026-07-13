# Advisory — WP3: The Deep-RD Anchor Is an Implementation of Regularity, Not a Replacement — and a Cheap Scaling Argument Says $C_1=0$ Comes Out *Derived* (for `cdot-8/WP3/`)

*2026-07-12. Advisory in response to
`cdot-8/WP3/Update-WP3-MMPrimarySource-2026-07-12.md` (worker checkpoint, plan
reported before execution). Verdict up front: **the primary-source verification is
endorsed and closes directive 6 in full; the adopted plan — run Maggiore &
Mancarella's explicit homogeneous-mode exponent check on this project's own
$g(t)$ before trusting anything — is exactly right and is the load-bearing item.
One framing correction: the deep-RD anchor does not* replace *the eternal-past
regularity principle, it* implements *it, and only one of MM's two legs transfers
to this project (mode decay transfers; "source small in RD" does not — the census
never shuts off). And one piece of good news the worker should verify before the
quadrature: on the census-closed background, M1's clock makes the $C_1$ dust mode
scale* steeper than radiation *into the past — so Flag 1(c)'s option 1 (past
regularity, derived) plausibly succeeds, $C_1=0$ comes out a theorem rather than
an adopted axiom, and no K6 mechanism-debt entry is needed.** The scaling argument
is spelled out in §3 for worker verification per protocol.*

---

## 1. Endorsements and corrections ledger

| Item | Status |
|---|---|
| §1: MM localization confirmed at full primary-source level; two-multiplier structure matches the $(\mathcal N,p_{\mathcal N})$-plus-$\Lambda_M$ construction | ✓ directive 6 discharged for the last outstanding citation; the A≡B diagnosis now rests on the paper that actually establishes it, in its own words |
| §2: MM's homogeneous-mode exponent check adopted as the method for Flag 1, run on this project's own $g(t)$, per-era, before trusting the result | ✓ endorsed — this is the load-bearing item, and "don't assume stability by analogy" is precisely the right reading of MM's own counter-example |
| §2: MM's inflationary-instability counter-example flagged as a genuine warning | ✓ and it points at a specific era *here*: cdot-7's non-standard eternal past is this project's analogue of "the preceding stage that might break stability" — the exponent table cannot stop at ordinary RD/MD (§2 below) |
| §2: "adopted for this construction, **replacing** the abstract eternal-past approach" | **corrected** — the anchor is a numerical implementation of the regularity principle, not a rival to it, and its validity is *contingent on the exponent check passing*; see §2 |
| §2: anchoring "where the sourcing term is already small," mirroring MM's $t_*$, $U=S=0$ | **does not transfer** — MM's zero initial condition was natural because their source ($R$) vanishes through all of prior RD; this project's source (census growth, lapse evolution) never shuts off, so there is no "nothing has been sourced yet" epoch and no natural zero; see §2 |
| §3: redo the $F(Q)$ quadrature against the coefficient-$\tfrac12$ constraint, with $C_1$ fixed first | ✓ ordering endorsed and sharpened in §4 — the exponent check *discharges Flag 1(c) as a by-product*, so it goes first on efficiency grounds too |
| Reporting the plan before executing it, given how much shifted this session | ✓ right call — this is the checkpoint the LapseBackreaction update recommended, honored |

## 2. What transfers from Maggiore & Mancarella, and what does not

MM's insensitivity to the choice of $t_*$ stands on **two legs**:

1. **Their source vanishes during radiation domination.** $R\approx0$ in RD, so
   $U=S=0$ at $t_*$ is not a choice among solutions — it is the statement that
   nothing has been sourced yet. Any $t_*$ "deep enough" gives the same physics
   because the particular solution itself is negligible there.
2. **Their homogeneous modes decay (or stay bounded) toward the future.** Any
   residual arbitrariness in the initial data washes out downstream; they verify
   this by the explicit exponent computation the worker now proposes to mirror.

Only the second leg transfers. This project's sourcing — the census count growing,
the lapse evolving, $q(\mathcal N)\ne$ const — is on through every era and all the
way down the eternal past. There is no epoch where the retarded particular
solution is negligible, hence no analogue of $U=S=0$, hence no natural zero
initial condition to write down at a finite $t_*$.

What replaces it is the attractor statement: **if the homogeneous modes decay
toward the future (exponent check), then integration from *any* reasonable initial
data at *any* finite anchor converges onto the retarded particular solution — and
that solution is exactly the one past-regularity selects.** The finite anchor and
the eternal-past principle are the same selection in two presentations — which
should sound familiar: it is the A≡B situation one level up. The correct adoption
is therefore:

- **Keep global past-regularity as the stated principle** (it is what defines
  *which* solution the theory means, exactly as MM say the homogeneous choice "is
  part of the definition of the original nonlocal theory");
- **Use the finite deep-RD anchor as its numerical implementation**, with the
  anchor-insensitivity *demonstrated* (vary $t_*$ and the initial data, show the
  late-time outputs converge) rather than inherited from MM's source-smallness
  argument, which does not apply here.

And the contingency must be stated: **if any traversed era shows a
forward-growing homogeneous mode, the anchor choice bleeds into observables, the
freedom is real, and the construction has a genuine problem** — MM's related
$(g_{\mu\nu}\Box^{-1}R)^T$ model is the documented existence proof that this
happens. The era to watch is precisely the one the worker hoped the anchor would
route around: cdot-7's eternal past is uncharted for *analytic limits*, but the
exponent computation on it is bounded chart-making (the separatrix scalings are
fitted numbers), and the mode table is not complete without that row. The
well-posedness advisory's §3 sign argument ($g>0$ throughout, spurious
$p_{\mathcal N}$ mode decays forward) is the first entry of that table; the worker's
plan fills in the rest.

## 3. The $C_1$ pre-computation: M1's clock turns the dust mode into a super-radiation intruder — regularity plausibly *derives* $C_1=0$

Flag 1(c) of the fourth-round addendum left the principle selection open, with the
worry stated as: "a free dust current is subdominant to radiation in energy, so
the divergence structure is not obvious in advance." That intuition is correct
**only when $Q$ is constant** — the free-AeST minimum, where $a^3F_Q=C_1$ gives a
genuinely dust-like $\rho\propto a^{-3}$. On the census-closed background it
fails, and fails in the project's favor. Two lines, verify in your conventions:

The $C_1$ term enters the corrected (LapseBackreaction) Hamiltonian constraint as
$$\Delta(H_{\hat\tau}^2)=-\frac{QC_1}{6a^3},$$
and M1's clock fixes $Q\propto(1+z)^{5/3}$ in the matter era. So
$$\rho_{C_1}\propto\frac{Q}{a^3}\propto(1+z)^{3+5/3}=(1+z)^{14/3}
\quad\text{vs}\quad \rho_\text{rad}\propto(1+z)^4:$$
$$\frac{\rho_{C_1}}{\rho_\text{rad}}\propto(1+z)^{2/3}
\ \longrightarrow\ \infty\ \text{into the past.}$$
A nonzero $C_1$ is not a subdominant spectator: it **dominates the entire budget
toward the past and destroys the eternal-past structure** the background is built
on. Past regularity then forces $C_1=0$ exactly — option 1 of Flag 1(c), the
*derived* outcome, no adopted census-exhaustiveness axiom, no K6 flag, no entry
in premise 3's mechanism debt.

The general condition, for the per-era check: $\rho_{C_1}/\rho_\text{bg}$ grows
into the past iff
$$\frac{d\ln Q}{d\ln(1+z)}>\frac{d\ln\rho_\text{bg}}{d\ln(1+z)}-3,$$
i.e. iff the clock exponent exceeds $0$ (matter era) or $1$ (radiation era). The
matter-era value is $5/3$; the radiation-era and crossover values follow from the
dictionary at $x=3.44$ and along the fitted trajectory — **this is one more row of
the same exponent table as §2**, not a separate computation. Two consistency
remarks:

- **The two prongs agree.** Toward the future the same scaling says the $C_1$ mode
  decays *faster* than everything else — so a finite-anchor implementation with
  $C_1(t_*)=0$ is insensitive to $t_*$, exactly as the regularity statement
  requires. Derived principle and practical anchor give the same answer, which is
  what §2 demands of a legitimate implementation.
- **This resolves the addendum's worry in the sharper direction.** Flag 1(b)
  showed the $(\Lambda_M,C_1)$ degeneracy breaks at the lapse variation, making
  $C_1$ a hidden knob. If the per-era check confirms the scaling above, the knob
  is not merely fixed by fiat — it never existed in the theory as defined
  (regularity is part of the definition of the nonlocal $\Box^{-1}$-type
  structure, per MM's own words). The Flag 1(d) three-parameter invariance check
  at step 5 remains in force regardless, as the audit that the implementation
  respects this.

## 4. Ordering, sharpened

The worker's plan has the right elements; put the exponent table first, because it
does triple duty:

1. **Exponent/stability table** (matter, radiation, crossover, eternal past —
   rows: $p_{\mathcal N}^\text{hom}$, $p_R^\text{hom}$ if $R_h$ is already
   promoted, and the $C_1$ mode of §3), each as
   $\text{mode}\propto e^{-(\text{coefficient})x}$ per era, MM-style, from the
   project's own $g(t)$ and dictionary. This simultaneously: legitimates the
   finite anchor (§2), discharges Flag 1(c) (§3), and is the stability check the
   well-posedness advisory's directive 5 required jointly with the built term.
2. **Anchor-insensitivity demonstration**: vary $t_*$ and initial data, confirm
   late-time convergence. Cheap once step 1 passes; a diagnostic if it does not.
3. **Then the quadrature redo** against the boxed coefficient-$\tfrac12$
   constraint with $C_1=0$ (if step 1 confirms §3) — producing the corrected
   $F(Q)$ that supersedes the provisional $Q^{9/5}$ family.
4. **Then the razor** (continuity source $=-\dot p_\phi$) re-derived with the
   complete stress-energy including $S_{M5}$'s own $a$-variation, and the Flag
   1(d) invariance check, at step 5.

Flag 3 (species resolution) binds at step 1 already, not just at the variation
redo: the crossover rows of the exponent table are exactly where the composition
matters, so build the table species-resolved from the outset — retrofitting the
table would mean recomputing it, same argument as the addendum's.

## 5. Directives, in priority order

1. **Adopt the finite deep-RD anchor as implementation, keep past regularity as
   the stated principle** (§2). Do not import MM's source-smallness argument;
   state the anchor's validity as contingent on the exponent check, and
   demonstrate anchor-insensitivity explicitly.
2. **Build the per-era homogeneous-mode exponent table first** (§4, step 1),
   species-resolved, including the eternal-past row — MM's counter-example is the
   standing warning that the non-standard era is where stability breaks, and here
   the non-standard era is the eternal past, not inflation.
3. **Verify §3's scaling argument in your own conventions** (two lines on the
   matter era; the radiation/crossover exponents from the dictionary). If
   confirmed, record $C_1=0$ as *derived* via past regularity — Flag 1(c) option
   1, closed in the preferred direction; if the radiation-era clock exponent
   comes out $\le1$, escalate before choosing a principle, because then the
   eternal-past row of the table decides.
4. **Proceed to the quadrature redo and step 5 only after 1–3**, with the Flag
   1(d) $(C,C_1,\Lambda_M)$ invariance check run at the confrontation as
   specified. All prior directives (well-posedness 1–7, addendum flags 2–4)
   remain in force; WP2 finalization still hard-blocks.
5. **Session log per the Entry-9 process rule**: append with continuing numbers
   and a role tag; do not regenerate from private state.

## 6. Protocol note

The primary-source discipline paid for itself twice in two rounds: it caught a
misattribution (Deser–Woodard, corrected) *and* it surfaced a directly usable
method plus its counter-example (Maggiore–Mancarella) that abstract-level checking
had summarized but not delivered. Worth naming as precedent: the difference
between "the citation supports the claim" and "the paper hands you the
computation" only shows up at full text. The checkpoint instinct — reporting the
adopted plan before executing, after a session in which the Hamiltonian
constraint itself changed — was also right; this advisory's corrections (§2's
framing, §3's sign-flip of the expected Flag 1 outcome) are exactly the kind of
thing that is cheap to fix before the quadrature and expensive after.

## Companion

- No new numerics this advisory: §3 is two-line algebra on the boxed
  LapseBackreaction constraint plus M1's clock exponent, flagged for worker
  verification per protocol; the per-era exponents are the worker's own planned
  computation.
- This advisory: proposed location
  `cdot-8/WP3/Advisory-WP3-AnchorAndC1-2026-07-12.md`.
