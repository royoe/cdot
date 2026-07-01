# UPDATE — T14 Correction: The $9/8$ Is an Artefact; the Sea→$a_0$ Normalization Is O(1)-Open

*Corrective update to T14 (§"Toward the RAR", §"Energy Scale", Open Items) and a downgrade
of the prior holographic-sea claim. Status: investigating the $9/8$ shows it is **not a
robust prediction** but the gap between two arbitrary choices of the profile-normalization
coefficient. The map from the (solid, $\hbar$-free) holographic sea density to $a_0$ carries
an undetermined O(1) factor. The prior "$a_0=(3/16)cH_0$, no free amplitude" was too strong.
Session: 2026-07-01.*

---

## 1. Summary (read first)

Localizing the $9/8$: it lives **entirely** in the profile-normalization coefficient (call it
PROFILE) in $g_\dagger = G\rho_\text{bg}R_0/\text{PROFILE}$. It is not three stacked factors —
it is one number. But that number is **not uniquely determined**. Three defensible
normalizations give three different answers spanning >1 order of magnitude:

| Profile normalization choice | PROFILE | Resulting $a_0$ |
|---|---|---|
| $1/r$-charge integral $Q=\int(B/4\pi r)4\pi r^2 dr = Br^2/2$, $B=\rho_\text{bg}R_0$ (used) | 2 | $(3/16)cH_0$ |
| Self-consistency with $g_\dagger=c^2/R_0$ | 9/4 | $cH_0/6$ (exact) |
| Match $\delta\rho(R_0)=\rho_\text{bg}$ → $B=4\pi\rho_\text{bg}R_0$ | — | $(3\pi/4)cH_0$ (×14) |

The $9/8$ was the gap between the first two; the third shows the coefficient is genuinely
O(1)-ambiguous, not pinned. **The $9/8$ is therefore an artefact of a specific normalization
choice, not a robust prediction.**

---

## 2. The Deeper Issue: Three Objects Were Being Conflated

The investigation exposed that three quantities were treated as interchangeable when they are
not dimensionally equivalent:

1. **Floor integral** $g_\dagger^2 \propto (4\pi G)^2\int P_\rho\,dk$. Dimensionally this is
   $\sim G^2\rho^2$, i.e. $G\rho \sim 1/\text{time}^2$ — **not an acceleration**. It requires
   an explicit length to become one. (A direct evaluation gave a result ~27 orders of
   magnitude off, confirming the floor-integral route as written was dimensionally
   incomplete.)
2. **Profile route** $g_\dagger = G\rho_\text{bg}R_0/\text{PROFILE}$. This *is* dimensionally
   an acceleration ($G\rho R_0$), but its coefficient depends on the profile amplitude $B$ —
   an undetermined O(1).
3. **Holographic identity** $\rho_\text{bg}=(\pi/6)\rho_\text{crit}=H_0^2/16G$. Clean,
   $\hbar$-free, unaffected — this stands.

The bug: the sea *density* (3) was mapped to the *acceleration* $a_0$ via the profile route
(2) with a hand-set coefficient, while the "no free amplitude" language implicitly leaned on
the floor route (1), which is dimensionally not an acceleration on its own. The apparent
precision was an illusion created by mixing the two.

---

## 3. Honest Revised Status of the Coefficient

- **The 6 in $cH_0/6$** — genuinely derived from horizon geometry ($R_0=6c/H_0=3P\,c/H_0$).
  **Solid, unchanged.**
- **The sea density** $\rho_\text{bg}=(\pi/6)\rho_\text{crit}$ — holographic, $\hbar$-free
  identity. **Solid, unchanged.**
- **The map from $\rho_\text{bg}$ to $a_0$** — carries an O(1) normalization (the profile
  amplitude / horizon-mode density contrast) that is **not derived**. The $9/8$ was one
  arbitrary choice's gap, presented as if it were the whole uncertainty. **Downgraded.**

