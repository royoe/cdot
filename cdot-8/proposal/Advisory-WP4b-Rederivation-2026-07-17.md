# Advisory — WP4b Re-Derivation: The 0.276 Is Refuted; the Worker's cdot-8 Side Is Confirmed and the Error Is Localized in the Reference Construction; Corrected Verdict: BBN-Compatible (for `cdot-8/WP4/`)

*2026-07-17. Advisory in response to
`Update-WP4b-BBN-Correction-2026-07-16.md` and
`Update-WP4b-Converged-2026-07-17.md`, executing the independent
re-derivation the converged update itself requested before its result feeds
the decision input. Full construction in `wp4b_rederivation.py`. Verdict up
front: **the severe result does not survive. At fixed local temperature —
the comparison BBN physics actually runs on — the ratio is
$H_{\hat\tau}(T)/H_\text{SBBN}(T)=0.965$–$1.007$ across the entire BBN
window, not $0.276$. The worker's escalation posture was exactly right
("verified as far as I can push alone, not asserted as final"), and their
cdot-8-side machinery is vindicated in detail: their trajectory sanity
numbers, their WP4a regression value, and their first-principles
$(11/4)^{1/3}$ reproduction are all also my numbers. The factor-3.5 error
is localized in the reference side of their ratio — two independently-built
sides with independently-applied temperature bookkeeping, where my
construction uses one shared map that cancels the bookkeeping identically.
Corrected leading-order verdict: cdot-8 is BBN-compatible — $Y_p\approx
0.242$ (within $1\sigma$ of observed), D/H shifted $\sim-1\%$ (negligible),
Li-7 down $\sim10$–$15\%$ (the favorable lean). The decision-input picture
inverts on the BBN side and sharpens on the acoustic side.***

---

## 1. The construction, and why it is immune to the error class involved

Both sides carry the identical local thermal physics (K1): $T_\gamma(a)$
solved exactly from photon$+e^\pm$ entropy conservation
($[1+s_{e^\pm}/s_\gamma(T)]\,T^3a^3=T_{\gamma,0}^3$); $T_\nu a=$ const
(frozen always — automatically equal to $T_\gamma$ above the transition);
$e^\pm$ at equilibrium with the corrected $1.75$ ratio. The census
$u(a)$ is then one function used by *both* sides: cdot-8's
$H=H_0E(a)$ from the closure with this source, and SBBN's
$H_\text{SBBN}=H_0\sqrt{u(a)}$ — so at any temperature $T$, with the single
shared $a(T)$ map,
$$\frac{H_{\hat\tau}(T)}{H_\text{SBBN}(T)}=\frac{E(a(T))}{\sqrt{u(a(T))}},$$
and every $T$-vs-$z$ bookkeeping choice cancels *identically* because there
is only one of it. This ratio is manifestly the square root of the invoice
fraction — the one genuinely cdot-8-specific quantity at these epochs.

Checks, all clean: $u_{e^\pm}/u_\gamma(A{=}0)=1.7500$ and
$s_{e^\pm}/s_\gamma=1.7500$; the high-$T$ boost emerges as
$T a/T_{\gamma,0}\to0.7138=(4/11)^{1/3}$ exactly (the worker's own §1 check,
reproduced); **WP4a regression: $E(1090)=18397.6$** against the established
$18398$–$18404$; $\mu$-saturation monitor: max $y=0.775$ — precisely the
radiation-fixed-point value, no saturation anywhere.

## 2. The result

| $T$ (MeV) | $z$ | $x(s)$ | $H_{\hat\tau}/H_\text{SBBN}$ |
|---:|---:|---:|---:|
| 3.0 | $1.8\times10^{10}$ | 3.441 | 0.966 |
| 2.0 | $1.2\times10^{10}$ | 3.438 | 0.967 |
| 1.0 | $5.9\times10^{9}$ | 3.421 | 0.972 |
| 0.7 | $4.1\times10^{9}$ | 3.402 | 0.978 |
| 0.3 | $1.7\times10^{9}$ | 3.315 | 1.007 |
| 0.1 | $4.6\times10^{8}$ | 3.350 | 0.995 |
| 0.05 | $2.1\times10^{8}$ | 3.442 | 0.966 |
| 0.02 | $8.5\times10^{7}$ | 3.444 | 0.965 |

The deficit is **3.5% in $H$, not 72%** — and non-uniform in an interesting
way: during the annihilation transient the closure trajectory dips below
the radiation fixed point ($x\to3.315$) and the ratio briefly *exceeds*
unity before settling back to $\sqrt{0.93}\approx0.965$. The effective
$\Delta N_\text{eff}$ is $-0.34$ at $T=1$ MeV, $-0.28$ at weak freeze-out
($0.7$ MeV), $\sim-0.1$ during helium formation — milder than even the
originally-withdrawn $-0.7$.

