# UPDATE — First-Principles $R$ at Recombination: A Structural Obstruction for the Static Map

*Status: proposed update, for cross-check and merge. Session 2026-07-04.*
*Targets: T16 §(A) Thermal Origin, §(B) Thermalization, §(C) Acoustic Peaks; Core §1 (static-$a$ premise); T1, T7 (energy $\propto c^2$).*
*Depends on: REVIEW_NOTE_T16_First_Peak.md (same session).*

---

## 0. One-line result

Derived from first principles, the baryon-to-photon ratio at recombination in a
static-$a$ model is **neither** the draft's $R\approx680$ **nor** the
CMB-passing $R\approx0.6$. A static map forces $R_\text{rec}\approx R_0/(1+z)^4
\approx 5\times10^{-10}$ — a radiation-dominated plasma with negligible baryon
loading, which fails the acoustic-peak structure in a **new** way. The result is
independent of the counting law and exposes a structural obstruction of the
$a=1$ premise itself. **This is a serious negative result and should be weighted
as such, subject to the caveats in §5.**

---

## 1. Where $680$ comes from, and why the argument is void

$R=680$ is simply $R$ evaluated at **today's** densities:
$R_0=3\rho_b^0/4\rho_\gamma^0 = 679.8$ using $\Omega_bh^2=0.0224$ and the
$T_0=2.725$ K blackbody. Equivalently it encodes the measured baryon-to-photon
number ratio $\eta\approx6.1\times10^{-10}$.

The draft's argument that this value holds at recombination is: "$\rho_b\propto
c^2$ and $\rho_\gamma\propto c^2$, so $R$ is epoch-invariant." **This argument is
void.** The $c^2$ factors cancel in the ratio *identically* — so the argument
establishes only that $R$ does not change *because $c$ changes*. It says nothing
about the value, which is fixed by the **number densities and the photon
temperature**:
$$R=\frac{3}{4}\frac{n_b\,m_p c^2}{n_\gamma\langle E_\gamma\rangle}
=\frac{3}{4}\frac{n_b\,m_p c^2}{\rho_\gamma c^2}\propto\frac{n_b}{T^4}.$$
The whole question is the epoch dependence of $n_b$ and $T$ — which the
$c^2$-cancellation never touches.

## 2. The two forced scalings

**Photon temperature $T_\text{rec}=T_0(1+z)$ — forced by the model's own redshift
law.** The model's redshift is an energy/frequency shift, $1+z=(c_\text{now}/
c_\text{emit})^2$. A relic photon bath observed at $T_0$ today was hotter at
emission by exactly this factor. Hence $T_\text{rec}=T_0(1+z)$ and
$\rho_\gamma\propto T^4\propto(1+z)^4$. (Numerically $T_0(1+z_{1090})=2973$ K
$\approx$ the atomic recombination temperature $\sim3000$ K — self-consistent,
though this is circular until the model derives $z_\text{rec}$ independently; see
T16-A.) This is the standard radiation scaling and is **required** for a hot,
optically-thick recombination epoch (T16-A/B) — without it there is no
thermalized blackbody and no acoustic oscillations at all.

**Baryon number density $n_b\approx$ const — forced by $a=1$.** $n_b$ is baryons
per proper volume. On a static map the proper volume of a comoving region is
epoch-independent *by definition*, and baryon number is conserved. Therefore
$n_b^\text{rec}\approx n_b^0$. To get the LCDM scaling $n_b\propto(1+z)^3$ one
needs proper volumes $(1+z)^3$ smaller in the past — i.e. expansion — which is
exactly what $a=1$ forbids.

## 3. The forced value of $R_\text{rec}$

Combining the two forced scalings:
$$R_\text{rec}=R_0\,\frac{n_b^\text{rec}/n_b^0}{(T_\text{rec}/T_0)^4}
=R_0\,\frac{1}{(1+z)^4}=\frac{680}{(1+z)^4}\approx5\times10^{-10}.$$

The plasma at recombination is then **essentially pure radiation** ($R\ll1$),
with negligible baryon loading. This gives the wrong acoustic structure: no
baryon drag, wrong odd/even peak modulation, and a first-peak height set by an
unloaded oscillator.

**Why LCDM gets $\approx0.6$ and the static map cannot.** LCDM's near-balance is
a *direct consequence of expansion*: $n_b\propto(1+z)^3$ against
$\rho_\gamma\propto(1+z)^4$ gives $R\propto(1+z)^{-1}$, so
$R_\text{rec}=680/1091\approx0.62$. Reaching $R_\text{rec}\approx0.6$ requires
$n_b\propto(1+z)^p$ with $p\approx2.99$ — essentially LCDM's $p=3$. The static
map forces $p=0$. There is no mechanism in $a=1$ to reproduce the balance.

## 4. Why none of the escape routes work (self-check)

