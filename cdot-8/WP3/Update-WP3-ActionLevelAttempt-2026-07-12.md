# Update — WP3: The Action-Level Attempt, and Why Directive 2 Isn't Optional

*Companion: `SessionLog-2026-07-12.md` (this directory), Entry 6. Attempts directive 1
of `Advisory-WP3-InverseReconstruction-2026-07-12.md` ("implement M5 at the action
level... derive the modified scalar equation of motion"). This is not a kill report and
not a clean pass — it is substantial progress that sharpens exactly why directive 2
(the constraint-propagation/energy-bookkeeping check) is necessary, via a direct
calculation rather than by assuming the prior resolution's zero-freedom quadrature was
the end of the story.*

---

## 1. The minisuperspace reduction, validated against the known result first

Reduced AeST's action to the homogeneous (FRW, flat, unitary/khronon gauge $\phi=t_
\text{coord}$) sector, keeping the lapse $N(t)$ explicit rather than fixing it to 1:
Einstein-Hilbert term plus $-\frac{a^3N}{16\pi\tilde G}F(Q)$ with $Q=\dot\phi/N=1/N$
(unitary gauge), $Y=0$ (homogeneity kills the spatial invariant identically). Varying
w.r.t. $N$ and setting $N=1$ at the end reproduces
$$H^2=\frac{8\pi\tilde G}3\rho_m-\frac13(F-QF_Q)$$
— **exactly WP0's extracted AeST Friedmann equation**, a validating check before
trusting anything built on top of this reduction. Varying w.r.t. $\phi$ (before
imposing the unitary-gauge identification) reproduces the free shift-current
conservation $\frac{d}{dt}(a^3F_Q)=0$ — also matching WP0's extraction exactly.

**The gauge subtlety, resolved.** M1's "$\phi=t_\text{coord}$" (flagged as dimensionally
awkward in `Update-WP3-ReconstructionResolved-2026-07-12.md` §2) is the standard
unitary/khronon gauge of ghost-condensate and Hořava-gravity-type constructions — φ's
dimensions become "time" *by the gauge choice itself*, with the physical content
carried by the lapse function $N=d\tau/dt_\text{coord}=(c/c_0)^{5/2}$ (exactly the
two-clock dictionary's lapse). This is not an error; it dissolves the earlier caveat.

---

## 2. The direct check: does the "free" conservation law survive M5, or is it actually
mandatory absent explicit sourcing?

Computed the continuity equation for the scalar sector's own energy density and
pressure ($\rho_\phi=-\frac1{8\pi\tilde G}(F-QF_Q)$, $p_\phi=\frac1{8\pi\tilde G}F$ —
AeST's own definitions, WP0 extraction), for *arbitrary* $F(Q)$ and $Q(t)$:
$$\dot\rho_\phi+3H(\rho_\phi+p_\phi)=\frac{Q}{8\pi\tilde G}\left[\frac{d}{dt}F_Q+3HF_Q
\right]=\frac{Q}{8\pi\tilde G a^3}\frac{d}{dt}(a^3F_Q).$$
Verified numerically (finite differences, arbitrary smooth test functions for $a(t)$,
$Q(t)$, and $F(Q)$ unrelated to the physical trajectory) to $3\times10^{-9}$ absolute
precision against a typical term magnitude of $\sim12$ — **a pure algebraic identity**,
not contingent on any special trajectory.

**Consequence, stated plainly: ordinary energy-momentum conservation (the Bianchi
identity), applied to a scalar sector whose stress-energy takes AeST's own standard
$(F,Q)$-only form, is *equivalent to* the free conservation law $\frac{d}{dt}(a^3F_Q)
=0$ — not merely "what you get without sourcing," but *what continuity demands outright*
once matter is separately conserved (which it is, ordinarily).** The corrected
reconstruction (`Advisory-WP3-InverseReconstruction`, §4(iii)) demands $a^3F_Q\propto
a^{5/3}$, manifestly not constant. **This means the quadrature-constructed $F(Q)$,
taken alone — with the scalar sector still described by the standard, unmodified
$\rho_\phi(F,Q)$ formula — is not yet Bianchi-consistent.** Finding *a* function $F(Q)$
that balances the Friedmann equation (what the quadrature does) is necessary but not
sufficient; the scalar sector's *own* conservation law, once $Q(a)$ is fixed by the
unitary-gauge/M1 identification, independently constrains $F(Q)$ to satisfy the free
law — and the two requirements (Friedmann-balance vs. free-conservation) are only
simultaneously satisfiable if $a^3F_Q$ is *actually* constant, contradicting what the
invoice demands.

---

## 3. This is not a contradiction of the prior resolution — it is directive 2, arrived
at independently

The stand-in advisory's own directive 2 anticipated exactly this: "a sourced scalar
current must exchange energy consistently under the Bianchi identity; the natural
ledger is WP2's census evolution equation, whose shell-sweep term $3c/R_h$ is the
open-boundary (Machian) channel... this is delicate and novel — it is proposal §5 item
1, the program's heart." This session's own, independent route to the same conclusion
(via the direct continuity-equation calculation in §2, not by taking directive 2 on
faith) confirms that check is not a formality: **M5 cannot be "for free" — reproducing
the invoice requires the scalar sector to exchange energy with something outside its
own standard stress-energy budget, and the natural, already-available candidate is the
census's shell-sweep term** ($3c/R_h$ in WP2's $\dot{\mathcal N}/\mathcal N$ decomposition
— new mass/energy entering the horizon purely from its own geometric growth, a genuinely
global, Machian channel distinct from ordinary local energy exchange, and structurally
suited to being what an honest, action-level M5 term needs to supply).

**What remains genuinely open, not resolved this session**: constructing the actual
action-level term (a Lagrange multiplier or boundary term coupling $\phi$ explicitly —
not just $Q$ — to the census integral, so that it contributes its own stress-energy)
and verifying that *its* contribution, added to $\rho_\phi,p_\phi$, makes the *total*
system's continuity equation balance while reproducing the demanded $a^3F_Q\propto
a^{5/3}$ for the $\phi$-sector alone. This is real, substantial, original theoretical
construction — plausibly what the proposal's own §5 item 1 ("the program's heart") was
always going to require — not a quick follow-up.

---

## 4. Status

Not a kill: nothing here shows the required exchange term *cannot* exist — only that
it must, and that it hasn't been built yet. Not a pass: the zero-freedom criterion from
the prior resolution is necessary but demonstrably not sufficient, given the direct
Bianchi check in §2. Recommend continuing to attempt the construction (the shell-sweep
channel is a concrete, motivated starting point) in a follow-up pass, flagging this
honestly as the hardest remaining piece of the whole program rather than either
declaring premature success or manufacturing a kill from an incomplete construction.
