# Day 4 Optimization Slides Format

## Highest Rule: Minimal and Complete

Every slide must be:
- **Minimal:** No extraneous words, no 'how to use' explanations, no roadmap descriptions
- **Complete:** Sufficient for self-learning without external references
- **Self-contained:** Example statement and solution together, theorem and proof together

## Required Order

The slides MUST follow this exact sequence:

1. **4.1 Unconstrained Optimization** - FOC, SOC, necessary vs sufficient
2. **4.2 Concavity, Convexity, Quasiconcavity** - Function shapes
3. **4.3 Equality Constraints** - Lagrange multipliers
4. **4.4 Envelope Theorem** - Constrained and unconstrained
5. **4.5 Inequality Constraints** - KKT conditions
6. **4.6 Why Equality Multipliers Are Unrestricted** - Explained AFTER KKT

## No Unnecessary Slides

- **NO** 'How to use these slides' pages
- **NO** long roadmap/structure explanations
- **NO** 'Today we will learn...' summaries
- Start directly with content or minimal roadmap

## Slide Format Rules

### Length
- Each slide: 4-6 sentences maximum
- Packed but readable
- No empty slides

### Exercise Format
- Use `\QFrame` for in-class exercises
- Use `\THFrame` for take-home exercises
- Use "Exercise" NOT "Question" in titles
- Exercises MUST be self-contained:
  - Full problem statement
  - Full solution provided
  - No "work through on paper, see solution below"
  - No hints like "try using the hint"

### Proof Format
- State theorem/result first
- Then provide proof in proof environment or clearly marked
- Two versions for complex proofs:
  - Main deck: concise version (4-6 sentences)
  - Appendix: rigorous version with full details

### Section Transitions
- Each section starts with motivation slide
- Explain why we're moving to this topic
- Smooth logical flow from previous section

### Figure Requirements
- Farkas cone: acute angle, centered, no truncation
- All figures must display fully within frame
- Use width=0.85\textwidth or appropriate scaling

### Macros
```latex
\newcommand{\QFrame}[1]{%
  \begin{frame}{#1 \quad {\small\textcolor{mAccent}{Together}}}}
\newcommand{\THFrame}[1]{%
  \begin{frame}{#1 \quad {\small\textcolor{mAccent}{Take home}}}}
```

## Content Rules

### Lagrangian Convention
- Use ONE convention only: $\mathcal{L} = f + \sum \mu_k h_k + \sum \lambda_j g_j$ (all plus)
- Explain sign rules clearly
- Equality $\mu$ unrestricted, inequality $\lambda$ sign-restricted

### Unrestricted Multiplier Explanation
- Must come AFTER KKT
- Contrast equality (two-sided) vs inequality (one-sided)
- Explain directional feasibility

### Economics Integration
- Each section needs economics examples
- Examples should be:
  - Relevant (profit, utility, cost)
  - Not too simple (not just $f(x)=x^2$)
  - Not too hard (no complex matrix algebra)
  - Self-contained with full solution

### Proof Detail Level
- Main deck: Intuition + key steps
- Appendix: Full rigorous proofs
- SOC proof: Both versions required
  - Main: Taylor sketch
  - Appendix: Symmetric difference OR Taylor with remainder

## Page Budget
- Main content: 50-60 pages
- Appendix: As long as needed
- Total: 60-70 pages acceptable

## Critical Format Rules (DO NOT VIOLATE)

### Frame Endings
- ALWAYS use `\end{frame}` (NOT `\end{QFrame}` or `\end{THFrame}`)
- `\QFrame` and `\THFrame` only open frames, standard `\end{frame}` closes them

### Content Per Slide
- Maximum 4-6 sentences per slide
- Each bullet point = one line with blank line before next
- Theorem statement: one line
- Proof: starts on next line with bullet points
- Example statement: one line
- Solution: starts on next line with bullet points

### Figure Rules
- Graph FIRST, then concept (always show before explaining)
- Check figure is not cut off/covered by text
- Use width=0.85\textwidth or appropriate scaling
- Captions below figures, short and clear

### Required Figures
1. **Concave/convex**: Smooth curves, NO kinks, multiple tangent lines at different points, multiple colors (red/green/purple for different tangents)
2. **Quasiconcavity intuition**: 2D plane showing convex upper contour sets vs non-convex (dumbbell shape)
3. **Farkas**: Two panels - optimal (-?f in cone) and not optimal (separating hyperplane with feasible direction d clearly labeled)

### Farkas Statement Rule: PURELY GEOMETRIC FIRST