- **"Recombination is a cold $c$-threshold, not a hot event" (T16-A):** then
  there is no thermal Saha recombination and no acoustic oscillations — the
  entire peak apparatus (T16-C) collapses. Can't be invoked to save the peaks.
- **"$n_b$ isn't constant — genesis had different densities":** $n_b$=const
  follows from $a=1$ + baryon conservation, both model commitments; changing it
  means abandoning $a=1$.
- **"$\rho_\gamma\propto c^2$ is right; the CMB is a present-value bath, not a
  relic":** then $\rho_\gamma\propto(1+z)^{-1}$ (colder in the past) — no hot
  phase, no blackbody — and $R\approx680$ at *all* epochs including
  recombination, which is **excluded by the observed peak heights**: $R=680$
  gives $(1+R)\approx681$ and suppresses the 2nd/3rd peaks by ~that factor,
  whereas Planck sees strong 2nd/3rd peaks (observed $(1+R)\sim1.6$). This is a
  clean falsification with zero counting-law input.

Each route requires discarding another model commitment. The obstruction is
robust and model-internal — it does not import LCDM assumptions; it uses the
model's own redshift law and its own static-$a$ definition.

## 5. Caveats (weight the result accordingly)

- **Thermalization is assumed, not derived.** The argument grants the model a hot,
  optically-thick, thermalized early phase (T16-B, itself unworked) in order to
  even *have* a $T_\text{rec}=T_0(1+z)$ relic. If that phase cannot be produced,
  the CMB has a different origin and this calculation's premises change. The
  obstruction is conditional on the model wanting a redshifted-relic CMB — which
  it does (T16-A/B).
- **$z_\text{rec}$ is borrowed.** The near-coincidence $T_0(1+z_{1090})\approx3000$
  K is self-consistent but circular until $z_\text{rec}$ is derived within the
  model (still open, T16-A). The obstruction does not depend on the exact
  $z_\text{rec}$: for any $z_\text{rec}\gg1$, $R_\text{rec}=R_0/(1+z)^4\ll1$.
- **Peak-height quantification is a proxy.** The "$(1+R)$ modulation / ~400×"
  statement is the standard qualitative baryon-loading scaling, not a Boltzmann
  code. A full CAMB/CLASS-style computation should confirm the exclusion
  magnitude; it will not change the sign or the order of magnitude.
- **This bears on the $a=1$ premise, not the counting law.** It neither rescues
  nor condemns T23's $D_p(z)$. It says the CMB tension identified in the T16
  review is *dominantly* a static-$a$ baryon-loading problem, upstream of the
  counting law — consistent with the review's decomposition (the $R$ lever
  dominates the distance lever).

## 6. Consequences

1. **The T16 §C "conditional counting-law failure" framing is superseded.** The
   first-peak problem is not primarily the counting-law extrapolation; it is that
   the static map cannot produce the observed baryon loading at recombination.
   T23's $D_p(z)$ is substantially exonerated on the CMB first peak (as the review
   anticipated): even a perfect distance law cannot fix an $R\approx5\times10^{-10}$
   plasma.
2. **$R\approx680$ should be removed from T16 as the recombination value.** It is
   the *today* value; using it at recombination is the error. Replace the
   "self-similar $R\approx680$" status with this derivation.
3. **A new load-bearing obstruction for Core.** The static-$a$ premise cannot
   simultaneously deliver (i) a hot redshifted-relic CMB and (ii) the observed
   baryon-to-photon loading at recombination, because baryon-number conservation
   without expansion cannot track the $(1+z)^4$ photon growth. This is arguably a
   deeper problem than the $D_p$/$\ell_1$ issue and is independent of it.
4. **The only apparent escapes each cost a pillar:** give up $a=1$ (not a static
   map anymore); give up the hot-relic CMB (then explain the blackbody and peaks
   some other way); or find a static-$a$-compatible mechanism that makes the
   *effective* baryon loading at recombination $O(1)$ despite $n_b$=const and
   $\rho_\gamma\propto(1+z)^4$ — no such mechanism is currently in the model.

---

## 7. Proposed edits

- **T16 §C:** replace the $R\approx680$ self-similarity claim with §§1–3 here;
  change the status row to "structural obstruction — static-$a$ forces
  $R_\text{rec}\approx R_0/(1+z)^4\ll1$; peaks fail from radiation domination,
  independent of the counting law."
- **T16 §A/§B:** note that a redshifted-relic CMB *requires* $\rho_\gamma\propto
  (1+z)^4$, which is incompatible with the $\rho_\gamma\propto c^2$ statement used
  elsewhere; flag this photon-sector inconsistency explicitly.
- **T16 Status table & Open Questions:** promote "$R$ at recombination under
  $a=1$" from a peak-*height* footnote to the load-bearing CMB obstruction;
  demote the "third regime between DESI and recombination" question (it does not
  address $R$).
- **Core §1:** add the static-$a$ baryon-loading obstruction as a named open
  problem of the premise, cross-referencing this update.
