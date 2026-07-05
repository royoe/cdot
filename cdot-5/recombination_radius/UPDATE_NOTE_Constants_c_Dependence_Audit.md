# UPDATE NOTE — Audit of Constant $c$-Dependence in the Recombination Sector

*Status: audit note, to be folded into cdot-5 T16 (§R-derivation, §z_rec open item).*
*Date: 2026-07-05.*
*Targets: T16 cdot-5 §"$R$ at recombination", §"$z_\text{rec}$", §"Thermal Origin"; T7 (constants).*
*Depends on: UPDATE_R_at_Recombination_Derivation.md; cdot-5 T16.*

---

## 0. Why this note exists

The recombination-sector results depend on the $c$-scaling of several "constants."
Some of these carry hidden $c$-dependence (notably the radiation constant
$a_\text{rad}\propto c^{-3}$), and getting them wrong is exactly what produced the
original $R\approx680$ error. This note audits every constant in the sound-speed
and Saha equations, records which carry $c$-dependence, and states precisely what
that does — and does not — rescue. **Net result: the audit confirms $R_\text{rec}
\approx20.6$ on firmer footing, closes two candidate escape routes for the
$z_\text{rec}$ problem ($\eta$ and hidden constants), and shows $z_\text{rec}$
hinges solely on a kinetics question (sudden vs gradual recombination).**

---

## 1. Constant-by-constant audit

**$k_B$ (Boltzmann) — no $c$-dependence; convention.**
$k_B$ is not a constant of nature but a kelvin↔joule unit conversion. The physical
quantity is always the *energy* $k_B T$, never $k_B$ alone. Holding $k_B$ fixed is
harmless **provided** all $c$-dependence is tracked in $T$. Clean.

**$\hbar$ (action quantum) — taken fixed.**
The natural map invariant. Appears in $\lambda_\text{th}$ and $E=\hbar\omega$; with
$\hbar$ fixed the redshift/energy shift lives in $\omega$. *Flag for T7 to confirm
explicitly*, but standard.

**$a_\text{rad}$ (radiation / Stefan–Boltzmann constant) — carries $c^{-3}$.**
$a_\text{rad}=\pi^2 k_B^4/(15\hbar^3 c^3)\propto c^{-3}$ (with $k_B,\hbar$ fixed).
**This is the one that matters**, and it was the hidden factor behind the original
$R\approx680$ error, which implicitly treated $\rho_\gamma\propto c^2$.

## 2. Corrected photon-sector scalings

With $a_\text{rad}\propto c^{-3}$ and the effective bath temperature $T_\text{eff}
\propto c$ (from $n_\gamma$-conservation):

| quantity | expression | $c$-scaling |
|---|---|---|
| radiation constant | $a_\text{rad}=\pi^2k_B^4/15\hbar^3c^3$ | $c^{-3}$ |
| photon energy density | $\rho_\gamma=a_\text{rad}T^4$ | $c^{-3}\cdot c^4=c^{1}$ |
| photon number density | $n_\gamma\propto(k_BT/\hbar c)^3$ | $(c/c)^3=c^{0}$ (const ✓) |
| mean photon energy | $\langle E_\gamma\rangle=\rho_\gamma/n_\gamma$ | $c^{1}/c^{0}=c^{1}$ |
| baryon energy density | $\rho_b=n_b m_p c^2$ ($n_b$ const) | $c^{2}$ |

The $n_\gamma=$ const line is a consistency check: it reproduces the cdot-5
photon-number-conservation premise **from** $T_\text{eff}\propto c$ plus the
correct $a_\text{rad}$, rather than assuming it.

## 3. Consequence for $R$ — cdot-5 confirmed, on a cleaner route

$$R=\frac{3}{4}\frac{\rho_b}{\rho_\gamma}\propto\frac{c^2}{c^1}=c^1\propto(1+z)^{-1/2},$$
since $c\propto(1+z)^{-1/2}$ from the redshift law. This is **identical** to
cdot-5's corrected $R_\text{rec}=R_0(1+z)^{-1/2}=20.6$. The $a_\text{rad}\propto
c^{-3}$ factor is therefore already (implicitly) baked into the corrected result;
making it explicit puts $R_\text{rec}\approx20.6$ on firm footing. **The $R$ sector
survives the audit unchanged.** The original $R=680$ came precisely from omitting
the $a_\text{rad}$ $c^{-3}$ (equivalently, assuming $\rho_\gamma\propto c^2$); this
note documents that omission so it cannot recur.

## 4. Consequence for $z_\text{rec}$ — the audit closes two escape routes