**CRITICAL:** Farkas lemma statement must be PURELY GEOMETRIC:
- Cone K (not gradients)
- Vector y (not ?f)
- NO ?g, NO ?f, NO optimization language in statement
- Two cases: (1) y ? K, (2) y ? K with separating hyperplane
- **ONLY AFTER** the pure geometric statement: introduce optimization application with ?f and ?g

**Correct Farkas Order:**
1. Feasible directions (concept)
2. Farkas graph (two panels)
3. **Farkas statement: PURELY GEOMETRIC** (cone K, vector y)
4. **Apply to optimization:** introduce K = cone{?g_j}, y = -?f
5. Inequality problem with multipliers
6. KKT conditions

### Section Content Requirements

#### 4.1 Unconstrained
- FOC necessary condition with proof
- Critical points example with solution (separate lines)
- SOC sufficient condition
- Example showing $-x^4$ strict concave but $f''(0)=0$

#### 4.2 Concavity/Quasiconcavity  
- Graph first (concave/convex with multiple tangents)
- Tangent characterization theorem
- Rigorous proof $f'' \leq 0$ iff concave (in main text, not appendix)
- Multivariate: tangent hyperplane explanation, Hessian PSD
- Quasiconcave vs quasiconvex definitions
- Hierarchy: concave ? log-concave ? quasiconcave
- Proof: concave implies quasiconcavity
- Equivalence: segment def ? convex upper contours

#### 4.3 Equality Constraints
- 3D Lagrange figure
- Tangent argument with geometric intuition
- Lagrangian derivation
- Shadow-price derivation with chain rule ($dV/dw=\mu$), BEFORE exercises
- Cobb-Douglas budget + multiplier exercises (together)
- Cost minimization exercise

#### 4.4 Envelope
- Unconstrained theorem + proof
- Profit function example with explicit verification
- Constrained theorem
- Budget set $B(p,w)$ and indirect utility $V(p,w)$, before Roy
- Roy's identity example
- Cost function exercise (take home)

#### 4.5 Farkas/KKT
- **Order**: feasible directions ? Farkas graph ? Farkas statement (PURELY GEOMETRIC) ? apply to optimization ? inequality problem ? KKT
- Feasible directions: geometric definition
- Farkas: 3 slides minimum (graph, pure geometric statement, optimization application)
- Farkas statement: cone K, vector y (NO gradients)
- Apply Farkas: K = cone{?g_j}, y = -?f
- Binding vs slack with geometric ? explanation
- KKT conditions theorem
- Sign table
- Budget example + corner solution exercise

#### 4.6 Unrestricted Multipliers
- Two-sided vs one-sided explanation
- Formal argument
- Example comparing equality vs inequality
- Summary Lagrangian
- Exercise + take home exercise

### Exercises Required
- **4.1**: Critical points (together), SOC (together)
- **4.2**: Concavity global max (together), concavity vs convexity (together), Cobb-Douglas quasiconcave (together), Cobb-Douglas not concave (together), quasiconcavity test (take home)
- **4.3**: Cobb-Douglas budget (together), multiplier interpretation (together), cost minimization (take home)
- **4.4**: Profit envelope (together), Roy's identity (together), cost envelope (take home)
- **4.5**: Budget nonnegativity (together), corner solution (together), cost min inequality (take home)
- **4.6**: Equality vs inequality (together), unrestricted action (take home)

## Verification Checklist
- [ ] Correct section order: 4.1 ? 4.2 ? 4.3 ? 4.4 ? 4.5 ? 4.6
- [ ] `\end{frame}` used everywhere (not `\end{QFrame}` or `\end{THFrame}`)
- [ ] All exercises: "Exercise" in title, self-contained, full solution
- [ ] Theorem: one line, proof: next line with bullet points
- [ ] Example: one line, solution: next line with bullet points
- [ ] Each bullet point on separate line with blank line before next
- [ ] Maximum 4-6 sentences per slide
- [ ] Graphs first, then concept explanation
- [ ] Concave figure: smooth curves, multiple colored tangents
- [ ] Quasiconcave intuition: 2D plane with convex vs non-convex
- [ ] Farkas: two panels, clear labels, feasible direction arrow
- [ ] **Farkas statement: PURELY GEOMETRIC (no ?f, no ?g)**
- [ ] **Farkas applied to optimization AFTER the pure statement**
- [ ] Rigorous SOC proof in main text (after concave/convex figure)
- [ ] Multivariate tangent plane explanation included
- [ ] Quasiconvex included
- [ ] Concave?quasiconcave proof included
- [ ] Hierarchy of concavity types included
- [ ] Unrestricted multipliers AFTER KKT
- [ ] NO 'How to use these slides' pages
- [ ] Page count: main ~50-60, appendix additional, total ~60-70
