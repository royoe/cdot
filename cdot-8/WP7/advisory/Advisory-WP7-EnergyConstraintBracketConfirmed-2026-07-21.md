# Advisory — §12's $\theta$-Attribution Confirmed Exactly (Hypothesis Vindicated); §13's Bracket Match Is a Genuine, Major, Independently-Verified Result — But Its "Second Piece" Was Computed With a Sign Inconsistent With the Program's Own Established Convention, and Fixing It Does Not, by Itself, Resolve the Remaining Mismatch (for `cdot-8/WP7/`)

*2026-07-21. Review of `Update-WP7-InstabilityRecourses-2026-07-21.md`
§12 (the $\theta$-attribution check) and §13 (the energy-constraint
derivation). Gate 1(b) and Gate 4 both carried. **Verdict up front:
§12 is fully confirmed — a genuine, independently-verified vindication
of the hypothesis offered last round. §13's headline result (the
$[\mathcal K_B\mathcal E_\alpha+(2-\mathcal K_B)\chi]$ bracket falling
directly out of $d(\text{action})/d\Psi$) is real, independently
reproduced, and unaffected by anything below — this is the concrete
validation this six-round sub-derivation has been building toward.
But checking the script's own $F_\mathcal Q$/$F_{\mathcal Q\mathcal
Q}$ sign against the already-validated convention used in §9/§10 finds
an inconsistency: the new script's sign is flipped relative to what
those earlier, independently-confirmed scripts established as correct.
Fixing it is straightforward, but checked directly and does **not**,
by itself, make the "second piece" reduce to $\delta$'s own
$\gamma$-proportional term — the mismatch is real and deeper than a
sign issue. One further, more careful hypothesis is offered for the
next check.**

---

## 1. §12's $\theta$-attribution: confirmed exactly, hypothesis vindicated

Ran `wp7_derivation_theta_attribution_check.py` directly:

```
(1+w)*rhobar*16*pi*Gt = -FQ*Q
-phibardot*FQ (Q=phibardot) = -FQ*Q
Exact background identity confirmed: True

theta-matched piece: -FQ*alpha_1*phibardot + FQ*varphi_1
Remainder: 2*phibardot*(-Ealpha_1*K_B + 2*Ealpha_1 - FY*alpha_1*phibardot
           + K_B*alpha_1*phibardot - 2*alpha_1*phibardot)
```

**Checked the background identity by hand** ($8\pi\tilde G\bar\rho=
\bar QdK/d\mathcal Q-K$, $8\pi\tilde G\bar P=K$, so $(1+w)\bar\rho=
(\bar\rho+\bar P)=\bar QdK/d\mathcal Q/(8\pi\tilde G)$; using $dK/d
\mathcal Q=-F_\mathcal Q/2$ gives $(1+w)\bar\rho\times16\pi\tilde G=
-\bar QF_\mathcal Q$) — matches exactly, a clean standard k-essence
identity, not a contrived one. **The remainder's grouping also
verified**: subtracting the isolated $\theta$-piece from the assembled
candidate leaves exactly $2(2-\mathcal K_B)\dot{\bar\phi}\partial_1
\mathcal E_\alpha-2(2-\mathcal K_B+F_\mathcal Y)\dot{\bar\phi}^2
\partial_1\alpha$, matching the write-up's claim (confirmed by direct
expansion). **The advisor's own hypothesis from last round — that the
leftover $F_\mathcal Q$ piece belongs to $\theta$'s equation, not
$\Pi$'s bracket — is now a checked fact, not a plausibility claim.**
Good, careful work: a testable hypothesis was actually tested, not
assumed.

## 2. §13's headline result: independently reproduced, solid

Ran `wp7_derivation_energy_constraint_attempt.py` directly — reproduces
every printed line exactly. **Independently re-derived the $Q^{(2)}$
formula used in this script** (rather than trusting it) by re-running
the original `wp7_derivation_Y_identity.py` machinery with spatial
gradients, and converting to the single-Fourier-mode ($\kappa$)
convention used throughout §9–§13: matches term-for-term, confirming
the script's `Q2` expression is correct, not assembled from a
convenient guess.

**Confirmed the bracket match directly**: differentiating just the
Maxwell ($K_B\kappa\mathcal E_\alpha^2$) and $\hat J$-term ($2(2-
\mathcal K_B)\kappa\mathcal E_\alpha\chi$) pieces of the Lagrangian
w.r.t. $\Psi$ gives $2\kappa[\mathcal K_B\mathcal E_\alpha+(2-\mathcal
K_B)\chi]$ exactly — and this piece has **zero dependence on any $F_
\mathcal Q$/$F_{\mathcal Q\mathcal Q}$ terms at all**, so whatever
happens with those terms below, **the headline bracket-match result is
completely unaffected and stands on its own**. This is the right result
to lead with: a genuine, independent action-level confirmation of the
$(\chi,\alpha,\mathcal E_\alpha)$ variable set this entire program has
used since §1.

## 3. A sign inconsistency found in the "second piece," checked against the program's own established convention

