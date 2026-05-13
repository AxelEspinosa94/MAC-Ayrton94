
---

# **Differential Equations — Extended Theorem & Methods Compendium**  
*A complete reference for theory, classification, solution methods, and modeling.*

---

# **Table of Contents**

1. [Introduction](#introduction)  
2. [Classification of Differential Equations](#classification-of-differential-equations)  
3. [Existence and Uniqueness Theorem](#existence-and-uniqueness-theorem)  
4. [First‑Order Differential Equations](#first-order-differential-equations)  
   - Separable  
   - Exact  
   - Linear (Integrating Factor)  
   - Substitution Methods  
5. [Higher‑Order Linear Differential Equations](#higher-order-linear-differential-equations)  
   - Constant Coefficients  
   - Nonhomogeneous Methods  
   - Cauchy–Euler  
6. [Nonlinear Differential Equations](#nonlinear-differential-equations)  
7. [Systems of Differential Equations](#systems-of-differential-equations)  
8. [Series Solutions](#series-solutions)  
9. [Modeling with Differential Equations](#modeling-with-differential-equations)  
10. [Appendices](#appendices)

---

# **Introduction**

A **differential equation (DE)** is an equation involving an unknown function and one or more of its derivatives.

General form:

$$
F\left(x, y, y', y'', \dots, y^{(n)}\right)=0
$$

A **solution** is a function $y(x)$ that satisfies the equation on an interval.

---

# **Classification of Differential Equations**

## **By Order**
Order = highest derivative appearing.

## **By Linearity**
A DE is **linear** if it can be written as:

$$
a_n(x)y^{(n)} + \cdots + a_1(x)y' + a_0(x)y = g(x)
$$

Otherwise, it is **nonlinear**.

## **By Homogeneity**
A linear DE is **homogeneous** if:

$$
g(x)=0
$$

Otherwise, **nonhomogeneous**.

## **By Autonomy**
Autonomous if:

$$
y' = f(y)
$$

---

# **Existence and Uniqueness Theorem (Picard–Lindelöf)**

For the IVP:

$$
y' = f(x,y), \quad y(x_0)=y_0
$$

If $f$ and $\frac{\partial f}{\partial y}$ are continuous near $(x_0,y_0)$,  
then a **unique** solution exists.

---

# **First‑Order Differential Equations**

---

# **1. Separable Differential Equations**

## **Definition**
A DE is separable if it can be written as:

\[
\frac{dy}{dx} = g(x)h(y)
\]

## **Algorithm**
1. Rewrite:  
   \[
   \frac{1}{h(y)}dy = g(x)dx
   \]
2. Integrate both sides.
3. Solve for \(y\) if possible.
4. Apply initial condition.

## **Example**
\[
y' = xy
\]

\[
\frac{1}{y}dy = xdx
\]

\[
\ln|y| = \frac{x^2}{2} + C
\]

\[
y = Ce^{x^2/2}
\]

---

# **2. Exact Differential Equations**

## **Definition**
A DE of the form:

\[
M(x,y)dx + N(x,y)dy = 0
\]

is **exact** if:

\[
\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}
\]

## **Algorithm**
1. Check exactness.  
2. Integrate \(M\) w.r.t. \(x\).  
3. Differentiate result w.r.t. \(y\) and match with \(N\).  
4. Solve for constant.

## **Example**
\[
(2xy + 3)dx + (x^2 + 4y)dy = 0
\]

Check exactness:

\[
M_y = 2x, \quad N_x = 2x
\]

Integrate:

\[
\int (2xy + 3)dx = x^2y + 3x + h(y)
\]

Differentiate w.r.t. \(y\):

\[
x^2 + h'(y) = x^2 + 4y
\]

\[
h'(y)=4y \Rightarrow h(y)=2y^2
\]

Solution:

\[
x^2y + 3x + 2y^2 = C
\]

---

# **3. Linear First‑Order Equations**

General form:

\[
y' + P(x)y = Q(x)
\]

## **Integrating Factor**
\[
\mu(x)=e^{\int P(x)dx}
\]

## **Algorithm**
1. Compute \(\mu(x)\).  
2. Multiply entire equation.  
3. Recognize derivative:  
   \[
   (\mu y)' = \mu Q
   \]
4. Integrate.  
5. Solve for \(y\).

## **Example**
\[
y' + 2y = e^{-x}
\]

\[
\mu = e^{2x}
\]

\[
(e^{2x}y)' = e^{x}
\]

\[
e^{2x}y = e^{x} + C
\]

\[
y = e^{-x} + Ce^{-2x}
\]

---

# **4. Substitution Methods**

## **4.1 Homogeneous Equations**
\[
y' = F\left(\frac{y}{x}\right)
\]

Substitute:

\[
y = vx, \quad y' = v + xv'
\]

## **4.2 Bernoulli Equation**
\[
y' + P(x)y = Q(x)y^n
\]

Substitute:

\[
v = y^{1-n}
\]

## **4.3 Riccati (special case)**
\[
y' = a(x)y^2 + b(x)y + c(x)
\]

If one solution is known, reduce to linear.

## **4.4 Clairaut**
\[
y = xy' + f(y')
\]

Solution:  
General: \(y = Cx + f(C)\)  
Singular: envelope.

---

# **Higher‑Order Linear Differential Equations**

---

# **5. Constant Coefficients**

\[
a_n y^{(n)} + \cdots + a_1 y' + a_0 y = 0
\]

Characteristic equation:

\[
ar^n + \cdots + a_0 = 0
\]

## **Cases**
- Real distinct roots  
- Repeated roots  
- Complex roots  

## **Example**
\[
y'' - 3y' + 2y = 0
\]

\[
r^2 - 3r + 2 = 0
\]

\[
r=1,2
\]

\[
y = C_1 e^x + C_2 e^{2x}
\]

---

# **6. Nonhomogeneous Linear ODEs**

## **6.1 Method of Undetermined Coefficients**
Works for RHS of form:

- Polynomials  
- Exponentials  
- Sines/cosines  
- Products of these  

## **Algorithm**
1. Solve homogeneous part.  
2. Guess particular solution.  
3. Plug in and solve coefficients.  
4. Add solutions.

---

## **6.2 Method of the Annihilator**

Use differential operators to eliminate RHS.

---

## **6.3 Variation of Parameters**

General formula:

\[
y_p = -y_1 \int \frac{y_2 g}{W}dx + y_2 \int \frac{y_1 g}{W}dx
\]

---

# **7. Cauchy–Euler Equation**

\[
x^n y^{(n)} + \cdots + a_1 xy' + a_0 y = g(x)
\]

Try:

\[
y = x^r
\]

---

# **Nonlinear Differential Equations**

Autonomous:

\[
y' = f(y)
\]

Phase line analysis.

Example:

\[
y' = y(1-y)
\]

---

# **Systems of Differential Equations**

---

# **Linear Systems**

\[
\mathbf{x}' = A\mathbf{x}
\]

Solution via eigenvalues/eigenvectors.

---

# **Nonlinear Systems**

Linearize using Jacobian.

---

# **Series Solutions**

---

# **Power Series Method**

Assume:

\[
y = \sum_{n=0}^\infty a_n x^n
\]

Find recurrence.

---

# **Frobenius Method**

\[
y = x^r \sum_{n=0}^\infty a_n x^n
\]

Indicial equation.

---

# **Modeling with Differential Equations**

## **How to Identify the Type of ODE from the Wording**

| Keyword | Type of ODE |
|--------|--------------|
| proportional to | separable / linear |
| mixing, inflow/outflow | linear first‑order |
| cooling, heating | Newton cooling (linear) |
| population, growth | logistic / separable |
| spring, mass, damping | 2nd order linear |
| circuits (RLC) | 2nd order linear |
| predator–prey | nonlinear system |
| chemical reaction | separable / system |

---

## **Full Modeling Example**

A tank contains 100 L of brine with 2 kg of salt. Brine with 0.1 kg/L enters at 5 L/min; mixture leaves at 5 L/min.

Let \(y(t)\) = salt (kg).

\[
y' = \text{rate in} - \text{rate out}
\]

\[
y' = 0.1(5) - \frac{y}{100}(5)
\]

\[
y' + \frac{1}{20}y = \frac{1}{2}
\]

Solve using integrating factor.

---

# **Appendices**

- Common integrating factors  
- Common annihilators  
- Substitution table  
- Quick algorithms  
- Glossary  

---

