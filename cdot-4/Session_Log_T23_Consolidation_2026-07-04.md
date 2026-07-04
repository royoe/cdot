# Session Log — T23 Consolidation ("The Failed Tests")

**Date:** 2026-07-04
**Scope:** Consolidate the honest, final record of cdot-4's cosmological-sector testing
before starting cdot-5, per the author's explicit instruction: write a new topic
document including all `new_tests/` content not already merged into T22, plus the
`desi_bao/` and `cmb_peak/` results, ending in the conclusion that parts of Core
Principles cannot stand.
**Outputs:** T23_The_Failed_Tests.md; edits to Core_Principles.md; this log
**Session classification:** Terminal/consolidating — closes out cdot-4's active testing
phase.

---

## Context

This session followed directly from a multi-stage investigation earlier the same day
(and the day prior): the CMB first-peak angular-scale calculation and its Etherington
correction (`cmb_peak/`), the DESI DR2 BAO confrontation and Alcock–Paczyński shape test
(`desi_bao/`, largely produced by a parallel/prior session using the same repository),
and this session's own test of whether a Machian mass-counting premise could rescue the
cosmological sector. The author, having reviewed the BAO material and this session's own
negative/partial results, judged the project had reached a natural endpoint for cdot-4
and asked for a single, honest, consolidated record before starting a new iteration.

## Session Activity

- Surveyed the actual current state of `new_tests/`, `desi_bao/`, and `cmb_peak/` on
  disk (14, 8, and 4 files respectively) to establish ground truth before consolidating.
- Read T22_Gravitational_Lensing_and_Local_Gravity.md's section structure and dispatched
  two parallel research agents to cross-reference all seven `new_tests/` update
  documents against T22, T12, and T14 — specifically hunting for content that was
  dropped, softened, superseded, or walked back during the original 2026-07-02 merges,
  since that content would otherwise be permanently lost.
- Findings from the cross-reference (see agent reports, not separately filed):
  - PPN/PV, GEM, and River-Derivation material is substantially merged into T22, but
    the *withdrawn* branches (Two-Regime Dictionary and its two decisively-excluded
    sub-branches), the abandoned GEM+PV hybrid architecture, the superfluid/Madelung
    derivation apparatus (including the "harmonic miracle," a real technical result not
    carried forward), and the circulation-quantization-vs-frame-dragging tension (which
    T22 sidesteps via a classical reframing rather than resolving) all needed rescuing.
  - Connecton Ontology is almost fully merged into T12, with one clean finding: a
    headline claim ("the exact identity that clinches it," re: holographic bit-thread
    density) was itself walked back the same day as a tautology — a documented instance
    of the project's own rhetoric outrunning its result.
  - Restored-Checks is the most thoroughly merged of all seven documents (T14 marks the
    relevant items RESOLVED); only minor gaps found (a missing T22 cross-annotation, the
    "reconstructing lost work" meta-narrative itself not preserved).
  - The Observational Test Battery is almost entirely unmerged — confirmed by direct
    grep across all T-documents for its key terms (redshift drift, Alcock-Paczynski,
    Bullet Cluster, quasar dipole, FRB, etc.), all returning zero hits except one T15
    sign-fix. The T22 slot this document proposed creating was later taken by an
    unrelated topic; the rest of a 15-item prioritized test program was simply never
    revisited. This is the single largest block of unmerged material.
- Independently already had full context on `desi_bao/` (four documents read earlier
  this session and the session prior: the DESI DR2 fit, the assumptions audit, the
  frozen-large/CMB cross-check addendum, and the Alcock-Paczyński shape test) and on
  `cmb_peak/` (both documents authored earlier this session).
- Synthesized all of the above, plus this session's own Machian-mass-count test results
  (the family-level reconfirmation via reverse-engineering, the two-component curve
  fit's promise, and the PBH-sink mechanism's partial success and remaining tension with
  $\Omega_\text{PBH}$), into a single new document, T23 — The Failed Tests, organized in
  four parts: (I) the cosmological distance-sector failure, decisive and premise-level;
  (II) the local-gravity program's superseded machinery and live-but-sidestepped
  tensions, explicitly separable from Part I; (III) the deferred 15-item test battery,
  never before consolidated in one place; (IV) the conclusion — what cannot stand
  (premises 1+2+4 combined, as the cosmological mechanism) and what survives (T14/T22's
  connecton program).
- Edited Core Principles: added a closing note immediately after the document's opening
  description, and updated the status-table rows for premises 1/2/4, the horizon law,
  the distance formula, and the CMB entry to point to T23 and state the exclusion
  plainly, rather than leaving the prior "Core, stable" / "closest to a working number"
  language standing uncontested.

## Results Summary

1. **A single, complete, honest record now exists** of every result — positive,
   negative, superseded, and walked-back — produced across the `new_tests/`,
   `desi_bao/`, and `cmb_peak/` working directories, consolidated in one place for the
   first time.
2. **The conclusion is explicit and premise-level**: Core Principles premises 1
   (static geometry), 2 (horizon counting), and 4 (photon frequency conserved in
   flight), taken together, are excluded as the cosmological redshift-distance
   mechanism — not by a bad parameter choice, but structurally, because they force a
   single function $c(t)$ to fix both the observable redshift and the observable
   distance ruler at once, and DESI's Alcock-Paczyński data show no one-function model
   can match its shape.
3. **What survives is explicitly scoped**: the connecton local-gravity program (T14,
   T22) is logically separable and unaffected — this is stated as a finding, not an
   assumption, tracing back to the original DESI update's own separability argument.
4. **cdot-5's starting task is named**: replace premise 2 with a structurally
   different, most likely multi-channel mechanism for $c(t)$'s cosmological history,
   using the connecton-sink direction (PBH mass fixed at genesis, shrinking as a
   fraction of an ever-growing raw sea) as the most promising lead currently in hand —
   itself explicitly flagged as unfinished, not a proposed replacement premise.

## Merge Recommendation

This document is the terminal record for cdot-4's active testing phase, by the author's
own framing — no further merge into other T-documents is intended; T23 stands on its
own as the closing chapter. cdot-5 should begin by reading T23 in full before touching
any other topic document, since it both scopes what must be rebuilt (Part I/IV) and
what can be carried forward unchanged (Part II's surviving results, net of its own
listed debts) and what observational program to hold the replacement accountable to
(Part III).
