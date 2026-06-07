# Laplace Transform 

> All functions are assumed real‑valued unless stated otherwise.

---

## 1.1 Integral transforms

### Definition 1.1 (Integral transform)

Let $f\colon [0,\infty)\to\mathbb{R}$ be a function and $K(s,t)$ a kernel.  
An **integral transform** of $f$ is a function $F$ of a new variable $s$ defined by

$$
F(s) = \mathcal{T}\{f\}(s) = \int_{0}^{\infty} K(s,t)\,f(t)\,dt,
$$

whenever the integral converges.

- **Example kernels:**
  - Fourier transform: $K(s,t) = e^{-ist}$
  - Laplace transform: $K(s,t) = e^{-st}$

---

## 1.2 Laplace transform and existence conditions

### Definition 1.2 (Laplace transform)

Let $f\colon [0,\infty)\to\mathbb{R}$. The **Laplace transform** of $f$ is

$$
\mathcal{L}\\{f(t)\\}(s) = F(s) = \int_{0}^{\infty} e^{-st} f(t)\,dt,
$$

for all $s\in\mathbb{R}$ (or $\mathbb{C}$) such that the integral converges.

### Definition 1.3 (Exponential order)

A function $f$ is said to be of **exponential order $\alpha$** if there exist constants $M>0$, $\alpha\in\mathbb{R}$, and $T\ge 0$ such that

$$
|f(t)| \le M e^{\alpha t} \quad \text{for all } t\ge T.
$$

### Theorem 1.4 (Existence of Laplace transform)

**Theorem.**  
If $f$ is piecewise continuous on every finite interval $[0,b]$ and of exponential order $\alpha$, then $\mathcal{L}\{f\}(s)$ exists for all $s > \alpha$.

**Proof.**  
For $t\ge T$,
$$
|e^{-st} f(t)| \le e^{-st} M e^{\alpha t} = M e^{-(s-\alpha)t}.
$$

If $s>\alpha$, then $s-\alpha>0$ and $\int_T^{\infty} |e^{-st} f(t)|\,dt \le M \int_T^{\infty} e^{-(s-\alpha)t}\,dt < \infty$.

On $[0,T]$, $f$ is piecewise continuous, so the integral is finite. Hence the Laplace transform converges for $s>\alpha$. ∎

---

## 1.3 Laplace transforms of elementary functions

Below, $s>0$ unless otherwise stated.

### Proposition 1.5 (Basic transforms)

1. **Constant:**
  
   $$
   \mathcal{L}\{1\}(s) = \int_0^\infty e^{-st}\,dt = \frac{1}{s}.
   $$

2. **Power:**
  
   $$
   \mathcal{L}\{t^n\}(s) = \frac{n!}{s^{n+1}},\quad n\in\mathbb{N}\cup\{0\}.
   $$

   **Proof sketch.**  
   Use
  
   $$
   \int_0^\infty t^n e^{-st}\,dt = \frac{n!}{s^{n+1}}
   $$
  
   via repeated integration by parts or the Gamma function. ∎

3. **Exponential:**
  
   $$
   \mathcal{L}\{e^{at}\}(s) = \int_0^\infty e^{-(s-a)t}\,dt = \frac{1}{s-a},\quad s>a.
   $$

4. **Sine and cosine:**
  
   $$
   \mathcal{L}\{\sin bt\}(s) = \frac{b}{s^2 + b^2},\quad
   \mathcal{L}\{\cos bt\}(s) = \frac{s}{s^2 + b^2}.
   $$

   **Proof sketch.**  
   Integrate by parts or use complex exponentials $e^{ibt}$. ∎

### Example 1.6

Compute $\mathcal{L}\{3t^2 - 5\}(s)$.

$$
\mathcal{L}\{3t^2 - 5\}(s) = 3\mathcal{L}\{t^2\}(s) - 5\mathcal{L}\{1\}(s)
= 3\cdot\frac{2!}{s^3} - 5\cdot\frac{1}{s}
= \frac{6}{s^3} - \frac{5}{s}.
$$

---