**Where the worker's $0.276$ came from (diagnosis, hypothesis-grade until
their code confirms):** their cdot-8 side is correct — their trajectory
check ($x=3.3$–$3.44$), their regression ($E(1090)=18403$), and their boost
reproduction are all numerically *my* values. The error must therefore live
in the reference side or the comparison mapping. The magnitude is
suggestive: $0.965/[(11/4)^{2/3}\times1.75]=0.281\approx0.276$ — exactly
the stack produced if the reference $H_\text{SBBN}$ is evaluated through a
naive $T=T_{\gamma,0}(1+z)$ mapping (factor $(11/4)^{2/3}\approx1.96$ in
radiation-era $H$ at fixed $T$) while missing or mismatching the $e^\pm$
content (factor up to $1.75$). Locate the exact anatomy in the code for
the ledger; the structural lesson is already clear and is adopted as a K6
rule: **when confronting two models at a shared physical variable, build
the comparison through one shared map so that bookkeeping cancels by
construction — never through two independently-assembled sides.** Two
independently-built sides invite exactly the single-sided-correction class
of error that three rounds of this confrontation have now produced.

## 3. Corrected leading-order BBN verdict

With $\Delta N_\text{eff}^\text{eff}\approx-0.3$ (freeze-out epoch) and the
census $\omega_b$ 3% below Planck, standard sensitivity coefficients are
back in their validity regime:
$$Y_p\approx0.243\pm0.001\ \text{(obs }0.2453\pm0.0034\text{: within }1\sigma),$$
$$\text{D/H}\approx-1\%\ \text{vs SBBN (negligible against }\sim1.5\%\text{ obs precision)},$$
$$\text{Li-7}\approx-10\text{ to }-15\%\ \text{(favorable lean, far short of the }-70\%\text{ deficit)}.$$
**cdot-8 passes BBN at leading order** — comfortably, and with the
annihilation-transient structure mildly helping. The "severe tension"
framing of the converged update is withdrawn along with its number; the
"borderline (−2.3σ)" framing of the checklist round is also superseded
(it was built on the earlier bugged table). A reaction-network code remains
the precision instrument if this is ever pushed past leading order, but
nothing at this order motivates urgency.

## 4. What this does to the decision input — sharper on both ends

The Foundation §6 item 6 input now reads: **the expansion-history deficit
is confirmed to be a crossover-era phenomenon, not a radiation-era one.**
Deep in radiation ($T\gtrsim0.02$ MeV, $z\gtrsim10^8$) the deficit is
3.5% and BBN passes; at recombination it is 21% and the acoustic scale
fails by 27%. The localization from the discrepancy hunt is thus
strengthened and narrowed: the failure lives specifically in the census
matter-radiation crossover structure ($z_\text{eq}^\text{census}\approx
z_*$, set by the heavy-neutrino census loading), the one place the
framework's expansion history departs by tens of percent from what the
data requires. One epoch, one structural cause, one failing observable —
and one passing one on either side of it (SN diagram below, BBN above).
The KATRIN coupling tightens correspondingly: $\Sigma m_\nu$ sets the
crossover.

## 5. Ledger and endorsements

- **Worker's escalation posture: exemplary and credited.** They found a
  severe result, failed to break it alone, and explicitly routed it
  through independent re-derivation *before* the decision — which is the
  only reason a factor-3.5 error is a ledger entry rather than a
  contaminated author decision.
- **Worker's WP3 symbolic closure (correction update §1): accepted.**
  $\partial g_i/\partial N=0$ by inspection is a mathematical identity;
  $D\equiv0$ follows; **WP3 is formally closed** — the checklist item is
  discharged, and their point that inspection beats re-running is well
  taken.
- **My Flag-1 assessment corrected**: I guessed "likely benign prose
  slip"; the worker showed it was a real factor-2 code bug. Their
  confirmation discipline beat my charitable guess — noted.
- **Their entropy machinery (converged update §1) is endorsed as
  correct** — the $T_\gamma(a)$ construction, the frozen-$\nu$ treatment,
  the sharp-decoupling continuity argument all check out; one prose
  slip flagged: their above/below-decoupling sentence is inverted
  relative to what the physics (and evidently their code, given the
  regression) does.
- Log hygiene: the accidental SessionLog overwrite (correction update
  preamble) plus the standing numbering reconciliation — one combined
  repair per the Entry-9 rule at next worker delivery.

## 6. Directives

1. Worker verification of §1's construction and locating the
   reference-side bug anatomy for the ledger.
2. The consolidation batch (now including: this round's K6 shared-map
   rule; the withdrawn WP4b tables' errata chain; the census-law scope
   statement; everything previously listed).
3. **Then the author's Foundation §6 item 6 decision, with the corrected
   input of §4**: crossover-era failure, radiation-era pass, low-$z$ pass,
   levers 5–10% against a 27% requirement, KATRIN coupled at the
   crossover.
4. KATRIN clock: unchanged, most time-critical.

## Companion

- `wp4b_rederivation.py` — the shared-map construction, all limit checks,
  the regression, the ratio table, the saturation monitor.
- This advisory: proposed location
  `cdot-8/WP4/Advisory-WP4b-Rederivation-2026-07-17.md`.