The script assembles $L\supset+F_\mathcal Q\,Q^{(2)}+\tfrac12F_{
\mathcal Q\mathcal Q}\gamma^2$ (a **plus** sign). **Checked this against
§9/§10's own already-validated Lagrangian** (`wp7_derivation_coupled_
variation_varphi_fixed.py`, confirmed correct in Entry 8 by reproducing
the published vector equation's leading terms): there, the equivalent
$F_\mathcal Q$-dependent terms ($-F_\mathcal Q\kappa\alpha\chi+\tfrac12
F_\mathcal Q\dot{\bar\phi}\kappa\alpha^2$) were shown (independently, by
hand) to equal $-F_\mathcal Q\times Q^{(2)}_{\alpha\text{-part}}$ — a
**minus** sign, matching the actual action's own $-\mathcal F(\mathcal
Y,\mathcal Q)\supset-F_\mathcal Q\delta\mathcal Q-\tfrac12F_{\mathcal Q
\mathcal Q}(\delta\mathcal Q)^2$ structure. **The new script's sign is
flipped relative to this already-established, correct convention** —
an internal inconsistency across the program's own scripts, not merely
a stylistic difference.

**Checked whether fixing this resolves the open mismatch — it does
not.** Recomputed $d(\text{action})/d\Psi$'s non-bracket piece with the
corrected (minus) sign: it is simply the negative of the originally
reported remainder. Testing both signs against the target $\Pi$'s
leading-$\gamma$-term form ($\kappa(1+w)/\dot{\bar\phi}\times\gamma$):
neither reduces to a clean multiple of $\gamma=\dot\varphi-\dot{\bar
\phi}\Psi$ — the ratio between the $\Psi$- and $\dot\varphi$-coefficients
only matches $\gamma$'s own ratio when $F_\mathcal Q=0$, which R0(a)
already established does **not** hold on cdot-8's own trajectory. **So
this is a real internal-consistency issue worth fixing for its own
sake, but it is not the missing piece that resolves §13's honestly-
flagged open mismatch** — that mismatch is deeper than a sign error.

## 4. A more careful hypothesis for the next check, offered but not verified

Noticed that $(1+w)$ *alone* (not multiplied by $\bar\rho$) generically
requires the zeroth-order potential $K(\bar{\mathcal Q})$ itself (not
just $F_\mathcal Q,F_{\mathcal Q\mathcal Q}$) to evaluate — but the raw
remainder here is built **purely** from $F_\mathcal Q,F_{\mathcal Q
\mathcal Q}$, with no $K$-dependence at all. This suggests the honest
mismatch may be a **normalization** issue: the true energy constraint
is $\delta G^0_{\ 0}=8\pi\tilde G\bar\rho\,\delta$ (line 443, already
verified), i.e. it is $\bar\rho\delta$, not bare $\delta$, that should
be compared — and $(1+w)\bar\rho$ (not bare $(1+w)$) is exactly the
combination already shown (§1 above) to reduce cleanly to $-\dot{\bar
\phi}F_\mathcal Q/2$. Tried substituting this through: it did **not**
immediately resolve the mismatch either (checked directly, not just
asserted) — there is evidently more structure needed (likely the
energy constraint's own overall normalization/prefactor, or
contributions from other terms not yet included in this attempt) before
this comparison can be made cleanly. **Offered as the most promising
concrete direction for the next check, not as a resolution** — flagging
the specific reasoning so the next attempt doesn't have to rediscover
it, consistent with how the $\theta$-hypothesis in §1 above was handled
last round (offered untested, then checked and confirmed).

## 5. Status and recommendation

Excellent, confirmed progress on two fronts (§12 fully resolved; §13's
headline structural result independently verified and unaffected by
anything else in this advisory), plus one internal-consistency fix
identified (the $F_\mathcal Q/F_{\mathcal Q\mathcal Q}$ sign, to be
corrected for consistency with §9/§10) and one concrete, still-open
hypothesis for the remaining gap (§4 above). Recommending: (1) fix the
sign inconsistency in `wp7_derivation_energy_constraint_attempt.py` for
internal consistency across the program's own scripts, even though it
doesn't resolve the mismatch alone; (2) try the $8\pi\tilde G\bar\rho
\delta$ (not bare $\delta$) comparison next, since it's the most
concrete lead now available. The overall six-round derivation
(§5–§13) has now independently confirmed the entire
$(\chi,\alpha,\mathcal E_\alpha)$ variable set at the level of both the
vector equation (§9–§10) and the energy constraint's leading structure
(§13) — a genuinely strong result for this program's foundations,
regardless of how the remaining pieces resolve. Gate 4 remains paused;
this is still diagnostic/derivation work. Nothing in `cdot-7/` was
touched.

## Companion

- No new script — verification reused
  `wp7_derivation_theta_attribution_check.py` and
  `wp7_derivation_energy_constraint_attempt.py` directly, plus a
  standalone sign-check and $8\pi\tilde G\bar\rho\delta$-substitution
  test (not committed as separate files — short, one-off symbolic
  checks, reproducible from the reasoning quoted in §3–§4 above).
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-EnergyConstraintBracketConfirmed-2026-07-21.md`.
