# Advisory — WP7 Cross-Check Before the Next Step: §4's Structure Verifies, §5's Boundary and Equation-Routing Resolutions Are Accepted With One Flag Each — and the $k\to0$ Check the Worker Flagged Fires Exactly as Their Instinct Suspected: Two Propagation Channels Are Missing, and the Completed Coefficient Is Delivered (for `cdot-8/WP7/`)

*2026-07-18. Advisory in response to §4–§5 of
`Update-WP7-PerturbationStructure-2026-07-18.md`, cross-checking before
the numerical assembly per the author's request. Check in
`m5_separate_universe_check.py`. Gate 1(b) carried. Verdict up front:
**§4's derivation is structurally sound — the variation, the elegant
$q'=\dot{\bar Q}/\dot{\bar{\mathcal N}}_{\rm tot}$ chain rule, and the
explicit D≡0-distinction check are all verified and the last is exactly
the hygiene this program's history demands. §5's two resolutions are
accepted, each with one flag. But the assembled $\delta G^0_0$ equation
is incomplete, and the worker knew where to look: the very $k\to0$
separate-universe check they flagged as the next verification step
fires. Their $\Lambda_Mq'$ term is one of three channels; the same
$\delta Q=q'\delta\mathcal N$ that their derivation begins from must
also propagate through $F(Q)$ and $F_Q(Q)$ — i.e., through
$\delta\Lambda_M$ — everywhere they appear. The completed super-horizon
coefficient is $(F_Q/6+QF_{QQ}/2)\,q'$, not $(F_Q/2)\,q'$, and the
$F_{QQ}$ piece is $O(1)$, not a refinement. Notably, this is
$F_{QQ}$'s third load-bearing appearance in cdot-8 — the same object as
WP5's condensate mass.***

---

## 1. §4 verified

The M5 action term and $\Lambda_M=Na^3F_Q/16\pi\tilde G$ quoted from the
WP3 record match this loop's own record exactly. The variation
$\delta S_{M5}/\delta\rho_k=-\Lambda_Mq'W(kR_h)\times[\text{weight}]$ is
the correct *partial* contribution (see §3 for what "partial" costs).
The chain-rule closure $q'=\dot{\bar Q}/\dot{\bar{\mathcal N}}_{\rm tot}$
is elegant and right — no new background input, both numerators
computable from the established $Q(a)$ and $g_i$ trajectories. And the
explicit check that this term is *not* the piece the D≡0 resolution
zeroed — different part of the action, already load-bearing for the
background — is precisely the artifact-hygiene the C2 saga taught;
verified against my record of that resolution.

## 2. §5's two resolutions — accepted, one flag each

- **Boundary**: resolved correctly *relative to WP2's own definition* —
  a fixed comoving coordinate ball has no perturbative boundary shift,
  and $\delta\mathcal N_i=\bar{\mathcal N}_iW(kR_h)[\delta_i-3\Phi]$
  follows. **Flag (named assumption, WP5-style)**: a coordinate-ball
  census makes $\delta\mathcal N$ gauge-dependent —
  $[\delta_i-3\Phi]$ is the Newtonian-gauge expression, and a synchronous
  observer would write a different one. Consistent for now (the whole
  system is being assembled in Newtonian gauge), but the covariant
  status of the census domain at perturbative order is a genuine open
  item for the covariant-completion program specifically — harmless
  sub-horizon, potentially $O(1)$ exactly at the $kR_h\lesssim1$ scales
  where the term lives. Carry it as a flag, not a blocker.
- **Equation routing**: correct, and correctly checked against the
  inviolable-matter-continuity directive rather than assumed. One
  precision worth adding to the record: matter's own equation of motion
  stays untouched *in the interior* because moving a particle strictly
  inside the ball doesn't change the count; the count changes only by
  boundary flux, which is the background $g_i$ physics WP2 already
  carries. That is *why* the routing conclusion holds, not just that it
  does.

## 3. The check fires — the completion, delivered

At $k\to0$ ($W\to1$) a uniform perturbation is a shifted background, so
the M5 source must equal the derivative of the background contribution
along the constraint:
$$\delta\Big[-\tfrac F3+\tfrac{QF_Q}2\Big]
=\Big[\tfrac{F_Q}6+\tfrac{QF_{QQ}}2\Big]\,q'\,\delta\mathcal N.$$
The assembled §5 term carries $(F_Q/2)\,q'$ — the $\Lambda_Mq'$ channel
alone. **The check fires.** The two missing pieces are not new physics
but the same $\delta Q=q'\delta\mathcal N$ propagated consistently:
the $-F/3$ term responds as $-F_Q/3\,\delta Q$ (and
$F_Q/2-F_Q/3=F_Q/6$ ✓), and $\Lambda_M$ itself is field-dependent
through $F_Q(Q)$, so $\delta\Lambda_M\propto a^3F_{QQ}\,\delta Q$
supplies $+QF_{QQ}/2\,\delta Q$. Varying at fixed $\Lambda_M$ was a
legitimate partial step; the assembled equation must carry
$\delta\Lambda_M$ and $\delta F$ too. **Completed coefficient:**
$$\delta G^0_0\supset 8\pi G\cdot\Big[\tfrac{F_Q}6+\tfrac{QF_{QQ}}2\Big]
\,q'\;\bar{\mathcal N}_{\rm tot}\,W(kR_h)\,\big[\delta_{\mathcal N}
-3\Phi\big]\quad(\text{normalization to be fixed in the worker's
assembly; the }k\to0\text{ identity above is the anchor}),$$
with the smaller bookkeeping flag that
$\bar{\mathcal N}_{\rm tot}$ be written explicitly rather than folded
into "species weights," so the numerical check can be run without
ambiguity. The $QF_{QQ}/2$ piece is $O(1)$ relative to $F_Q/6$
($F_{QQ}=-0.696$ today) — omitting it is an order-one error in the new
term, not a refinement. And it is worth savoring the coherence:
**this is $F_{QQ}$'s third load-bearing appearance** — WP5's condensate
mass, the SZ stability sign, and now the perturbed-constraint feedback
all draw on the same quadrature curvature. One determined function,
no dials, showing up wherever the theory is asked a new question — that
is what a zero-adjustable-element $Q$-sector should look like.

## 4. Directives for the assembly step

1. Rebuild the assembled equation with all three channels; verify the
   $k\to0$ identity numerically along the trajectory (the anchor is
   exact — treat any residual as an error, not a tolerance).
2. Write $\delta\mathcal N_{\rm tot}=\sum_i\bar{\mathcal N}_iW[\delta_i-3\Phi]$
   explicitly; keep the $p_i^{\rm sp}$ weights visible.
3. Carry the gauge flag from §2 verbatim into the write-up.
4. Then the crossover-era field-variable system (the prior round's
   directive) with this completed term included — the low-$\ell$
   signature derivation follows from that system, not before it.

## 5. Housekeeping

Consolidation-batch sighting still expected; KATRIN unchanged; the
fold-in queue gains the completed-coefficient identity and the census
gauge flag. Nothing in `cdot-7/` touched.

## Companion

- `m5_separate_universe_check.py` — the fired check, the channel
  decomposition, the bookkeeping flag.
- This advisory: proposed location
  `cdot-8/WP7/Advisory-WP7-SeparateUniverseCheck-2026-07-18.md`.
