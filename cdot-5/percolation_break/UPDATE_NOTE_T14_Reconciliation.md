# UPDATE NOTE — Reconciling the T14 Rewrite with the T23 Broken Counting Law

*Status: correction note, to be folded into the T14 (cdot-5) rewrite before merge.*
*Date: 2026-07-04.*
*Targets: T14 draft §"Energy Scale", §"Toward the RAR", Verdict table, Open Items 1.*
*Depends on: T23_Percolation_Transition.md (same session).*

---

## 0. One-line summary

The T14 rewrite's central new claim — that connectivity counting has **no finite
particle horizon** — is an artifact of extrapolating the log branch past the
percolation break $z_*$. With the T23 broken law, the horizon is **finite**
($D_p(z\to\infty)\approx117\,r_d$), set by the occupancy branch. Holographic
saturation does **not** need rebuilding on the stated grounds; the $g_\dagger$
and $\rho_\text{bg}$ derivations need **recalibration against a finite,
computable horizon**, not a search for a finite length that supposedly no longer
exists.

---

## 1. The error

The rewrite computes the particle horizon from
$D_p(z)=(L/2)\ln(1+z)$ and finds $D_p\to\infty$ as $z\to\infty$ (draft §"Energy
Scale", verified there at $z=10^{20}$, $D_p/(L/2)=46.05$ "and climbing").

But per T23, the log law is the **connectivity (percolated) branch, valid only
for $z<z_*=1.20$.** For $z>z_*$ the network is subcritical and counting reverts
to **occupancy** (the volume-like branch), with $D_H\propto(1+z)^{-q}$,
$q=1.37$. The horizon ($z\to\infty$) lies ~20× beyond the break, entirely inside
the occupancy branch. Evaluating $D_p$ there with the log branch is applying a
formula outside its domain.

## 2. The correct horizon (finite)

Using the T23 broken law (parameters $B=33.55$, $z_*=1.201$, $q=1.37$,
$D_0=-0.46$, all in $r_d$):

$$D_p(z)\Big|_{z>z_*}=\big(D_0+B\ln(1{+}z_*)\big)+a\,\frac{(1{+}z)^{1-q}-(1{+}z_*)^{1-q}}{1-q},
\qquad a=B(1{+}z_*)^{q-1}.$$

Since $q=1.37>1$, the term $(1+z)^{1-q}\to0$ as $z\to\infty$, so

$$\boxed{\,D_p(z\to\infty)=\big(D_0+B\ln(1{+}z_*)\big)-\frac{a\,(1{+}z_*)^{1-q}}{1-q}\approx117\,r_d\,}$$

— **finite.** Numerically:

| $z$ | $D_p/r_d$ |
|---:|---:|
| $z_*=1.20$ | 26.0 |
| 5 | 54.1 |
| 20 | 77.3 |
| $10^{2}$ | 94.7 |
| $10^{4}$ | 112.7 |
| $\to\infty$ | **116.7** |

For comparison, the percolation tie gives $R_\text{now}=L+D_p(z_*)\approx93\,r_d$,
so the horizon sits at $D_p(\infty)/R_\text{now}\approx1.25$ — a finite,
order-unity multiple of the present scale, exactly the kind of finite boundary
the old $R_0$ provided. **The occupancy branch supplies the finite horizon that
the old occupancy law supplied, because at high $z$ it *is* the old occupancy
law.**

## 3. What this changes in the rewrite

- **§"The particle horizon is infinite under connectivity counting":** retract.
  The horizon is finite; the divergence was a domain error. Replace with the §2
  computation.
- **§"Energy Scale" holographic saturation:** the premise "there is no finite
  area to bound anything with" is false. A finite boundary area exists (set by
  $D_p(\infty)$, or equivalently the occupancy-branch horizon). Holographic
  saturation can be re-attempted against it; whether the specific
  $\rho_\text{bg}=(\pi/6)\rho_\text{crit}$ identity survives is now a
  **recalculation** (does the finite occupancy horizon reproduce the coefficient?),
  not an impossibility.
- **Verdict table, row "Holographic saturation / $\rho_\text{bg}$":** change
  "Does not survive as constructed — connectivity counting's particle horizon is
  infinite" to "Reopened — horizon is finite but no longer the clean
  $R_0=6c/H_0$; coefficient needs recomputation against the occupancy-branch
  horizon $D_p(\infty)\approx117\,r_d$."
