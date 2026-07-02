# Update — PPN and Lensing: Checking the PV-Symmetry Assumption (2026-07-02)

*Session type: constructive. Question posed: the working assumption has been that the
model's symmetry with Polarizable Vacuum (PV) theory (Dicke 1957; Puthoff 2002) preserves
alignment with GR's weak-field/PPN phenomenology (light bending, Shapiro delay,
gravitational redshift, perihelion precession). This session checks that assumption. The
answer: **alignment is preservable — and, given the model's own EM sector, the local PV
dictionary is uniquely forced by two data points — but it is not automatic.** It requires
reinstating, locally, the exact PV mass law the model rejected cosmologically, as an
explicit new two-regime premise. One uniform dictionary demonstrably fails. Two genuinely
new constraint classes are also identified (the K-field coefficient derivation, and
preferred-frame PPN parameters α₁/α₂).*

---

## 1. Setting Up the Check: Two Separable Ingredients

"PV symmetry" bundles two logically distinct things, which respond to different
observations:

**(a) The K-field equation** — what a local mass does to the vacuum index:
$K(r) = 1 + A\,\frac{GM}{rc^2} + \dots$ with coefficient $A$ set by the gravity
mechanism. In Puthoff's PV, $K = e^{2GM/rc^2}$, i.e. $A = 2$.

**(b) The matter-response dictionary** — how clocks, rulers, and masses respond to a
given local $K$. Here the model and PV **already disagree**, because the model broke from
PV cosmologically (invariant mass, T4/T8; invariant $G$, T8):

| Quantity | PV dictionary (local) | Model dictionary (cosmological) |
|---|---|---|
| $\epsilon_0,\mu_0$ | $\propto K$ | $\propto K$ (same — EM-forced, Core §2) |
| $m$ | $\propto K^{3/2}$ | $\propto K^0$ (invariant) |
| $E,\ \nu_\text{atomic}$ | $\propto K^{-1/2}$ | $\propto K^{-2}$ (i.e. $\propto c^2$) |
| lengths ($a_B$) | $\propto K^{-1/2}$ | $\propto K^{+1}$ (i.e. $\propto c^{-1}$) |

Because both share the EM sector, **light propagation depends only on (a)**: the index
seen by light is $n = c_0/v = K$ exactly (from $c = 1/\sqrt{\epsilon_0\mu_0}$ with both
$\propto K$). Clocks and orbits depend on (b). This decomposition is what makes the
assumption checkable.

## 2. The Check: Bending Pins A; Redshift Pins the Local Mass Exponent — Uniquely

Let the local mass exponent be $m \propto K_\text{grav}^{\sigma}$ (σ free for now). Then
the atomic frequency is $\nu \propto m\,\epsilon_0^{-2} \propto K^{\sigma-2}$ (Rydberg,
$e,h$ invariant — the model's own machinery, Core §5a, applied to local $K$).

**Test 1 — light deflection and Shapiro delay.** With $n = K = 1 + A\,GM/rc^2$, the
deflection is $\delta = 2A\,GM/(bc^2)$. The observed $1.75''$ ($= 4GM/bc^2$; VLBI:
$\gamma - 1 \sim 10^{-4}$; Cassini: $\gamma-1 = (2.1\pm2.3)\times10^{-5}$) **forces
$A = 2$**, independent of the matter dictionary.

**Test 2 — gravitational redshift.** Clock-rate shift $= (\sigma-2)\,A\,\Phi/c^2$; the
observed GR value ($-|\Phi|/c^2$; Galileo GREAT eccentric-orbit test:
$(0.19\pm2.48)\times10^{-5}$ fractional accuracy on the GR prediction) requires
$(\sigma-2)A = -1$. With $A=2$ pinned by Test 1:
$$\boxed{\sigma = 3/2\ \text{— exactly, and uniquely, the PV mass law.}}$$

**Both failure branches are decisively excluded:**
- Keep the model's cosmological dictionary locally ($\sigma=0$): predicted gravitational
  redshift is **4× GR** — excluded by GPS/Galileo at $\sim10^4\sigma$.
- Renormalize the K-field to fix the clocks instead ($A = 1/2$ with $\sigma=0$):
  predicted light bending is **¼× GR** ($0.44''$) — excluded by VLBI/Cassini.
No intermediate $(A,\sigma)$ pair exists: Test 1 fixes $A$ with no reference to matter,
then Test 2 fixes $\sigma$. One vacuum index cannot serve both jobs under the
invariant-mass dictionary.

**Everything else then falls out matching PV automatically:**
- Rulers: $a_B \propto \epsilon_0/m \propto K^{1-3/2} = K^{-1/2}$ — matching the GR
  isotropic spatial metric factor, so light-based and ruler-based $\gamma$ agree
  ($\gamma = 1$).
- Rest energy $mc^2 \propto K^{3/2-2} = K^{-1/2}$: **all local energies scale
  uniformly**, so the equivalence principle is composition-clean (MICROSCOPE $10^{-15}$
  safe), consistent with T21's uniform-energy pattern.
- Perihelion precession / $\beta$: with the full PV dictionary the local sector *is*
  Puthoff's exponential-metric PV, which reproduces $\beta = 1$ and the classical tests
  to current precision (deviations from GR arise at higher orders and in the strong
  field, below present solar-system sensitivity).

## 3. The Verdict on the Assumption

**Half right, and the right half is stronger than assumed.** PV alignment is *not*
automatic from symmetry — the model's empirically forced breaks from PV (invariant mass,
invariant $G$) are precisely what destroyed the automatic alignment, and a uniform
dictionary fails observationally by factors of 4. But alignment is *recoverable*, and
better: given the model's EM sector, the local PV dictionary is **uniquely selected by
the data** (bending → $A=2$; redshift → $\sigma=3/2$). The assumption should therefore
be upgraded from "symmetry preserves alignment" to a derived-but-unexplained structural
statement:

> **Two-Regime Dictionary (proposed new premise, to be added alongside premise 3):**
> matter responds to *spatial/gravitational* vacuum-index variation with the PV
> exponents ($m \propto K_\text{grav}^{3/2}$, all energies $\propto K_\text{grav}^{-1/2}$),
> and to the *cosmological temporal* variation with invariant mass
> ($m \propto K_\text{cosmo}^{0}$, all energies $\propto c^2$).

**An elegant reframing of an old fork.** In redshift-power language, the local sector
has $\nu \propto c_\text{local}^{1/2}$ — i.e. $P = 1/2$, *the PV-mass branch that T1
showed gives an infinite proper age and T4 rejected cosmologically*. The
invariant-vs-PV-mass fork (T8 §"Why Mass is Invariant") is thus resolved not by
discarding the PV branch but by **regime-splitting**: the PV branch governs space
(static gravity), the invariant branch governs time (cosmology). Both are now
empirically forced in their own domains — by Cassini/GREAT locally, and by
Pantheon+/LLR cosmologically.

**Consistency sweep (all pass):**
1. *Premise 3 wording*: Core states $m$, $G$ are "local invariants, **independent of the
   cosmological vacuum state**" — as written, this already permits local-gravitational
   dressing; the new premise is a clarification, not a contradiction. The wording should
   nonetheless be made explicit.
2. *LLR*: the local dressing drifts only through $K_\text{grav} \propto c^{-2}(t)$;
   with $K_\text{grav}(\text{Moon}) \sim 10^{-11}$, secular effects are
   $\sim10^{-22}$–$10^{-19}$/yr — utterly negligible. The ×720 refutation of
   cosmological $G\propto c^{-2}$ is untouched.
3. *Cosmological redshift derivation*: galaxy/cluster potentials contribute only the
   standard $\sim10^{-5}$ gravitational redshifts astronomers already handle; the
   squared law is unaffected.
4. *$\alpha$*: locally invariant too ($\epsilon_0 c$ invariant regardless of regime) —
   consistent with null clock-comparison and tower experiments.
5. *T14 inertia no-go*: no contradiction, but the wording needs care — the no-go
   concerns momentum-transfer origination of inertia; the PV dressing is a
   vacuum-polarization modification of the *value* of $m$. Premise 3 should read:
   axiomatic baseline $m_0$, locally dressed as $m_0 K_\text{grav}^{3/2}$.

## 4. What the Symmetry Does NOT Deliver (new open items)

1. **The coefficient $A = 2$ must be derived, not imported.** This is the sharpened form
   of T14 open item 5 (promoted to top priority in the Test Battery update): the
   connecton diffusion mechanism produces the Newtonian potential $\phi \propto M/r$;
   the required identification is $\delta K = 2\phi/c^2$ — i.e. the connecton density
   perturbation must map onto the vacuum polarizability with exactly the
   time-plus-space factor 2. In Puthoff's PV this comes from a tuned Lagrangian; in the
   connecton picture it must come from how a local connecton overdensity modifies
   $\epsilon_0,\mu_0$. Until derived, $A=2$ is an assumption at exactly the same
   epistemic level as invariant $G$ — empirically forced, theoretically owed.
