# Update — WP3: The Machian Closure's Energy Budget Does Not Fit an Ordinary Friedmann Equation

*Companion: `SessionLog-2026-07-12.md` (this directory), Entry 3. WP3 was unblocked by
the two-clock dictionary fix (Entry 2); resuming it to check whether AeST's Friedmann
sector admits the required $H_\tau(a)$ surfaced a second, more severe issue, upstream of
the Bianchi/constraint-algebra question the proposal's WP3 text literally names. This is
reported for author review before proceeding further, following the same protocol as the
first WP3 escalation: independently checked, not a unilateral kill call, options laid
out. This one is more consequential than the last.*

---

## 1. Setting up the check, with the corrected dictionary in hand

Per the WP1 addendum, the target is $H_\tau^2\propto a^{-3}$ (matter fixed point) plus
the fitted late-time departure, on matter's own proper time $\tau$. AeST's own Friedmann
equation (WP0 extraction) is an *ordinary*, additive structure:
$$H_\tau^2=\frac{8\pi\tilde G}{3}\rho_m-\frac13(F-QF_Q)+\frac\Lambda3.$$
Setting $\Lambda=0$ (cdot-7's own acceleration mechanism is the separatrix instability,
M6 — not a bare constant; a bare $\Lambda$ would also fail to track $a^{-3}$ at the fixed
point regardless). The question: can this equation, sourced by ordinary matter
$\rho_m$ (baryons + neutrinos, $\Omega_\text{closure}=0.074$) plus whatever the
scalar/aether sector contributes, reproduce $H_\tau^2=H_0^2(a/a_0)^{-3}$?

---

## 2. Why AQUAL's own mechanism cannot supply the difference at the background level

cdot-7's closure is $\mu(x)g_h=GM_h/R_h^2$ — AQUAL's field equation, whose entire
content is a statement about how gravitational *field strength* (a spatial gradient)
compares to $a_0$. Applied to the cosmological background, this treats "the mass within
the horizon" as if it were an isolated, spherically symmetric source in otherwise-empty
space — the same structure AQUAL uses for a galaxy. **In an exactly homogeneous FRW
background, there is no spatial gradient at all** ($\nabla\Phi\equiv0$ by symmetry,
nothing distinguishes one direction from another) — the very quantity AQUAL's
modification depends on vanishes identically. AQUAL's characteristic feature — using
$\mu(x)<1$ to make a given mass produce *more* binding than Newton alone would give,
exactly how MOND explains flat rotation curves without dark matter — has no natural
home in the homogeneous limit of a genuinely covariant field theory. cdot-7's own
closure gets around this by treating "the horizon" as a Machian, quasi-local boundary
(the sense in which the whole program is explicitly Machian, following Sciama), but that
is an *additional*, cdot-7-specific postulate layered on top of AQUAL's local field
equation — not something the local equation, taken at face value and covariantized,
supplies on its own.

---

## 3. The numerical severity — not a subtle effect

Using Foundation §5.6's own formula and the four-term fit's own numbers
($\kappa\lambda=0.4355$, $\lambda=0.3056$, $x_0=1.10$, simple $\mu$), independently
recomputed:
$$\Omega_\text{closure}=\frac89(\kappa\lambda)\lambda x_0^2\mu(x_0)=0.0750\quad
\text{(matches the quoted 0.074).}$$
An ordinary Friedmann equation sourced by *only* this density gives $H^2=0.075\,H_0^2
(a/a_0)^{-3}$ — reproducing the fixed point's claimed $H^2=H_0^2(a/a_0)^{-3}$ needs
**13.3$\times$ more density than $\Omega_\text{closure}$ supplies** — a shortfall of
$\Delta\Omega\approx0.925$, not a percent-level correction. Dividing by AQUAL's own
local boost factor $\mu(x_0)=0.524$ (checking whether the *value* of $\mu$ at today's
operating point could bridge the gap by itself) reaches only $\Omega_\text{closure}/
\mu(x_0)=0.143$ — nowhere close to closing a factor-of-13 gap. **Whatever supplies the
missing $\sim0.93$ in $\Omega$-units, it is not a small correction that a clever
choice of $\mu$ or $\kappa\lambda$ absorbs — it is comparable in size to $\Lambda$CDM's
entire dark sector.**

