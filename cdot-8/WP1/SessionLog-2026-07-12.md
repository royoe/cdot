# Session Log — cdot-8/WP1 (2026-07-12)

---

## Entry 1 — Executing WP1: the dictionary as a frame map (2026-07-12)

**Prompt (verbatim):**
> Yes, proceed.

(In response to the offer, at the end of `cdot-8/WP0/`'s session, to proceed to WP1
once the author had reviewed the WP0 full-pass findings.)

**Summary of work performed:**

1. **Extracted the precise AeST action, invariant definitions, matter-coupling
   statement, and published FRW background equations**, via direct re-fetch of
   arXiv:2007.00082 (the founding PRL), arXiv:2309.06232, and arXiv:2402.04091 (full
   text/ar5iv, not secondary paraphrase), since WP1's derivation needed the *exact*
   coupling structure, not a remembered summary. Key finding, load-bearing for
   everything that follows: **AeST's matter action is $S_m[g]$ alone — one metric, no
   disformal $\hat g$** — a deliberate departure from TeVeS, stated explicitly in the
   founding paper as what fixes both the lensing and the GW170817 tensor-speed
   problems. This corrects the proposal's own K5/M3 language (which presupposes a
   $\hat g$ distinct from $g$).

2. **Derived the frame map.** M1 (foliation) is a direct, near-trivial identification:
   AeST's FRW cosmic time and aether-comoving spatial slices *are* cdot-7's coordinate
   time and static Euclidean space. The Planck-unit relabeling principle (coordinate
   quantities = physical quantities expressed in a bookkeeping-$c(t)$ Planck-unit
   system, with $G,\hbar$ conventionally fixed) reproduces cdot-7's mass ($c^{1/2}$),
   length ($c^{-3/2}$), and frequency ($c^{5/2}$) exponents directly. The redshift law
   forces (not merely permits) $c(t)=c_0(a(t)/a_0)^{2/3}$ by requiring cdot-7's
   internally-consistent bookkeeping redshift to equal AeST's actual physical redshift
   — and this relation independently reproduces cdot-7's own previously-derived
   $H_0^\text{obs}=\tfrac32\dot c_0/c_0$, a non-trivial cross-check not built in by
   construction. The density map ($p\to p-7$) was verified as a corollary of the same
   single relation for both matter ($p=5/2\to-9/2$, matching $(1+z)^3$) and radiation
   ($p=1\to-6$, matching $(1+z)^4$) — cdot-7 Foundation §2.4's "two independent hits on
   exponents not fitted to produce them" are shown to be one theorem, not two
   coincidences.

3. **Bonus discharge**: cdot-7 Foundation §6 item 9 ("comoving number density constant,
   assumed not derived") is resolved as ordinary FRW particle-number conservation, on
   the same footing as $\Lambda$CDM's own homogeneity assumption.

4. **M2 explicitly left open, correctly** — identifying $a_0=\lambda\dot c$ with
   $Q_0(t)$ requires AeST's own Friedmann equation (extracted this session:
   $H^2+k/a^2=\tfrac{8\pi\tilde G}3\rho-\tfrac13(F-QF_Q)+\Lambda/3$, $F_Q\propto
   a^{-3}$), which is dynamical content belonging to WP2/WP3, not WP1's kinematic
   scope.

5. **Verdict: WP1's success condition (exponents $\tfrac32,\tfrac52,p{-}7$) is met
   exactly; the kill condition does not trigger and is moot** (no disformal map was
   available or needed — the single-metric AeST kinematics is simpler than the
   proposal anticipated). **The central honest finding, stated plainly**: at the
   kinematic level, cdot-7's entire "variable $c$" apparatus is exactly equivalent to
   ordinary FRW cosmology with fixed local physics under one forced unit rescaling —
   zero new physical content at this level. cdot-7's distinctive claims live entirely
   in the *dynamics* (the census, the closure, the $a_0$ portal), which is exactly
   what WP2–WP4 exist to build and is now the *entire* remaining test of cdot-8's
   worth.

**Files produced:** `Update-WP1-DictionaryAsFrameMap-2026-07-12.md`, this log.

**Open items handed forward:** the $\hat g\to g$ language correction to Proposal K5/M3
(alongside WP0's six carry-forward amendments, still queued for the next consolidation
pass); WP2 (the covariant census as a foliation integral over $\Sigma_t$, using the now
load-bearing $c(t)=c_0(a(t)/a_0)^{2/3}$ relation) is next, pending author review of this
pass. cdot-7's own priority queue, above all the KATRIN clock, remains unstarved.

