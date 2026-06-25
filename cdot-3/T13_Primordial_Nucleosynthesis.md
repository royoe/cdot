# T13 — Primordial Nucleosynthesis and Baryogenesis

*Note: This topic is substantially more speculative than T1–T12. The ideas here
depend on unresolved aspects of the model (the S′ variant, the connecton hypothesis,
the count-vs-mass fork) and should be read as research directions, not established
results.*

---

## Observational Background

### Big Bang Nucleosynthesis

Big Bang Nucleosynthesis (BBN) is the process by which the light elements H, D, $^3$He,
$^4$He, and $^7$Li were forged in the hot early universe during the first few minutes
($T \sim 0.1$–$1$ MeV, $t \sim 10$–$200$ s). BBN is a precise theoretical framework
with few free parameters (primarily the baryon-to-photon ratio $\eta = n_b/n_\gamma$
and the number of neutrino species $N_\nu$), and it fits the observed primordial
abundances well:
- $^4$He mass fraction: $Y_P \approx 0.247$ (very sensitive to expansion rate at freeze-out)
- D/H $\approx 2.5 \times 10^{-5}$ (sensitive to baryon density)
- $^7$Li/H: the "lithium problem" — standard BBN predicts $3\times$ more than observed

The $^4$He abundance is particularly sensitive to the expansion rate $H(T)$ at freeze-out
($T \sim 1$ MeV), because $H$ determines the freeze-out temperature of the weak
$n \leftrightarrow p$ reaction: faster expansion → higher freeze-out temperature →
more neutrons → more $^4$He.

Any modification to $H(T)$ at BBN epochs must keep $Y_P$ within $\sim 1\%$ of the
observed value.

### Matter-Antimatter Asymmetry

The observable universe contains essentially only matter, no significant amounts of
antimatter (evidenced by the absence of $\gamma$-ray backgrounds from bulk
matter-antimatter annihilation). The baryon asymmetry is:
$$\eta = \frac{n_b - n_{\bar{b}}}{n_\gamma} \approx 6 \times 10^{-10}.$$
The Sakharov conditions (1967) for generating this asymmetry require:
1. Baryon number violation
2. C and CP violation
3. Departure from thermal equilibrium

Standard ΛCDM does not explain the asymmetry from first principles; it is a major
open problem in particle physics and cosmology.

---

## BBN in the Model

### The role of $c$ and $H$ at BBN

In the model, $H = \dot{c}/c$ and $c$ was much larger at BBN epochs than today.
With $c \propto R^3$ and the volume-law horizon ODE, the coordinate Hubble rate at
$z \sim 10^{10}$ would be $H_\text{BBN} \gg H_0$, and $c_\text{BBN} \gg c_0$.

The nuclear reaction rates also depend on $c$ (via the nuclear Gamow energy, thermal
velocities, and electromagnetic coupling), so the freeze-out calculation is more
complex than simply substituting a different $H$. A full BBN calculation within the
model's framework has not been done.

What can be said qualitatively:
- The model's $H(z)$ at high $z$ differs from ΛCDM's. Whether it predicts the
  correct $^4$He abundance requires explicit computation.
- The baryon-to-photon ratio $\eta$ depends on how baryons and photons are generated,
  which depends on the genesis scenario (below).

### The BBN discriminator for the premise fork

The count-vs-mass fork (T12) predicts different values of $c$ at BBN epochs:
- **Count ($c \propto N$ including relativistic species):** $c$ at BBN is dominated
  by the vast number of relic photons and neutrinos ($\sim 10^9$ per baryon). $c$ would
  be enormous.
- **Classical Mach ($c \propto M_u$):** $c$ at BBN is set by the baryon rest mass only.
  Photons contribute zero; neutrinos contribute negligibly (they are relativistic and
  $m_\nu \ll m_p$).

These two formulations predict very different expansion histories at BBN, leading to
different $^4$He abundances. This is, in principle, a decisive observational test —
though the actual calculation depends on the full model including the BBN nuclear
reaction network.

---

## The Genesis Bootstrap (Speculative)

### The S′ variant