So $a_0 = (\text{O(1)})\times cH_0/6$, with the O(1) currently unpinned — a weaker claim than
the prior "$(3/16)cH_0$, 12% high, no free amplitude." The earlier update overstated the
closure.

---

## 4. Is It Real or an Artefact? — Verdict

**The specific value $9/8$ is an artefact.** It is the ratio between profile-coefficient $=2$
(the value used) and $=9/4$ (the value that would make the profile route agree with
$g_\dagger=c^2/R_0$). Neither is uniquely forced, and a third reasonable choice differs by
14×. The $9/8$ is not a physical residual; it is an accounting gap between two hand-set
normalizations.

**What is real:** the *scale* $a_0\sim cH_0/6$ (horizon geometry + holographic sea density are
both solid and both point here to order unity). **What is not real:** the claimed 12%-level
precision. The true present uncertainty in the coefficient is the unpinned O(1) profile
normalization, which is larger than 9/8.

---

## 5. Suggested Document Edits (on merge)

- **T14 §"Toward the RAR" (lines ~146–148)** — replace "$a_0=(3/16)cH_0$… no free amplitude…
  residual $9/8$" with: the sea density is holographically pinned to $(\pi/6)\rho_\text{crit}$,
  but the map to $a_0$ via the profile carries an **undetermined O(1) normalization**; the
  scale is $a_0\sim cH_0/6$, the overall coefficient is not yet pinned. Remove the "no free
  amplitude" claim.
- **T14 §"Energy Scale"** — keep $\rho_\text{bg}=(\pi/6)\rho_\text{crit}$ ($\hbar$-free,
  solid). Add that the floor-integral expression is dimensionally $\sim G\rho$ (needs an
  explicit length $R_0$ to give an acceleration), so the profile route — not the bare floor
  integral — is what maps density to $a_0$, with its O(1) profile amplitude open.
- **T14 Open Items 1(b) and 3** — reframe: the task is not "resolve the $9/8$" but "**derive
  the profile amplitude $B$** (equivalently the horizon-mode density contrast) from the
  connecton dynamics." That single O(1) is the real remaining normalization.
- **T14 Verdict + Scorecard** — soften "$a_0=(3/16)cH_0$… no free amplitude" to "scale
  $a_0\sim cH_0/6$ from horizon geometry + holographic sea density; overall O(1) normalization
  (profile amplitude) open."
- **Core §7 / T6 / T15** (from the consistency update): where the new $a_0$ status is being
  written, use "$a_0\sim cH_0/6$; the 6 derived from horizon geometry, sea density
  holographically pinned, overall O(1) normalization open" — **not** "$(3/16)cH_0$, 12% high."
  This supersedes the coefficient wording proposed in `UPDATE_Consistency_Core_T6_T15.md` §2–§4.
- **Supersedes** the precision claim in `UPDATE_T14_Holographic_Sea_Density.md`: the
  $\hbar$-free sea-density identity stands; the "$(3/16)cH_0$, residual only $9/8$, no free
  amplitude" framing does not.

---

## 6. The Next Computation (the real one)

Derive the profile amplitude $B$ — the amplitude of the connecton density perturbation a test
orbit actually feels — from the connecton dynamics, rather than normalizing it by hand.
Equivalently: what is the horizon-mode density contrast of the $q=2$ sea? That single O(1)
number converts the solid holographic density into $a_0$. Until it is derived, the honest
statement is: **scale $a_0\sim cH_0/6$ derived; overall coefficient O(1)-open** — and the $9/8$
should not appear as a result.

---

## 7. Note

This is a correction to the prior session, produced by taking the "$9/8$: real or artefact?"
question seriously. The answer is *artefact* — and pursuing it revealed that the earlier
"no free amplitude" claim was too strong. This is the intended function of the critical pass:
a convenient-looking 12% result did not survive scrutiny, and the honest status is a clean
scale ($cH_0/6$) with an openly-acknowledged O(1) normalization rather than a false precision.