## 1.4 Fundamental theorems (properties)

### Theorem 1.7 (Linearity)

For functions $f,g$ with Laplace transforms and constants $a,b$,

$$
\mathcal{L}\{af(t) + bg(t)\}(s) = aF(s) + bG(s),
$$

where $F = \mathcal{L}\{f\}$, $G = \mathcal{L}\{g\}$.

**Proof.**  
Directly from the integral:

$$
\mathcal{L}\{af+bg\}(s) = \int_0^\infty e^{-st}(af(t)+bg(t))\,dt
= a\int_0^\infty e^{-st}f(t)\,dt + b\int_0^\infty e^{-st}g(t)\,dt.
$$

∎

---

### Theorem 1.8 (First shifting theorem – time domain)

If $\mathcal{L}\{f(t)\}(s) = F(s)$, then

$$
\mathcal{L}\{e^{at}f(t)\}(s) = F(s-a).
$$

**Proof.**  

$$
\mathcal{L}\{e^{at}f(t)\}(s)
= \int_0^\infty e^{-st} e^{at} f(t)\,dt
= \int_0^\infty e^{-(s-a)t} f(t)\,dt
= F(s-a).
$$

∎

---

### Theorem 1.9 (Differentiation in time domain)

If $f$ is differentiable and of exponential order, then

