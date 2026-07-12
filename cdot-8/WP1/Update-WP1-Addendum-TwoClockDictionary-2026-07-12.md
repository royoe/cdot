# Update — WP1 Addendum: The Two-Clock Dictionary (Reopening WP1, Narrowly)

*Companion: `SessionLog-2026-07-12.md` (this directory) and
`cdot-8/proposal/Advisory-WP3-TwoClocks-2026-07-12.md` (the advisory this addendum
responds to, per its own directive 1: "reopen WP1 narrowly... the resolution above is
the hypothesis to verify covariantly, not settled by this advisory"). This is not a
rubber stamp of the advisory — its numerics are independently re-verified below by a
different computational method, and its central physical claim is independently
re-derived from first principles rather than accepted on the strength of its own
(self-described as unverified) intra-cdot-7 argument. The result: directive 1 is
satisfied, with an unexpected bonus — the resolution turns out to already be implemented,
silently, in cdot-7's own pre-existing code.*

---

## 1. Independent numerical re-verification

`twoclocks_check.py` requires `scipy`, unavailable in this environment. Re-verified
every claim by an independent method instead: the fixed-point ODE ($\dot R_h=c$,
$R_h\propto c^{3/4}$) has a closed form, $c(t)^{-1/4}=c_0^{-1/4}-t/(3B)$, checked
against the ODE by direct differentiation (relative error $2.5\times10^{-10}$). Fitting
power laws to this closed-form solution:

| Quantity | Advisory's script | This session, closed form | Claim |
|---|---|---|---|
| $H_t\equiv d\ln a/dt \propto a^p$ | $p=0.166667$ | $p=0.166667$ | $+1/6$ ✓ |
| $\dot c\propto c^p$ | $p=1.250000$ | $p=1.250000$ | $5/4$ ✓ |
| $H_{\hat\tau}\propto a^p$ | $p=-1.500000$ | $p=-1.500000$ | $-3/2$ ✓ |
| $\hat\chi(z)$ vs. analytic EdS | agreement to $10^{-9}$ | agreement to $1.9\times10^{-11}$ | bounded, matches |
| $H_t(0)/H_{\hat\tau}(0)$ | $1.000000000000$ | $1.0000000000$ | today-coincidence |

All independently confirmed by a different computational route (closed-form solution
vs. numerical ODE integration). The advisory's numerics were not the weak point;
whether the physical identification behind them is covariantly justified was.

---

## 2. Where WP1 actually went wrong

WP1 (§3) established, correctly: coordinate mass, length, and frequency are physical
quantities re-expressed in a Planck-unit system built from the bookkeeping variable
$c(t)$, with $G,\hbar$ held fixed by convention — $X_\text{coord}(t)\equiv X_\text{phys}
\times(c(t)/c_0)^{n_X}$, $n_X$ fixed by $X$'s Planck dimension. This was applied to
mass ($n=1/2$), length ($n=-3/2$), frequency ($n=+5/2$) — **and silently *not* applied
to time itself**, where WP1 tacitly set $t_\text{coord}=\tau_\text{phys}$ (i.e., $n=0$)
without deriving or even stating that choice. That is the gap: **there is no principled
reason time should be the one Planck dimension exempted from the same treatment**, and
once it isn't, the fix is immediate. The Planck time is $t_\text{Pl}(t)=\sqrt{\hbar
G/c(t)^5}\propto c(t)^{-5/2}$; applying WP1's own rule (freeze the ratio $\tau_\text{phys}
/t_\text{Pl}$ at today's value) gives
$$t_\text{coord}=\tau_\text{phys}\times\left(\frac{c(t)}{c_0}\right)^{-5/2}
\quad\Longleftrightarrow\quad
\boxed{\ \frac{d\tau_\text{phys}}{dt_\text{coord}}=\left(\frac{c}{c_0}\right)^{5/2}\ } ,$$
**exactly the advisory's proposed relation — now derived, not asserted**, as the missing
fourth row of WP1's own dictionary table, not an ad hoc addition to it.

