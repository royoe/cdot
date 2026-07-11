# Update — Radiation-Era Closure, First Attempt (Foundation.md §6 item 5)

*Session: 2026-07-10. Status: proposed — for cross-check and merge, not yet applied.
Companion files: `SessionLog-2026-07-10.md` (full prompt-by-prompt record),
`radiation_closure.py` (every number below is independently reproducible by running
it — not merely asserted).*

**Note on sourcing:** this session worked from `project_knowledge_search` retrieval,
not a full linear read of `Foundation.md`/`ResearchNotes.md`. Section numbers below
(§2.1, §5.6, §6 item 5, etc.) are as they stood at the point of retrieval; whoever
merges this should treat exact placement and cross-reference numbering as needing a
final check against the live files, not as guaranteed correct.

---

## What this update covers, and what it deliberately doesn't

Extends the matter-only closure of §2.1/§2.2 to include a radiation term, far enough
to say something concrete about matter-radiation equality and the AQUAL operating
point through recombination. **Does not** touch the perturbation/structure sector
(§6 item 6) — no acoustic peaks, no CMB anisotropies, no BAO. Everything here is
background-history only: a smooth trajectory and where it kinks, not oscillations in
it. That distinction was the opening question of this session and is the one thing
that should not get lost in a merge.

---

## Part A — Proposed changes to `Foundation.md`

### A.1 — Amend §0's scope-limit statement

Current text states the closure sources $c(t)$ from rest mass only and is scope-limited
to $z\ll z_\text{eq}$. Propose amending to note this is now partially lifted:

> **Scope limit, updated.** The Machian closure (§2) can now be extended to include a
> radiation term (§2.3), tested numerically from today through matter-radiation
> equality and recombination out to $z\sim10^6$. This extension rests on two
> additional assumptions beyond §2's premises — conserved coordinate photon number
> (paired with item 9's particle-number assumption) and a specific, scope-motivated
> choice for how radiation sources the AQUAL closure (§2.3) — and does not yet cover
> $e^+e^-$ annihilation, the QCD transition, or earlier epochs ($z\gtrsim10^9$), nor
> does it touch the perturbation/structure sector (item 6).

### A.2 — New subsection, §2.3: Extending the closure to the radiation era

**Proposed new content**, placed after §2.2:

> ### 2.3 Extending the closure to the radiation era
>
> §2.1's $M_h(t)$ counts rest mass only. Extending premise 2's "number conserved"
> logic symmetrically to photons — a new assumption, not yet justified any more than
> item 9's particle-number assumption is — gives a conserved coordinate photon number
> density $n_\gamma$. Combined with §3.3's already-established per-photon coordinate
> energy law $E_\gamma(t)=\hbar k\,c(t)$ (from the conserved wavenumber $k$, not
> conserved frequency), every photon present at time $t$ has energy $\propto c(t)$
> regardless of emission time, giving
> $$u_\gamma(t)=n_\gamma\langle\hbar k\rangle\,c(t)\ \propto\ c(t)^{+1},\qquad
> \rho_\gamma^\text{eff}(t)\equiv\frac{u_\gamma(t)}{c(t)^2}\ \propto\ c(t)^{-1}.$$
> This is the opposite sign from matter's $\rho_m\propto c^{+1/2}$: toward genesis
> matter's contribution vanishes while radiation's diverges, so a crossover epoch —
> this framework's own analog of $z_\text{eq}$ — must exist.
>
> **Cross-check.** A general coordinate$\to$local dictionary, built from §3.1's own
> local length ($\propto c^{-3/2}$) and frequency ($\propto c^{5/2}$) scalings, maps a
> coordinate density $\propto c^p$ to a local density $\propto c^{p-7}$. Applied to
> $u_\gamma\propto c^1$: predicts $\hat u_\gamma\propto(1+z)^4$, matching §10's already
> -established result exactly. Applied to matter's $\rho_mc^2\propto c^{5/2}$: predicts
> $\hat\rho_m\propto(1+z)^3$ — not previously stated in this document, but exactly the
> standard matter-dilution law. Two independent hits on quantities not fitted to
> produce them.
>
> **The sourcing prefactor.** Radiation's contribution to the AQUAL closure is taken as
> $\rho_\gamma^\text{eff}=u_\gamma/c^2$ (no pressure correction) rather than the GR-motivated
> $2u_\gamma/c^2$ that a $w=\tfrac13$ fluid would carry via $\rho+3p/c^2$. This is not a
> simplification of convenience: AQUAL's field equation (premise 4) is a genuinely
> Newtonian Poisson equation, $\nabla^2\Phi=4\pi G\rho$ in the $\mu\to1$ limit — the
> $\rho+3p/c^2$ correction is a feature of *General Relativity's* field equations
> (visible already in GR's own weak-field/Tolman-mass limit, not only the Friedmann
> acceleration equation), which this framework has explicitly declined to build
> (§0's scope reduction; item 7). $u/c^2$, from mass-energy equivalence alone, is the
> only correction AQUAL's literal structure can express. Adopted as the working
> choice; revisit if item 7 is ever built.
>
> **The extended closure and its two fixed points.** With
> $\rho_\text{tot}(c)=\rho_0(c/c_0)^{1/2}+\rho_{\gamma,0}(c/c_0)^{-1}$, §2.2's argument
> becomes $x=\mu^{-1}\!\left(R_h^2/(B_m^2c^{3/2})+R_h^2/(B_\gamma^2c^3)\right)$ — a sum
> of two differently-scaling terms, so §2.2's $x=$const solution survives only as an
> asymptote on either side. Repeating §2.2's own fixed-point method for a general
> source $\rho\propto c^n$: kinematics ($\dot R_h=c$) force $R_h\propto c^{1-n/2}$,
> and matching against the AQUAL closure's own $\dot c$ pins
> $$x_*(n)=\frac{1-n/2}{\kappa\lambda},$$
> independent of $\mu$'s functional form. Matter ($n=\tfrac12$) reproduces §2.2's
> $x_*=3/(4\kappa\lambda)$ exactly. Radiation ($n=-1$) gives a **second fixed point**,
> $$x_*^{(\text{rad})}=\frac{3}{2\kappa\lambda}=2\,x_*^{(\text{matter})}$$
> — exactly double, also $\mu$-independent. Using the four-term fit's $\kappa\lambda=
> 0.436$: $x_*^\text{(matter)}=1.72$ (as in §2.2), $x_*^\text{(rad)}=3.44$ — still
> squarely in AQUAL's transition zone, not deep-Newtonian; this framework's own
> self-similar structure means the early universe does not automatically simplify the
> way it does in standard cosmology (§4: $a_0=\lambda\dot c$ is tied to the same
> solution as $g_h$, so $g_h/a_0$ need not grow large just because $c$ is small).
>
> **The crossover.** Setting the two density terms equal gives a closed form using
> only already-fitted quantities:
> $$1+z_\text{eq}=\frac{\rho_0}{\rho_\gamma^\text{eff}(t_0)}.$$
> Numerically (measured CMB temperature, this document's own $\Omega_\text{closure}$):
> $z_\text{eq}\approx1466$ at the current working value ($\Omega_\text{closure}=0.074$),
> ranging to $\approx2656$ under the earlier SN+$a_0(z)$-only convention (§6 item 1 /
> ResearchNotes §13) — systematically below standard cosmology's $\approx3400$, as
> expected since $\Omega_\text{closure}\ll\Omega_m^{\Lambda\text{CDM}}$ by this
> framework's own design.
>
> **The trajectory through the crossover, integrated numerically.** Recast as
> $dr/ds=\kappa\lambda\,x(r,s)\,r$ with $r\equiv R_h/R_{h,0}$, $s\equiv\ln(c/c_0)$,
> and integrated backward from today's actual operating point ($x_0=1.10$, §5.5/§5.6):
> $x(z)$ recovers to the matter fixed point ($1.72$) by $z\sim10$ — a numerical
> confirmation of §2.2's "negligible in the past" instability claim — holds near
> $1.72$–$2.0$ out to $z\sim400$, rises smoothly over **2–3 e-folds in $z$** (not a
> discontinuity) through the crossover, and settles at the radiation fixed point
> ($3.44$) by $z\sim10^5$–$10^6$, exactly as predicted. **At $z_\text{recomb}\approx
> 1100$, $x\in[2.14,2.37]$** (using the adopted $u/c^2$ prefactor; up to $2.67$ under
> the un-adopted $2u/c^2$ alternative) across every $\Omega_\text{closure}$ convention
> tried — substantially (25–45%) above the matter-only value in every case. **Any
> future treatment of recombination-era dynamics in this framework should use this
> value, not $x_*=1.72$.**

### A.3 — §6 item list amendments

Propose updating item 5 and adding new sub-items:

> 5. **Radiation-era closure — substantially advanced (§2.3), not complete.** The
>    two-fluid (matter+photon) extension is derived and numerically verified from
>    today through recombination and deep radiation domination ($z\lesssim10^6$).
>    Remaining, explicitly flagged: (a) coordinate photon-number conservation is an
>    unforced assumption, paired with item 9, and known to fail once genuine
>    particle-creating processes become relevant; (b) **a third, mass-threshold term
>    for neutrinos is needed, not yet built** — using this document's own fitted
>    $\Sigma m_\nu=1.374$ eV (§5.6), the neutrino relativistic$\to$non-relativistic
>    transition lands at $z\approx2733$, at the edge of the $z_\text{eq}$ range found
>    above, meaning the two-fluid split is incomplete precisely where it matters most;
>    (c) $e^+e^-$ annihilation and the QCD transition are not included — real, sized
>    kinks (§ResearchNotes, order-of-magnitude only) but confined to $z\gtrsim10^9$,
>    outside anything tested here.
> 9. *(cross-reference added)* — see item 5(a) above; the radiation-era extension
>    inherits this item's unresolved status rather than resolving it.

---

## Part B — Proposed new `ResearchNotes.md` section

*(Full derivation trail — Steps 1–5, including the Step 5 material that is
estimate-level and should **not** be promoted into `Foundation.md` proper until it's
derived to the same standard as Steps 1–4.)*

> ## §16. The Radiation-Era Closure: First Attempt
>
> Prompted by a direct question about how varying $c$ and particle-species
> domination would interact in earlier epochs, and whether species-domination
> transitions would produce "bursts" with observable (the question specifically
> raised "acoustic") signatures.
>
> **Opening distinction, load-bearing throughout.** Two mechanisms were separated at
> the outset: background-history features (a species-domination transition changing
> $M_h(t)$'s functional form, producing a kink in $\dot c(t)$'s history) versus
> genuine acoustic oscillations (a coupled photon-baryon fluid's pressure-vs-gravity
> standing wave, frozen at decoupling — item 6, gated, and flagged by this project's
> own cdot-4/cdot-5 history as its most dangerous territory). Everything below is the
> former. The latter is untouched.
>
> **A structural note surfaced before any radiation term was added.** §2.2's fixed
> point $x_*=g_h/a_0\approx1.72$ holds arbitrarily far into the past on the
> matter-only closure, because $a_0=\lambda\dot c$ is tied to the same self-similar
> solution as $g_h$ — confirmed below to extend to the radiation-dominated regime too
> (a second, different, but equally non-Newtonian fixed point, $x_*^\text{rad}=3.44$).
> Unlike standard cosmology, this framework does not automatically simplify to
> deep-Newtonian Sciama early on.
>
> **§16.1 Step 1 — coordinate scaling of the radiation source.** [full derivation as
> in §2.3 above, plus:] The photon-number-conservation assumption is new and unforced
> — paired with item 9, not resolved by it. The $u/c^2$ vs. $2u/c^2$ sourcing
> ambiguity was initially left open with both options carried explicitly.
>
> **§16.2 Step 2 — the extended closure, two fixed points, the crossover.** [as in
> §2.3.] Verified `radiation_closure.py::fixed_point(0.5)` and `fixed_point(-1)`
> reproduce $1.72$ and $3.44$ exactly, independently of `mu`'s functional form (never
> evaluated in the derivation). $z_\text{eq}$ computed across all three standing
> $\Omega_\text{closure}$ conventions (§13's $0.134/0.115/0.104$ three-way spread,
> using the current working $0.074$ from the four-term mass-census fit as primary)
> and both sourcing options: $z_\text{eq}\in[730,2660]$.
>
> **§16.3 Step 3 — numerical integration through the crossover.** ODE recast in
> $s=\ln(c/c_0)$, integrated with `scipy.integrate.solve_ivp` (`rtol=1e-9`) from
> today's actual $x_0=1.10$ backward to $z\sim10^6$, for all four
> $(\eta,\Omega_\text{closure})$ combinations. $x(z)$ recovers to $1.72$ by $z\sim10$,
> transitions over 2–3 e-folds in $z$, settles at $3.44$ by $z\sim10^5$–$10^6$. At
> $z_\text{recomb}\approx1100$: $x\in[2.14,2.67]$ across all combinations (narrowing
> to $[2.14,2.37]$ once §16.4 adopts $\eta=1$). Reframed the opening question's
> "burst" as a real, quantified, multi-e-fold kink — not a discontinuity.
>
> **§16.4 Step 4 — resolving the sourcing prefactor.** Traced the $2u/c^2$ option to
> GR's field-equation structure specifically (visible already in GR's weak-field
> Tolman-mass limit, not only the cosmological acceleration equation) — something
> AQUAL's literal, non-relativistic Poisson equation has no structure to express.
> Checked whether an internal conservation law (the Bianchi-identity route that fixes
> this in standard cosmology) could force a value here instead of relying on a scope
> argument: no — that route needs an expanding volume doing work against pressure,
> with no analog under premise 1's static space, and this framework's matter sector
> isn't "energy conserving" in the naive sense either ($m(t)\propto c^{1/2}$ already
> grows rest energy over time). **Adopted $\eta=1$ ($u/c^2$, no pressure term) as the
> working choice** — the option licensed by what premise 4 says as written, not
> merely the conservative one — flagged for revisiting only if a relativistic
> completion (item 7) is ever built.
>
> **§16.5 Step 5 — multi-species (estimate-level, not derived to Steps 1–4's
> standard).** Standard always-relativistic neutrino treatment would just rescale
> $\rho_{\gamma,0}$ by $1+\tfrac78N_\text{eff}(4/11)^{4/3}\approx1.69$ — no new
> structure. Using **this document's own fitted mass** (§5.6, $\Sigma m_\nu=1.374$
> eV) instead: $\hat T_{\nu,0}=(4/11)^{1/3}\hat T_{\gamma,0}\approx1.945$ K,
> $m_\nu=0.458$ eV per species (three quasi-degenerate), giving a
> relativistic$\to$non-relativistic transition at $1+z_{\nu,\text{nr}}\approx2733$ —
> at the top edge of §16.3's own $z_\text{eq}$ range. **This is the one Step 5 finding
> judged solid enough to carry into `Foundation.md`'s item list** (§6 item 5(b)
> above): it connects two already-existing, independently-arrived-at numbers in this
> project ($\Sigma m_\nu$ from the mass census, $z_\text{eq}$ from this session), not
> a new free parameter. The fix (a genuine relativistic Fermi-Dirac energy-density
> term for the transitioning neutrino component, replacing the crude mass-threshold
> marker used here) is not attempted. Separately: standard entropy-transfer
> bookkeeping gives $e^+e^-$ annihilation a real kink ($u_\gamma$ boosted
> $(11/4)^{4/3}\approx3.85\times$ relative to naive extrapolation) at
> $1+z\approx2.2\times10^9$ — confirmed this requires **no correction** to any result
> already computed (Steps 1–4's coordinate law, anchored to today's measured CMB
> temperature, is exact down to, and including, everything already tested); it would
> only matter if extended past this much deeper epoch. QCD transition and earlier:
> real, deeper still, not attempted.
>
> **Ledger for this attempt, precisely, in the style of §13/§14.** Derived and
> cross-checked at least two independent ways: the radiation scaling exponent
> ($c^{+1}$/$(1+z)^4$), the matter local-density law ($(1+z)^3$, not previously
> stated), both fixed points ($1.72$, $3.44$, exactly double), the crossover formula.
> Derived once, numerically verified, not independently cross-checked a second way:
> the full trajectory shape and the $x(z_\text{recomb})$ values. Argued from scope
> rather than derived: the $\eta=1$ sourcing choice. Estimated, not derived: every
> Step 5 number (neutrino threshold redshift order-of-magnitude marker, $e^+e^-$ kink
> size and epoch). Not attempted: the neutrino third-term fix, $e^+e^-$/QCD in
> coordinate-frame form, anything in the perturbation sector.

---

## Files in this delivery

- `Update-RadiationEraClosure-2026-07-10.md` — this document.
- `SessionLog-2026-07-10.md` — full prompt-by-prompt record, six entries, timestamped.
- `radiation_closure.py` — every numerical claim above, independently re-runnable
  (`python3 radiation_closure.py` reproduces all of Steps 1, 2, 3, and 5's numbers
  in one pass).
