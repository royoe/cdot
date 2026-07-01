# SESSION LOG — T17 Prose Correction: What Sources $B_c$

**Topics:** T17 (Galaxy Morphology & M-σ), T14 (Connecton Gravity)
**Date:** 2026-06-30
**Session type:** Prose correction following the T14/T17 consistency check.

---

## Timeline

**[2026-06-30 ~13:30 UTC] — Prior turn.**
Consistency check of merged T14/T17 surfaced: Issue 1 (dimensional error in T17 line 152,
$M_\text{BH}^{1/4}\sim(GM_\text{bary}a_0)^{1/4}/r$ — kg^{1/4} vs frequency); Issue 2
(T17 still says the BH "sources" $B_c$, contradicting the derived-M-σ picture);
Issue 3 ($B_c$-grows-with-$c$ hedged in T14 but asserted in T17); Issue 4 (evaporation
ceiling vs derived M-σ); plus minor $v_f\approx\sigma$ bridge note.

**[2026-06-30 14:04 UTC] — User prompt (verbatim):**
> Good catches. I think we need to be more clear about what sources B_c. Can we improve the prose?

**[2026-06-30 14:04 UTC] — Analysis.**

Traced the source of $B_c$ from established results. Two candidates:
- Central BH (old "Role 1") — RULED OUT: if $B_c \propto M_\text{BH}$, then $a_0$ varies
  per-galaxy with BH mass, destroying the universality the RAR's 0.13 dex tightness
  evidences.
- Baryonic mass via transition-radius construction — CORRECT:
  $B_c = (GM_\text{bary}g_\dagger)^{1/4}/r$, $g_\dagger=\dot c=cH_0$. Quarter power on
  baryonic mass, not BH mass. $M_\text{BH}$ enters only as a co-tracer of $GM_\text{bary}a_0$
  (the derived M-σ relation).

Clean statement adopted: **$B_c$ is baryon-sourced; the BH is a correlate of $B_c$, not its
cause.** This preserves all four morphology links (they require $B_c$ to correlate with
$M_\text{BH}$, which it does observationally) while removing the false causal arrow.

**[2026-06-30 14:04 UTC] — Result: five surgical prose replacements + one new subsection.**

- Fix A (lines 64–68): replace the dimensionally-broken $B_c\sim M_\text{BH}^{1/4}/r$ with
  the correct baryonic $B_c=(GM_\text{bary}g_\dagger)^{1/4}/r$; note BH as co-tracer.
- Fix B: insert new subsection "What Sources $B_c$" stating baryonic source, $a_0$
  universality argument, and the read-as convention for "high-$M_\text{BH}$ galaxy."
- Fix C (lines 83–84): replace asserted low-$z$-more-stripping with a hedged version tied
  to the joint $c,H$ evolution (Issue 3).
- Fix D (lines 98–101): rewrite "massive BH sources stronger $B_c$" as "galaxy high on the
  shared normalization has both stronger $B_c$ and a more massive BH."
- Fix E (line 127): same co-tracer rephrasing inside Link 3.

Plus consistency notes: T17 line 152 (PBH section) carries the same dimensional error as
old line 66 — flagged for the same fix, not rewritten (sits in PBH framing). Issue 4
(evaporation-ceiling break = departure from the derived relation) flagged for a separate
focused pass. T14 needs no fix; optional one-sentence symmetry addition suggested.

**[2026-06-30 14:04 UTC] — Verdict.**
The contradiction was substantive, not cosmetic: T17 carried two incompatible causal
stories. The fix (baryon-sourced $B_c$, BH as correlate) is forced by the $a_0$-universality
constraint, resolves Issues 1 and 2 together, and strengthens rather than weakens the
morphology chain.

**[2026-06-30 14:04 UTC] — Deliverables.**
- `UPDATE_T17_Bc_Source_Prose.md`
- `SESSION_LOG_T17_Bc_Source_Prose.md` (this log)

**Not done this session (flagged for follow-up):** PBH-section dimensional fix (T17 §152);
Issue-4 evaporation-ceiling clarifying sentence; Issue-3 sign check against actual
$c(t),H(t)$ scalings; $v_f\approx\sigma$ one-line justification across the disk/bulge
dichotomy.
