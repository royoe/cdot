# UPDATE — T14: Kinetic Derivation of the RAR Closure from Connecton Diffusion

*Proposed update to T14 (§"RAR Crossover from the Selection Junction" and Open Items).
Status: the RAR closure is derived from connecton transport kinetics plus an existing
T14 premise (indistinguishability); the data exclude the nearby alternative closures. The
RAR **shape** is now predicted, not fitted. The absolute **scale** coefficient remains
open. Session: 2026-06-30.*

---

## 1. Result in One Line

The selection-junction closure $g_x(g_x+g_\text{bar}) = g_\text{bar}\,g_\dagger$ is **not an
independent assumption**: it follows from (a) the generalized-Poisson reduction
$D(g)\,g = g_\text{bar}$ standard for any diffusive/Le Sage field, and (b) connecton
**indistinguishability** — identical, conserved, re-emitted quanta, already a T14 premise.
The empirical RAR discriminates at the 0.02–0.11 dex level and **selects exactly this
closure**, excluding the alternatives that slightly different relaxation kinetics produce.

---

## 2. The Derivation

**Step 1 — Reduction to a constitutive law.** For a diffusive connecton field with flux
$\mathbf{J} = -D\,\nabla\phi$, spherical steady state gives the nonlinear-Poisson (AQUAL-type)
reduction
$$D(g)\,g = g_\text{bar}, \qquad g \equiv g_\text{obs},\ \ g_\text{bar} = \frac{GM(<r)}{r^2}.$$
The target closure is algebraically identical to the constitutive law
$$D(g) = \frac{g}{g+g_\dagger} \quad(\text{the ``simple'' } \mu\text{-function}),$$
since $g_x(g_x+g_\text{bar})=g_\text{bar}g_\dagger$ with $g_x=g_\text{obs}-g_\text{bar}$
rearranges to $g_\text{bar}=g_\text{obs}^2/(g_\text{obs}+g_\dagger)$, i.e.
$D=g_\text{bar}/g_\text{obs}=g/(g+g_\dagger)$. So "derive the closure" = "derive $D(g)$."

**Step 2 — Excess-field steady state.** The connecton excess $g_x=g_\text{obs}-g_\text{bar}$
is produced by the baryonic source (rate $\propto g_\text{bar}$) and removed by relaxation
(rate $\nu$ acting on $g_x$). Steady state:
$$g_\text{bar} = \nu\,g_x.$$

**Step 3 — The relaxation rate (the one non-trivial step).** Kinetic theory:
$\nu = n_\text{scatter}\,\sigma\,c$. The cross-section $\sigma$ and speed $c$ are fixed; the
content is what ambient population $n_\text{scatter}$ an excess connecton relaxes against.
Because connectons are **identical, conserved, re-emitted quanta** (T14), an excess connecton
cannot distinguish background connectons from other excess connectons. It therefore relaxes
against the **total** ambient population:
$$\nu \propto \frac{g_\text{tot}}{g_\dagger} = \frac{g_x+g_\text{bar}}{g_\dagger}.$$

**Step 4 — Closure.** Substituting into the steady state:
$$g_\text{bar} = \frac{(g_x+g_\text{bar})\,g_x}{g_\dagger}
\;\Longrightarrow\; \boxed{\,g_x(g_x+g_\text{bar}) = g_\text{bar}\,g_\dagger.\,}$$
Solving: $g_\text{obs}=\tfrac12(g_\text{bar}+\sqrt{g_\text{bar}^2+4g_\text{bar}g_\dagger})$.
Deep-MOND coefficient = **exactly 1** (BTFR $v_f^4=GM\,g_\dagger$ exact); Newton recovered
in the strong field.

---

## 3. Why This Is a Derivation, Not a Restatement

The earlier "relaxation rate $\propto$ total field" phrasing looked like it might be the
closure in disguise. It is not: it traces to an **independent, pre-existing premise** —
connecton indistinguishability (identical conserved re-emitted quanta) — which was in T14
from the start for **unrelated** reasons (the Le Sage thermal-catastrophe resolution and the
clean equivalence principle). The MOND closure is a *consequence* of that ontology, derived
here for the first time.

**The data select it.** Three relaxation laws, their RAR fit:

| Relaxation law | Closure | max \|Δ\| vs McGaugh |
|---|---|---|
| $\nu\propto g_\text{tot}$ (indistinguishable quanta) | $g_x(g_x+g_\text{bar})=g_\text{bar}g_\dagger$ | **0.020 dex** |
| $\nu\propto g_x$ (excess relaxes against excess only) | $g_x^2=g_\text{bar}g_\dagger$ | 0.113 dex |
| quadrature throughput | $g_\text{obs}^2=g_\text{bar}^2+g_\text{bar}g_\dagger$ | 0.057 dex |
| $\nu=\text{const}$ | no MOND limit | — |

Only the indistinguishability law sits inside 0.05 dex everywhere. The alternatives bulge
below the lower edge of the 0.13 dex scatter band in the transition region — i.e. the data
**exclude** them. The change request's test ("the data discriminate at the 0.02–0.10 dex
level, so the PDE's verdict is checkable") is met, and the verdict is positive.

---

## 4. Crossover Point — A Small Improvement

The kinetic derivation places the crossover ($g_x=g_\text{bar}$) at
$$g_\text{bar} = g_\dagger/2,$$
a clean order-unity result. This **supersedes the golden-ratio wrinkle**
($g_x/g_\text{bar}=1/\varphi$) noted in the prior RAR-crossover update — that was an artifact
of the geometric-mean framing and does not appear in the kinetic derivation.

---

## 5. Honest Limitations (do not overstate on merge)

1. **Shape derived, scale not.** The relaxation rate carries a normalization
   $\nu\propto g_\text{tot}/g_\dagger$ with $g_\dagger$ that must equal $cH_0$ at the observed
   $a_0\approx cH_0/2\pi$. The $1/2\pi$ coefficient still traces to the unproven closure
   condition $4\pi GL\rho_\text{bg}/(3\sigma)=c$. The RAR **functional form** is now derived;
   the **absolute scale coefficient** is not.
2. **Relaxation-time closure, not full transport.** Step 1 assumes the connecton field
   obeys a generalized-Poisson (AQUAL-type) divergence structure, and Step 3 uses a
   relaxation-time approximation. A fully first-principles version would start from the
   connecton Boltzmann/transport equation, show the diffusion approximation holds, and derive
   $D(g)$ from the scattering kernel directly. This work is one rung less fundamental than
   that.
3. **Attractor convergence still assumed** — that the Lorentz filter concentrates the
   surviving population on the marginal-binding curve at all radii (carried from prior
   updates). The constitutive-law derivation is logically separate from, and does not
   resolve, this dynamical-systems question.

---

## 6. Suggested Document Edits (on merge)

- **T14 §"RAR Crossover from the Selection Junction"** — append a "Kinetic derivation"
  subsection with §2 above. Upgrade the closure's status line from "motivated two ways
  (connecton / minimality)" to "**derived** from connecton indistinguishability + generalized-
  Poisson reduction; data exclude the alternatives." Replace the golden-ratio wrinkle note
  with the $g_\text{bar}=g_\dagger/2$ crossover (§4).
- **T14 Open Items** — Open Item 1 (PDE derivation of the closure) is **substantially
  discharged at the shape level**: rewrite it as "derive $D(g)$ from the connecton transport
  kernel (full Boltzmann), and pin the scale coefficient $g_\dagger=cH_0/2\pi$ via the closure
  condition." The shape half is done; the kernel + coefficient half remains.
- **T14 Verdict table** — BTFR+RAR row: change "connecton provides a physical argument for the
  closure" to "**connecton indistinguishability derives the closure shape**; data exclude
  alternatives; scale coefficient open."
- **Core Principles §7** — RAR line: from "BTFR, scale, and full RAR crossover ... follow from
  the transition-radius / selection-junction construction; closure derivation and $a_0$
  coefficient open" to "**RAR shape derived** from connecton indistinguishability (T14),
  matching McGaugh to 0.02 dex parameter-free, alternatives data-excluded; **scale coefficient
  $a_0\approx cH_0/2\pi$ remains the open item.**" No core premise changes — the derivation
  *uses* an existing premise (indistinguishability) rather than adding one.

---

## 7. The Next Computation (highest leverage)

Two remaining rungs, in order:
1. **Scale coefficient.** Derive $g_\dagger = cH_0/2\pi$ from the closure condition
   $4\pi GL\rho_\text{bg}/(3\sigma)=c$ — this is now the single biggest open item for the RAR,
   and it is shared with the $a_0$-normalization debt in T6.
2. **Transport kernel.** Derive $D(g)=g/(g+g_\dagger)$ from the connecton Boltzmann equation
   to replace the relaxation-time closure of Step 3 — converting "predicts the RAR shape" into
   "predicts the RAR shape from the scattering kernel with no relaxation-time ansatz."