$$
\mathcal{L}\{f'(t)\}(s) = sF(s) - f(0),
$$

$$
\mathcal{L}\{f''(t)\}(s) = s^2 F(s) - sf(0) - f'(0),
$$

and in general

$$
\mathcal{L}\{f^{(n)}(t)\}(s) = s^n F(s) - s^{n-1}f(0) - \cdots - f^{(n-1)}(0).
$$

**Proof sketch.**  
Integrate by parts:

$$
\mathcal{L}\{f'(t)\}(s) = \int_0^\infty e^{-st} f'(t)\,dt
= \left[e^{-st}f(t)\right]_0^\infty + s\int_0^\infty e^{-st}f(t)\,dt.
$$

The boundary term at $\infty$ vanishes by exponential order; at $0$ it gives $-f(0)$. ∎

---

### Theorem 1.10 (Differentiation in s-domain)

If $\mathcal{L}\{f(t)\}(s) = F(s)$, then

$$
\mathcal{L}\{t f(t)\}(s) = -F'(s),
$$

and more generally

$$
\mathcal{L}\{t^n f(t)\}(s) = (-1)^n F^{(n)}(s).
$$

**Proof sketch.**  
Differentiate under the integral sign:

$$
F(s) = \int_0^\infty e^{-st} f(t)\,dt
\Rightarrow F'(s) = \int_0^\infty (-t)e^{-st} f(t)\,dt
= -\mathcal{L}\{t f(t)\}(s).
$$

∎

---

## 1.5 Applications of the Laplace transform

### Example 1.11 (Solving an IVP)

Solve

$$
y'' - 3y' + 2y = e^{2t},\quad y(0)=1,\quad y'(0)=0.
$$

1. Take Laplace transform of both sides:

   $$
   \mathcal{L}\{y''\} - 3\mathcal{L}\{y'\} + 2\mathcal{L}\{y\}
   = \mathcal{L}\{e^{2t}\}.
   $$

   Using Theorem 1.9 and $\mathcal{L}\{e^{2t}\} = \frac{1}{s-2}$:

   $$
   (s^2Y - sy(0) - y'(0)) - 3(sY - y(0)) + 2Y = \frac{1}{s-2}.
   $$

   Substitute $y(0)=1$, $y'(0)=0$:

   $$
   (s^2Y - s) - 3(sY - 1) + 2Y = \frac{1}{s-2}.
   $$

   $$
   s^2Y - s - 3sY + 3 + 2Y = \frac{1}{s-2}.
   $$

   $$
   (s^2 - 3s + 2)Y + (-s+3) = \frac{1}{s-2}.
   $$

   $$
   (s-1)(s-2)Y = \frac{1}{s-2} + s - 3.
   $$

2. Solve for $Y(s)$:

   $$
   Y(s) = \frac{1}{(s-1)(s-2)}\left(\frac{1}{s-2} + s - 3\right).
   $$

   Simplify and decompose en fracciones parciales (omitted details for brevity), then apply inverse Laplace to get $y(t)$.

This illustrates the workflow: transform → algebra → inverse transform.

---

## 1.6 Laplace transform of step, periodic, and impulse functions

### 1.6.1 Unit step (Heaviside) function

### Definition 1.12 (Unit step)

For $a\ge 0$,

$$
u(t-a) =
\begin{cases}
0, & 0\le t < a,\\
1, & t\ge a.
\end{cases}
$$

### Proposition 1.13

$$
\mathcal{L}\{u(t-a)\}(s) = \frac{e^{-as}}{s}.
$$

**Proof.**  

$$
\mathcal{L}\{u(t-a)\}(s) = \int_0^\infty e^{-st}u(t-a)\,dt
= \int_a^\infty e^{-st}\,dt
= \left[-\frac{1}{s}e^{-st}\right]_a^\infty
= \frac{e^{-as}}{s}.
$$

∎

### Shifted functions

If $f(t)$ is given and $g(t) = u(t-a)f(t-a)$, then

$$
\mathcal{L}\{g(t)\}(s) = e^{-as}F(s),
$$

where $F(s) = \mathcal{L}\{f(t)\}(s)$.

---

### 1.6.2 Periodic functions

Let $f$ be periodic with period $T>0$: $f(t+T)=f(t)$.

### Theorem 1.14 (Laplace transform of periodic functions)

If $f$ is piecewise continuous on $[0,T]$ and of exponential order, then

$$
\mathcal{L}\{f(t)\}(s) = \frac{1}{1-e^{-sT}} \int_0^T e^{-st} f(t)\,dt.
$$

**Proof sketch.**  
Write the integral as a sum over periods:

$$
\int_0^\infty e^{-st}f(t)\,dt = \sum_{n=0}^\infty \int_{nT}^{(n+1)T} e^{-st}f(t)\,dt.
$$

Use periodicity $f(t)=f(t-nT)$ and factor out $e^{-nsT}$. The sum becomes a geometric series. ∎

---

### 1.6.3 Impulse (Dirac delta)

Formally, the **Dirac delta** $\delta(t-a)$ satisfies

$$
\int_{-\infty}^{\infty} \delta(t-a)\varphi(t)\,dt = \varphi(a)
$$

for test functions $\varphi$.

### Proposition 1.15

$$
\mathcal{L}\{\delta(t-a)\}(s) = e^{-as}.
$$

**Heuristic proof.**  

$$
\mathcal{L}\{\delta(t-a)\}(s) = \int_0^\infty e^{-st}\delta(t-a)\,dt = e^{-as}.
$$

∎

---

## 1.7 Inverse Laplace transform – definition and basic properties

### Definition 1.16 (Inverse Laplace transform)

If $F(s)$ is the Laplace transform of $f(t)$, we write

$$
f(t) = \mathcal{L}^{-1}\{F(s)\}(t).
$$

Formally, one can define it via the Bromwich integral, but in practice we use tables and algebraic manipulation.

### Proposition 1.17 (Linearity)

If $F = aF_1 + bF_2$, then

$$
\mathcal{L}^{-1}\{F\} = a\mathcal{L}^{-1}\{F_1\} + b\mathcal{L}^{-1}\{F_2\}.
$$

---

### Example 1.18

Find $f(t) = \mathcal{L}^{-1}\left\{\dfrac{2s}{s^2+4}\right\}$.

We know $\mathcal{L}\{\cos(2t)\}(s) = \dfrac{s}{s^2+4}$.  
Thus

$$
\mathcal{L}^{-1}\left\{\frac{2s}{s^2+4}\right\} = 2\cos(2t).
$$

---

## 1.8 Convolution theorem

### Definition 1.19 (Convolution)

For functions $f,g$ on $[0,\infty)$, their **convolution** is

$$
(f*g)(t) = \int_0^t f(\tau)g(t-\tau)\,d\tau.
$$

### Theorem 1.20 (Convolution theorem)

If $F(s) = \mathcal{L}\\{f(t)\\}(s)$ and $G(s) = \mathcal{L}\\{g(t)\\}(s)$, then

$$
\mathcal{L}\{(f*g)(t)\}(s) = F(s)G(s).
$$

**Proof.**  

$$
\mathcal{L}\{f*g\}(s)
= \int_0^\infty e^{-st}\left(\int_0^t f(\tau)g(t-\tau)\,d\tau\right)dt.
$$

Change order of integration (Fubini) and substitute $u = t-\tau$:

$$
= \int_0^\infty f(\tau)\left(\int_\tau^\infty e^{-st}g(t-\tau)\,dt\right)d\tau
= \int_0^\infty f(\tau)e^{-s\tau}\left(\int_0^\infty e^{-su}g(u)\,du\right)d\tau
= F(s)G(s).
$$

∎

### Example 1.21

Compute $\mathcal{L}^{-1}\left\{\dfrac{1}{(s+1)^2}\right\}$.

We know $\mathcal{L}\{e^{-t}\}(s) = \dfrac{1}{s+1}$.  
Thus

$$
\frac{1}{(s+1)^2} = \frac{1}{s+1}\cdot\frac{1}{s+1}
\Rightarrow \mathcal{L}^{-1}\left\{\frac{1}{(s+1)^2}\right\} = (e^{-t}*e^{-t})(t).
$$

Compute the convolution:

$$
(e^{-t}*e^{-t})(t) = \int_0^t e^{-\tau}e^{-(t-\tau)}\,d\tau
= e^{-t}\int_0^t 1\,d\tau
= te^{-t}.
$$

So

$$
\mathcal{L}^{-1}\left\{\frac{1}{(s+1)^2}\right\} = te^{-t}.
$$

---

## 1.9 Solving ODEs with Laplace transforms

### General scheme

For a linear ODE with constant coefficients and initial conditions:

$$
a_n y^{(n)} + \cdots + a_1 y' + a_0 y = g(t),\quad y^{(k)}(0) = y_k,
$$

we:

1. Apply $\mathcal{L}$ to both sides.
2. Use Theorem 1.9 to express $\mathcal{L}\{y^{(k)}\}$ in terms of $Y(s)$ and initial values.
3. Solve the resulting algebraic equation for $Y(s)$.
4. Compute $y(t) = \mathcal{L}^{-1}\{Y(s)\}(t)$.

---

### Example 1.22 (Full worked IVP)

Solve

$$
y'' + y = \sin t,\quad y(0)=0,\quad y'(0)=1.
$$

1. Take Laplace transform:

   $$
   \mathcal{L}\{y''\} + \mathcal{L}\{y\} = \mathcal{L}\{\sin t\}.
   $$

   Using Theorem 1.9 and $\mathcal{L}\{\sin t\} = \dfrac{1}{s^2+1}$:

   $$
   (s^2Y - sy(0) - y'(0)) + Y = \frac{1}{s^2+1}.
   $$

   Substitute $y(0)=0$, $y'(0)=1$:

   $$
   s^2Y - 1 + Y = \frac{1}{s^2+1}.
   $$

   $$
   (s^2+1)Y = 1 + \frac{1}{s^2+1}.
   $$

   $$
   Y(s) = \frac{1}{s^2+1} + \frac{1}{(s^2+1)^2}.
   $$

2. Inverse Laplace term by term:
   - $\mathcal{L}^{-1}\left\{\dfrac{1}{s^2+1}\right\} = \sin t$.
   - $\mathcal{L}^{-1}\left\{\dfrac{1}{(s^2+1)^2}\right\} = \dfrac{1}{2}\sin t - \dfrac{1}{2}t\cos t$ (can be derived via convolution or tables).

   So

   $$
   y(t) = \sin t + \left(\frac{1}{2}\sin t - \frac{1}{2}t\cos t\right)
   = \frac{3}{2}\sin t - \frac{1}{2}t\cos t.
   $$

---
