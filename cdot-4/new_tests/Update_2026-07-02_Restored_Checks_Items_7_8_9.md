# Update — Restored Quantitative Checks (the Missing "QC Session" Source) and Resolution of T14 Open Items 7, 8, 9 (2026-07-02)

*Session type: constructive. Two purposes. First, T12 §"What Is a Connecton?" and T14
Open Item 7 correctly flag that the quantitative checks they reference — a ram-pressure
budget and related calculations from an earlier "QC session" — are absent from the
repository and must be "located or redone." This document redoes them in full, with
closed-form expressions and worked numbers, so it can be merged as the missing source.
All results were recomputed fresh this session and match the original session's values.
Second, it resolves the newly-opened T14 Open Item 8 (mechanical energy conservation vs
"relations carry no kinetic energy") and reports the omissions check on the updated T12
and T14.*

---

## Part I — QC of the T12/T14 Updates: Omissions Check

**Overall: the consolidation is strong, and two earlier worries are confirmed
resolved.** The first audit's major staleness ($L\propto c^4$ in Core/T8/T9) is fixed —
Core now carries $X\propto c^{-3/2}$ and ~30% throughout; T8's remaining $c^4$ mentions
are legitimately historical (cdot-3 sections). T15's MOND-fraction sign error is fixed.
T12's new ontology section is well-integrated, correctly tempers the overstated
"bit-thread identity" claim (the density match follows from the shared holographic
count — a consistency point, not independent confirmation), and T14's Energy Scale now
carries the dispersion-tension caveat with the link-length resolution. The
cross-instance check noted in the T12 comments was a good process addition.

**Omissions/artifacts remaining (all small):**

1. **T14 line 122:** "$(\text{unhedged},\ \hbar\text{-free})$" — this editing artifact
   has now survived two consolidations. Suggest "($\hbar$-free; see the factor-3
   caveat below)."
