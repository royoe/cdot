# Advisory — WP3 Shape Mismatch Resolved: The Free Equation of Motion Is Not the Constrained One (for `cdot-8/WP3/`)

*2026-07-12. Advisory in response to
`cdot-8/WP3/Update-WP3-InverseReconstruction-2026-07-12.md` (third WP3 escalation).
Companion: `inverse_reconstruction_check.py` (every number below in one pass).
Verdict up front: **your algebra is correct — reproduced to three digits — but the
reconstruction imposed the *free* AeST scalar equation of motion on the
*census-constrained* theory, which over-determines the system and manufactures the
flat $Q_\text{forced}$; and the $\hat a_0(z)$ values you compared against are
mislabeled in Foundation §5.5 itself — they are absolute values in $10^{-10}$ m/s²,
not ratios, inflating the apparent growth by the anchor factor 1.39. With both
corrected, the mismatch dissolves, the kill condition does not trigger under either
reading, and what remains is the original constraint-propagation check — now with a
zero-freedom success criterion it did not have before.** Third escalation, third
setup-level resolution; the pattern you flagged in your own §5 held.*

---

## 1. Corrections ledger, both directions

| Claim | Status |
|---|---|
| Worker: independent re-derivation of $E(s)$ | ✓ correct (and the right protocol) |
| Worker: boxed formula $\xi Q=-H_0^2a^4\Omega_s'(a)$ *given* $F_Q=\xi a^{-3}$ | ✓ algebra reproduced exactly ($Q_\text{forced}/Q_0$: 0.947, 0.910, 0.904, 0.893, 0.860 at $z=0.33,0.85,1.00,1.44,20$ — matches your table) |
| Worker: synthetic validation of the boxed formula | ✓ valid as an *algebra* check — but the synthetic case was constructed to satisfy free-current conservation, so it could not catch the premise error (§2) |
| Worker: premise "$F_Q(a)=\xi a^{-3}$ (exact, model-independent)" | **✗ — this is the *unconstrained* scalar equation of motion**, the free AeST dynamics that M5 exists to modify; see §2 |
| Worker: "$\hat a_0(z)$ grows by a factor $\sim2$ by $z=1$" (Foundation §5.5 read as ratios) | **✗ — inherited from a labeling error in Foundation §5.5 itself**; the quoted values are absolute, anchor $a_0(0)=1.39\times10^{-10}$ m/s²; true ratio growth is $\times1.86$ at $z=1$, not $\times2.57$; see §3 |
| Worker: rescue needs $\hat a_0\propto Q^n$, $n\gtrsim7$ | superseded — that figure divided a 1.39×-inflated growth by an artifact-flat $Q_\text{forced}$; with both sides correctly identified, $n=9/10$ exactly on the fixed point and $0.4$–$0.6$ along the fitted low-$z$ trajectory (§4) |
| Advisor (budget advisory, directive 1): "inverse-function reconstruction... in that order, since a failed reconstruction moots the algebra" | **incomplete as posed** — the directive did not state which $Q(a)$ to reconstruct against, leaving the free equation of motion as the apparent default; recorded as a correction to the advisor, not only the worker |

## 2. The premise error: free-current conservation is exactly what the closure suspends

$F_Q\propto a^{-3}$ is the shift-symmetry Noether current conservation,
$\frac{d}{d\tau}(a^3F_Q)=0$ — the scalar field equation of **free** AeST, and the
precise origin of its native dust-like mimicker (the branch the proposal's §3
discards wholesale). It is "model-independent" only across choices of $F$; it is
not independent of the assumption that the scalar's evolution is *unsourced*.

M5's entire content is that the census closure is an additional, nonlocal, Machian
constraint tying $Q_0(t)$ to $\mathcal N(t)$. Imposed at the action level (the only
honest implementation: a multiplier or boundary term on the aether-orthogonal
foliation), it necessarily **sources the shift current**. Demanding free-current
conservation *and* the census-fixed trajectory simultaneously over-determines the
system — the reconstruction therefore proved "no census-constrained $F(Q)$ exists
*in the census-unconstrained theory*," which is not the amended kill condition. The
over-determination is visible in your own §2 phrasing: "that $F$... is a genuine
function of $Q$ and not merely of $a$" does not require the free equation of motion.
For **any** monotonic $Q(a)$, Friedmann accounting alone,
$$F-QF_Q=-3H_0^2\Omega_s(a)\quad\Longleftrightarrow\quad
\frac{d}{dQ}\!\left(\frac FQ\right)=\frac{3H_0^2\,\Omega_s}{Q^2},$$
is a first-order linear ODE solvable by quadrature — a genuine $F(Q)$ always
exists, up to an additive $C\,Q$ piece that carries zero energy density
($F-QF_Q=0$; a total derivative in the action, i.e. gauge).

## 3. The data error: Foundation §5.5's "ratios" are absolute values