2. **Preferred-frame PPN parameters $\alpha_1, \alpha_2$ — a genuinely new constraint
   class.** The model has a real preferred frame (the static sea; the solar system
   moves at $\sim370$ km/s relative to it, $v/c \approx 1.2\times10^{-3}$).
   Preferred-frame gravity generically produces PPN $\alpha_1$ (bounded $<10^{-4}$) and
   $\alpha_2$ (bounded $<4\times10^{-7}$ from the Sun's spin-axis alignment,
   Nordtvedt 1987) effects at order $(v/c)^2 \sim 1.5\times10^{-6}$ — i.e. the raw
   scale sits *above* the $\alpha_2$ bound, so the model needs the coefficient to be
   suppressed or zero. Puthoff's PV analysis does not cover a moving frame through the
   polarizable medium. Whether connecton/PV gravity in the sea frame generates
   $\alpha_2 \neq 0$ is now the **sharpest unexamined solar-system threat** to the
   whole program — potentially more dangerous than the (now-resolved-in-principle)
   $\gamma$ question.
3. **The seam rationale.** Why does matter distinguish spatial gradients of $K$ from
   the global secular level? Candidate (relational): local $K_\text{grav}$ is a
   *redistribution* of connecton density at fixed global count, while cosmological
   $K_\text{cosmo}$ is the count level itself; the relational principle anchors all
   scales to the global count, so local rearrangements dress particle self-energies
   (PV-style polarization) without re-anchoring them. Speculative — recorded as the
   open theoretical task attached to the new premise, parallel to the standing
   invariant-$G$/invariant-$m$ debts (T8).
4. **Frame-dragging / gravitomagnetism.** Gravity Probe B and LAGEOS test the
   Lense-Thirring precession at ~20% and ~2% respectively; scalar PV has no natural
   frame-dragging, but the connecton picture *does* have a gravitomagnetic-type field
   ($B_c$, T14/T17/T19). Whether the $B_c$ machinery reproduces the GR
   Lense-Thirring value around a spinning mass is an untested, two-sided check
   (could be a failure or a distinctive success). New open item.

## 5. Consolidated Edits (for merge)

| # | File | Edit | Type |
|---|------|------|------|
| 1 | Core_Principles.md premise 3 | Add the Two-Regime Dictionary: baseline $m_0$ invariant cosmologically; locally dressed $m = m_0K_\text{grav}^{3/2}$ (all local energies $\propto K^{-1/2}$); state that this is uniquely forced by bending ($A=2$) + gravitational redshift given the EM sector | New premise (forced) |
| 2 | T8 §"Why Mass is Invariant" | Reframe the fork: PV branch ($P=1/2$) governs local statics, invariant branch ($P=2$) governs cosmology — both empirically forced in-domain | Reframing |
| 3 | T1/T4 | One-line note: the rejected $P=1/2$ branch is not dead — it is the local sector | Cross-note |
| 4 | T14 open items | Sharpen item 5: derive $\delta K = 2\phi/c^2$ (the factor 2) from connecton diffusion; add $\alpha_1/\alpha_2$ preferred-frame check and Lense-Thirring/$B_c$ check; reword inertia no-go ("axiomatic baseline, locally dressed") | Open items (2 new) |
| 5 | Test Battery (T22 proposal) | Update Tier-1 item 3: $\gamma,\beta$ alignment resolved-in-principle via the forced local PV dictionary; the live solar-system threats are now $A=2$'s derivation and $\alpha_2 < 4\times10^{-7}$ | Update |
| 6 | New topic T23 (or T22 §) | "Local Gravity: the PV Correspondence and the Two-Regime Dictionary" — this document's content | New topic |

**Bottom line.** The assumption checks out in its conclusion but not in its reasoning:
alignment with PPN/lensing is preserved *only* by reinstating the full PV matter
dictionary locally — and, satisfyingly, the model's own EM sector plus two solar-system
measurements force exactly that dictionary, uniquely. The cost is one new explicit
premise (the regime split) carrying the same class of theoretical debt as invariant $G$;
the gain is that the old invariant-vs-PV mass fork becomes a both/and rather than a
rejection. The remaining genuine exposure in the solar system is no longer $\gamma$ or
the redshift — it is the underived factor 2 in the K-field equation and, above all, the
preferred-frame parameter $\alpha_2$, where the model's raw $(v/c)^2 \sim 10^{-6}$ scale
sits an order of magnitude above the observational bound unless the coefficient
vanishes.