The volume-law horizon ($c \propto R^3$) has no finite coordinate-time origin: $c \to 0$
only as $t \to -\infty$. The variant S′ ($c \propto R^{2/3}$, the "surface law with
Compton self-consistency") has a **finite coordinate-time origin**: there exists a time
$t_0$ in the past when $R = 0$ and $c = 0$. This is a genuine Big Bang in map time.

S′ is motivated by a self-consistency argument: the minimal quantum that can be
localized within the horizon has a Compton wavelength $\lambda_C = \hbar/(mc)$, and
at very early times, $\lambda_C$ exceeds $R$. This means particles cannot be localized
within the horizon, which provides a natural floor and a change in the scaling of $c$
with $R$.

The physical picture: at the finite origin of S′, $R = 0$ and $c = 0$. As $R$ grows
(by some mechanism), $c$ increases. At very early times ($R \ll \lambda_C$), the
Compton-scale self-consistency enforces $c \propto R^{2/3}$; at later times, the volume
law may take over.

### The counting-Mach bootstrap

In the count reading of premise 2, the value of $c$ is set by the number of particles
in the horizon. At the moment of genesis, $N = 0$ and $c = 0$. But if a particle is
created (by a vacuum fluctuation, say), $N = 1$ and $c$ becomes non-zero. A slightly
larger $c$ allows the horizon to grow faster, encompassing more volume and allowing
more pair creation. More pairs → larger $N$ → larger $c$ → faster horizon growth →
more pairs. This is a **self-sustaining bootstrap**.

The energy scale of the first pair is set by $c$ at the moment of creation; but
$c$ is in turn set by the number of pairs. The self-consistent fixed point of
$c \propto N$ with $N$ sourced by pair creation in a $c$-dependent vacuum is the
key quantity to derive. Whether this bootstrap converges to the volume law or requires
S′ is unknown.

### The connecton role

In the connecton picture (T14), each pair-creation event produces connectons, which
mediate the relational counting (they are the physical objects that "inform" distant
parts of the universe about the local particle count). In the earliest moments, when
$c$ is small and the horizon is tiny, the connecton sea is sparse — but even a few
connectons propagating at the local (tiny) $c$ can bootstrap the system.

This is highly speculative. The physical mechanism of the bootstrap — specifically
whether the vacuum pair-creation rate in a varying-$c$ background is fast enough to
sustain the growth — has not been computed.

---

## Matter-Antimatter Asymmetry

Standard BBN and all known cosmological models struggle to explain the baryon asymmetry
from first principles. This model is no exception.

In the genesis bootstrap picture:
- The S′ finite origin provides a period of departure from thermal equilibrium (the
  third Sakharov condition): the system starts from $c = 0$, $N = 0$ and bootstraps
  up. This is not a thermal equilibrium state.
- Whether the process violates C and CP symmetry and baryon number — the other two
  Sakharov conditions — is not addressed by the current framework.

The matter-antimatter asymmetry is listed as an **open, unsolved problem** in the
model. The genesis bootstrap might provide the right thermodynamic out-of-equilibrium
condition, but the actual asymmetry requires a more specific mechanism.

---

## The Lithium Problem

Standard BBN predicts roughly 3 times more $^7$Li than observed in old, metal-poor
halo stars ("the lithium problem"). The discrepancy is at the $\sim 5\sigma$ level
and is a known tension in standard cosmology.

In this model, the modified expansion history at BBN epochs would give a different
$^7$Li yield. Whether the model produces more or less $^7$Li than standard BBN (and
whether it can resolve the problem or worsens it) is not known without a full
calculation.

---

## Open Questions

- A full BBN calculation within the model: given the horizon ODE and the $c(t)$
  profile at BBN epochs, what are the predicted $^4$He, D, $^3$He, and $^7$Li
  abundances? Does the model produce a reasonable $^4$He fraction?
- The premise-2 fork discriminator: compute the BBN abundances for both the count
  and mass versions of premise 2, and compare to observations.
- The genesis bootstrap: can the self-consistent $c \propto N$ fixed point be
  derived from a vacuum pair-creation model? What is the resulting time evolution
  of $c$ at the earliest moments?
- Matter-antimatter asymmetry: is there a specific mechanism within the S′ bootstrap
  that selects matter over antimatter? Does the connecton's propagation structure
  break CP symmetry in any way?
- The $^7$Li problem: does the model's modified BBN alleviate or worsen the
  discrepancy?