---

## Entry 2 — WP1 reopened narrowly: the two-clock dictionary (2026-07-12)

**Prompt (verbatim):**
> Advice added to the proposal directory.

(In response to a WP3 escalation over a distance-formula tension — see
`cdot-8/WP3/Update-WP3-DistanceTension-2026-07-12.md` — the author consulted a separate
advisory session, which produced `cdot-8/proposal/Advisory-WP3-TwoClocks-2026-07-12.md`
and `twoclocks_check.py`, directing WP1 to be reopened narrowly to *covariantly verify*
a proposed two-clock resolution, not accept it on the strength of its own,
self-described-as-unverified intra-cdot-7 argument.)

**Summary of work performed:**

1. **Independently re-verified every numerical claim** in the advisory's script by a
   different method (`scipy` unavailable in this environment; used the fixed-point
   ODE's closed-form solution instead of numerical integration) — full agreement to
   the reported precision on all five checks.

2. **Found and fixed the actual gap in WP1**, rather than accepting the advisory's own
   argument at face value: WP1 §3 applied its Planck-unit relabeling rule to mass,
   length, and frequency, but silently exempted *time itself* from the same treatment
   (tacitly setting $t_\text{coord}=\tau_\text{phys}$ without deriving or stating that
   choice). Applying the identical rule to time gives $d\tau/dt_\text{coord}=(c/c_0)^{5/2}$
   — the advisory's proposed relation, now derived as a missing row of WP1's own
   dictionary rather than accepted as an external hypothesis. Cross-checked
   independently against Foundation §5.4's own quoted $a_0\propto c^{5/4}$ — exact
   match.

3. **Found the resolution already implemented, silently, in cdot-7's own pre-cdot-8
   code**: `Fable-1/closure_dynamics.py` (2026-07-07) integrates a three-component
   state `[r, tau_proper, t_coord]` with $d\tau_\text{proper}/dt_\text{coord}=a_\text{code}
   ^{2.5}$ — which, once a notational trap is untangled (that file's own "$a$" is
   $c/c_0$, not WP1's FRW scale factor), is exactly $(c/c_0)^{5/2}$. Its own validation
   line confirms $\tau_\text{proper}$ (not $t_\text{coord}$) gives the finite,
   EdS-matching $\tfrac23H_0^{-1}$ age quoted in Foundation §5.2 — the project's own
   authors had already, correctly, kept the two clocks distinct in code, without ever
   stating the distinction as a general principle in prose. That silent gap between
   code and documentation is what let WP1 miss it.

4. **Addressed all of the advisory's directives**: 1(a)-(d) (both clocks as frame
   objects; independent re-derivation; covariant distance check; lapse ratio recorded)
   fully satisfied. 2(a) today-coincidence confirmed structurally, not just
   numerically. 2(b): inspected `four_term_fit.py` directly — its distance
   calculation is purely algebraic in $r(a)$, with no time integral at all, so the SN
   photometry fit was never exposed to the coordinate/proper-time issue; no re-run
   needed. 2(c): fixed-point $\hat a_0(z)\propto(1+z)^{3/2}$ compared against
   Foundation §5.5's fitted values — reasonably consistent, expected deviation from
   being off the fixed point. 2(d): the two clocks coincide exactly at $t_0$, so the
   $H_0$ calibration is clock-unambiguous. 3: the 12.9 Gyr four-term-fit age's exact
   provenance script was not directly located (only the fixed-point demo's age was
   traced), so this is reported as a strong structural inference, not a direct
   confirmation — flagged with that caveat for the consolidator, no cdot-7 file
   touched.

**Files produced:** `Update-WP1-Addendum-TwoClockDictionary-2026-07-12.md`, this entry.

**Open items handed forward:** the one-paragraph Foundation documentation fix (state
the $t$-vs-$\tau$ distinction and the $(c/c_0)^{5/2}$ relation explicitly) for the
consolidator; the 12.9 Gyr age provenance remains an inference, not a direct trace —
worth confirming if a session has time; WP3 is unblocked with a precise target
($H_\tau^2\propto a^{-3}$ fixed point plus fitted departure, evaluated on matter's
proper time). cdot-7's own priority queue, above all the KATRIN clock, remains
unstarved throughout.