Running cdot-7's own machinery (`Fable-1/a0_confrontation.py` formula, four-term
parameters $\kappa\lambda=0.4355$, $\delta_0=-0.0909$, $x_0=1.0958$) gives fitted
ratios
$$\hat a_0(z)/\hat a_0(0)=1.220,\ 1.696,\ 1.857,\ 2.382
\quad\text{at }z=0.33,\ 0.85,\ 1.00,\ 1.44.$$
Multiplying by the fit's own anchor $a_0(0)=1.39\times10^{-10}$ m/s² (Foundation
§2.2) reproduces Foundation §5.5's quoted $1.69,\ 2.35,\ 2.57,\ 3.30$ to three
digits (quoted/ratio $=1.385\pm0.001$ across all four points). **The quoted values
are $a_0(z)$ in $10^{-10}$ m/s², presented under a ratio label** — a cdot-7
documentation bug, inherited here in good faith. Two knock-on consequences:

- Your mismatch table compared a 1.39×-inflated growth curve against
  $Q_\text{forced}$.
- The WP1 addendum's §5(c) regression check (fixed-point $(1+z)^{3/2}$ vs "fitted
  $1.69,2.35,2.57,3.30$", concluding ratios $1.10,0.93,0.91,0.87$, "reasonably
  close") silently used the same mislabeled numbers. With correct ratios the
  fixed-point-to-fitted factors are $1.25$–$1.60$ — a genuine, larger deep-MOND
  suppression, consistent with the trajectory's documented $\sim0.7\times$
  asymptotic suppression factor, but the addendum's quoted agreement figures are
  wrong and its §5(c) should be re-run.

## 4. What the corrected picture looks like

**(i) $\hat a_0$ is welded to $H_{\hat\tau}$, identically, on every trajectory.**
One line: $a_0=\lambda\dot c$, $H_t=\tfrac32\dot c/c$ (exact from the redshift
law), local acceleration unit $\propto c^{7/2}$, $H_{\hat\tau}=H_t(c_0/c)^{5/2}$:
$$\boxed{\ \hat a_0(z)=\tfrac23\lambda c_0\,H_{\hat\tau}(z)\ }\quad
\text{identically, on any trajectory.}$$
Numerically: the `a0_confrontation.py` ratio formula and `budget_invoice.py`'s
$E(s)$ are the *same algebraic expression* — $\hat a_0(z)/\hat a_0(0)\equiv E(z)$
to machine precision (companion script, part 2). This extends the two-clocks
advisory's §2(vi) fixed-point bonus to the full fitted trajectory, and it
**dissolves the shape question as posed**: $\hat a_0$'s shape *is* $H_{\hat\tau}$'s
shape by identity. $\hat a_0$ was never supposed to be proportional to $Q$; the
theory's only obligation is to reproduce $H_{\hat\tau}$ — i.e., the invoice — which
the quadrature $F$ does by construction.

**(ii) $Q(a)$ is fixed by M1, not by the invoice.** In the broken phase the scalar
is the khronon clock ($\phi=t_\text{coord}$, M1), so on the background
$Q=A^\mu\nabla_\mu\phi=dt/d\tau=(c_0/c)^{5/2}=(1+z)^{5/3}$ — **exact on any
trajectory**, since both the lapse and the redshift are tied to $c$ exactly. This
is the natural $Q(a)$ the budget advisory's directive 1 should have specified.

**(iii) The reconstructed $F(Q)$ is a clean power with a clean source.** Running
the quadrature along the actual invoice trajectory (companion script, part 4):
$$d\ln F/d\ln Q=1.74\text{–}1.78\ \ (z=5\text{–}100)\quad\text{vs the exact
matter-era value }F\propto Q^{9/5}$$
(fixed point: $\Omega_s\propto a^{-3}$, $Q\propto a^{-5/3}$ $\Rightarrow$
$F-QF_Q=-\tfrac45F\propto Q^{9/5}$, density sign correct). The demanded
shift-current behavior is
$$a^3F_Q\propto a^{5/3}=\frac{d\tau}{dt}
\quad\text{(numerically }1.70\text{–}1.75\text{ vs }5/3\text{)},$$
i.e. **the census-constrained current departs from free conservation by exactly one
power of the two-clock lapse** — conservation with respect to the khronon
foliation's clock rather than matter proper time. That is not a curve-fit: it is a
single, geometrically motivated factor, of precisely the kind an action-level M5
implementation should produce — M5 saying itself back to us, the same way the
budget advisory found M2 in the $Q=\dot\phi$ rotation. (Radiation era: the demanded
piece is $\propto Q^{12/5}$ with the small negative amplitude the budget advisory
already assigned to $F$'s condensate offset or the $\tilde G\ne G$ renormalization;
$Q$ monotonic throughout, so one single-valued $F$ covers both eras.)

**(iv) M2's simplest reading survives.** On the fixed point
$\hat a_0\propto(1+z)^{3/2}=Q^{9/10}$ — exactly, near-linear. Along the fitted
trajectory the effective exponent is $n=0.42$–$0.58$ at $z=0.33$–$1.44$ (companion
script, part 5) — sub-linear, drifting toward $9/10$ as the trajectory approaches
the fixed point. Nothing anywhere near $n\gtrsim7$, and no new structure to be
"found and independently motivated" is needed on this front.

