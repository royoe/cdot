# Update — WP4a: Advisor Confirmation Verified; One Loose Thread in Their Own Script Closed; Routing the Verdict to the Author

*Companion: `SessionLog-2026-07-16.md` (this directory). Responds to
`Advisory-WP4a-AcousticScale-Assessment-2026-07-16.md` and `wp4a_check.py`.*

---

## 1. The advisory's own script raises a concern its written text never answers

`wp4a_check.py` reproduces the calculation exactly, then trails off (lines
100–112) into an unresolved worry: whether the $D_p$ integral needs an
explicit $c(z)$ factor inside it, since this is a varying-$c$ framework and a
null geodesic might not simply give $\int c_0/H(z)\,dz$ the way standard
cosmology's constant-$c$ geodesic does. The comment block ends mid-thought
("Need to check WHICH clock/frame $D_p$ is computed in cdot-8") and this
question does not appear anywhere in the delivered advisory prose, which
instead states the provenance audit as settled.

**Checked directly rather than assuming the cross-check already reported
disposes of it.** Foundation §5.2's analytic fixed-point formula, $D_p(z)=
R_{h,0}[1-(1+z)^{-1/2}]$, is derived independently of my numerical
integration. Verified that the constant-$c_0$ integral $\int_0^z c_0/(H_0
(1+z')^{3/2})\,dz'$ reproduces this exactly (residual $1.9\times10^{-6}$,
grid-resolution-limited) — **no $c(z)$ factor belongs inside the integral**;
the constant-$c_0$ form is exactly what Foundation's own, independently
derived distance formula requires. The advisory's reported cross-check
(matching $8306$ Mpc on the fixed point) was already the answer to this
question; it just wasn't connected back to the specific worry raised in the
companion script. Closing that thread explicitly here rather than leaving an
admitted-but-silently-dropped concern sitting in a script file.

## 2. Everything else re-checked and confirmed

The term-by-term reproduction ($D_p$, $r_s$, $100\theta_*=1.326$), the
provenance audit's six leak-point checks, and the "self-caught" $8.6$ Gpc
asymptote concern (resolved correctly — a fitted, accelerating trajectory
legitimately exceeds the fixed-point asymptotic bound, exactly as $\Lambda$CDM's
$D_M(z_*)$ exceeds pure EdS's) all hold up. No disagreement with the
advisory's numbers or its six-leak-point provenance conclusion.

## 3. The verdict is not mine or the advisor's to make

Both the advisory and this update agree: Foundation §6 item 6 reserves this
decision for the author, given cdot-4/5's history, and neither of us should
pre-empt it. The three readings the advisory laid out (soft miss pending WP7;
provisional structural failure; decisive kill) are all defensible depending on
how much weight a 27% zero-knob miss against a $0.03\%$-precision measurement
should carry, and how much benefit of the doubt "WP7 might recover this via
peak-height/ratio physics rather than peak position" deserves. Recommend
presenting this three-way choice to the author directly rather than the
advisory or worker narrowing it further.

## 4. Status

WP4a's numerical result stands, confirmed independently twice now (by the
advisor, and by this round's check of the one thread their own script left
open). Awaiting the author's routing decision. WP4b, the sign-errata
propagation, and the consolidation-log entry remain queued exactly as the
advisory listed, unaffected by which of the three readings is chosen. The
KATRIN clock remains the program's most time-critical item; nothing in
`cdot-7/` was touched.
