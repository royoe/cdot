# Advisory — WP6 Step 1 Cross-Checked: the Dictionary $c_1=K_B,\ c_3=-K_B$ Is Confirmed End-to-End by a Physical Cross-Check the Signature Bookkeeping Cannot Fool — With One Correction the Boxed Result Doesn't Need but Step 3 Does: the $c_4$-Structure Flips (for `cdot-8/WP6/`)

*2026-07-18. Advisory in response to
`Update-WP6-PPNDerivation-2026-07-18.md` Step 1. Cross-check in
`dictionary_crosscheck.py`. All results inherit Gate 1(b)'s caveat.
Verdict up front: **the boxed dictionary — $c_1=K_B$, $c_2=0$,
$c_3=-K_B$, $c_4=0$, shared $1/16\pi G$ prefactor — is confirmed, and
upgraded from "high confidence" to verified, by two routes: a
link-by-link audit of the signature reasoning, and a
convention-independent physical cross-check the worker didn't run —
feeding the dictionary into Foster-Jacobson's own mode-speed formulas
reproduces SZ's independently-derived results exactly (spin-1 speed$^2=1$;
spin-0 numerator $=0$). Mode speeds cannot depend on signature
bookkeeping, so this validates the dictionary end-to-end. One correction
to the reasoning, harmless to the boxed result but mandatory for Step 3:
the $c_4$-structure carries one explicit metric and flips sign under the
signature change — the dictionary must record
$c_4^{\rm FJ}\leftrightarrow-c_4^{(-+++)}$ before FJ's $c_4$-dependent
formulas are used. And with $c_{14}=K_B$ now exact, the endgame is
explicit: the æ-limit is $\alpha_1=-4K_B$, and a pulsar-class bound would
squeeze $K_B\lesssim3\times10^{-6}$ if the leading form survives — a
corner in which, notably, every WP5 conclusion stands unchanged and the
$m_\times$ two-limit question dissolves by parameter squeeze.***

---

## 1. Route A — the signature audit, with the one correction

The worker's chain verifies at every link but one blanket statement:
Christoffels invariant (two internal flips cancel) ✓; Riemann/Ricci
tensors invariant ✓; Ricci scalar flips (one explicit inverse metric) ✓;
the unit constraint transforms $u^2=+1\to A^2=-1$ with components fixed
✓ — matching SZ's $-\lambda(A^\mu A_\mu+1)$ term exactly; the overall
translation lands on SZ's action with the same prefactor ✓; and the
Maxwell decomposition $F^2=2[(c_1\text{-str})-(c_3\text{-str})]$ gives
the boxed values *exactly* ✓. The correction: "the vector kinetic terms
each have an even number of explicit metric contractions" is false for
the $c_4$-structure — $c_4u^au^bg_{mn}\nabla_au^m\nabla_bu^n$ carries
exactly one explicit $g_{mn}$ (with $u^m$ components held fixed) and
**flips sign**. Harmless today ($c_4=0$), but Step 3 uses FJ's field
equations and formulas in which $c_4$ and $c_{14}$ appear throughout,
and the $\phi$-completion could induce effective $u^au^b$-type terms
whose matching would then inherit a sign error. **Dictionary entry
added: $c_4^{\rm FJ}\leftrightarrow-c_4^{(-+++)}$.** This is the WP4b
lesson operating preemptively rather than forensically.

## 2. Route B — the cross-check that can't be fooled

Signature reasoning can contain correlated errors; physical quantities
cannot. Feeding the dictionary into Foster-Jacobson's own mode formulas:
spin-1 speed$^2=(2c_1-c_1^2+c_3^2)/(2c_{14}(1-c_{13}))\to\mathbf{1}$
exactly, matching SZ's independently-derived mostly-plus result (the
worker's own §5c quote); spin-0 speed$^2$ numerator
$c_{123}(2-c_{14})\to\mathbf{0}$, matching the $\phi$-replaced
non-dynamical aether scalar. **Two physical quantities, computed by both
papers in their own conventions, agree through the dictionary — the
end-to-end validation Step 1's own confidence statement asked for.** The
worker's flagged request for independent cross-check is discharged; the
result may now be used to quote numbers, subject only to §1's $c_4$
entry.

## 3. Route C — the endgame, now explicit and registered

With $c_{14}=K_B$ exact, the previously loose value structure sharpens:

- **æ-limit: $\alpha_1=-4K_B$.** A pulsar/LLR-class bound
  $|\alpha_1|\lesssim10^{-5}$ would give $K_B\lesssim2.5\times10^{-6}$
  *if* the leading form survives the $\phi$-completion — the Step-3
  derivation's whole job is the correction term
  $O(Q_0^2/c_{\mathcal Y}^{\rm screened})$, whose size the Cassini lower
  bound on screening (sub-task 1) caps from above. The chain
  Cassini → screening floor → $\alpha_1$ correction ceiling → pulsar
  bound on $K_B$ is now fully explicit.
- **The $K_B\to0$ corner is benign for everything already built**:
  $\mu_{\rm eff}\to\sqrt{-F_{QQ}}/2=0.417\,H_0/c$
  ($1/\mu\approx10.3$ Gpc — the end of WP5's quoted band; every WP5
  conclusion unchanged); $m_\times\to\infty$, so Mistele's one-field
  limit applies at all scales and **the two-limit question would
  dissolve by parameter squeeze** — wide binaries take their one-field
  value, becoming the surviving $m_\times$ observable; spin-1 energy
  $\propto2K_B$ decouples; SZ stability holds on the open interval as
  $K_B\to0^+$. Registered as consequences-if-the-squeeze-lands, not
  claims.

## 4. Step 2's plan — endorsed as written

The 6-step Foster-Jacobson order-by-order solve, with their own
order-counting convention adopted verbatim from the archived source
rather than a bespoke scheme, and the scalar terms
$2(2-K_B)J^\mu\nabla_\mu\phi-(2-K_B)\mathcal Y-\mathcal F$ carried from
SZ's action (quoted correctly, matching the fetched original) — this is
the right shape, staged correctly. One standing instruction for Step 3:
the $\delta\phi$/$A_\parallel$ sector should be solved in the $U$/$\chi$
variables from the fork-resolution round (rank-1 structure; the
orthogonal combination is constraint-eliminated) — solving in raw
$(\delta\phi,A_i)$ variables invites exactly the spurious inversion that
produced vanilla æ-theory's artifact singularity.

## 5. Housekeeping — one item now blocking

**The consolidation batch is now requested for the fourth consecutive
advisory.** It carries author-facing charter material (the
$\mathcal Y$-sector scope statement), a Gate-1-revisit question
(single-$\mu$ economy), the accumulated errata of three days, and now
this round's $c_4$ dictionary entry. It ships before Step 3 begins —
treat this as sequencing, not preference: Step 3 is long, and a
multi-week derivation stacked on an unshipped errata pile is how records
rot. Brouwer version line, WP4b file sighting, log repairs: fold them
into the same delivery.

## Companion

- `dictionary_crosscheck.py` — the three routes.
- This advisory: proposed location
  `cdot-8/WP6/Advisory-WP6-DictionaryCrossCheck-2026-07-18.md`.