The Saha ionization exponent is $\exp(-E_\text{bind}/E_\text{ion})$ with
$E_\text{bind}\propto c^2$ (T7). The ionizing-photon energy scale, checked **two
independent ways**, is:

- thermal: $k_B T_\text{eff}\propto c^1$;
- mean photon energy: $\langle E_\gamma\rangle=\rho_\gamma/n_\gamma\propto c^1$.

Both give $c^1$. Hence the exponent scales as $c^2/c^1=c^1$, i.e. the exponent
index $p=1$, giving $z_\text{rec}\approx2\times10^6$ and a catastrophic first peak.

This **closes two candidate rescues** that were on the table:

1. **$\eta$ (baryon-to-photon ratio) / conserved $n_b$ is NOT the driver.** $\eta$
   enters only through the Saha prefactor logarithm; varying $\eta$ (via $n_b$) by
   $10^{12}$ moves $z_\text{rec}$ by $<5\times$ (from $4.7\times10^6$ to
   $1.1\times10^6$). $z_\text{rec}\approx(X_0/\ln\text{pref})^2$ with
   $X_0=E_\text{bind}/k_BT_0\approx5.8\times10^4$; the driver is the large $X_0$
   combined with the weak $p=1$ scaling, not $\eta$.
2. **Hidden constant $c$-dependence is NOT a rescue.** The only constant carrying
   $c$-dependence ($a_\text{rad}$) affects the $R$/$\rho_\gamma$ sector, not the
   ionization exponent, whose photon energy scale is $c^1$ by two routes.

## 5. What actually decides $z_\text{rec}$ — the one remaining lever

The exponent $p$ is the whole ballgame ($p=1\Rightarrow z_\text{rec}\sim2\times10^6$,
disaster; $p=2\Rightarrow z_\text{rec}\sim1240$, $\ell_1\approx304$, works). $p=2$
requires the ionizing-photon energy scale to be $c^0$ (frozen, absolute) rather
than $c^1$ (thermal). Per §4 and the prior derivation, the photons **during**
recombination are still coupled, so their energy scale is $c^1$ — the frozen ($c^0$)
description applies only to the post-decoupling relic. Therefore:

> $z_\text{rec}$ hinges entirely on whether recombination is **sudden**
> (decoupling-limited — the ionizing bath is the just-frozen population, licensing
> $c^0$, $p=2$) or **gradual** (equilibrium — thermal tail governs, forcing $c^1$,
> $p=1$). Neither $\eta$, nor $n_b$-conservation, nor any constant's $c$-dependence
> changes this. It is a kinetics question.

The static-$a$ context is genuinely ambiguous here: the standard gradual
(Peebles) recombination relies on expansion redshifting Ly-$\alpha$/recombination
photons off resonance, a mechanism $a=1$ lacks — which could make recombination
effectively sudden. Establishing this requires comparing the recombination /
photoionization rate to the horizon turnover rate $H_\text{hor}$ at the candidate
epoch. That calculation is the decisive next step and is not yet done.

## 6. Recommended edits to cdot-5 T16

- **§$R$-derivation:** add the §1–3 audit; state explicitly that $R\propto(1+z)^{-1/2}$
  follows from $a_\text{rad}\propto c^{-3}$ with $T_\text{eff}\propto c$, and that
  the original $R=680$ came from omitting the $a_\text{rad}$ $c^{-3}$ factor.
- **§$z_\text{rec}$ open item:** record that $\eta$ and hidden constants are ruled
  out as levers (§4); reframe the open item as the single sudden-vs-gradual
  kinetics question (§5), with the rate-vs-$H_\text{hor}$ comparison as the
  deciding calculation.
- **§Thermal Origin / constants:** add a short "constant $c$-scaling" table (§2)
  and a note that $k_B$ is convention-fixed (track $k_B T$, never $k_B$) and
  $\hbar$ is taken fixed pending T7 confirmation.
- **Status:** the $R$ result is confirmed and stable; the first-peak $\ell_1$
  remains **conditional on the unresolved kinetics** — do not present $\ell_1\approx304$
  as established until the sudden-recombination case is made.

## 7. Caveats

- $\hbar$ fixed is assumed, not derived from T7; confirm there.
- The equilibrium-Saha treatment is a marker, not the true kinetics; §5's rate
  comparison supersedes it once done, and could in principle reintroduce $\eta$
  with more leverage through the recombination *rate* ($\propto n_b$) — worth
  checking in that calculation, though it will not change the $c^1$ vs $c^0$
  exponent question, which is about the photon energy scale, not $\eta$.
