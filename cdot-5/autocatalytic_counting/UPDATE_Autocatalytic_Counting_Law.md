# UPDATE — The Autocatalytic Counting Law: $c\propto e^{R/L}$ (CONSTRUCTIVE)

*Status: proposed update, for cross-check and merge. Session 2026-07-04 (cont.).*
*Targets: Core §2 (premise 2), §3 (horizon law), §4/§4a (distance); T4 (counting-law variants); T12 (premise-2 fork, "what is a connecton"); T14 (network kinetics).*
*Depends on: UPDATE_Static_Map_cz_Inversion.md (same session).*
*Figures: desi_static_map.png, desi_counting_laws.png (same session).*

---

## Summary

Fitting counting-law candidates to the **clean DESI galaxy bins** ($z<1.3$; QSO
and Lyα excluded for their distinct tracer bias) selects a single form:
$$\boxed{\,D_p \propto \ln(1+z)\quad\Longleftrightarrow\quad c(R)\propto e^{R/L}\,,}$$
an **exponential counting law**, with a candidate **derivation** from the
connecton network: counting *connectivity* (transitive reach) rather than
*occupancy* (particles in a volume) gives $dN/dR=N/L$ autocatalytically. The
derivation is conditional (three named assumptions) but yields a new falsifiable
structural claim: the exponential form is **equivalent to the network having a
fixed recruitment length**, not a scale-free (fraction-of-horizon) one.

This supersedes the interim "running index $n\sim0.4$–0.7" reading of
UPDATE_Static_Map_cz_Inversion (see Correction below).

---

## 1. What the clean bins select

Restricting to the four galaxy bins ($z=0.510,0.706,0.934,1.321$) removes the
$z\sim1.5$ dip (which was driven by the QSO/Lyα points). Fitting one-parameter
counting laws jointly to $D_M/r_d$ and $D_H/r_d$ (8 data), with the
squared-redshift law held fixed ($c_\text{emit}/c_\text{now}=(1+z)^{-1/2}$):

| Law | form | free params | $\chi^2$ |
|---|---|---:|---:|
| **log / exponential** | $D_p\propto\ln(1+z)$, $c\propto e^{R/L}$ | 1 ($B\!=\!L/2\!\approx\!33\,r_d$) | **13.2 / 7** |
| power, volume | $n=3$ | 1 | 98 |
| power, surface | $n=2$ | 1 | 178 |
| power, $n=1$ | | 1 | 552 |
| power, S′ | $n=2/3$ | 1 | 1104 |
| power, $n=1/2$ | | 1 | 1798 |
| — ref: $\Lambda$CDM | $\Omega_m,A$ | 2 | 10.5 / 6 |

The one-parameter exponential law ($\chi^2/\text{dof}\approx1.9$) is competitive
with two-parameter $\Lambda$CDM. Its only real tension is a $-3.2\sigma$ pull in
$D_H$ at $z=0.934$ — a single bin that also sits high relative to $\Lambda$CDM,
so plausibly a data feature.

**Correction to the prior update.** UPDATE_Static_Map_cz_Inversion reported the
data "want a low, running index $n\sim0.4$–0.7." That came from *differentiating*
$D_p$ at an assumed $R_\text{now}$ (a local slope), not from a fit. A direct fit
shows constant low power laws are *worse*, not better ($n=1\!\to\!\chi^2\!=\!552$;
$n=0.5\!\to\!1798$): the data do not want a low constant index. They want an index
that **grows with $R$**, which is precisely $n_\text{eff}(R)=d\ln c/d\ln R=R/L$ —
the exponential law. The power-law fit "ran away" to $n\to\infty$ because that is
the exponential limit ($x^{-1/(2n)}\to1-\tfrac{\ln x}{2n}$, giving $D_p\propto\ln(1+z)$).
The arithmetic of the prior update stands; its interpretive "running index"
framing is superseded here.

---

## 2. The exponential law on a static map

With the squared-redshift law retained, $c(R)\propto e^{R/L}$ (equivalently
$N\propto e^{R/L}$, since $c\propto N$) implies:

- **Distance:** $D_p=R_\text{now}-R_\text{emit}=B\ln(1+z)$, $B=L/2$;
  $D_H=dD_p/dz=B/(1+z)$; $D_L=(1+z)D_p$.
- **Observable Hubble law (crisp signature):** $H_\text{obs}(z)=c/D_H\propto(1+z)$
  — **linear**. Distinguishable from $\Lambda$CDM (steeper) and from the volume
  law ($\propto(1+z)^{7/6}$). Directly testable with more BAO bins.
- **Horizon rate:** $H^\text{hor}=\dot c/c=c/L\propto(1+z)^{-1/2}$.
- **$c(t)$ history:** solving $\dot R=c=k e^{R/L}$ gives $c(t)=L/(t_*-t)$:
  $c\to0$ as $t\to-\infty$ (no Big Bang in map time, preserved), but $c$
  **diverges at a finite future time $t_*$** — a new feature (a "map ends"
  prediction) absent from the power law's open-ended future. Flagged as a
  modeling judgment, not resolved.
- **Proper age preserved:** $\tau=\int_{-\infty}^{0}(c/c_0)^2\,dt=(t_*-t_0)$ is
  **finite**, so the finite-proper-age success (T1, ~21 Gyr scale) survives.

---

## 3. Derivation of $dN/dR=N/L$ from the connecton network

**The conservation tension and its resolution.** "Autocatalytic" must not mean
*creating* connectons — that would violate T14's conservation premise (C2:
connectons conserved, total number fixed by holographic saturation). The
resolution: the $N$ in $c\propto N$ is **not** total connecton number but the
**connectivity (degree) of the local reference node** — how many connectons the
local point is currently connected to within the horizon. Total links conserved;
local *reach* grows as the horizon admits more of the network into causal
contact. Autocatalysis = the *rate of acquiring* connections scales with the
number already held. No connectons created; C2 safe.

