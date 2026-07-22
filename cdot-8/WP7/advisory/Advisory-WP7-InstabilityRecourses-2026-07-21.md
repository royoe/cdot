# Advisory — the ISW/Growth Vector-Sector Instability Assessed: the Mechanism Map Is Confirmed (Anti-Jeans on the $c_{\rm ad}^2<0$ Branch), One Required Correction Is Flagged in the Stage-4 Assembly, and There Are Plausible Recourses — Ordered Here by Cost and Principle, With the Two Cheap Ones Decision-Informing and the Two Real Ones Already Living Inside the Promoted Joint Re-Fit (for `cdot-8/WP7/`)

*2026-07-21. Advisory in response to WP7 §42–§43 and the author's
question: are there likely recourses that could plausibly recover a
sensible spectrum? Supporting computation in
`isw_instability_recourses.py`. Gate 1(b) carried; this item remains
the author-level fork §43 agreed to route. Verdict up front: **yes —
there are plausible recourses, and the most principled one lives in a
sector the census never claimed to determine. The instability is
confirmed as the anti-Jeans branch of the already-accepted
$c_{\rm ad}^2<0$ sign (rate $\sim|c_{\rm ad}|k/aH$, growing with $k$,
never crossing zero — the order-of-magnitude and scalings check against
the reported eigenvalues), which means the pathology is the
$c_{\rm eff}^2k^2<0$ part of the dispersion while the scale-free
$\mu^2\approx-0.5H^2$ part remains the good, CDM-like clustering
driver. Separating those two is exactly what a recourse must do — and
AeST's own structure offers a linear-order lever that does it without
touching the background: the $\mathcal Y$-sector's small-gradient end,
$F_{\mathcal Y}(0,Q)$, undetermined by the quadrature, renormalizing
the gradient coefficient while leaving $\mathcal Y\equiv0$ on FRW. One
required correction rides along regardless: the Stage-4 assembly cites
§7's superseded all-$k$ cancellation; the corrected record's
$-F_Q(1-W(kR_h))$ field-side term is off at $z\gtrsim10$ (so it is not
the cause) but turns on at $z\lesssim1$–$3$ — squarely inside the ISW
window — and must be carried in any rebuilt system.***

---

## 1. The mechanism, pinned

