
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

For the IVP (Initial Value Problem):

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

$$
\frac{dy}{dx} = g(x)h(y)
$$

## **Algorithm**
1. Rewrite:  
   $\frac{1}{h(y)}dy = g(x)dx$
2. Integrate both sides.
3. Solve for $y$ if possible.
4. Apply initial condition.

## **Example**
$$
y' = xy
$$

$$
\frac{1}{y}dy = xdx
$$

$$
\ln|y| = \frac{x^2}{2} + C
$$

$$
y = Ce^{x^2/2}
$$

---

# **2. Exact Differential Equations**

## **Definition**
A DE of the form:

$$
M(x,y)dx + N(x,y)dy = 0
$$

is **exact** if:

$$
\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}
$$

## **Algorithm**
1. Check exactness.  
2. Integrate $M$ w.r.t. $x$.  
3. Differentiate result w.r.t. $y and match with $N$.
4. Solve for constant.

## **Example**
$$
(2xy + 3)dx + (x^2 + 4y)dy = 0
$$

Check exactness:

$$
M_y = 2x, \quad N_x = 2x
$$

Integrate:

$$
\int (2xy + 3)dx = x^2y + 3x + h(y)
$$

Differentiate w.r.t. $y$:

$$
x^2 + h'(y) = x^2 + 4y
$$

$$
h'(y)=4y \Rightarrow h(y)=2y^2
$$

Solution:

$$
x^2y + 3x + 2y^2 = C
$$

---

# **3. Linear First‑Order Equations**

General form:

$$
y' + P(x)y = Q(x)
$$

## **Integrating Factor**
$$
\mu(x)=e^{\int P(x)dx}
$$

## **Algorithm**
1. Compute $\mu(x)$.
2. Multiply entire equation.  
3. Recognize derivative:  
   $(\mu y)' = \mu Q$
4. Integrate.  
5. Solve for $y$.

## **Example**
$$
y' + 2y = e^{-x}
$$

$$
\mu = e^{2x}
$$

$$
(e^{2x}y)' = e^{x}
$$

$$
e^{2x}y = e^{x} + C
$$

$$
y = e^{-x} + Ce^{-2x}
$$

---

# **4. Substitution Methods**

## **4.1 Homogeneous Equations**

A first‑order differential equation of the form  
$$
y' = F\left(\frac{y}{x}\right)
$$  
is called **homogeneous** because the right‑hand side depends only on the ratio $y/x$.  
Such equations can be solved using the substitution:

$$
y = v x, \qquad y' = v + x v'.
$$

---

## ## **Algorithm**

### **1. Verify homogeneity**
Check that the differential equation can be written as:
$$
y' = F\left(\frac{y}{x}\right).
$$

If the right‑hand side depends only on $y/x$, the equation is homogeneous.

---

### **2. Apply the substitution**
Let:
$$
y = vx,
$$
where $v = v(x)$ is a function of $x$.  
Differentiate using the product rule:

$$
y' = v + x v'.
$$

Substitute both expressions into the original differential equation:

$$
v + x v' = F(v).
$$

---

### **3. Isolate $v'$**
Rearrange the equation to solve for $v'$:

$$
x v' = F(v) - v,
$$

$$
v' = \frac{F(v) - v}{x}.
$$

This is now a **separable differential equation**.

---

### **4. Separate variables and integrate**
Rewrite:

$$
\frac{dv}{F(v) - v} = \frac{dx}{x}.
$$

Integrate both sides:

$$
\int \frac{dv}{F(v) - v} = \int \frac{dx}{x}.
$$

The right-hand side integrates to $\ln|x| + C$.  
The left-hand side depends on the specific form of $F(v)$.

---

### **5. Substitute back $v = y/x$**
After integrating, replace:

$$
v = \frac{y}{x}.
$$

This gives an implicit solution of the form:

$$
C = G(x, y),
$$

where $G$ comes from the integration result.

---

### **6. (Optional) Solve explicitly for $y$**
If possible, isolate $y$ to obtain an explicit solution  
$$
y = y(x).
$$