**Mechanism — transitive reachability.** Treat the sea as a network; the local
node is connected to any node a chain of connectons reaches. When the horizon
grows by $dR$, it admits a new shell of nodes. A new node joins the local
connected set only if it links to a node **already** in that set. Hence the
number of newly reachable nodes is proportional to the current connected set at
the frontier, not to the raw shell volume. With a fixed recruitment fraction
$1/L$ per unit horizon growth (T12/T14 endpoint-only interaction, likelihood per
unit length $\propto1/L$):
$$\frac{dN}{dR}=\frac{1}{L}\,N\quad\Longrightarrow\quad N\propto e^{R/L}.$$

**Why this is principled, not fitted.** The old volume law counted *particles in
a volume* — a shell adds $n\cdot4\pi R^2 dR$ independent tokens, $dN/dR\propto R^2$.
The exponential is what one obtains the instant the count is **connectivity
(transitive reach)** rather than **occupancy (particles)** — exactly the
particle→relation shift T12 prescribes. The counting-law change is the counting
rule matching the model's own ontology, not an epicycle.

---

## 4. The sharpest result: fixed recruitment length vs scale-free

The law is a *pure* exponential only if $L$ is a fixed absolute length. The
alternative is decisive:

- If $L\propto R$ (recruitment over a fixed **fraction** of the horizon — a
  **scale-free** network), then $dN/dR=N/(\alpha R)\Rightarrow N\propto R^{1/\alpha}$
  — a **power law**, i.e. the excluded family.
- Therefore the data's preference for exponential over power law is *equivalent*
  to the structural statement:
  > **The connecton network recruits over a fixed length $L$, not a fixed
  > fraction of the horizon.** Scale-free connectivity is excluded by DESI.

This converts the curve-fit into a falsifiable claim about the network's
character, and pins the key open question to "what sets $L$?"

---

## 5. Grading and open items (honest)

The derivation **earns** the exponential form *given* three assumptions; it does
not force it from nothing:

1. **Supercriticality.** Transitive reach grows (rather than saturating) only if
   the network is supercritical (mean branching $>1$); subcritical → reach
   saturates → $c$ freezes. Assumed, not derived.
2. **The $1/L$ recruitment rate** reuses T12's endpoint-only "$1/L$ per unit
   length" heuristic, itself flagged in T14 as not yet derived from re-anchoring
   kinetics. This derivation is only as solid as that heuristic.
3. **Mean-field independence** (frontier connections recruit independently, no
   clustering); correlations would shift the exponent.

Further open items:
- **What sets $L$?** Fixing $L$ as microphysical is consistent, but $B\approx33\,r_d$
  ties it to the sound horizon for no evident reason — so $L$ is currently the
  one free scale (the old $R_\text{now}/r_d$ degeneracy relocated, not removed).
  Candidates: a re-anchoring mean free path (T14 diffusive fraction), or the
  Compton length of the lightest massive species (a genuine fixed length).
  **Not** the horizon (→ scale-free → excluded power law).
- **High-$z$ deferred component.** The exponential law overshoots the excluded
  QSO/Lyα points ($D_M$ slightly high, $D_H$ notably high at $z=2.33$). Once
  those tracers are trusted, either $L$ runs above $z\sim1.3$ or a second
  component enters — the "decide later" flagged earlier.
- **Future $c$-singularity at $t_*$.** New qualitative feature; needs a physical
  reading (does recruitment saturate near $t_*$, regulating the divergence?).

---

## 6. Proposed edits to existing documents

- **Core §2 (premise 2):** record that the volume law $c\propto R^3$ is
  **excluded by DESI** (AP shape, $\chi^2\approx94$; direct fit, $\chi^2=98$),
  and that the surviving candidate is the exponential/autocatalytic law
  $c\propto e^{R/L}$ with $D_p\propto\ln(1+z)$. Frame premise 2 as
  connectivity-counting, not occupancy-counting (cross-ref T12).
- **Core §3:** add the exponential horizon solution $c(t)=L/(t_*-t)$ alongside
  the power-law solution, noting the finite future $t_*$ and preserved finite
  proper age.
- **Core §4/§4a:** add $D_p=B\ln(1+z)$, $D_H=B/(1+z)$, $H_\text{obs}\propto(1+z)$
  as the working formulae under the exponential law; mark the power-law $D_p$
  formula as superseded for $z<1.3$.
- **T4:** the counting-law-variants section should be reorganized around
  power-law (all excluded, constant index) vs exponential (selected); include
  the fit table (§1).
- **T12:** elevate "what is a connecton" — the connectivity/reachability reading
  now does real work (resolves the conservation tension and yields the law);
  record the fixed-recruitment-length claim as a structural prediction.
- **T14:** the endpoint-$1/L$ heuristic is now load-bearing for cosmology
  (not only for the ballistic/diffusive split); its derivation from re-anchoring
  kinetics is promoted from "nice to have" to a gating open item.

---

## 7. Caveats

- Four BAO bins, one fitted parameter; the $-3.2\sigma$ $D_H(z{=}0.934)$ pull
  and the whole high-$z$ story need the full DESI covariance and DR3 bins.
- $B$ (hence $L$) is degenerate with the absolute scale; only the shape
  $\ln(1+z)$ is determined. Pinning $L$ needs a model $r_d$ from genesis/
  recombination physics (unworked, T16).
- The derivation is conditional (§5). It establishes that the connecton
  ontology *can* produce the selected law and makes a new falsifiable claim; it
  does not yet provide $L$ from first principles.
