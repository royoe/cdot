# SESSION LOG — Static-Map c(z) Inversion Against DESI

**Topic:** Testing whether any candidate $c(z)$ history on a static map (ruler
preserved) can fit the DESI BAO data, after the horizon-count law and the
BH-sink symmetry breaker both failed.
**Date:** 2026-07-04 (UTC) — continuation.
**Outcome:** Constructive — includes a correction of an earlier claim, clears
the static map, and extracts the required running counting index. One update
document produced.

---

## Timeline

**2026-07-04T~09:0x UTC — User prompt**
> I'm not really willing to break the ruler, as that would kill the whole concept
> of the static map, where c varies in time. But I'm willing to test any
> candidate function for c(z) that can work on a static map.

**Response.** Reframed: within a static map, is there any $c(z)$ (equivalently
$D_p(z)$) fitting BAO AP + SN jointly? Set up the model-independent test.

**Findings (in order):**
1. Proposed a static-map consistency test $D_H=dD_M/dz$; **then corrected it** —
   this identity is universal (LCDM satisfies it too, verified on the same grid:
   ratios 0.94–1.22, same finite-difference wobble as DESI). It is NOT a
   discriminator. Recorded the correction rather than burying it.
2. Showed the AP ratio alone cannot falsify the static map: it only sets
   $d\ln D_p/dz=1/F_\text{AP}$, always integrable.
3. Showed the static map fits BAO+SN jointly if $D_p(z)=$ observed $D_M(z)$;
   the SN $D_L=(1+z)D_p$ matches LCDM shape to ~1% (Etherington). So the static
   map is NOT falsified — only the horizon-count *derivation* of $D_p$ was.
4. Inverted DESI for the required counting index, holding the squared-redshift
   law fixed ($c/c_\text{now}=(1+z)^{-1/2}$). Result: $n(z)\sim0.4$–0.7, running
   with a shallow dip near $z\sim1.5$. Robust conclusions: $n=3$ excluded; $n$
   not constant. Absolute $n$ scales with $R_\text{now}/r_d$ (unfixed here).
5. Internal consistency (integrate DESI $D_H\to D_M$): agrees 2–7% on a 6-point
   quadratic fit — static map passes.

**Conclusion.** The static map survives DESI. The refutation was narrowly of the
volume counting law $c\propto R^3$. The data demand a counting map with a much
lower, mildly running index $n\sim0.4$–0.7. New central question: what physical
counting law yields $n_\text{eff}\lesssim1$ with a dip near $z\sim1.5$? (Even
area-counting $n=2$ over-counts; points to a sub-area law — a real clue.)

---

## Artifacts produced
- `UPDATE_Static_Map_cz_Inversion.md` — proposed update for merge.
- `SESSION_LOG_Static_Map_cz_Inversion.md` — this log.

## Corrections to prior session output
- The "$D_H=dD_p/dz$ lock" from UPDATE_BAO should be understood as a rigidity of
  the **power-law** counting map, not of the static map. The static map itself
  is not falsified. UPDATE_Static_Map_cz_Inversion supersedes the interpretive
  framing (not the arithmetic) of the earlier BAO update on this point.

## Open next steps
1. Pin $R_\text{now}/r_d$ via a model value of $r_d$ (needs genesis/
   recombination physics, T16) to fix absolute $n(z)$.
2. Search for a physical counting law giving running $n\sim0.4$–0.7 with a dip
   near $z\sim1.5$; test candidates against the inverted profile.
3. Re-run with full DESI covariance and DR3 bins to confirm the $z\sim1.5$ dip.
