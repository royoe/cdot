# Update — WP3: A Normalization Bug in the Back-Reaction Magnitude — Corrected, the Effect Is Real but Roughly Double the Advisory's Figure

*Companion: `SessionLog-2026-07-13.md` (this directory), Entry 15. Responds to
`Advisory-WP3-BackreactionMagnitude-2026-07-13.md` and its companion
`backreaction_magnitude.py`. The advisory's endorsement of the closed action and
its coupling-audit dispositions are correct and are not affected by what follows.
The magnitude computation, however, has a genuine normalization bug: `tilde_pi`
and `P`'s sourced term are integrated as if they were rates per unit $s$, when the
underlying equation they come from ($\dot\pi_i=-\Lambda_Mq'(\mathcal
N_\text{tot})\mathcal N_i$, verified in `Update-WP3-ClosedActionCouplingAudit-
2026-07-13.md`) is a genuine rate per unit coordinate time $t$. Found by building
an independent, from-scratch cross-check — not by re-reading the advisory's own
algebra — per this program's standing discipline of never trusting a script's
output without an independently-constructed comparison.*

---

## 1. Where the bug is, and how it was found

Re-deriving the advisory's working relation from my own verified equations (not
from theirs): using $Q=q(\mathcal N_\text{tot})$ to write $q'(\mathcal
N_\text{tot})=\dot Q/\dot{\mathcal N}_\text{tot}$, the ratio
$$q'(\mathcal N_\text{tot})\,\mathcal N_\text{tot}
=\frac{\dot Q}{d\ln\mathcal N_\text{tot}/dt}
=\frac{dQ/ds}{d\ln\mathcal N_\text{tot}/ds}\equiv\frac{dQ/ds}{\bar g}$$
**is** parametrization-free (both numerator and denominator pick up the same
$ds/dt$ Jacobian, which cancels) — this part of the advisory's construction is
exactly right, and is a genuinely elegant trick (using the M5 constraint itself to
get $q'\mathcal N_\text{tot}$ without ever needing $q$'s absolute normalization).

But the equation this feeds, $\dot\pi_\text{tot}=-\Lambda_Mq'(\mathcal
N_\text{tot})\mathcal N_\text{tot}$, is a **$d/dt$** equation (verified against a
solved coupled system in the prior update, residuals $\sim10^{-10}$) — substituting
the ratio above gives $\dot\pi_\text{tot}=\tfrac52\Lambda_MQ/\bar g$, still a
$\dot{}=d/dt$ statement. Converting to $d\pi_\text{tot}/ds$ requires one more
factor of $dt/ds=1/\dot s$, i.e.
$$\frac{d(16\pi G\,\pi_\text{tot})}{ds}=\frac52\,\frac{a^3F_Q}{\bar g\,\dot s},
\qquad\dot s\equiv\frac{ds}{dt}=\frac23\,N\,E(s)\ \ (H_{\tau,0}=1\text{ units}),$$
**not** $\tfrac52a^3F_Q/\bar g$ as the advisory's §2 states and
`backreaction_magnitude.py` computes. The same missing $\dot s$ enters $P$'s
sourced term the same way (the $+P$ homogeneous piece of $dP/ds$ is unaffected —
it is an unambiguous $s$-derivative already).

**Verification, three independent ways before reporting this:**
1. Re-derived by hand, tracking every $d/dt\leftrightarrow d/ds$ conversion
   explicitly (§1 above).
2. Built a genuine coordinate-time axis $t(s)=\int_{}^{s}dt/ds'\,ds'$ by
   numerically integrating $1/\dot s$ on the actual fitted trajectory, then
   integrated the (unambiguous) $d/dt$ form of the $\pi_\text{tot}$ equation
   directly in $t$, and mapped the result back onto $s$. This "gold standard,"
   built with no reference to which formula is right, agrees with the
   $\dot s$-corrected $s$-integration to $10^{-6}$ relative precision at every
   sampled point from $z=10^5$ to $z=0$, and disagrees with the advisory's
   as-delivered formula by the factor reported below.