**Consequence for cdot-7's closure ODE.** $\dot c\equiv dc/dt_\text{coord}=(dc/d\tau)
(c/c_0)^{5/2}$. Using $dc/d\tau=\tfrac23cH_\tau$ ($H_\tau\equiv d\ln a/d\tau$, the
genuine, physically meaningful Hubble rate) and the fixed point's $H_\tau\propto
a^{-3/2}\propto c^{-9/4}$ (§3 below): $a_0=\lambda\dot c\propto\lambda c^{7/2}\cdot
c^{-9/4}=\lambda c^{5/4}$ — **reproducing Foundation §5.4's independently-stated
$a_0\propto c^{5/4}$ exactly**, a second, separate confirmation of the corrected
dictionary (the first being §1's numerics).

---

## 3. Confirmation this is not new — cdot-7's own code already has it

`cdot-7/Fable-1/closure_dynamics.py` (2026-07-07, predating every cdot-8 session)
integrates a **three-component** state vector, `[r, tau_proper, t_coord]`:
```
return [KAPPA*lam*x*r/a, a**2.5*dtda, dtda]
```
i.e. $d\tau_\text{proper}/da = a^{2.5}\,dt_\text{coord}/da$, so $d\tau_\text{proper}/
dt_\text{coord}=a_\text{code}^{2.5}$. That file's own header states its redshift
convention as $1+z=a_\text{code}^{-3/2}$ — solving against cdot-7's actual redshift law
$1+z=(c_0/c)^{3/2}$ gives $a_\text{code}\equiv c/c_0$ (**this "a" is not WP1's FRW scale
factor** — a notational trap worth flagging explicitly for future sessions). Substituting:
$d\tau_\text{proper}/dt_\text{coord}=(c/c_0)^{2.5}$ — **the exact relation derived
independently in §2**, already implemented, unremarked upon in prose, in the project's
own pre-cdot-8 code. The file's own validation line, `abs(-sol.y[1,-1]*H0 - 2/3) <
1e-9`, checks precisely that $\tau_\text{proper}$ (not $t_\text{coord}$) gives the
finite $\tfrac23H_0^{-1}$ EdS age — confirming Foundation §5.2's "proper age
$\tau_\infty=\tfrac23H_0^{-1}\approx9.3$ Gyr" was always $\tau_\text{proper}$, and that
this project's own authors already, correctly, kept the two clocks apart in code while
Foundation's prose never states the distinction as a general principle. **That silent
gap between code and prose is what let WP1 (reading only the prose) miss it.**

---

## 4. Directive 1, item by item

- **(a) Both time maps as frame objects**: $t_\text{coord}$ — the khronon/gravity-sector
  clock, native to the closure ODE ($\dot R_h=c$, $a_0=\lambda\dot c$) and to M1's
  scalar-clock reading of the aether foliation; $\tau$ — matter's proper time, forced by
  K1 (universal coupling: photons/atoms couple to $g_{\mu\nu}$, whose proper time is
  what they measure), related by $d\tau/dt_\text{coord}=(c/c_0)^{5/2}$.
- **(b) Independent re-derivation of $H_\tau\propto a^{-3/2}$**: done, §2 above, via
  WP1's own Planck-unit logic extended to time — not via accepting the advisory's
  cdot-7-internal argument.
- **(c) Covariant distance re-derivation on $\tau$**: the closed-form check (§1) already
  confirms $\hat\chi(z)$ built on $\tau$ matches the analytic EdS formula to
  $1.9\times10^{-11}$; §3 shows this is not a new construction but the same one
  cdot-7's own code already performs. **Satisfied — the WP1-level kill condition does
  not trigger.**
- **(d) Lapse ratio as a named deliverable**: $d\tau/dt_\text{coord}=(c/c_0)^{5/2}$,
  recorded here as the fourth row of WP1's dictionary (alongside mass, length,
  frequency) — this *is* the disformal content the proposal's K5/M3 anticipated,
  located not in a second metric $\hat g$ (WP1 already ruled that out — AeST has none)
  but in the relationship between two time parametrizations of the same single metric.

---

## 5. Directive 2, regression checks

- **(a) Today-coincidence**: confirmed, both numerically (ratio $=1$ to 12 digits) and
  structurally — it is built into the "freeze the ratio at today's value" construction
  in §2, not a coincidence needing separate explanation.
- **(b) Fitted-trajectory SN photometry**: inspected `cdot-7/Fable-1/four_term_fit.py`
  directly. Its `trajectory()` function computes $D_L(z)$ purely algebraically from
  $r(a)$ — **no time integral at all**, coordinate or proper. Distances were never at
  risk from this issue in the actual fitting code; the divergence found in
  `Update-WP3-DistanceTension-2026-07-12.md` came from *this session's* attempt to
  build a standard covariant distance formula on the wrong clock ($t_\text{coord}$),
  not from any error in cdot-7's own fit. **No re-run needed — the four-term fit was
  never exposed to this issue.**
- **(c) $\hat a_0(z)$ comparison**: the exact fixed point predicts $\hat a_0(z)\propto
  (1+z)^{3/2}$ (§2's cross-check chain). Against Foundation §5.5's quoted *fitted*
  values (which sit on the perturbed $\delta_0\ne0$ trajectory, off the fixed point):
  $$\hat a_0(z)/\hat a_0(0):\quad\text{fixed-point }(1+z)^{3/2} = 1.53,\,2.52,\,2.83,\,3.81
  \quad\text{vs. fitted } 1.69,\,2.35,\,2.57,\,3.30$$
  at $z=0.33,0.85,1.00,1.44$ — ratios $1.10,\,0.93,\,0.91,\,0.87$. Reasonably close, with
  the fitted values falling increasingly below the pure fixed-point law at higher $z$ —
  expected, since the actual trajectory sits at $x_0=1.10$ (deep-MOND-ward of $x_*=1.72$),
  not exactly on it. Not a red flag; recorded as a sanity check, not a precision test.
- **(d) The $\tfrac32$ factor / $H_0$ identification**: at $t_0$ ($c=c_0$), $(c/c_0)^{5/2}
  =1$ exactly, so $\dot c_\text{coord}(t_0)=\dot c_\tau(t_0)$ — the two clocks coincide
  *at* calibration, so Foundation's $H_0^\text{obs}=\tfrac32\dot c_0/c_0$ is unambiguous
  regardless of which clock is meant; the ambiguity only matters when integrating over
  cosmic time (ages, high-$z$ distances built the wrong way), never at the $t_0$
  calibration point itself.

---

## 6. Directive 3 — the age-clock question (report only, per charter; nothing in
`cdot-7/` touched)

`closure_dynamics.py`'s $\tau_\text{proper}$ (not $t_\text{coord}$) is confirmed to give
the finite, EdS-matching $\tfrac23H_0^{-1}\approx9.3$ Gyr fixed-point age quoted in
Foundation §5.2. The actual four-term-fit's quoted 12.9 Gyr (Foundation §5.5) was **not**
found computed by an explicit, standalone script in this session's search — the closest
candidate, `four_term_fit.py`'s own `trajectory()`, does not track an age/$\tau$ state at
all (§5(b) above), so the 12.9 Gyr figure's exact provenance script was not located.
Given the shared `setup_closure`/`trajectory` structure between that file and
`closure_dynamics.py`, and that the latter is this project's established
age-calculation methodology, it is likely the 12.9 Gyr figure used the same
$\tau_\text{proper}$ convention — but this is an inference from structural similarity,
not a direct trace, and should be stated with that caveat. **Recommended cdot-7
documentation fix** (for the consolidator, not applied here): add one paragraph to
Foundation stating explicitly that $t$ (used in $\dot R_h=c$, $a_0=\lambda\dot c$) and
$\tau$ (proper time; used for all ages and, implicitly and correctly, already used in
`closure_dynamics.py`) are related by $d\tau/dt=(c/c_0)^{5/2}$ — the single sentence
that would have prevented this session's entire WP3 excursion.

---

## 7. Verdict

Directive 1 fully satisfied, with independent (not merely accepted) verification at
every step, and the added, unplanned finding that the resolution is not new theoretical
content invented for cdot-8 — it is a previously-implicit, uncodified piece of cdot-7's
own existing computational practice, now made explicit and covariantly grounded.
**WP3 is unblocked.** Per the advisory's directive 4, the target for WP3's actual
question (does AeST's Friedmann sector admit the required $H_\tau(a)$?) is now precise:
$H_\tau^2\propto a^{-3}$ (fixed point) plus the fitted late-time departure, evaluated on
matter's own proper time — a standard-looking matter-frame background, with the novelty
(and the $a^{1/6}$-rate evolution of the khronon/$Q_0$ sector) confined to the
gravity-sector clock, exactly where a covariant completion is built to host it.