---

## 4. What this means for the proposal's own plan

Proposal §3 states plainly: cdot-8 "must replace [AeST's] cosmological branch wholesale
with the census-closed one," discarding AeST's native dust-like scalar entirely, with
$\Omega_\text{closure}=\Omega_b+\Omega_\nu$ remaining the *whole* budget. §3's own
"critical divergence" passage already names this as the largest risk, but frames it as
a *choice* to be made (which branch to keep) rather than a *quantitative* constraint on
what's left after the choice is made. **This session's finding sharpens that risk into
an arithmetic fact**: once AeST's native dust-mimicking branch is discarded (as the
proposal requires), *something* still has to supply $\Delta\Omega\approx0.925$ at the
background level for the fixed point to hold — and it cannot come from AQUAL's own
gradient-based mechanism (§2), because that mechanism structurally does not survive
homogenization. The proposal does not yet name a candidate for what does supply it,
other than the very AeST-native scalar behavior it explicitly rules out.

**This bites earlier than WP7.** The proposal gates the perturbation/CMB sector (WP7)
behind everything else, "exactly as cdot-7 items 5–6." But this tension is a
*background*-level problem (WP3/WP4's territory), and — because the trajectory sits
closest to the exact fixed point at high $z$ (the departure "negligible in the past" per
Foundation §2.2) — it is *sharpest* exactly where CMB/structure-formation data are most
constraining, not a separate, later concern. The severity here is a structural reason
the WP7 worry is well-founded, discovered a work package earlier than expected.

---

## 5. Candidate escape routes considered, and their status

1. **Check the actual fitted trajectory, not the idealized fixed point.** Not yet done
   numerically this session — but Foundation's own description (deviation "negligible
   in the past," growing only at late times) suggests the *opposite* of relief: the
   trajectory is *closest* to the exact-EdS fixed point at high $z$, where this tension
   is computed, so departing from the fixed point at low $z$ is unlikely to remove a
   high-$z$ shortfall. Flagged as worth checking explicitly, not assumed to help.
2. **The missing component need not be literally cold dark matter.** True — nothing
   here shows the missing $\Delta\Omega\approx0.925$ must cluster like CDM or behave
   identically in every respect. But it *must* source $H^2$ additively and track
   $a^{-3}$ at the fixed point specifically (matching literal matter domination there)
   — a strong constraint on its own equation of state, and *energetically* equivalent
   to a dark-sector component regardless of what it's called. This softens the
   philosophical framing, not the arithmetic.
3. **M5's nonlocal, Machian sourcing of $Q_0(t)$ might make the missing component a
   genuine prediction (from the census) rather than a freely-fit parameter** —
   preserving some falsifiable, distinctive content even if energetically
   indistinguishable from a dark sector. This is the most promising *partial* rescue:
   it would not restore "no dark matter" as a literal claim, but could preserve "no
   *freely-adjustable* dark sector — only Machian, census-determined gravitational
   content." Whether this is what the proposal intends, or an acceptable fallback
   position, is a judgment call, not a technical one.
4. **A genuinely non-additive (background-level AQUAL-like) modification of AeST's own
   Friedmann equation**, rather than the literature-standard additive one used here,
   would resolve this cleanly if it exists — but nothing in the extracted AeST
   literature (WP0) suggests its FRW sector is anything other than the standard,
   additive structure; this would be new theoretical construction, not a known result
   to cite.

---

## 6. Verdict — escalating, not deciding

This is not a Bianchi/constraint-algebra inconsistency in the sense the proposal's WP3
kill condition literally names — the equations are perfectly consistent; they simply
require an energy budget the proposal's own stated plan (discard AeST's dust-like
scalar) does not supply. Whether this counts as triggering WP3's kill condition in
spirit, or is better read as a finding that **redefines what cdot-8 must mean by "no
dark matter"** (options 2–3 above), is exactly the kind of consequential, values-laden
judgment this project's protocol reserves for the author. Recommend the same routing as
before: author's call on which of §5's options (or another) to pursue, with the
observation that option 3 (Machian-determined, not freely-fit, gravitational-sector
energy content) is the most promising path that preserves *some* of cdot-7's
distinctive claim without requiring a technical result nobody has yet shown exists
(option 4). No file in `cdot-7/` touched.