If not, the implicit form $C = G(x,y)$ is the final solution.

---

# ## **Summary**
The method transforms a homogeneous differential equation into a separable one using the substitution $y = vx$. After integrating and substituting back, the constant of integration yields the implicit solution.

---


## **4.2 Bernoulli Equation**
$$
y' + P(x)y = Q(x)y^n
$$

Substitute:

$$
v = y^{1-n}
$$

## **4.3 Riccati (special case)**
$$
y' = a(x)y^2 + b(x)y + c(x)
$$

If one solution is known, reduce to linear.


### 📘 **Bernoulli & Riccati Differential Equations — Algorithms (Markdown)**

### # **1. Bernoulli Differential Equation**

A Bernoulli equation has the form:

$$
y' + P(x)y = Q(x)y^n, \qquad n \neq 0,1.
$$

It is nonlinear, but it becomes linear after a substitution.

---

### **Algorithm**

#### **1. Identify the Bernoulli form**
Verify the equation matches:

$$
y' + P(x)y = Q(x)y^n.
$$

#### **2. Apply the substitution**
Let:

$$
v = y^{1-n}.
$$

Differentiate:

$$
v' = (1-n)y^{-n}y'.
$$

#### **3. Substitute into the original equation**
Replace $y$ and simplify to obtain a **linear ODE in $v$**:

$$
v' + (1-n)P(x)v = (1-n)Q(x).
$$

#### **4. Solve the linear ODE**
Use the integrating factor:

$$
\mu(x) = e^{\int (1-n)P(x)\,dx}.
$$

Solve for $v(x)$.

#### **5. Substitute back**
$$
y = v^{\frac{1}{1-n}}.
$$

This gives the explicit or implicit solution.

---

## # **2. Riccati Differential Equation**

A Riccati equation has the form:

$$
y' = a(x)y^2 + b(x)y + c(x).
$$

It is nonlinear and **cannot be linearized directly**.  
However, if a *particular solution* $y_p(x)$ is known, the equation becomes solvable.

---

### **Algorithm**

#### **1. Identify the Riccati form**
Check that the ODE matches:

$$
y' = a(x)y^2 + b(x)y + c(x).
$$

#### **2. Assume a known particular solution**
Let $y_p(x)$ satisfy the equation.

#### **3. Apply the substitution**
Let:

$$
y = y_p + \frac{1}{v}.
$$

Differentiate:

$$
y' = y_p' - \frac{v'}{v^2}.
$$

#### **4. Substitute into the Riccati equation**
After simplification, the nonlinear terms cancel and you obtain a **linear ODE in $v$**:

$$
v' + (2a(x)y_p(x) + b(x))v = -a(x).
$$

#### **5. Solve the linear ODE**
Use the integrating factor:

$$
\mu(x) = e^{\int (2a y_p + b)\,dx}.
$$

Solve for $v(x)$.

#### **6. Substitute back**
$$
y = y_p + \frac{1}{v}.
$$

This yields the general solution.

---

# ## **3. Relationship Between Bernoulli and Riccati**

| Feature | Bernoulli | Riccati |
|--------|-----------|---------|
| General form | $y' + P y = Q y^n$ | $y' = a y^2 + b y + c$ |
| Nonlinearity | Power $y^n$ | Quadratic $y^2$ |
| Substitution | $v = y^{1-n}$ | $y = y_p + 1/v$ |
| Requires particular solution? | ❌ No | ✅ Yes |
| Reduces to linear ODE? | Always | Only after knowing $y_p$ |
| Is Bernoulli a special case of Riccati? | **Yes**, when $a(x)=Q(x)$, $b(x)=P(x)$, $c(x)=0$, and $n=2$. | Riccati is the general case |

---

## ## **Conclusion**

Yes, they are related — **Bernoulli is a special, simpler case of Riccati** — but the solution strategies differ enough that having **two separate Markdown sections** in your repo is absolutely worth it.

## **4.4 Clairaut**
$$
y = xy' + f(y')
$$

Solution:  
General: $y = Cx + f(C)$  
Singular: envelope.

