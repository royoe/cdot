# SESSION LOG — Profile Amplitude: Two Dimensional Errors, Coefficient O(1)-Open

**Topics:** T14 (Connecton Gravity)
**Date:** 2026-07-01
**Session type:** Derivation (the "next computation": derive the profile amplitude / horizon-
mode density contrast). Outcome: corrective — exposed two dimensional errors in prior work.

---

## Timeline

**[2026-07-01 10:28 UTC] — Prior session.**
Found the 9/8 is an artefact of an unfixed profile normalization; flagged "derive the profile
amplitude B from connecton dynamics" as the real next computation.

**[2026-07-01 10:35 UTC] — User prompt (verbatim):**
> Proceed with the next computation.

**[2026-07-01 10:35 UTC] — Work performed.**

1. Target: derive B in delta_rho=B/(4pi r), a0=G B/2. Found the value that gives cH0/6 is
   B=(8/9) rho_bg R0 (so the 9/8 is exactly this column coefficient's inverse).
2. Tried to fix B from the q=2 spectrum: found delta_rho(r) ∝ xi(r) (prior "profile") is the
   AUTOCORRELATION — units (kg/m^3)^2, not kg/m^3. Dimensional error #1: the 1/r "profile"
   was a correlation function, not a density profile.
3. Went to the linear response / RMS acceleration from Poisson: g_dagger^2 = (4piG)^2/(2pi^2)
   INT P_rho dk. Dimensionally this is ~ G^2 rho^2 => g_dagger ~ G rho ~ 1/time^2 — a
   FREQUENCY^2, NOT an acceleration. Dimensional error #2: the q=2 "floor integral" pillar
   never gave an acceleration; it needs an explicit length (R0). Direct evals were ~27-30
   orders off, confirming.
4. Resolved the apparent UV-independence: it held only when A was treated as fixed; fixing A
   physically (variance or horizon-contrast) makes the floor either UV-dependent or
   dimensionally a frequency. Either way it does not fix a0's coefficient.
5. Only dimensionally valid sea acceleration: g_dagger ~ G rho_bg R0 = (3/8) cH0 (clean).
   a0 = (3/8) cH0 / PROFILE, PROFILE an undetermined O(1) (2, 9/4, or pi-valued).

**[2026-07-01 10:35 UTC] — Result.**

SURVIVES (dimensionally checked): rho_bg=(pi/6)rho_crit (holographic, hbar-free); the 6 in
cH0/6 (horizon geometry); G rho_bg R0=(3/8)cH0; the RAR closure (indistinguishability, McGaugh
0.020 dex) — independent of the coefficient.
DOES NOT SURVIVE: the q=2 floor integral as a coefficient-fixing pillar (frequency^2, not
accel — DEMOTE); a0=(3/16)cH0 "no free amplitude"; the 1/r object as a literal density profile
(it was xi(r)).

Honest status: a0 ~ cH0/6 as a SCALE (solid: horizon geometry + holographic density give
G rho_bg R0=(3/8)cH0); overall coefficient O(1)-OPEN (PROFILE undetermined). Weaker than the
last two sessions claimed. The MOND regime and functional form are UNAFFECTED (rest on the
closure).

**[2026-07-01 10:35 UTC] — Critical assessment.**

This is the critical pass working as intended twice over: the user's "9/8 real or artefact?"
already downgraded the precision; proceeding to actually derive the amplitude uncovered that
TWO intermediate results (the 1/r profile and the floor integral) were dimensionally invalid
and had been propagating unnoticed. The convenient chain "q=2 -> horizon-set coefficient" does
not survive. What remains is genuinely solid (holographic density, horizon 6, the closure) and
is enough to state a0 ~ cH0/6 as a scale with an honest O(1)-open coefficient.

No result was lost that was real; overstated precision was removed. This is preferable to
carrying a dimensionally-invalid pillar that happened to land near the right number.

**[2026-07-01 10:35 UTC] — Deliverables.**
- `UPDATE_T14_Profile_Amplitude_Correction.md`
- `SESSION_LOG_Profile_Amplitude.md` (this log)

Supersedes/revises: UPDATE_T14_Holographic_Sea_Density.md (a0 precision), 
UPDATE_T14_9over8_Artefact.md (deeper cause than the profile coeff),
UPDATE_Consistency_Core_T6_T15.md (coefficient wording -> "cH0/6 scale, O(1) open").

**Next computation:** derive PROFILE from the connecton force law — the actual acceleration a
test mass feels from perturbing the holographic sea (same momentum-transfer/gradient physics
as g_N from foam diffusion, applied to the background). Closes or bounds the coefficient; if
not derivable, a0's coefficient is the theory's one normalization input, with cH0/6 the firm
scale.