3. Checked that the **algebraic** step converting $\tilde\pi\equiv16\pi
   G\pi_\text{tot}$ and $P$ into constraint contributions
   ($D_\pi=\tilde\pi\,\kappa\lambda x\,NE/(9a^3)$, $D_{p_R}=P/(6a^3)$) is
   **unaffected** — re-deriving it independently reproduces the advisory's own
   formula exactly. The bug is isolated entirely to how $\tilde\pi$ and $P$
   themselves are integrated, not to the constraint-contribution formula built on
   top of them, and not to any of the coupling-audit dispositions (items 1–3),
   which concern algebraic/structural properties unaffected by this time-axis
   question.

## 2. Corrected magnitude

| $z$ | $D/E^2$ (advisory, as delivered) | $D/E^2$ (corrected) |
|---|---|---|
| $1100$ | $-7.0\times10^{-8}$ | $-6.8\times10^{-7}$ |
| $100$ | $-1.0\times10^{-5}$ | $-6.5\times10^{-5}$ |
| $20$ | $-2.0\times10^{-4}$ | $-9.5\times10^{-4}$ |
| $2$ | $-7.8\times10^{-3}$ | $-2.5\times10^{-2}$ |
| $1$ | $-1.7\times10^{-2}$ | $-4.7\times10^{-2}$ |
| $0.5$ | $-2.7\times10^{-2}$ | $-6.8\times10^{-2}$ |
| $0$ | $-4.85\times10^{-2}$ | $-9.5\times10^{-2}$ |

The corrected peak (at $z=0$, same location as before) is **roughly double** the
advisory's figure — not a rounding-level correction. Ran the one-pass
perturbative iteration the advisory recommended, with the corrected formula: using
$\Omega_s^\text{corr}=\Omega_s-D_0$ as the quadrature's source and recomputing $D$
gives $D_1/E^2=-1.024\times10^{-1}$ at $z=0$ (a $7.4\%$ relative shift from $D_0$);
a second pass gives $D_2/E^2=-1.028\times10^{-1}$ (a further $0.4\%$ shift) —
**converges within two passes**, confirming the advisory's qualitative
"perturbative, not structural" claim survives the correction even though the
absolute size roughly doubles. Truncation/convergence of the retarded integral
checked the same way as the advisory's own script (edge/max ratio $3.5\times
10^{-10}$) — the correction does not reopen any convergence question.

## 3. What does and doesn't change

- **WP4a (acoustic scale) and WP4b (BBN) remain untouched**: even doubled, the
  effect is $\sim7\times10^{-7}$ at recombination and $\sim10^{-11}$ in the deep
  past — many orders of magnitude below anything either check is sensitive to.
- **The "perturbative, not structural" verdict stands**, now demonstrated with
  the corrected formula rather than inherited: two iterations converge to
  $0.4\%$, not one to an unstated precision — a small strengthening of the
  advisory's own claim, not a reversal of it.
- **Step 5 is still cleared to run**, but on $\Omega_s^\text{corr}\approx
  \Omega_s-D_2$ (the twice-iterated, $\sim10\%$ correction), not the
  once-iterated $\sim5\%$ figure — a real, if modest, change to what "the
  constraint" means going into the razor/total-Bianchi confrontation.
- **The coupling-audit dispositions (items 1–3) and the $N=1$/pre-verified-row
  validations of the closed action are untouched** — none of them depended on
  the time-integration of $\pi_\text{tot}$ or $P$, only on their instantaneous
  algebraic role in the constraint and in each other's equations of motion.

## 4. Status

Not a kill, not a pass on either side — a factual correction to a specific,
identified computational step, found by building an independent cross-check
rather than re-reading the delivered algebra, exactly the practice this program
runs on in both directions. Flagging explicitly for the advisor's own
independent check before this is taken as final (the same courtesy every prior
correction in this program has been given): verify the $\dot s=\tfrac23NE$
factor and the $t(s)$ cross-check in your own conventions, since a
factor-of-roughly-2 discrepancy at the input to step 5 is worth a second
confirmation before the razor is run. Recommend: confirm this correction, then
proceed to step 5 on the twice-iterated $\Omega_s^\text{corr}$. WP2
discharge-by-incorporation proposal (advisory §4 item 4) not yet assessed —
carried forward, no objection raised, not yet confirmed either. WP2 finalization
still hard-blocks pending that; the KATRIN clock remains the program's most
time-critical item; nothing in `cdot-7/` was touched.