The reported eigenvalues match the anti-Jeans rate
$|c_{\rm ad}|\,k/(aH)$ in order, in $k$-scaling, and in $z$-trend
(Part 1 of the script: $\sim3\,H_0$ estimated vs the corrected
$8$–$9\,H_0$ at $z=0$, $k=2.7\times10^{-3}$; the $O(2$–$3)$ residual is
the full system's mixing factors). So the finding decomposes cleanly:
$$\omega^2\;\simeq\;c_{\rm eff}^2(k,z)\,k^2\;+\;\mu^2(z),$$
with $\mu^2\approx-0.5H^2$ the *desired* scale-free clustering driver
(the §27 mechanism) and $c_{\rm eff}^2\approx c_{\rm ad}^2<0$ the
pathology — a negative effective pressure that destabilizes harder at
larger $k$, the reverse of Jeans stabilization, hence "worse at exactly
the ISW scales." A sensible spectrum requires $c_{\rm eff}^2\gtrsim0$
at cosmological gradients while keeping $\mu^2<0$; nothing requires
both to have the same origin, and in this theory they don't: $\mu^2$ is
census-determined ($F_{QQ}$), $c_{\rm eff}^2$ is not (below).

## 2. Required correction, independent of any recourse

§42's assembly states the field equations are "unmodified by M5 per
§7's exact cancellation." That statement was **superseded** in the
Q-definition round: the cancellation is exact only at $k\to0$; at
finite $k$ the field equations carry
$-F_Q(1-\mathcal W(kR_h))\times(A\text{-structure})$, with the pinned
asymptotics and window-shape band of the covariantization-freedom
round. For the ISW $k$'s this term is off at $z\gtrsim10$
($kR_h\ll1$) — so it is **not** the cause of the $z=100$ instability —
but it activates at $z\lesssim1$–$3$ (Part 2's table: $(1-W)$ reaching
$0.3$–$1.0$ by $z=0$), squarely where the ISW signal forms. It must be
carried in any rebuilt system, with its band. Flagged as a required
correction, not a cure.

## 3. The recourse ladder

**R0 — the audit (mandatory first; cheapest; decision-informing).**
Two concrete questions, both answerable in one focused round:
(a) *Were the imported $(\alpha,\mathcal E_\alpha)$ equations derived
under the founding paper's own $K_Q(\text{background})=0$ assumption?*
Vanilla AeST sits at its $K$-minimum; cdot-8 never does ($F_Q$ spans
$4473\to1.85$). Any term the founding paper legitimately dropped as
$\propto K_Q$ is enormous for cdot-8 — the exact class of the WP6
Step-2 sliding-condensate term. A recovered restoring term here would
change the dispersion outright. (b) *Where does the negative
$c_{\rm eff}^2$ net from, given that the bare $(2-K_B)\mathcal Y$ term
is a positive-definite gradient floor?* The unstable direction is the
longitudinal $(\alpha,\mathcal E_\alpha)$ combination that the rank-1
$U$-structure does not protect — tracing the operator chain that gives
it a net negative pressure response is the sharpest diagnostic in the
whole ladder and directly determines R1's feasibility.

**R1 — the $\mathcal Y$-sector small-gradient completion (the leading
physical recourse).** The quadrature determines only $F(0,Q)$; the
$\mathcal Y$-direction is the *same declared-free sector* as WP6's
screening scope statement. $F\supset F_{\mathcal Y}(0,Q(z))\,\mathcal Y$
renormalizes the gradient operator at linear order (since $\mathcal Y$
is quadratic in perturbations) while leaving the FRW background —
$\mathcal Y\equiv0$ — and therefore the quadrature, the invoice, and
WP1–WP4 *exactly* untouched. Requirement: the completion's
small-gradient end supplies the pressure support the $Q$-sector
removes, $c_{\rm eff}^2\gtrsim0$ at cosmological gradients. If R0(b)
shows the unstable direction is $F_{\mathcal Y}$-reachable, the
completion family becomes pinned from **three sides — T22
(deep-Newtonian), $Q_2$ (transition), and cosmological stability
(small-gradient) — plus KATRIN on the census side: one function family,
four external anchors, and the post-WP7 revisit consolidates into a
single joint design problem.** Stated honestly: there is a tension to
manage — deep-MOND galaxy phenomenology softens the gradient response
at small $|U|$ while stability wants a floor at smaller $|U|$ still —
but AeST's bare $(2-K_B)\mathcal Y$ term is a floor *separate from* the
free function, which is structural room pure AQUAL lacks.

**R2 — the AeST-native cross-check (attribution diagnostic; cheap).**
Run the same $6\times6$ at the same $k$'s on the founding paper's own
tuned $K(Q)$ (their minimum gives $c_{\rm ad}^2\gtrsim0$). Expected:
stable — confirming the pathology belongs to cdot-8's census-forced
$F$, not to the import, and closing the "undiagnosed assembly error"
branch from the other side.

**R3 — re-closure (the heavy lever; synergistic).** $c_{\rm ad}^2(z)$
is a trajectory *output*: the matter-era $w$ sitting slightly below
zero is what makes it negative, and that offset moves under a changed
census content or fit — notably the low-$\Sigma m_\nu$ re-closure that
is already the KATRIN-aligned WP4a lever. Cannot be tuned in isolation
(the invoice is forced at fixed $E(z)$ and census), which is precisely
why it belongs inside the joint re-fit rather than as a standalone fix.

**R4 — nonlinear $a_0$-saturation (fallback interpretation, not a
recourse).** The linear runaway self-quenches when gradients reach the
MOND/screening regime, so the physical endpoint may be a saturated
scalar texture rather than an infinity. This could mean the theory
survives while *linear* predictivity at these scales does not — a
materially worse outcome for WP7's deliverable, recorded for
completeness so the option space is honest.

## 4. Recommended sequencing (for the author's decision, not presumed)

R0 and R2 together are one short, cheap round and do not presume any
verdict — they convert "pathology or error?" into a known quantity and
determine whether R1 is even reachable. R1 and R3 are the actual
recovery paths, and both live inside the IF-re-fit program this loop
already recommended promoting after $Q_2$ — the instability therefore
does not open a second crisis so much as add the fourth anchor to a
re-fit that was already coming. If R0(b) returns
"$F_{\mathcal Y}$-unreachable," the honest remaining options are R3 and
R4, and the verdict conversation changes character — that is the
branch point worth knowing about before scheduling anything else.

## 5. Housekeeping

Fold-ins: the §42-assembly §7-citation correction (§2 above); the
recourse ladder. External clocks unchanged (KATRIN; $Q_2$). This item
stays routed to the author per §43's joint agreement; this advisory is
the option map requested, not a unilateral next step. Nothing in
`cdot-7/` was touched.

## Companion

- `isw_instability_recourses.py` — the rate consistency, the
  $(1-W)$ activation table, the $F_{\mathcal Y}$ linear-order
  mechanics.
- This advisory: proposed location
  `cdot-8/WP7/Advisory-WP7-InstabilityRecourses-2026-07-21.md`.
