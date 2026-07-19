#!/usr/bin/env python3
"""
dictionary_crosscheck.py — 2026-07-18. Independent cross-check of the
worker's Step-1 dictionary  c1=K_B, c2=0, c3=-K_B, c4=0  (exact, shared
1/16piG prefactor).

Route A — link-by-link audit of their signature-flip reasoning (one
correction found: the c4-structure is NOT invariant).
Route B — a convention-independent PHYSICAL cross-check they didn't run:
feed the dictionary into Foster-Jacobson's own mode formulas and compare
against SZ's independently-derived mostly-plus results. Physical
quantities (mode speeds) cannot depend on signature bookkeeping, so
agreement here checks the dictionary end-to-end.
Route C — the consequences now computable: the ae-limit alpha_1 = -4K_B
and the K_B -> 0 corner.
"""
import sympy as sp, numpy as np

print("=== Route A: structure-by-structure signature audit (u^m components fixed) ===")
print("""c1: g^{ab} g_{mn} (nabla u)(nabla u) — TWO explicit metrics -> invariant  [worker: OK]
c2: (div u)^2                    — ZERO explicit metrics -> invariant  [worker: OK]
c3: nabla_a u^m nabla_m u^a      — ZERO explicit metrics -> invariant  [worker: OK]
c4: u^a u^b g_{mn}(...)          — ONE explicit metric  -> FLIPS SIGN
CORRECTION to the worker's blanket 'each have an even number': false for
c4. Irrelevant to the boxed result (c4=0 for AeST's Maxwell term) but the
dictionary MUST carry  c4_FJ <-> -c4_(mostly-plus)  into Step 3, where
FJ's c4-dependent formulas (alpha_1 ~ c1*c4+c3^2, c14 everywhere) get
used and where the phi-sector could induce effective u^a u^b terms.""")

print("=== Route B: physical mode-speed cross-check (convention-independent) ===")
c1,c2,c3,c4,KB = sp.symbols('c1 c2 c3 c4 K_B', positive=False)
sub = {c1: KB, c2: 0, c3: -KB, c4: 0}
c13, c14, c123 = c1+c3, c1+c4, c1+c2+c3
# Foster-Jacobson / ae-theory small-ci-exact mode speeds (standard forms):
s1_sq = (2*c1 - c1**2 + c3**2)/(2*c14*(1-c13))     # spin-1
s0_num = c123*(2-c14)                               # spin-0 speed^2 propto c123*(...)
print(f"spin-1 speed^2 with dictionary: {sp.simplify(s1_sq.subs(sub))}"
      f"   [SZ mostly-plus result: exactly 1 — MATCH]")
print(f"spin-0 speed^2 numerator:       {sp.simplify(s0_num.subs(sub))}"
      f"   [SZ: aether spin-0 non-dynamical, phi-replaced — MATCH]")
print("Two independent physical quantities, computed by both papers in their")
print("own conventions, agree through the dictionary: end-to-end validation.\n")

print("=== Route C: consequences now explicit ===")
alpha1_ae = -4*c14.subs(sub)
print(f"ae-limit alpha_1 = -4*c14 = {alpha1_ae}   (leading form; phi-corrections ~ Q0^2/c_Y_screened)")
for a1_bound, label in [(1e-5,"pulsar/LLR class |alpha_1| bound"),]:
    print(f"{label}: {a1_bound:.0e}  ->  K_B <~ {a1_bound/4:.1e}  IF leading form survives")
F_QQ = -0.6962
mu0 = np.sqrt(-F_QQ/2/2)   # K_B->0: mu_eff = sqrt(-F_QQ/(2*(2-0)))
c_H0_Mpc = 2.99792458e8/(0.70*100*1000/3.0857e22)/3.0857e22
print(f"""K_B -> 0 corner (if the squeeze lands):
  mu_eff -> sqrt(-F_QQ)/2 = {mu0:.3f} H0/c -> 1/mu = {c_H0_Mpc/mu0:.0f} Mpc (~10.3 Gpc):
    WP5 conclusion UNCHANGED (was the K_B->0 end of the quoted band);
  m_x = Q0*sqrt((2-K_B)/(2K_B)) -> infinity: Mistele's ONE-field limit
    applies at all scales — the two-limit question would dissolve by
    parameter squeeze (for real this time), wide binaries take their
    one-field value;
  spin-1 energy ~ 2K_B -> vector modes decouple;
  SZ stability: K_B in (0,2) open interval — K_B -> 0+ smooth, healthy.
ALL of Route C is consequences-if-the-leading-form-survives: the Step-3
derivation must still deliver the phi-completed alpha_1 before any bound
is quoted.""")
