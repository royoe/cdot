# Session Log — Foundation (2026-07-21)

*Companion: `Advisory-NewFRBBaryonCensusAssessed-2026-07-21.md` (this
directory). Per-day session log, started fresh per this program's own
"one SessionLog per calendar day" convention — continues the entry
numbering from `SessionLog-2026-07-19.md`, not restarting it.*

---

## Entry 7 — new FRB baryon-census paper checked against cdot-8's own $\Omega_b$ input: consistent, no action needed (advisor session, 2026-07-21)

**Prompt (verbatim):** "There is some new data on \Omega_b that I
spotted. Please check if this affects our mass census.
https://www.nature.com/articles/s41550-025-02566-y"

**Summary.** Identified the paper (Nature's own login wall blocked a
direct fetch; located it via search instead): Connor, Ravi et al.
(2025), "A gas-rich cosmic web revealed by the partitioning of the
missing baryons," Nature Astronomy — a 69-FRB dispersion-measure
census giving $\Omega_bh_{70}=0.051^{+0.006}_{-0.006}$.

**Traced cdot-8's own $\Omega_b=0.044204$ back to its source** rather
than trusting the Foundation.md figure at face value: derived from
`cdot-7/Fable-1/four_term_fit.py`'s fixed $\omega_b=0.02166\pm0.00019$
(Cooke, Pettini & Steidel 2018, BBN deuterium abundance) at a **fixed**
$H_0=70$ km/s/Mpc (not fit) — reproduces $0.044204$ exactly. **This is
the same $H_0=70$ convention the new paper itself uses** ($h_{70}$ is
defined relative to 70 km/s/Mpc), so the comparison is a genuine,
same-convention apples-to-apples check, not requiring any extra
$H_0$-dependent conversion.

**Result**: the two values differ by $\Delta=0.0068$, or **$1.1\sigma$**
using the new paper's own uncertainty — mild, unremarkable, not a
tension. The FRB measurement's own relative precision ($\sim12\%$) is
roughly 13$\times$ coarser than the BBN value's ($\sim0.9\%$), so even
this small offset carries little evidential weight against the
already-adopted input. Considered and rejected any reason to prefer the
new number on non-precision grounds (the FRB method carries its own,
different model dependencies — host/MW dispersion-measure subtraction,
an assumed background cosmology — and isn't more fundamental for this
specific quantity than a primordial-abundance measurement).

**Verdict: no action needed.** cdot-8's $\Omega_b=0.044204$ (BBN)
remains the right input, unaffected by this paper — worth keeping on
file as a positive, independent consistency check, not as a reason to
revise anything in `Foundation.md`, `Progress.md`, or any WP's census
work.

**Files produced (Entry 7):**
`Advisory-NewFRBBaryonCensusAssessed-2026-07-21.md`, this log entry
(new dated file, per the one-log-per-day convention — continues Entry
numbering from `SessionLog-2026-07-19.md`'s Entry 6).

**Open items handed forward:** none new. Standing: author merge
decision on the onboarding-doc insertions (Entry 6, 2026-07-19); joint
staged WP7 round; $Q_2$/IF-re-fit sequencing decision; **KATRIN
watch**. Nothing in `cdot-7/` or `WP7/` was touched.
