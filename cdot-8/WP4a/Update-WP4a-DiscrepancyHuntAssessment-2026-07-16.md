# Update — WP4a: Discrepancy Hunt Verified; My Own Earlier Attribution Was Wrong; One Circularity Caveat on the "Vindication" Framing

*Companion: `SessionLog-2026-07-16.md` (this directory). Responds to
`Advisory-WP4a-DiscrepancyHunt-2026-07-16.md` and
`theta_star_diagnosis.py`.*

---

## 1. Reproduced the swap experiment; my own §4 attribution was wrong

Ran the delivered script (one compatibility fix needed — `np.trapezoid` isn't
available in this numpy version, substituted `np.trapz`, no effect on the
numbers). All four table rows reproduce exactly: baseline $100\theta_*=1.321$
(matches the earlier $1.326$ to grid precision), $\Lambda$CDM reference
$1.031$, cdot-8 $E$ with $\Lambda$CDM $\Omega_b\to1.307$, $\Lambda$CDM $E$ with
census $\Omega_b\to1.042$.

**My original update's §4 attributed ~20% of the $r_s$ excess to
$\Omega_b=0.0442$ vs. $\Lambda$CDM's $\approx0.049$, by hand-wave (comparing
the two $\Omega_b$ values directly) rather than by a controlled swap.** The
swap experiment shows this was wrong: holding cdot-8's own $E(z)$ fixed and
only changing $\Omega_b$ to the $\Lambda$CDM value moves $r_s$ by $1.1\%$, not
$20\%$. The advisory is right and I'm updating the ledger: the $\Omega_b$
attribution in my original WP4a update was an uncontrolled, hand-wave
estimate, corrected here by an actual controlled experiment.

## 2. One caveat on how much the "vindication" framing should carry

The genuinely decisive half of the swap experiment is the first one: cdot-8's
*own*, non-standard $E(z)$, with $\Omega_b$ swapped to the standard value,
barely moves ($1.321\to1.307$) — this is real, independent evidence that
$\Omega_b$ isn't the driver *within this framework's actual expansion
history*, and I accept it.

**The second swap ($\Lambda$CDM's $E(z)$ with the census $\Omega_b$ landing at
$1.042$, matching Planck) carries less independent weight than the "vindicated"
framing suggests.** $\Lambda$CDM's own $E(z)$ was itself calibrated using data
that includes the CMB acoustic scale as a primary constraint — so finding that
*any* reasonably-close-to-standard $\Omega_b$, run through $\Lambda$CDM's own
$E(z)$, reproduces close to $1.041$ is close to circular; it's confirming that
$\Lambda$CDM reproduces what it was built to reproduce, not delivering new
information about cdot-8. **What *is* a genuine, worth-keeping result from
this row**: the census $\Omega_b=0.0442$ (physical $\omega_b=0.0217$) sits only
$3\%$ below Planck's independently-measured $0.0224$ — a real, zero-tuning
agreement between this framework's mass-census closure and BBN-independent
data, on its own terms, regardless of what it's plugged into. That part of the
finding stands without the circularity concern; the "matches Planck to the
digit when run through $\Lambda$CDM" framing is the weaker half of the same
result, not additional independent confirmation that the miss is "100% $E(z)$,
0% $\Omega_b$."

Net effect on the localization claim: unchanged. The controlled, non-circular
swap (cdot-8's $E$, standard $\Omega_b$) already establishes that on its own.

## 3. Everything else checked, no disagreement

The $\nu$-mass sensitivity table reproduces exactly; the direction (lighter
$\nu\to$ smaller miss, $\sim5\%$ of the needed $27\%$) and the KATRIN-alignment
observation are both real and correctly flagged as insufficient alone. The
census-$\nu$-convention "closed, not a free parameter" finding and the
Stage-2/BBN-lithium bounding arguments are consistent with everything
established earlier this session; no independent objection.

## 4. Status

The localization stands, on firmer ground for the reason in §1 (my own
correction) and with one recorded caveat (§2) about which half of the
evidence is doing the real work. The pass/provisional-failure/kill decision
remains exactly where both prior rounds left it: the author's, under
Foundation §6 item 6, now informed by the sharper localization (the miss
lives in $E(z)$ over $z_*$-to-few$\times10^4$, not in the census $\Omega_b$,
which is independently vindicated). Not narrowing that decision further here.
WP4b, the sign-errata propagation, and the consolidation-log entries remain
queued as previously listed. The KATRIN clock remains the program's most
time-critical item, now formally linked to this tension per the advisory's
§3.2; nothing in `cdot-7/` was touched.