---

# **Higher‑Order Linear Differential Equations**

---

# **5. Constant Coefficients**

$$
a_n y^{(n)} + \cdots + a_1 y' + a_0 y = 0
$$

Characteristic equation:

$$
ar^n + \cdots + a_0 = 0
$$

## **Cases**
- Real distinct roots  
- Repeated roots  
- Complex roots

A linear homogeneous differential equation of order $n$ with constant coefficients has the form:

$$
a_n y^{(n)} + a_{n-1} y^{(n-1)} + \cdots + a_1 y' + a_0 y = 0
$$

To solve it, we associate the **characteristic equation**:

$$
a_n r^n + a_{n-1} r^{n-1} + \cdots + a_1 r + a_0 = 0
$$

The structure of the solution depends entirely on the roots of this polynomial.

---

## **1. Distinct Real Roots**

If the characteristic equation has distinct real roots:

$$
r_1, r_2, \dots, r_k
$$

then each root produces a solution of the form:

$$
y_i(x) = e^{r_i x}
$$

The general solution is:

$$
y(x) = C_1 e^{r_1 x} + C_2 e^{r_2 x} + \cdots + C_k e^{r_k x}
$$

---

## **2. Repeated Real Roots**

If a real root $r$ has multiplicity $m$, then the linearly independent solutions are:

$$
e^{rx},\; x e^{rx},\; x^2 e^{rx},\; \dots,\; x^{m-1} e^{rx}
$$

Thus, repeated roots introduce polynomial factors.

---

## **3. Complex Roots**

If the characteristic equation has a complex root:

$$
r = \alpha + i\beta,\quad \beta \neq 0
$$

its conjugate $\alpha - i\beta$ also appears.  
These produce the real solutions:

$$
y_1(x) = e^{\alpha x} \cos(\beta x), \qquad
y_2(x) = e^{\alpha x} \sin(\beta x)
$$

If the complex root has multiplicity \(m\), then each solution is multiplied by powers of \(x\):

$$
x^k e^{\alpha x} \cos(\beta x),\quad
x^k e^{\alpha x} \sin(\beta x),\quad k = 0,1,\dots,m-1
$$

---

## **4. Summary of All Possible Solution Forms**

Every solution of a homogeneous linear differential equation with constant coefficients is a **linear combination** of functions of the form:

- **$x^k e^{rx}$** for real roots $r$
- **$x^k e^{\alpha x} \sin(\beta x)$** for complex roots $\alpha \pm i\beta$

where $k$ runs from $0$ to the multiplicity minus one.

As a special case:

- If $r = 0$, then $e^{0x} = 1$, so constants and polynomials appear.


## **Example**
$$
y'' - 3y' + 2y = 0
$$

$$
r^2 - 3r + 2 = 0
$$

$$
r=1,2
$$

$$
y = C_1 e^x + C_2 e^{2x}
$$

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

# **What “Plug In and Solve Coefficients” Really Means**

In the **Method of Undetermined Coefficients**, step 3 means:

> **Take your guessed particular solution $y_p$, compute its derivatives, substitute them into the differential equation, and solve for the unknown constants by matching coefficients.**

En otras palabras:  
**metes tu “guess” en la ecuación y resuelves un sistema de ecuaciones para los parámetros desconocidos.**

---

# **Full Algorithm (Clarified)**

## **1. Solve the homogeneous equation**
Find the complementary solution $y_h$ using the characteristic equation.

---

## **2. Guess the form of the particular solution**
Based on the RHS $g(x)$:

- If $g(x)$ is a polynomial → guess a polynomial  
- If $g(x)$ is $e^{ax}$ → guess $A e^{ax}$
- If $g(x)$ is $\sin bx$ or $\cos bx$ → guess $A\cos bx + B\sin bx$
- If it’s a product → multiply the guesses  
- If the guess overlaps with $y_h$ → multiply by $x^k$

---

## **3. Plug in and solve coefficients**
This is the step you asked about.  
It means:

### **Step 3.1 — Compute derivatives of your guess**
Example guess:
$$
y_p = Ax + B
$$