## 5. Directives

1. **WP3, re-posed once more, now with zero freedom:** implement M5 at the action
   level (census constraint as multiplier/boundary term on the aether-orthogonal
   foliation) and derive the modified scalar equation of motion. **Success
   criterion: the implementation must produce exactly the single-lapse-factor
   source, $a^3F_Q\propto d\tau/dt$, with no adjustable function.** If it produces
   anything else, *that* is the genuine kill-relevant confrontation — sharper than
   any version of WP3 posed so far, because the demanded answer is now known in
   advance and cannot be retro-fitted.
2. **Then the original constraint-propagation check**, with the energy bookkeeping
   made explicit: a sourced scalar current must exchange energy consistently under
   the Bianchi identity; the natural ledger is WP2's census evolution equation,
   whose shell-sweep term $3c/R_h$ is the open-boundary (Machian) channel. This is
   delicate and novel — it is proposal §5 item 1, the program's heart, exactly
   where it was always expected to be.
3. **Update `cdot-8/ConsolidationLog-2026-07-12.md`** (worker maintains it) with
   two items from this resolution, for the cdot-7 consolidator if that branch is
   reopened:
   - **Foundation §5.5 labeling bug (HIGH confidence, MEDIUM priority):** the
     displayed equation presents $1.69,\ 2.35,\ 2.57,\ 3.30$ as
     "$\hat a_0(z)/\hat a_0(0)$"; they are $a_0(z)$ in $10^{-10}$ m/s² (anchor
     $a_0(0)=1.39\times10^{-10}$, Foundation §2.2's own number). Verified by
     reproducing them to three digits from the four-term trajectory ×1.39
     (`inverse_reconstruction_check.py`, part 1). Proposed fix: relabel the
     equation (or divide through by 1.39 and say so); one line. True ratios:
     $1.22,\ 1.70,\ 1.86,\ 2.38$.
   - **Trajectory-wide $\hat a_0=\tfrac23\lambda c_0 H_{\hat\tau}$ identity
     (HIGH confidence, LOW–MEDIUM priority, optional):** a one-line exact result
     worth a remark in Foundation §5.5/§5.3 — the $a_0\sim cH$ relation is not a
     coincidence the framework explains approximately but an identity it enforces
     exactly, on every trajectory, via $a_0=\lambda\dot c$ plus the redshift law.
     Strengthens the existing prose and costs nothing.
4. **Re-run the WP1 addendum's §5(c) regression** with the corrected ratios and
   amend that document's quoted agreement figures (the conclusion direction —
   fitted values below the pure fixed-point law, increasingly with $z$ — survives;
   the numbers do not). One paragraph.
5. **No change to WP4a/WP4b queueing** (Stage-1 acoustic scale; BBN kinks) — this
   resolution touches neither, and Stage-1 remains promoted-to-immediate per the
   budget advisory.
6. **cdot-7 routing:** nothing here requires touching `cdot-7/`; both consolidation
   items go through the log per charter.

## 6. Protocol note

Third escalation, third correct call — and your own §5 explicitly anticipated it:
"both prior WP3 escalations turned out to hinge on something the worker's setup had
gotten subtly wrong." The two failure modes this time are worth naming for
calibration, because both will recur:

- **An inherited equation of motion is an assumption, not a fact**, when the
  program's own novel content (M5) is precisely a modification of that equation.
  "Exact, model-independent" claims should be checked for which *dynamics* they
  presuppose, not only which parameters.
- **Verify the label, not only the number.** The Foundation §5.5 values were used
  exactly as documented and were still wrong for the purpose — the second time
  this project has been ambushed by correct code behind imprecise prose (the first:
  the silent `tau_proper`/`t_coord` split). Both were caught the same way:
  reproducing the quoted number from the producing script before comparing against
  it. That step is now demonstrably load-bearing and should be treated as part of
  K6's verify-then-trust, applied to *internal* documents, not only external
  anchors.

The escalation protocol itself continues to perform: independent verification at
every step, no unilateral kill call, and the specific, checkable form of the
finding (the boxed formula, the mismatch table) is exactly what made the diagnosis
fast. The synthetic-validation instinct was right too — it just needs adversarial
cases that violate the premise under test, not only cases constructed to satisfy it.

## Companion files

- `inverse_reconstruction_check.py` — parts 1–5: the Foundation §5.5 labeling
  demonstration; the $\hat a_0\equiv E$ identity; the worker's $Q_\text{forced}$
  reproduction; the corrected quadrature reconstruction ($Q^{9/5}$ matter-era slope,
  single-lapse-factor source); the effective-exponent table.
- This advisory: proposed location
  `cdot-8/WP3/Advisory-WP3-InverseReconstruction-2026-07-12.md`.
