# UPDATE — T14 Correction: The Floor-Integral Pillar Is Dimensionally Invalid; Coefficient Is O(1)-Open

*Major corrective update to T14 (§"Energy Scale", §"Toward the RAR", Open Items). Status: the
attempt to derive the profile amplitude uncovered **two dimensional errors** carried in prior
sessions — the "$1/r$ density profile" was an autocorrelation (density², not density), and the
"$q=2$ floor integral" computes a frequency² ($G\rho$), not an acceleration. Neither fixes the
coefficient. What survives: the holographic sea density and the horizon-geometry 6. The
overall $a_0$ coefficient is genuinely O(1)-open. The MOND regime itself is unaffected (it
rests on the closure, not on these). Session: 2026-07-01.*

---

## 1. Summary (read first)

Deriving the profile amplitude $B$ (the last open O(1)) instead exposed that two intermediate
results from prior sessions were dimensionally invalid:

1. **The "$1/r$ density profile"** (profile session) was the **autocorrelation** $\xi(r)$ of
   the $q=2$ field — units (kg/m³)², not kg/m³. The $1/r$ *shape* is real for a $k^{-2}$
   field, but $\delta\rho(r)\ne\xi(r)$. The "$1/r$ profile → constant acceleration" argument
   does not stand as written.
2. **The "$q=2$ floor integral"** $g_\dagger^2=(4\pi G)^2/(2\pi^2)\int P_\rho\,dk$ evaluates
   to $\sim G\rho \sim 1/\text{time}^2$ — a **frequency², not an acceleration**. An
   acceleration needs an explicit length; the only one available is $R_0$. So the floor
   integral never legitimately fixed the coefficient (this is why direct evaluations came out
   ~27–30 orders off). **Demote this pillar.**

The only dimensionally valid sea acceleration is $g_\dagger\sim G\rho_\text{bg}R_0$ — the
profile route — whose O(1) coefficient (PROFILE) is not fixed by the (invalid) floor work.

---

## 2. What Survives (dimensionally checked)

- **Holographic sea density** $\rho_\text{bg}=(\pi/6)\rho_\text{crit}=H_0^2/16G$ — solid,
  $\hbar$-free. Unchanged.
- **The 6 in $cH_0/6$** — horizon geometry $R_0=6c/H_0=3P\,c/H_0$. Solid.
- **The dimensionally valid combination** $G\rho_\text{bg}R_0=(3/8)cH_0$ — clean number.
- **The RAR closure** $g_x(g_x+g_\text{bar})=g_\text{bar}g_\dagger$ — derived from
  indistinguishability, matches McGaugh to 0.020 dex, alternatives data-excluded. **Wholly
  independent of the profile/floor errors** — it uses $g_\dagger$ as a scale, not its
  microphysical value. The MOND regime and functional form are secure.

## 3. What Does Not Survive

- The claim that the $q=2$ spectrum + floor integral **fixes** the coefficient
  (UV-independently). The integral is dimensionally a frequency², not an acceleration; its
  "UV-independence" does not transfer to $a_0$.
- The claim $a_0=(3/16)cH_0$ "with no free amplitude, residual only $9/8$." The $9/8$ and the
  $3/16$ both came from a specific (unforced) value of PROFILE.
- The "$1/r$ density profile" as a literal density profile (it was $\xi(r)$).

## 4. Honest Coefficient Status

$$a_0 = \frac{G\rho_\text{bg}R_0}{\text{PROFILE}} = \frac{(3/8)\,cH_0}{\text{PROFILE}},$$
with $\rho_\text{bg}=(\pi/6)\rho_\text{crit}$ solid and PROFILE an **undetermined O(1)** set by
how the sea density maps to the force a test orbit feels — which requires the connecton force
law, not yet derived independently of the closure. Reasonable choices give PROFILE ∈ {2, 9/4,
π-valued}, spanning a factor of a few. Therefore:

**The scale is $a_0\sim cH_0/6$ (solidly, from horizon geometry + holographic density,
$G\rho_\text{bg}R_0=(3/8)cH_0$); the overall coefficient is genuinely O(1)-open.** This is
weaker than the prior two sessions claimed, and it is the honest status.

---

## 5. Suggested Document Edits (on merge)

- **T14 §"Energy Scale"** — keep $\rho_\text{bg}=(\pi/6)\rho_\text{crit}$ ($\hbar$-free,
  solid). **Remove** the claim that the $q=2$ floor integral fixes $g_\dagger$; add that the
  floor integral is dimensionally $G\rho$ (frequency², not acceleration) and so does not by
  itself set the coefficient. Retain the $q=2$ slope derivation as a spectral result, but
  drop its role in pinning $a_0$.
- **T14 §"Toward the RAR"** — replace the $(3/16)cH_0$ / $9/8$ text with §4 above:
  $a_0=(3/8)cH_0/\text{PROFILE}$, PROFILE an undetermined O(1); scale $\sim cH_0/6$ solid,
  coefficient open. Remove "no free amplitude."
- **T14 — the $1/r$ profile passage** (from the profile-session merge) — correct: the derived
  $1/r$ object was the autocorrelation $\xi(r)$ (density²), not the density profile; the
  constant-acceleration claim from it does not hold. Note the MOND regime instead rests on the
  closure (unaffected).
- **T14 Open Items 1(b), 3** — reframe the task as: **derive PROFILE from the connecton force
  law** — the amplitude of the actual force a test mass feels in the sea. This is the single
  O(1) between the solid holographic density and $a_0$. Do not phrase it as "resolve the
  $9/8$" (that number was an artefact of one PROFILE choice).
- **T14 Verdict / Scorecard** — soften to: "scale $a_0\sim cH_0/6$ from horizon geometry +
  holographic sea density; overall O(1) coefficient (PROFILE) open; MOND functional form and
  flat regime secured by the closure, independent of the coefficient."
- **Core §7 / T6 / T15** — the $a_0$ status to write is "$a_0\sim cH_0/6$; scale derived
  (horizon geometry + holographic density), overall O(1) coefficient open; MOND form derived
  from the closure." **Not** "$(3/16)cH_0$" and **not** "$cH_0/2\pi$."
- **Supersedes:** the coefficient-precision claims in `UPDATE_T14_Holographic_Sea_Density.md`
  (the sea-density identity stands; its $a_0$ precision does not) and the "resolve the $9/8$"
  framing of `UPDATE_T14_9over8_Artefact.md` (correct that it's an artefact, but the deeper
  issue is the demoted floor pillar + the two dimensional errors, not just the profile
  coefficient). Also revises the coefficient wording in `UPDATE_Consistency_Core_T6_T15.md`.

---

## 6. What This Does NOT Touch

The RAR functional form, the 0.020-dex McGaugh match, the indistinguishability closure, the
BTFR asymptote, and the M-σ-as-derived-consequence all rest on the closure and the *scale*
$g_\dagger$, not on its microphysical coefficient. They are unaffected. Only the absolute
value of $a_0$ is O(1)-open — as it has effectively been all along, now stated honestly.

---

## 7. The Next Computation

Derive PROFILE from the connecton force law: given the holographic sea density
$\rho_\text{bg}=(\pi/6)\rho_\text{crit}$, what acceleration does a test mass actually
experience from its perturbation of the sea? This requires the connecton momentum-transfer /
gradient law (the same physics behind $g_N$ from foam diffusion), applied to the background
sea rather than to a point source. That single O(1) closes — or bounds — the coefficient. If
it cannot be derived cleanly, $a_0$'s coefficient is the theory's one normalization input, and
should be stated as such (its $\Omega_\Lambda$ analogue), with the *scale* $cH_0/6$ as the
firm, derived content.