Compute:
$$
y_p',\; y_p'',\; \dots
$$

---

### **Step 3.2 — Substitute into the differential equation**
Insert $y_p$, $y_p'$, $y_p''$, etc. into:

$$
a_n y^{(n)} + \cdots + a_1 y' + a_0 y = g(x)
$$

---

### **Step 3.3 — Collect like terms**
Group terms by powers of $x$, exponentials, or trig functions.

---

### **Step 3.4 — Match coefficients with the RHS**
This produces a **system of linear equations** for the unknown constants $A, B, C, \dots$.

Solve it.

That’s literally what “plug in and solve coefficients” means.

---

## **4. Add the solutions**
$$
y = y_h + y_p
$$

---

# **Mini‑Example (Super Clear)**

Solve:

$$
y'' - 3y' + 2y = 4e^{x}
$$

### **Step 1 — Homogeneous**
Roots: $(1, 2)$

$$
y_h = C_1 e^x + C_2 e^{2x}
$$

### **Step 2 — Guess**
RHS is $4e^x$.  
But $e^x$ **is already in** $y_h$.  
So multiply by $x$:

$$
y_p = A x e^x
$$

### **Step 3 — Plug in and solve coefficients**

Compute derivatives:

$$
y_p = A x e^x
$$

$$
y_p' = A e^x + A x e^x
$$

$$
y_p'' = 2A e^x + A x e^x
$$

Substitute into the DE:

$$
(2A e^x + A x e^x) - 3(A e^x + A x e^x) + 2(A x e^x) = 4e^x
$$

Simplify:

$$
(2A - 3A)e^x + (A - 3A + 2A)x e^x = 4e^x
$$

$$
(-A)e^x + 0 = 4e^x
$$

Match coefficients:

$$
-A = 4 \Rightarrow A = -4
$$

So:

$$
y_p = -4x e^x
$$

### **Step 4 — Final solution**

$$
y = C_1 e^x + C_2 e^{2x} - 4x e^x
$$

---

## **6.2 Method of the Annihilator**

### **1. Introduction**

The *Annihilator Method* is a systematic procedure for solving linear nonhomogeneous differential equations of the form  

$$
L[y] = f(x),
$$

where $L$ is a linear differential operator with constant coefficients.

The key idea is to apply another differential operator $A$, called an **annihilator**, such that  

$$
A[f(x)] = 0.
$$

Once the right-hand side is annihilated, the equation becomes a **higher‑order homogeneous ODE**, which can be solved using standard techniques.

---

## **2. What Is an Annihilator?**

An **annihilator** is a differential operator $A(D)$ such that  

$$
A(D)\, f(x) = 0.
$$

Examples:

| Function $f(x)$ | Annihilator $A(D)$ |
|-------------------|-----------------------|
| $e^{ax}$ | $(D - a)$ |
| $(x^n e^{ax})$ | $((D - a)^{n+1})$ |
| $(\sin bx, \cos bx)$ | $(D^2 + b^2)$ |
| Polynomials of degree $n$ | $(D^{n+1})$ |
| $(e^{ax}\sin bx, e^{ax}\cos bx)$ | $((D - a)^2 + b^2)$ |

---

## **3. General Strategy (Algorithm)**

Given a linear ODE:

$$
L[y] = f(x),
$$

where $L$ has constant coefficients.

### **Step 1 — Identify an annihilator for $f(x)$**  
Find an operator $A$ such that:

$$
A[f(x)] = 0.
$$

### **Step 2 — Apply the annihilator to both sides**

$$
A[L[y]] = A[f(x)] = 0.
$$

This produces a **higher‑order homogeneous equation**:

$$
(AL)[y] = 0.
$$

### **Step 3 — Solve the homogeneous equation**
Find the general solution of:

$$
(AL)[y] = 0.
$$

### **Step 4 — Extract the complementary and particular parts**
The solution of the original ODE is:

$$
y = y_c + y_p,
$$

where:

- $y_c$ comes from the original homogeneous equation $L[y]=0$,
- $y_p$ is selected from the additional solutions introduced by the annihilator.

### **Step 5 — Use initial conditions (if any)**  
Solve for constants.

---

## **4. Example 1 — Basic Case**

Solve:

$$
y'' - y = e^{x}.
$$

### **Step 1 — Identify an annihilator**
For $(f(x) = e^{x})$, the annihilator is:

$$
A = D - 1.
$$

### **Step 2 — Apply the annihilator**
$$
(D - 1)(y'' - y) = 0.
$$

### **Step 3 — Solve the homogeneous equation**
Characteristic equation:
$$
(D - 1)(D^2 - 1) = 0.
$$

Roots:

$$
r = 1,\quad r = 1,\quad r = -1.
$$

General solution of annihilated equation:

$$
y = C_1 e^{x} + C_2 x e^{x} + C_3 e^{-x}.
$$

### **Step 4 — Extract the particular solution**
Original homogeneous equation:

$$
y'' - y = 0 \quad\Rightarrow\quad y_c = C_1 e^{x} + C_3 e^{-x}.
$$

The new term $x e^{x}$ is the particular solution:

$$
y_p = C_2 x e^{x}.
$$

Thus:

$$
y = C_1 e^{x} + C_3 e^{-x} + C_2 x e^{x}.
$$

---

## **5. Example 2 — Trigonometric Forcing**

Solve:

$$
y'' + 4y = \cos(2x).
$$

### **Step 1 — Annihilator**

$$
A = D^2 + 4.
$$

### **Step 2 — Apply the annihilator**

$$
(D^2 + 4)(y'' + 4y) = 0.
$$

### **Step 3 — Solve homogeneous equation**
Characteristic equation:

$$
(D^2 + 4)^2 = 0.
$$

Roots:

$$
r = \pm 2i \quad \text{(multiplicity 2)}.
$$

General solution:

$$
y = C_1\cos 2x + C_2\sin 2x + C_3 x\cos 2x + C_4 x\sin 2x.
$$

### **Step 4 — Extract particular solution**
Original homogeneous solution:

$$
y_c = C_1\cos 2x + C_2\sin 2x.
$$

New terms:
$$
y_p = C_3 x\cos 2x + C_4 x\sin 2x.
$$

---

## **6. Example 3 — Polynomial Forcing**

Solve:

$$
y'' - 3y' + 2y = x^2.
$$

### **Step 1 — Annihilator**
Polynomial of degree 2 → annihilator:

$$
A = D^3.
$$

### **Step 2 — Apply annihilator**

