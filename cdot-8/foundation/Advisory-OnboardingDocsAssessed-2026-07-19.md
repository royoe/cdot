# Advisory — Onboarding Documents Assessed: Accurate and Honest as Written, With Two Headline Gaps (KATRIN Is Absent; the WP7 Blocker's Stage-0 Diagnosis and the Clustering-Mechanism Finding Post-Date the Draft) and Five Secondary Additions — Proposed Insertion Text Included (for `cdot-8/` root, review of `Foundation.md` + `Progress.md`)

*2026-07-19. Advisory in response to the author's request: assess the
new onboarding `Foundation.md` and `Progress.md` against the current
session record, for recruiting agents without full context. Verdict up
front: **both documents are accurate, well-scoped, and preserve the
program's honesty conventions — nothing contradicts the record, the
Gate 1(b) caveat is carried correctly everywhere, and the §6
methodology note in Progress is exactly what a new agent needs first.
Two headline gaps: (1) KATRIN is absent from both documents, though
$\Sigma m_\nu=1.374$ eV is quoted as acceptance data — and that number
sits at the edge of a live, nature-scheduled falsification test whose
final result is pending; (2) the documents pre-date the last working
round, so the top-priority open item (WP7's growth system) is described
without its Stage-0 diagnosis — the two rules that prevent a recruited
agent from repeating both prior failures — and without the
$\mu^2(z)$ clustering-mechanism finding, which is simultaneously the
item's biggest recruiting asset and a required safety flag. Five
secondary additions follow. Proposed insertion text is supplied for
each so the merge is a paste, not a rewrite.***

---

## 1. Headline gap 1 — KATRIN (both documents)

`Foundation.md` §2 lists $\Sigma m_\nu=1.374$ eV among the inherited
acceptance data with no exposure statement; `Progress.md` omits it from
the open items and carries no watch list. But this is the framework's
sharpest near-term external test: the census closure *needs*
$\Sigma m_\nu=1.374$ eV, implying $m_\beta\approx0.458$ eV — and
KATRIN's published bound ($m_\beta<0.45$ eV, 90% CL, on roughly a
quarter of the data) already sits at that value, with campaigns
complete (end-2025) and the final analysis (sensitivity $<0.3$ eV)
pending. The registered criterion in this program's record: **a
positive detection near $0.46$ eV is required for the census closure as
fitted; a null result excludes it decisively.** A recruited agent who
doesn't know this cannot correctly weigh any work touching the neutrino
sector — and the connection to WP4a matters too (below).