- **Verdict table, row "$g_\dagger$":** the root cause is **not** "no finite
  horizon." It is that the finite horizon is now $D_p(\infty)$ (or $R_\text{now}$,
  or $L$ — see §4), not the clean $6c/H_0$. Reword accordingly.
- **Open Item 1:** rescope from "find a finite length/count that connectivity
  counting actually supplies … $L$ is the only candidate" to "recalibrate
  $g_\dagger$ and $\rho_\text{bg}$ against the finite occupancy-branch horizon;
  decide which finite length is physically correct (§4)."

## 4. The genuine (narrower) open problem that remains

The finite horizon is restored, but its **value** is no longer the clean
$R_0=6c/H_0$ that fed $g_\dagger=c^2/R_0\approx1.13\times10^{-10}$ (6% match).
There are now *three* candidate finite cosmological lengths, and the $g_\dagger$
recalibration must pick the physically correct one:

| length | value ($r_d$) | $g\propto c^2/\ell$ relative to naive $c^2/L$ |
|---|---:|---:|
| $L$ (recruitment / percolation correlation length) | 67.1 | 1.00 (naive) |
| $R_\text{now}$ (present horizon) | 93.1 | 0.72 |
| $D_p(\infty)$ (occupancy-branch particle horizon) | 116.7 | 0.57 |

The naive $R_0\to L$ substitution (draft: $2.8\times$ too large vs $a_0$) used
the *smallest* of these. A crossing-rate acceleration built on the actual
particle horizon $D_p(\infty)$ is $1.74\times$ smaller than the naive-$L$ value,
i.e. much closer to (and possibly below) the observed $a_0$ — so the "$2.8\times$
too large" verdict is itself an artifact of using $L$ rather than the true
horizon. **This should be recomputed properly:** it may substantially close, or
overshoot, the MOND-scale gap. Either way it is a finite-arithmetic problem, not
a search for a missing length.

Note the physical subtlety to settle: $g_\dagger$ was read as a *crossing-rate*
acceleration $c\cdot(c/R_0)$. The relevant "crossing distance" in a
connectivity-counted network is arguably $L$ (the recruitment length — the scale
over which the local node's reach turns over), **not** the particle horizon
$D_p(\infty)$ (which is a light-travel distance, not a turnover scale). If so,
the naive-$L$ value may be the correct crossing-rate scale after all, and the
$2.8\times$ discrepancy is real and physical — a genuine tension, not an
artifact. This is the actual open question: **which finite length sets the
turnover rate.** The rewrite's framing ("no finite length exists") obscured it;
the true framing is "several finite lengths exist and we must derive which one is
the crossing scale."

## 5. Unaffected by this note

The rewrite's survives/breaks partition is otherwise correct and this note does
not disturb it: foam-diffusion $1/r$, the RAR closure's functional form (with
$g_\dagger$ external), dynamical selection, the river, and the inertia no-go's
robustness argument all stand. The cascade-slope-survives / IR-cutoff-changes
split also stands **with one correction**: the IR cutoff (longest accessible
wavelength) is **not** unbounded — it is set by the finite occupancy-branch
horizon $D_p(\infty)$, just as the old IR cutoff was set by $R_0$. Update that
bullet alongside the horizon retraction.

## 6. Two secondary flags (raised in review, not blocking)

- **Symbol clash on $L$.** The draft (line ~94) flags that the recruitment length
  $L$ and the T22 link mean free path share the symbol. Given the merge risk,
  rename the microphysical one to $\ell_\text{link}$ throughout; keep $L$ for the
  recruitment/percolation length (which now has the fixed physical meaning from
  T23).
- **BH-sink amendment (draft lines 38–41).** The "conserved except at BH
  horizons" revision should state its purpose. Fork A (BH-confined mass as the
  $c(t)$ symmetry breaker) was **tested and failed this session** by 2–4 orders
  of magnitude (UPDATE_ForkA_BH_Confined_Mass_NEGATIVE). If the sink is retained
  for a different reason, name it; as written it reads as reviving a falsified
  mechanism. Also account for the cost: "conserved in number" is what T12 uses to
  distinguish connectons from photons, so weakening it is not free.

---

## 7. Recommended action

Fold §§1–5 into the T14 rewrite before it merges; do not merge the current
"infinite horizon" version alongside T23, as the two directly contradict. The net
effect is *less* work for the connecton program, not more: the holographic
apparatus is recoverable, and the MOND-scale question reduces to a
finite-arithmetic recalibration plus one conceptual choice (which length sets the
crossing rate).
