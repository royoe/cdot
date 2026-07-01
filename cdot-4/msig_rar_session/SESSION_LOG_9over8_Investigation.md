# SESSION LOG — Is the 9/8 Factor Real or an Artefact?

**Topics:** T14 (Connecton Gravity)
**Date:** 2026-07-01
**Session type:** Critical investigation of the 9/8 coefficient residual.

---

## Timeline

**[2026-07-01 10:14 UTC] — Prior session.**
Consistency pass; recommended Core/T6/T15 wording updates including "a0=(3/16)cH0, residual
9/8". This session tests whether that 9/8 is physical.

**[2026-07-01 10:28 UTC] — User prompt (verbatim):**
> While that update is running, let's make one more attempt at investigating the issue of the
> 9/8 factor. Is it real or is it an artefact?

**[2026-07-01 10:28 UTC] — Work performed.**

1. Localized the 9/8: rebuilt a0 = G rho_bg R0/PROFILE symbolically. rho_bg=(pi/6)rho_crit
   =H0^2/16G (pi cancels), R0=6c/H0 => G rho_bg R0 = (3/8)cH0. With PROFILE=2 -> (3/16)cH0.
   For agreement with g_dagger=c^2/R0=cH0/6, PROFILE must = 9/4. The 9/8 = (9/4)/2 lives
   ENTIRELY in the profile coefficient. One number, not three stacked factors.

2. Tested whether PROFILE is uniquely forced. Three defensible normalizations:
   - 1/r charge integral with B=rho_bg R0: PROFILE=2 -> (3/16)cH0.
   - self-consistency with c^2/R0: PROFILE=9/4 -> cH0/6 exact.
   - delta_rho(R0)=rho_bg => B=4pi rho_bg R0: -> (3pi/4)cH0, ×14 too big.
   Span >1 order of magnitude. NOT uniquely determined.

3. Dimensional audit exposed a deeper conflation of three objects:
   - floor integral g^2 ~ (4piG)^2 INT P dk ~ G^2 rho^2 => G rho ~ 1/time^2, NOT accel
     (direct eval was ~27 orders off — floor route dimensionally incomplete without a length);
   - profile route g=G rho_bg R0/PROFILE IS an acceleration but coeff = profile amplitude B,
     an undetermined O(1);
   - holographic rho_bg=(pi/6)rho_crit — clean, hbar-free, stands.
   The "no free amplitude" claim mixed the floor route (not an accel alone) with the profile
   route (hand-set coeff), creating illusory precision.

**[2026-07-01 10:28 UTC] — Result / Verdict.**

The 9/8 is an ARTEFACT — the gap between profile-coeff 2 (used) and 9/4 (self-consistent),
neither uniquely forced; a third choice differs 14×. Not a physical residual.

What stands: the 6 in cH0/6 (horizon geometry, solid); rho_bg=(pi/6)rho_crit (hbar-free,
solid). What is downgraded: the map from rho_bg to a0 carries an undetermined O(1) (profile
amplitude / horizon-mode density contrast). Prior "a0=(3/16)cH0, no free amplitude, 12% high"
was too strong — the "no free amplitude" hid an unfixed O(1).

Honest status: scale a0 ~ cH0/6 derived; overall coefficient O(1)-open. The 9/8 should not
appear as a result.

**[2026-07-01 10:28 UTC] — Critical assessment.**

This is a correction to the prior session. Taking "real or artefact?" seriously showed the
convenient 12% result did not survive scrutiny. Intended function of the critical pass:
false precision replaced by an honest scale + acknowledged O(1). No physics lost — the
holographic identity and horizon geometry both stand; only the overstated closure is removed.

**[2026-07-01 10:28 UTC] — Deliverables.**
- `UPDATE_T14_9over8_Artefact.md`
- `SESSION_LOG_9over8_Investigation.md` (this log)

Supersedes: the precision claim in UPDATE_T14_Holographic_Sea_Density.md, and the coefficient
wording proposed in UPDATE_Consistency_Core_T6_T15.md §2–§4 (use "a0~cH0/6, O(1) normalization
open" instead of "(3/16)cH0, 12% high").

**Next computation:** derive the profile amplitude B (horizon-mode density contrast of the
q=2 sea) from connecton dynamics — the single O(1) that converts the solid holographic
density into a0.