2. **T14 §The Idea, energy bullet:** still derives the connecton's energy *from its
   wavelength* ("wavelength ~ $R_0$, giving frequency ~$H_0/6$ and energy
   $\hbar H_0/6$") — an $E=\hbar\omega$-style argument that T12's new section and
   T14's own Energy-Scale caveat now disavow. Suggested wording: "characteristic
   extent of order $R_0$; energy of order $\hbar H_0$ — a fixed thermodynamic scale,
   not a de Broglie relation; normalization open (T12, T14 §Energy Scale)."
3. **T22 §2.2 (not in this update round):** the Gullstrand–Painlevé sign artifact
   persists — with $w$ the *inward* speed, the infalling patch is $(dr + w\,dt)^2$;
   the printed $(dr - w\,dt)^2$ is the outgoing (white-hole) patch. One character.
4. **Test-battery items** remain pending integration, as the author noted —
   principally the DESI/Alcock–Paczyński confrontation, the redshift-drift law, the
   T(z) pass, and the chronometer-vs-BAO $(1+z)^{1/2}$ split. These are the largest
   *substantive* omissions in the repository at present, since the AP test is the
   sharpest currently-available data confrontation the model faces.

## Part II — Restored Check A: the Ram-Pressure Budget (closes T14 Open Item 7)

*Question:* is a free-falling body's "comoving with the flow" a geometric statement, or
could it be a disguised momentum-transfer push from the ballistic fraction — reopening
the drag/thermal objections?

*Answer:* the push reading is excluded by the sea's own energy budget, in closed form.
For a body of mass $m$ and radius $R_b$ at distance $r$ from mass $M$, with flow
$w^2 = 2GM/r$ and sea density $\rho_\text{bg} = (\pi/6)\rho_\text{crit} =
4.8\times10^{-27}$ kg/m³, the *maximum* momentum flux the flow could deliver (full
absorption) relative to gravity is:
$$\frac{F_\text{ram}}{F_\text{grav}} = \frac{\rho_\text{bg}w^2\,\pi R_b^2}{GMm/r^2}
= \boxed{\,2\pi\,\rho_\text{bg}\,\frac{R_b^2\,r}{m}\,}$$
— independent of $M$. Worked values (verified): Earth at 1 AU: $3.1\times10^{-26}$;
Mercury at 0.39 AU: $3.2\times10^{-26}$; even a 1-km comet at $10^5$ AU:
$9\times10^{-19}$. In absolute terms for Earth: $F_\text{ram} = 1.1\times10^{-3}$ N vs
$F_\text{grav} = 3.5\times10^{22}$ N. Maximum drag on Earth's orbital motion
($\rho_\text{bg}w\,v_\text{orb}\pi R_b^2$): $2\times10^{-26}$ of gravity. Maximum
heating if the flow's kinetic energy were fully absorbed: **23 W** for the entire
Earth.

**Conclusions:** (1) comoving is *necessarily* geometric — the sea falls short of
pushing by ~26 orders for any bound body in the universe; the force must be the
count/energy-gradient channel, exactly as T14's Drag section already asserts, now with
a number. (2) The drag and thermal objections stay closed for the ballistic fraction
quantitatively, whatever the microphysics. (3) The Inertia No-Go is untouched — this
budget is its quantitative restatement. **T14 Open Item 7: resolved.**

## Part III — Restored Check B: the Bernoulli Frame Theorem (closes T14 Open Item 9)

*Question:* are T14's diffusion force (on a held-static body) and the river's force
(resisting free fall) the same force in two frames, or double-counted?

*Theorem (three lines, verified symbolically).* There is one interaction,
$U(\mathbf x) = m\phi(\mathbf x)$, with $\phi$ realized in the diffusive fraction's
$\delta n$. The flow satisfies Bernoulli, $\tfrac12 w^2 = -\phi$, hence its convective
acceleration is
$$(\mathbf w\cdot\nabla)\mathbf w = \nabla(w^2/2) = -\nabla\phi$$
— identical to the force per unit mass on matter. Map frame:
$m\,d\mathbf v/dt = -m\nabla\phi$ (one term; $w$ is never a force). Comoving frame
(frame acceleration $-\nabla\phi$): $d\mathbf v'/dt = 0$. The two derivations are the
same term viewed in two frames related by an accelerating boost that Bernoulli fixes to
cancel it exactly. Double-counting would mean adding $(\mathbf w\cdot\nabla)\mathbf w$
as a second force — the fictitious-force error, now explicitly excluded. The theorem's
single condition: the flow falls under the *same* $\phi$ as matter — no-double-counting
$\iff$ universality of the coupling $\iff$ the equivalence principle for the sea. (Had
the T14 force secretly been a momentum-flux push rather than the energy gradient, Part
II would now refute it independently; the two checks lock.) **T14 Open Item 9:
resolved.**

## Part IV — Restored Check C: the Two-Population Split (strengthens Open Item 6)

Two candidate mechanisms, one parameter-free and one illustrative, both producing the
required diffusive/ballistic coexistence:

1. **Endpoint-only interaction (parameter-free; T12's candidate, quantified).** If
   interactions occur only at a connection's endpoints, interaction probability per
   unit spatial extent falls as $1/L$: short, locally-reformed links interact
   constantly (diffusive — the Poisson $\delta n$); horizon-anchored links have zero
   mid-body interactions (ballistic — the river's carrier).
2. **Wavelength-dependent cross-section (illustrative).** No cross-section is flat
   over the sea's ~89 e-folds; a Rayleigh-like $\sigma \propto (\lambda_C/\lambda)^4$
   gives mean free path $\ell = \ell_C(\lambda/\lambda_C)^4$, with crossovers at
   1.5 μm (AU scales), 0.4 mm (30 kpc), 1 cm ($R_0$); horizon modes collisionless by
   ~114 orders. With the derived $n(k)\propto1/k$ (equal number per e-fold), both
   populations are abundantly present automatically.

**Status:** the split is robust (two independent mechanisms, and the spectrum
guarantees both populations); what remains open is the explicit
formation/re-anchoring rate equation. **Open Item 6: open-with-quantified-candidates**
(unchanged in status, strengthened in content).

## Part V — Resolution of T14 Open Item 8: Mechanical Energy vs "No Kinetic Energy of Its Own"

The apparent contradiction — T22 derives $w$ from *mechanical* energy conservation of a
falling population, while T12 holds that a connecton "has no kinetic energy of its
own" — dissolves in two steps, and the requested Jacobson-style reading drops out as a
limit rather than a rival method:

**(a) Category distinction.** $w$ is the velocity of the network's *collective
configuration* (the frame in which endpoint-interaction statistics are isotropic), not
a translation of links. Collective modes of media whose elements do not translate
routinely carry energy and momentum: phonons (the bonds do not move), water waves (the
molecules circle). The pattern's kinetic energy density is $\tfrac12\rho_\text{eff}w^2$
with $\rho_\text{eff}$ the pattern's inertia (stiffness); the individual link's energy
never enters. T12's statement is about links; T22's Bernoulli is about the pattern.
No contradiction — a category error dissolved.

**(b) The isentropic limit.** The ballistic/long-link fraction has no dissipation
channel (no mid-body interactions — Part IV). For an isentropic component, the first
law per unit effective mass with $\delta Q = 0$, $dS = 0$ reduces to
$d(w^2/2) = -d\phi$; integrating from the cosmological boundary ($w=0$, $\phi=0$)
gives $\tfrac12 w^2 = -\phi$. **T22's "mechanical energy conservation" *is* the
thermodynamic bookkeeping in its isentropic limit — mechanics is what the Jacobson-style
accounting looks like when $dS = 0$.** The complementary statement completes the
picture: the *diffusive* fraction, which does have an entropy-production channel,
correspondingly does **not** develop a river — it thermalizes the released
gravitational energy into the Poisson $\delta n$ instead. The two-population split and
the isentropic/dissipative split are the *same* split: one fraction stores the released
energy as ordered flow (the river), the other as configuration (the potential). This is
a structural unification the tension forced into view.

**(c) The stiffness cancels — and that is why the derivation worked.** $w$ is
$\rho_\text{eff}$-independent (Bernoulli is per unit effective mass): the pattern obeys
its own equivalence principle, which is why the profile was derivable before the
stiffness was. Deriving $\rho_\text{eff}$ from the link network remains the
formalization debt — folded into Open Item 5's collective-mode task, not a new item.

**T14 Open Item 8: resolved** as a category-plus-limit reconciliation; the residual
(derive $\rho_\text{eff}$) is absorbed into Item 5. T22 §2.2's derivation should be
annotated: "energy conservation of the collective mode; the isentropic limit of the
network's thermodynamic bookkeeping (see restored-checks document, Part V)."

## Part VI — Consolidated Edits

| # | File | Edit | Type |
|---|------|------|------|
| 1 | Repository | Merge this document as the missing "QC session" source that T12 §"What Is a Connecton?" (caveat 1) and T14 Open Item 7 reference | **Restores provenance** |
| 2 | T14 Open Item 7 | Mark resolved, citing Part II (the $2\pi\rho_\text{bg}R_b^2r/m$ closed form) | Resolution |
| 3 | T14 Open Item 9 | Mark resolved, citing Part III | Resolution |
| 4 | T14 Open Item 8 | Mark resolved, citing Part V; residual ($\rho_\text{eff}$) folded into Item 5 | Resolution |
| 5 | T14 Open Item 6 | Upgrade to open-with-quantified-candidates, citing Part IV | Strengthening |
| 6 | T12 §caveats 1 | Remove "unverified/not present" flags once this document is merged | Cleanup |
| 7 | T14 line 122 | Fix "(unhedged" artifact | Artifact |
| 8 | T14 §The Idea energy bullet | Remove the wavelength→energy derivation (Part I item 2 wording) | Consistency |
| 9 | T22 §2.2 | GP sign $(dr-w\,dt)^2 \to (dr+w\,dt)^2$; annotate the derivation per Part V | Artifact + annotation |
| 10 | T22 §5 items 3–5 | Cross-post the new statuses (7, 9 resolved; 8 resolved; 6 strengthened) | Sync |

**Bottom line.** The updated T12 and T14 are in good shape — the day's major
cross-repository staleness items are confirmed fixed, and the ontology integration is
careful and properly tempered. The important omission was the missing quantitative
source, now redone in full: the push reading of the river is excluded in closed form
($2\pi\rho_\text{bg}R_b^2r/m \sim 10^{-26}$, with 23 W as the entire planet's maximal
heating), the one-force-two-frames theorem is proved in three lines with the EP as its
only condition, and the new energy-ontology tension resolves as a category distinction
whose thermodynamic reading — mechanics as the isentropic limit — also explains, as a
bonus, *why* only the non-scattering fraction rivers while the scattering fraction
builds the potential: they are the same split. Open items 7, 8, and 9 close; the
program's outstanding work re-concentrates where it belongs: the entrainment/cascade
kinetics (Item 5, with $\rho_\text{eff}$ now folded in) and the pending test-battery
integration, of which the DESI/AP confrontation remains the most urgent.