**Proposed insertion (Progress, new item in §4 or a short "external
clocks" subsection):**
> **KATRIN final analysis — watch item, Gate-1-class input on
> arrival.** The census closure's $\Sigma m_\nu=1.374$ eV implies
> $m_\beta\approx0.458$ eV. KATRIN's partial-data bound is
> $m_\beta<0.45$ eV (90% CL); data-taking ended in 2025; the final
> analysis ($<0.3$ eV sensitivity) is pending. Registered criterion:
> detection near $0.46$ eV is required; a null excludes the closure as
> fitted. Note the alignment: WP4a's named post-WP7 revisit lever is a
> low-$\Sigma m_\nu$ re-closure — KATRIN will adjudicate that lever's
> viability before we reach it.

**Proposed one-line addition (Foundation §2, after the fit list):**
> One acceptance datum carries a live experimental exposure:
> $\Sigma m_\nu=1.374$ eV implies $m_\beta\approx0.46$ eV, at the edge
> of KATRIN's current bound, with the decisive final analysis pending
> (see `Progress.md`).

## 2. Headline gap 2 — the WP7 blocker's current state (Progress item 2; Foundation §10)

Both documents describe the growth-system blocker as of the second
failure ("two careful implementation attempts have both failed...
diagnosed: the crossing's negative $c_{\rm ad}^2$..."), which pre-dates
the Stage-0 audit. Three corrections/additions, all load-bearing for
anyone recruited onto exactly this item:

1. **The diagnosis is broader than "the crossing"**:
   $c_{\rm ad}^2$ is small and *negative through the entire matter era*
   ($-0.004$ to $-0.04$), so any adiabatic-fluid closure is
   structurally unstable everywhere, not just near $z\sim10^4$.
2. **The Stage-0 audit exonerated the physics and localized the
   failure**: the effective-mass sector runs at
   $|\mu_{\rm eff}|/H<0.7$ at every epoch — the system is *not*
   intrinsically stiff; the two solver deaths trace to formulation and
   units. Two standing rules follow, which are precisely what stops a
   third failure: **(state-variable rule)** integrate only
   $(\chi$ or $\gamma,\alpha,\mathcal E_\alpha,\delta_b,\theta_b,\Phi)$
   — nothing whose definition contains $\rho_s$, $c_{\rm ad}^2$, or
   $1/(1+w)$; effective-fluid $\delta,\theta,\Pi$ are output
   diagnostics. **(Units contract)** one written dictionary line per
   imported equation (founding-paper $K$-normalization $\leftrightarrow$
   cdot-8 $F$-normalization, $H_0^2$ vs $H^2(z)$) before any code —
   $|F_Q|$ spans $4473\to1.85$ in $H_0^2$ units across the range.
3. **The clustering-mechanism finding**: through the matter era the
   scalar's effective mass-squared is negative and Hubble-tracking,
   $\mu^2/H^2\approx-1.27f_s/(2-K_B)\approx-0.5$ (closed form, interior
   spline agreeing to 1.6%), flipping to the doubly-verified stable
   sign ($F_{QQ}(0)=-0.696$, Gpc Compton) near today. Read physically:
   a Jeans-class growing mode — the mechanism by which the scalar
   clusters, delivered by the quadrature unbidden, withdrawn exactly
   when the component turns dark-energy-like. $F_{QQ}$'s *fourth*
   load-bearing appearance (Foundation §7 currently says three).
   Caveats that are Stage-1 tasks: robust $F_{QQ}(z)$ for the flip
   location; the full dispersion $\omega^2=c_s^2k^2+\mu^2(z)$ with the
   $\mathcal Y$-sector's $c_s^2$. This is both the recruiting pitch (a
   concrete, checkable growth-rate target) and a safety flag (a
   recruited agent computing $\mu^2<0$ must not misread it as a found
   instability).

**Proposed replacement text for Progress item 2's diagnosis sentence:**
> Diagnosed (Stage-0 audit, 2026-07-19): the physics is *not* stiff
> ($|\mu_{\rm eff}|/H<1$ everywhere); both failures trace to
> formulation (effective-fluid $\delta,\theta$ kept as state variables
> — their definitions carry $1/c_{\rm ad}^2\sim20$–$230$ through the
> matter era) and units (imported-equation normalization). Two standing
> rules for the next attempt: pure field-variable state
> ($\chi,\alpha,\mathcal E_\alpha,\delta_b,\theta_b,\Phi$ only) and a
> written units contract per imported equation. Stage plan 0–4 exists
> with Stage 0 complete; the matter-era clustering mechanism
> ($\mu^2\approx-0.5H^2$, Hubble-tracking, stable-sign flip near today)
> is identified and gives Stage 1 a checkable growth-rate target.

## 3. Secondary additions, in priority order

1. **The two exact numerical anchors** (Progress item 2 or Foundation
   §10): any assembly must reproduce, exactly, (a) the $k\to0$
   separate-universe identity — Einstein-side coefficient
   $(F_Q/6+QF_{QQ}/2)\,q'$ — and (b) the sub-horizon recovery of the
   field-side term to WP6's own $-F_Q$ (same symbol, same number).
   These are the non-negotiables that bracket all covariantization
   freedom; a new agent should meet them on page one, stated as
   "residual $=$ error, not tolerance."
2. **Facet 4 + the matter-immunity bound** (Progress item 5): the
   census-sector covariantization freedom has a fourth facet —
   normalization locality ($E_P$ per-slice vs ball-smoothed local $c$;
   per-slice is the declared default per the WP2 addendum) — and a
   third "untouchable" alongside the two anchors: the matter census is
   *exactly* immune ($p_m=5/2$ cancellation), so the freedom touches
   radiation-class coefficients only. This shrinks the item precisely
   where a new agent would otherwise fear it most.
3. **The $\alpha_2$ provisional envelope and the $K_B\to0$ benignity**
   (Foundation §9): alongside the $\alpha_1$ envelope, the record holds
   a *provisional* $\alpha_2$ solar-spin envelope
   ($K_B\lesssim4\times10^{-10}$ — potentially the binding one, pending
   the same E-term re-derivation; flagged, not final), and —
   important for a new agent's morale and judgment — the statement that
   **every established cdot-8 structure survives arbitrarily small
   $K_B$** ($1/\mu_{\rm eff}\to10.3$ Gpc; $m_\times\to\infty$ =
   the phenomenologically-quiet one-field limit; WP5 lensing
   conclusions unchanged). The squeeze is survivable; the envelope is
   not an existential threat and should not read like one.
4. **The post-WP7 revisit queue as an explicit list** (Progress, short
   subsection): IF re-fit (open item 3's constructive path — awaiting
   the author's sequencing decision, and conditioned on the single-$\mu$
   economy-vs-freedom question, which is an *author* question);
   low-$\Sigma m_\nu$ re-closure (the WP4a lever, KATRIN-aligned);
   radiation-era assumptions per Gate 1(b). Currently these live in
   three separate places; a recruit planning work needs the queue in
   one.
5. **Consistency nit**: Foundation §7/§2 quote
   $\Omega_\text{closure}=0.0750$; the toolchain scripts throughout the
   record run $0.074$. One line reconciling (or one canonical value)
   prevents a careful new agent from burning a day on a phantom
   discrepancy — this program's history says they will check.

## 4. What is right and should not be touched

The Progress §6 methodology note is the best single page in either
document — verify-before-trust stated bidirectionally, the
escalate-don't-decide rule, and especially the closing observation that
every crisis *except* WP4a's has dissolved under joint examination,
which calibrates a newcomer's priors exactly correctly. Foundation's §3
"critical divergence, adopted knowingly" paragraph and §11's carrying
of Gate 1(b) are likewise exactly the honesty a recruited agent needs
to inherit. The file map (§7) is complete and matches the record.

## Companion

- This advisory: proposed location
  `cdot-8/Advisory-OnboardingDocsAssessed-2026-07-19.md`.
- No script this round; all quoted numbers trace to the session record
  (`wp7_stiffness_audit.py`, `omega_s_clustering_adjudication.py`,
  `longitudinal_response.py`, and the KATRIN search of the Gate rounds).