$$
D^3(y'' - 3y' + 2y) = 0.
$$

### **Step 3 — Solve homogeneous equation**
Characteristic equation:

$$
D^3(D - 1)(D - 2) = 0.
$$

Roots:

$$
r = 0,0,0,1,2.
$$

General solution:

$$
y = C_1 + C_2 x + C_3 x^2 + C_4 e^{x} + C_5 e^{2x}.
$$

### **Step 4 — Extract particular solution**
Original homogeneous:

$$
y_c = C_4 e^{x} + C_5 e^{2x}.
$$

Particular solution:

$$
y_p = C_1 + C_2 x + C_3 x^2.
$$

---

### **7. Summary Table of Common Annihilators**

| Forcing Term $f(x)$ | Annihilator $A(D)$ |
|------------------------|-----------------------|
| $e^{ax}$ | $D - a$ |
| $x^n e^{ax}$ | $(D - a)^{n+1}$ |
| $\sin bx, \cos bx$ | $D^2 + b^2$ |
| $x^n$ | $D^{n+1}$ |
| $e^{ax}\sin bx$ | $(D - a)^2 + b^2$ |

---

### **8. When to Use the Annihilator Method**

Use it when:

- The forcing term is a combination of exponentials, polynomials, and trigonometric functions.
- The differential equation has **constant coefficients**.
- You want a systematic alternative to undetermined coefficients.

Avoid it when:

- Coefficients are variable.
- Forcing term is not annihilable by a finite‑order operator (e.g., $e^{x^2}$, $\ln x$.

---

## **6.3 Variation of Parameters**

Consider the second–order linear ODE in standard form:

$$
y'' + p(x)y' + q(x)y = g(x)
$$

Let $y_1(x)$ and $y_2(x)$ be two linearly independent solutions of the homogeneous equation:


$$
y'' + p(x)y' + q(x)y = 0
$$

Then a particular solution is obtained by the following algorithm.

---

### **Algorithm (Universal Version)**

1. **Write the equation in standard form**

Ensure the ODE is written as: 

$$
   y'' + p(x)y' + q(x)y = g(x)
$$

2. **Find the fundamental solutions**

Solve the homogeneous equation: 

$$
   y'' + p(x)y' + q(x)y = 0
$$

Obtain two independent solutions:

$$
   y_1(x),\quad y_2(x)
$$


3. **Compute the Wronskian** 

$$
   W(x) =
   \begin{vmatrix}
   y_1 & y_2 \\
   y_1' & y_2'
   \end{vmatrix}
   = y_1 y_2' - y_2 y_1'
$$

4. **Compute the auxiliary functions**

$$
   u_1'(x) = -\,\frac{y_2(x)\,g(x)}{W(x)}
$$ 

$$
   u_2'(x) = \frac{y_1(x)\,g(x)}{W(x)}
$$

5. **Integrate**   

$$
   u_1(x) = \int u_1'(x)\,dx,\qquad
   u_2(x) = \int u_2'(x)\,dx
$$

(Constants of integration are omitted because they are absorbed into the homogeneous solution.)

6. **Construct the particular solution**

$$
y_p(x) = u_1(x)\,y_1(x) + u_2(x)\,y_2(x)
$$

7. **Write the general solution** 

$$
y(x) = C_1 y_1(x) + C_2 y_2(x) + y_p(x)
$$

---

### **Notes**

- This algorithm works for *any* linear ODE with continuous coefficients.
- If $p(x)=0$, the formulas reduce to the simpler version:

$$
y_p = -y_1\int \frac{y_2 g}{W}dx + y_2\int \frac{y_1 g}{W}dx
$$

- Integrals may not always have elementary closed forms; the method is still valid.


---

# **7. Cauchy–Euler Equation**

$$
x^n y^{(n)} + \cdots + a_1 xy' + a_0 y = g(x)
$$

Try:

$$
y = x^r
$$

## **1. Problem Form**

A *Cauchy–Euler* (or *equidimensional*) differential equation of order $n$ has the structure:

$$
x^n y^{(n)} + a_{n-1} x^{n-1} y^{(n-1)} + \cdots + a_1 x y' + a_0 y = g(x)
$$

When $g(x)=0$, the equation is **homogeneous**.

---

## **2. Key Idea: Try a Power‑Law Solution**

Because the equation is *equidimensional*, we try:

$$
y = x^r
$$

Then:

$$
y' = r x^{r-1},\quad
y'' = r(r-1)x^{r-2},\quad
\ldots,\quad
y^{(n)} = r(r-1)\cdots(r-n+1)x^{r-n}
$$

Substituting into the differential equation will factor out $x^r$, leaving an algebraic equation in $r$.

---

## **3. Algorithm (Step‑by‑Step)**

### **Step 1 — Assume a trial solution**

$$
y = x^r
$$

### **Step 2 — Compute derivatives**
Use:

$$
y^{(k)} = r(r-1)\cdots(r-k+1)x^{r-k}
$$

### **Step 3 — Substitute into the differential equation**
Every term becomes:

$$
x^n y^{(n)} = x^n \cdot r(r-1)\cdots(r-n+1)x^{r-n}
= r(r-1)\cdots(r-n+1)x^r
$$

All terms will contain $x^r$. Factor it out.

### **Step 4 — Obtain the *indicial equation***
The remaining algebraic equation in $r$ is:

$$
P(r) = 0
$$

This is the **characteristic equation** of the Cauchy–Euler problem.

### **Step 5 — Solve the characteristic equation**
Depending on the roots:

- **Distinct real roots** $r_1, r_2, \ldots, r_n$
  $$
  y = C_1 x^{r_1} + \cdots + C_n x^{r_n}
  $$

- **Repeated root** $r$ of multiplicity $m$
  $$
  y = x^r \left(C_1 + C_2 \ln x + \cdots + C_m (\ln x)^{m-1}\right)
  $$

- **Complex roots** $r = \alpha \pm i\beta$
  $$
  y = x^\alpha \left(C_1 \cos(\beta \ln x) + C_2 \sin(\beta \ln x)\right)
  $$

### **Step 6 — (If non‑homogeneous) Propose a particular solution**
Use:
- **Method of Undetermined Coefficients** (if $g(x)$ is a power, log, or combination)
- **Variation of Parameters** (general case)

---

## **4. Summary Table**

| Case | Roots | General Solution |
|------|-------|------------------|
| Distinct real | $r_1, r_2, \ldots$ | $\sum C_i x^{r_i}$ |
| Repeated root | $r$ mult. $m$ | $x^r (C_1 + C_2 \ln x + \cdots)$ |
| Complex | $\alpha \pm i\beta$ | $x^\alpha(\cos(\beta\ln x), \sin(\beta\ln x))$ |

---

## **5. Example (Homogeneous)**

Solve:

$$
x^2 y'' - 3x y' + 4y = 0
$$

### **Step 1 — Try $y = x^r$**

$$
y' = r x^{r-1},\quad y'' = r(r-1)x^{r-2}
$$

### **Step 2 — Substitute**

$$
x^2 r(r-1)x^{r-2} - 3x r x^{r-1} + 4x^r = 0
$$

Factor $x^r$:

$$
x^r \left[r(r-1) - 3r + 4\right] = 0
$$

### **Step 3 — Indicial equation**

$$
r(r-1) - 3r + 4 = 0
$$

$$
r^2 - r - 3r + 4 = 0
$$

$$
r^2 - 4r + 4 = 0
$$

$$
(r-2)^2 = 0
$$

Repeated root $r = 2$.

### **Step 4 — General solution**

$$
y = C_1 x^2 + C_2 x^2 \ln x
$$

---

## **6. Example (Complex Roots)**

Solve:

$$
x^2 y'' + xy' + y = 0
$$

Indicial equation:

$$
r(r-1) + r + 1 = 0
$$

$$
r^2 + 1 = 0
$$

$$
r = \pm i
$$

Solution:

$$
y = C_1 \cos(\ln x) + C_2 \sin(\ln x)
$$

---

## **7. Final Notes**

- Cauchy–Euler equations are solved **exactly like constant‑coefficient equations**, but with the substitution $y = x^r$ instead of $y = e^{rx}$.
- The presence of **$\ln x$** in repeated roots is the analogue of multiplying by **$x$** in constant‑coefficient equations.
- Complex roots produce oscillations in **$\ln x$**, not in $x$.

---

# **Nonlinear Differential Equations**

Autonomous:

$$
y' = f(y)
$$

Phase line analysis.

Example:

$$
y' = y(1-y)
$$

---

# **Systems of Differential Equations**

---

# **Linear Systems**

$$
\mathbf{x}' = A\mathbf{x}
$$

Solution via eigenvalues/eigenvectors.

---

# **Nonlinear Systems**

Linearize using Jacobian.

---

# **Series Solutions**

---

# **Power Series Method**

Assume:

$$
y = \sum_{n=0}^\infty a_n x^n
$$

Find recurrence.

---

# **Frobenius Method**

$$
y = x^r \sum_{n=0}^\infty a_n x^n
$$

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

Let $y(t)$ = salt (kg).

$$
y' = \text{rate in} - \text{rate out}
$$

$$
y' = 0.1(5) - \frac{y}{100}(5)
$$

$$
y' + \frac{1}{20}y = \frac{1}{2}
$$

Solve using integrating factor.

---

# **Appendices**

- Common integrating factors  
- Common annihilators  
- Substitution table  
- Quick algorithms  
- Glossary  

---

