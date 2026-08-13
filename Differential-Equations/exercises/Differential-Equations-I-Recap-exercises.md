
---

# **Differential Equations – Extraordinary Exam Level Exercises**  
*Exercises organized by chapter, aligned with the Extended Theorem Compendium.*

---

# **Table of Contents**

-  [Introduction](#introduction)
-  [Classification and Basic Concepts](#classification-and-basic-concepts)
-  [First-Order Differential Equations](#firstorder-differential-equations)
    -  [Separable](#separable-equations)
    -  [Exact Equations](#exact-equations)
    -  [Linear](#linear-firstorder-equations)
    -  [substitution](#substitution-methods)
    -  [Homogeneous](#homogeneous)
    -  [Bernoulli](#bernoulli)
    -  [Riccati](#riccati-special-case)
    -  [Clairaut](#clairaut)
-  [Higher-Order Linear Differential Equations](#higherorder-linear-differential-equations)
    - [Homogeneous with Constant Coefficients](#homogeneous-with-constant-coefficients)
    - [Non-Homogeneous Equations](#nonhomogeneous-equations)
        - [Undetermined Coefficients](#undetermined-coefficients)
        - [Annihilator Method](#annihilator-method)
        - [Variation of Parameters](#variation-of-parameters)
        - [Cauchy-Euler](#cauchyeuler)
-  [Non-Linear Differential Equations](#nonlinear-differential-equations)
-  [Systems of Differential Equations](#systems-of-differential-equations)
    - [Linear Systems](#linear-systems)
    - [Non-Linear Systems](#nonlinear-systems)
-  [Series Solutions](#series-solutions)
    - [Power Series](#power-series)
    - [Frobenius Method](#frobenius-method)
-  [Modeling with Differential Equations](#modeling-with-differential-equations)

# **Introduction**

## **Classification and Basic Concepts**

---

Classify each differential equation as linear/nonlinear, autonomous/non‑autonomous, and determine its order:  

**a)** $y'' + y' + y = \sin(x)$ → Linear, non-autonomous, order 2
**b)** $y' = y^2 - 3y + 2$ → Non-Linear, autonomous, first order 
**c)** $x^2 y'' + xy' - y = 0$ → Linear, non-autonomous, order 2
**d)** $y' + \sqrt{xy} = 0$ → Non-linear, autonomous, first order

---

---

Determine whether the following equations are exact, linear, separable, or none:

**a)** $(2xy + 3)dx + (x^2 + 4y)dy = 0$. It is an exact DE since $M(x,y)=2xy + 3$ and $N(x,y)=x^2 + 4y$ and

$$
\frac{\partial M}{\partial y} = 2x = \frac{\partial N}{\partial x}
$$

**b)** $y' = x e^{y}$. Separable since $\frac{dy}{dx}=g(x)h(y)$, where $g(x)=x$ and $h(y)=e^{y}$

**c)** $y' + y = x^2$. It is a linear DE since by definition it can be written as:

$$
a_n(x)y^{(n)} + \cdots + a_1(x)y' + a_0(x)y = g(x)
$$

where this equation is first order and $a_i(x)=1$ and $g(x)=x^2$.

---

---

For each IVP, determine whether the Existence and Uniqueness Theorem guarantees a unique solution: 

**a)** $y' = \sqrt{y},\; y(0)=0$ → If we calculate the y-partial derivative of $\sqrt{y}$, we have $\frac{1}{2\sqrty{y}}$ which is continuous to $x$ values near 0,  therefore there is an unique solution to it

**b)** $y' = \frac{1}{x-y},\; y(1)=1$. Calculating the y-partial derivative of $\frac{1}{x-y}$ we have $\frac{1}{(x-y)^2}$, which is continous to $x$ values near 1, therefore there is an unique solution to it

**c)** $y' = x^{1/3} y^{2/3},\; y(0)=0$. Calculating the y-partial derivative of $x^{1/3} y^{2/3}$ we have $\frac{2x^{1/3}}{3y^{1/3}}$ which is continuous to $x$ values near 0, therefore there is an unique solution to it.

---

# **First‑Order Differential Equations**

---

## **Separable Equations**

---

Solve the following separable equations (no need to simplify constants):

**a)** $y' = x^2 y^3$. We rewrite the equation to:

$$
\frac{dy}{dx}=x^2 y^3
$$

Then we separate the differentials to match the variables
  
$$
\frac{dy}{y^3}=x^2 dx
$$

Then we integrate the equation

$$
\int \frac{dy}{y^3}=\int x^2 dx
$$

which is equivalent

$$
-\frac{1}{2y^2} = \frac{x^3}{3}
$$

Then we isolate $y$

$$
-\frac{3}{2x^3} = y^2 \Rightarrow y = if(x), i\in \mathbb{C}
$$

Therefore we can't find a solution to it, at least not in $\mathbb{R}$

**b)** $y' = \frac{x}{1+y^2}$

We rewrite the equation to:

$$
\frac{dy}{dx}=\frac{x}{1+y^2}
$$

Then we separate the differentials to match the variables

$$
(1+y^2)dy=x dx
$$

Then we integrate the equation

$$
\int (1+y^2)dy=\int x dx
$$

which is equivalent

$$
y + \frac{y^3}{3} = x^2
$$

Then we isolate $y$

$$
y(1+\frac{y^2}{3}) = x^2
$$

which means there is more than one solution

**c)** $y' = (y-1)(y+2)$

We rewrite the equation to:

$$
\frac{dy}{dx}=\frac{y-1}{y+2}
$$

Then we separate the differentials to match the variables

$$
\frac{y+2}{y-1}dy=dx
$$

Then we integrate the equation

$$
\int \frac{y+2}{y-1}dy=\int dx
$$

which is equivalent

$$
\int \(1+\frac{3}{y-1}\)dy=\int dx
$$

$$
y + 3ln(y-1) = x
$$

However we can't isolate y, so the equation may have multiple solutions

---

Solve the IVPs:  

**a)** $y' = xy,\; y(0)=3$

This can be rewritten as

$$
\frac{dy}{dx} = xy
$$

Which is equivalent to

$$
\frac{dy}{y}=x dx
$$

Let's integrate

$$
\int \frac{dy}{y}=\int x dx \Rightarrow ln(y) = \frac{x^2}{2}
$$

If an $e^x$ is applied to the equation we have

$$
y = e^{\frac{x^2}{2}} + C
$$

$C$ constant. Taking the initial value we have

$$
\begin{align}
y(0) = e^{\frac{0^2}{2}} + C    \\
= e^{0} + C \\
= 1 + C = 3 
\Rightarrow C = 2
\end{align}
$$

Therefore $y = e^{\frac{x^2}{2}} + 2$

**b)** $y' = (1+y^2)\cos x; y(0)=0$

This can be rewritten as

$$
\frac{dy}{dx} = (1+y^2)\cos x
$$

Which is equivalent to

$$
\frac{dy}{(1+y^2)}=\cos x dx
$$

Let's integrate

$$
\int \frac{dy}{(1+y^2)}=\int \cos x dx \Rightarrow \arctan(y) = \sin(x)
$$

If $\tan(x)$ is applied to the equation we have

$$
y = \tan(\sin(x)) + C
$$

$C$ constant. Taking the initial value we have

$$
y(0) = \tan(\sin(0)) + C = \tan(0) + C = 0 + C = 0 \Rightarrow C = 0
$$

Therefore $y = \tan(\sin(x))$

---

Determine all equilibrium solutions and classify their stability:  

**a)** $y' = y(3-y)$  

An equilibrium solution is a constant solution $y(t)=C$ such that $y'=0$.

So we equalize the right side to $0$:

$$
y(3-y)=0 \Rightarrow y=0 | y=3
$$

So the equilibrium solutions are $y=0$ and $y=3$.

Now, the idea is to check what happens with solutions near each equilibrium, we can use the derivative criteria of $f(y)$ where

$$
y'=f(y)=y(3-y) \Rightarrow f'(y)=3-2y
$$

If we set $y=0$, $f'(0)=3-0=3>0$. If $f'(y*)>0$, then the equilibrium $y*$ is unstable (near solutions go away).

If we set $y=3$, $f'(3)=3-6=-3<0$. If $f'(y*)<0$, then the equilibrium $y*$ is asintotically stable (near solutions get close).

**b)** $y' = y^2 - 4$

Let's equalize $y^2-4=0$, so the equilibrium solutions are $y=2$ and $y=-2$, so we use the derivative criteria of $f(y)$ where

$$
y'=f(y)=y^2-4 \Rightarrow f'(y)=2y
$$

If we set $y=-2$, $f'(-2)=2(-2)=-4<0$. If $f'(y*)<0$, then the equilibrium $y*$ is asintotically stable (near solutions get close).

If we set $y=2$, $f'(2)=2(2)=4>0$. If $f'(y*)>0$, then the equilibrium $y*$ is unstable (near solutions get away).

---

## **Exact Equations**

---

Determine whether each equation is exact. If exact, solve it:  

**a)** $(3x^2 + 2y)dx + (2x + 4y^3)dy = 0$

$$
\begin{align}
M(x,y) = 3x^2 + 2y \Rightarrow \frac{\partial M}{\partial y} = 2    \\
N(x,y) = 2x + 4y^3 \Rightarrow \frac{\partial N}{\partial x} = 2
\end{align}
$$

Since $\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}$, the DE is exact. Then we solve the DE, first we inegrate $M$

$$
\int M(x,y)dx = \int (3x^2+2y)dx=\int 3x^2 dx + \int 2y dx = x^3+2yx + h(y)
$$

Now we take the derivative of this result on $y$ and equalize to $N$ having

$$
\begin{align}
\frac{d}{dy}\(x^3+2yx+h(y)\)=N(x,y)=2x+4y^3 \\
\Rightarrow 2x + h'(y)=2x+4y^3  \\
\Rightarrow h'(y) = 2x+4y^3-2x=4y^3
\end{align}
$$

If we integrate $h'(y)$ on y we have that $h(y)=y^4$. Therefore the solution to the DE is $x^3+3xy+y^4=C$

**b)** $(y\cos x - 2x)dx + (\sin(x) + x^2)dy = 0$

$$
\begin{align}
M(x,y) = y\cos x -2x \Rightarrow \frac{\partial M}{\partial y} = \cos x \\
N(x,y) = \sin(x) + x^2 \Rightarrow \frac{\partial N}{\partial x} = \cos x
\end{align}
$$

Since $\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}$, the DE is exact. Then we solve the DE, first we inegrate $M$

$$
\int M(x,y)dx = \int (y\cos x - 2x)dx=\int y\cos x dx - \int 2x dx = y\sin(x) - x^2 + h(y)
$$

Now we take the derivative of this result on $y$ and equalize to $N$ having

$$
\frac{d}{dy}\(y\sin(x) - x^2 + h(y)\) = N(x,y) = \sin(x) + x^2 \Rightarrow \sin(x) + h'(y) = \sin(x) + x^2 \Rightarrow h'(y) = x^2
$$

If we integrate $h'(y)$ on y we have that $h(y)=yx^2$. Therefore the solution to the DE is $y\sin(x) -x^2 + yx^2=C$

---

Find an integrating factor (if it exists) depending only on $x$ or only on $y$:  

**a)** $(2xy - y)dx + (x^2 - x)dy = 0$

$$
\begin{align}
M(x,y) = 2xy - y \Rightarrow \frac{\partial M}{\partial y} = x - 1  \\
N(x,y) = x^2 - x \Rightarrow \frac{\partial N}{\partial x} = x - 1
\end{align}
$$

Since $\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}$, the DE is exact. Therefore the integrating factor is $\mu = 1$

**b)** $(y + x e^{xy})dx + (x + y e^{xy})dy = 0$

$$
\begin{align}
M(x,y) = y + x e^{xy} \Rightarrow \frac{\partial M}{\partial y} = 1 + x^2 e^{xy}    \\
N(x,y) = x + y e^{xy} \Rightarrow \frac{\partial N}{\partial x} = 1 + y^2 e^{xy}
\end{align}
$$

Since $\frac{\partial M}{\partial y}\neq\frac{\partial N}{\partial x}$, the DE is not exact. 
Now we have to prove either there exist an integrating factor dependant on $x$ or dependant on $y$. However
- If $\frac{M_y - N_x}{N}=f(x)\Rightarrow \mu = \mu(x)$
- If $\frac{N_x - M_y}{M}=g(y)\Rightarrow \mu = \mu(y)$

Then we calculate $M_y - N_x = (1 + x^2 e^{xy}) - (1 + y^2 e^{xy}) = (x^2 - y^2)e^{xy}$, and now we test first $\mu(x)$

$$
\frac{M_y - N_x}{N} = \frac{(x^2 - y^2)e^{xy}}{x + y e^{xy}}
$$

However, it still depends on both, testing on $\mu(y)$ we have a similar situation, so there is no integrating factor that depends only on either $x$ or $y$

---

## **Linear First‑Order Equations**

---

Solve using the integrating factor method:  

**a)** $y' + 3y = e^{-x}$

Since the equation matches the general form $P(x) = 3$ and $Q(x) = e^{-x}$, then the integrating factor has the form:

$$
\begin{align}
\mu(x) = e^{\int P(x)dx} \\
\Rightarrow \mu(x) = e^{\int 3dx} \\
\Rightarrow \mu(x) = e^{3x}
\end{align}
$$

Then we multiply $\mu(x)$ to the entire equation

$$
\mu(x)y'+3(\mu(x))y = \mu(x)e^{-x}
$$

We recognize the derivative as:

$$
\begin{align}
(\mu(x)y)' = \mu(x)e^{-x} \\
\Rightarrow \(e^{3x}y\)' = e^{3x}e^{-x} \\
\Rightarrow \(e^{3x}y\)' = e^{2x}
\end{align}
$$

Then we integrate on x, having

$$
\begin{align}
\int \(e^{3x}y\)' =  \int e^{2x} \\
\Rightarrow e^{3x}y = \frac{1}{2}e^{2x} + C \\
\Rightarrow y = \frac{e^{-x}}{2} + Ce^{-x}
\end{align}
$$

**b)** $y' - \frac{2}{x}y = x^3$

Since the equation matches the general form $P(x) = \frac{2}{x}$ and $Q(x) = x^3$, then the integrating factor has the form:

$$
\begin{align}
\mu(x) = e^{\int P(x)dx} \\
\Rightarrow \mu(x) = e^{\int \frac{2}{x}dx} \\
\Rightarrow \mu(x) = e^{2ln(x)} = x^2
\end{align}
$$

Then we multiply $\mu(x)$ to the entire equation

$$
\mu(x)y'+\frac{2}{x}(\mu(x))y = \mu(x)x^3
$$

We recognize the derivative as:

$$
\begin{align}
(\mu(x)y)' = \mu(x)x^3 \\
\Rightarrow \(x^2 y\)' = x^2 x^3 \\
\Rightarrow \(e^{3x}y\)' = x^5
\end{align}
$$

Then we integrate on x, having

$$
\begin{align}
\int \(x^2 y\)' =  \int x^5 \\
\Rightarrow x^2 y = \frac{1}{6}x^6 + C \\
\Rightarrow y = \frac{x^4}{6} + \frac{C}{x^2}
$$

**c)** $y' + y\tan(x) = \sin(x)$

Since the equation matches the general form $P(x) = \tan(x)$ and $Q(x) = \sin(x)$, then the integrating factor has the form:

$$
\begin{align}
\mu(x) = e^{\int P(x)dx} \\
\Rightarrow \mu(x) = e^{\int \tan(x) dx} \\
\Rightarrow \mu(x) = e^{-\ln(\cos x)} = \sec(x)
\end{align}
$$

Then we multiply $\mu(x)$ to the entire equation

$$
\mu(x)y'+\tan(x)(\mu(x))y = \mu(x)\sin(x)
$$

We recognize the derivative as:

$$
\begin{align}
(\mu(x)y)' = \mu(x)\sin(x) \\
\Rightarrow \(\sec(x) y\)' = \sec(x) \sin(x) \\
\Rightarrow \(\sec(x) y\)' = \tan(x)
\end{align}
$$

Then we integrate on x, having

$$
\begin{align}
\int \(\sec(x) y\)' = \int \tan(x) \\
\Rightarrow \sec(x) y = -\ln(\cos x) + C \\
\Rightarrow y = -\frac{\ln(\cos x)}{\sec(x)} + C\cos x
\end{align}
$$

---

---

Solve the IVPs:  

**a)** $y' + 4y = 8; y(0)=1$

Since the equation matches the general form $P(x) = 4$ and $Q(x) = 8$, then the integrating factor has the form:

$$
\begin{align}
\mu(x) = e^{\int P(x)dx} \\
\Rightarrow \mu(x) = e^{\int 4 dx} \\
\Rightarrow \mu(x) = e^{4x}
\end{align}
$$

Then we multiply $\mu(x)$ to the entire equation

$$
\mu(x)y'+4(\mu(x))y = \mu(x)8
$$

We recognize the derivative as:

$$
\begin{align}
(\mu(x)y)' = 8\mu(x) \\
\Rightarrow \(e^{4x} y\)' = 8e^{4x} \\
\Rightarrow \(e^{4x} y\)' = 8e^{4x}
\end{align}
$$

Then we integrate on x, having

$$
\begin{align}
\int \(e^{4x} y\)' = \int 8e^{4x} \\
\Rightarrow e^{4x} y = 2e^{4x} + C \\
\Rightarrow y = 2 + Ce^{4x}
\end{align}
$$

Since we have $y(0)=1$, then $y(0) = 2 + Ce^{0} = 1 \Rightarrow 2 + C = 1 \Rightarrow C=-1$. Therefore the solution of the IVP is $y = 2 -e^{4x}$

**b)** $y' - \frac{1}{x}y = x,\; y(1)=2$

Since the equation matches the general form $P(x) = \frac{1}{x}$ and $Q(x) = x$, then the integrating factor has the form:

$$
\begin{align}
\mu(x) = e^{\int P(x)dx} \\
\Rightarrow \mu(x) = e^{\int \frac{1}{x} dx} \\
\Rightarrow \mu(x) = e^{\ln x} = x
\end{align}
$$

Then we multiply $\mu(x)$ to the entire equation

$$
\mu(x)y'+\frac{1}{x}(\mu(x))y = \mu(x)x
$$

We recognize the derivative as:

$$
\begin{align}
(\mu(x)y)' = x\mu(x) \\
\Rightarrow \(x y\)' = x^2 \\
\Rightarrow \(x y\)' = x^2
\end{align}
$$

Then we integrate on x, having

$$
\begin{align}
\int \\(x y\\)' = \int x^{2} \\
\Rightarrow x y = \frac{x^3}{3} + C \\
\Rightarrow y = \frac{x^2}{3} + \frac{C}{x}
\end{align}
$$

Since we have $y(1)=2$, then $y(1) = \frac{1^2}{3} + \frac{C}{1} = 2 \Rightarrow \frac{1}{3} + C = 2 \Rightarrow C=\frac{5}{3}$. Therefore the solution of the IVP is $y = \frac{x^2}{3} + \frac{5}{3x}$

---

## **Substitution Methods**

### **Homogeneous**

---

Solve:  

**a)** $y' = \frac{x+y}{x-y}$

Let's substitute $y = vx, \quad y' = v + xv'$

$$
v + xv' = \frac{x(v+1)}{x(1-v)} \Rightarrow xv' = \frac{x(v+1)-xv(1-v)}{x(1-v)}= \frac{(v+1)+(v^2 - v)}{1-v}=\frac{v^2+1}{1-v} \Rightarrow v' = \frac{1}{x}\frac{v^2 +1}{1-v}
$$

We then make $v' = \frac{dv}{dx}$ and

$$
\frac{1-v}{v^2 +1}dv =\frac{dx}{x}
$$

So, if we split the equation we have that $\int \frac{dx}{x}=\ln x$, on the other side:

$$
\int \frac{1-v}{v^2 +1}dv=\int\frac{dv}{v^2 +1}-\int\frac{vdv}{v^2 +1}
$$

From Calculus we know that $\int\frac{dv}{v^2 +1}= \arctan(v)$ and let $u=v^2 +1$, so $du=2vdv\Rightarrow vdv=\frac{du}{2}$, then

$$
\begin{align}
\int \frac{1-v}{v^2 +1}dv = \arctan(v)- \frac{1}{2}\\
\int\frac{du}{u}=\arctan(v)-\frac{1}{2}\ln(u) \\
=\arctan(v)-\frac{1}{2}\ln(v^2 +1)
\end{align}
$$

So in the end we have the following equation

$$
\arctan(v)-\frac{1}{2}\ln(v^2 +1) =\ln(x) + C
$$

Considering $y=vx\Rightarrow v\frac{y}{x}$, we substitute the value of $v$

$$
\arctan(\frac{y}{x})-\frac{1}{2}\ln(\frac{y}{x}^{2} +1) =\ln(x) + C
$$

By properties of $\ln$

$$
\ln(\frac{y}{x}^{2} +1)=\ln(\frac{x^2 + y^2}{x^2})=\ln(x^2 + y^2)-\ln(x^2)
$$

Therefore

$$
\begin{align}
\arctan(\frac{y}{x})-\frac{1}{2}\\(\ln(x^2 + y^2)-\ln(x^2)\\) \\
= \arctan(\frac{y}{x})-\frac{1}{2}\ln(x^2 + y^2)-\frac{1}{2}\ln(x^2) \\
= \arctan(\frac{y}{x})-\frac{1}{2}\ln(x^2 + y^2)+\frac{1}{2}2\ln(x) \\
= \arctan(\frac{y}{x})-\frac{1}{2}\ln(x^2 + y^2)+\ln(x) \\
=\ln(x) + C
\end{align}
$$

Finally having

$$
\arctan(\frac{y}{x})-\frac{1}{2}\ln(x^2 + y^2)= C
$$

Which is a valid form for an implicit solution

**b)** $y' = \frac{y}{x} + \frac{x}{y}$

Let's substitute $y = vx, \quad y' = v + xv'$

$$
\begin{align}
v + xv' = \frac{vx}{x} + \frac{x}{vx} \\
\Rightarrow xv' = v+\frac{1}{v}-v=\frac{1}{v}   \\
\Rightarrow v'=\frac{1}{vx}
\end{align}
$$

We then make $v' = \frac{dv}{dx}$ and

$$
vdv =\frac{dx}{x}
$$

So, if we split the equation we have that $\int \frac{dx}{x}=\ln x$, on the other side:

$$
\int vdv=\frac{v^2}{2}
$$

So in the end we have the following equation

$$
\frac{v^2}{2}=\ln(x) + C
$$

Considering $y=vx\Rightarrow v\frac{y}{x}$, we substitute the value of $v$

$$
\frac{1}{2}\\(\frac{y}{x}\\)^2=\ln(x) + C
$$

where

$$
C = \\(\frac{y}{x}\\)^2 - \ln(x)
$$

Which is a valid form for an implicit solution

---

### **Bernoulli**

---

Solve:  

**a)** $y' + y = y^3$

From Bernoulli we use the substitution $v=y^{1-n}=y^{1-3}=y^{-2} \Rightarrow v' = -\frac{2}{y^3}y'  \Rightarrow y' = -\frac{y^3 v'}{2}=\frac{(v^{-1/2})^3 v'}{2}=\frac{v^{-3/2} v'}{2}$ then we have

$$
\frac{v^{-3/2} v'}{2} + v^{-1/2}=v^{-3/2}
$$

Then we dvide the equation by $v^{-3/2}$ having

$$
\frac{v'}{2} + v= 1 \Rightarrow v' +2v = 2
$$

This last equation can be solved using the integrating factor with $P(x)=2$ and $Q(x)=2$. Now we calculate the integrating factor:

$$
\mu(x) = e^{\int P(x)dx}=e^{\int 2dx}=e^{2x}
$$

Then we multiply $\mu(x)$ to the entire equation

$$
\mu(x)v'+2(\mu(x))v = 2\mu(x)
$$

We recognize the derivative as:

$$
\begin{align}
(\mu(x)v)' = 2\mu(x) \\
\Rightarrow \(e^{2x}v\)' = 2e^{2x} 
\end{align}
$$

Then we integrate on x, having

$$
\begin{align}
\int \\(e^{2x}v\\)' = \int 2e^{2x} \\
\Rightarrow e^{2x}v = e^{2x} + C \\
\Rightarrow v = 1 + Ce^{-2x}
\end{align}
$$

Then we substitute the value of $v=y^{-2}$ having

$$
\begin{align}
y^{-2} = 1 +Ce^{-2x}    \\
\Rightarrow y = \(1 +Ce^{-2x}\)^{-1/2}
\end{align}
$$

**b)** $y' - 2y = 3y^{-1}$

From Bernoulli we use the substitution $v=y^{1-n}=y^{1-(-1)}=y^{2} \Rightarrow v' = 2yy'  \Rightarrow y' = \frac{v'}{2\sqrt(v)}$ then we have

$$
\frac{v'}{2\sqrt(v)} - 2\sqrt(v) = \frac{3}{\sqrt(v)}
$$

Then we multiply the equation by $\sqrt(v)$ having

$$
v' - 2v = 3 
$$

This last equation can be solved using the integrating factor with $P(x)=-2$ and $Q(x)=3$. Now we calculate the integrating factor:

$$
\mu(x) = e^{\int P(x)dx}=e^{\int -2dx}=e^{-2x}
$$

Then we multiply $\mu(x)$ to the entire equation

$$
\mu(x)v'-2(\mu(x))v = 3\mu(x)
$$

We recognize the derivative as:

$$
\begin{align}
(\mu(x)v)' = 3\mu(x) \\
\Rightarrow \\(e^{-2x}v\\)' = 2e^{-2x}
\end{align}
$$

Then we integrate on x, having

$$
\begin{align}
\int \\(e^{-2x}v\\)' = \int 3e^{-2x} \\
\Rightarrow e^{-2x}v = \frac{3}{2}e^{-2x} + C \\
\Rightarrow v = \frac{3}{2} + Ce^{2x}
\end{align}
$$

Then we substitute the value of $v=y^{2}$ having

$$
\begin{align}
y^{2} = \frac{3}{2} +Ce^{2x}    \\
\Rightarrow y = \\(1 +Ce^{-2x}\\)^{1/2}
\end{align}
$$

---

### **Riccati (special case)**

---

Solve the Riccati equation given a particular solution $y_p = x$:  

$$
y' = y^2 - xy + x^2
$$

The Riccati form can be identified as $a(x)=1, b(x)=-x$ and $c(x)=x^2$, and we have the particular solution $y_p = x$, Then we apply the substitution $y = y_p + \frac{1}{v}$, where $y'=y_{p}'-\frac{v'}{v^2}= 1- \frac{v'}{v^2}$. Substituting this result in the original equation we have:

$$
\begin{align}
v' + (2a(x)y_{p}(x)+b(x))v =-a(x)   \\
\Rightarrow v' +(2(1)x-x)v=-1   \\
\Rightarrow v' +xv =-1
\end{align}
$$

Which can be calculated by the integrating factor using $P(x)=x$ and $Q(x)=-1$. Now we calculate the integrating factor:

$$
\mu(x) = e^{\int P(x)dx}=e^{\int xdx}=e^{\frac{x^2}{2}}
$$

Then we multiply $\mu(x)$ to the entire equation

$$
\mu(x)v'+x(\mu(x))v = -\mu(x)
$$

We recognize the derivative as:

$$
\begin{align}
(\mu(x)v)' = -\mu(x) \\
\Rightarrow \(e^{\frac{x^2}{2}}v\)' = -e^{\frac{x^2}{2}}
\end{align}
$$

Then we integrate on x, having

$$
\begin{align}
\int \\(e^{\frac{x^2}{2}}v\\)' = \int -e^{\frac{x^2}{2}}    \\
\Rightarrow e^{\frac{x^2}{2}}v = \int -e^{\frac{x^2}{2}} + C \\
\Rightarrow v = E(x) + Ce^{\frac{x^2}{2}}
\end{align}
$$

where $E(x)=\int -e^{\frac{x^2}{2}}$. Then we substitute the value of $v=\frac{1}{y-y_p}$ having

$$
\begin{align}
y-y_p = \frac{1}{E(x) + Ce^{\frac{x^2}{2}}} \\
\Rightarrow y = \frac{1}{E(x) + Ce^{\frac{x^2}{2}}} + y_p
\end{align}
$$

---

### **Clairaut**

---

Solve the Clairaut equation:  

$$
y = xy' + (y')^2
$$

Using Clairaut, we identify $f(y')=(y')^2$, So, the solution will have the form

$$
y=Cx + C^2
$$

---

# **Higher‑Order Linear Differential Equations**

---

## **Homogeneous with Constant Coefficients**

---

Solve:  

**a)** $y'' - 5y' + 6y = 0$

We take the characteristic equation as

$$
r^2 -5r +6=0
$$

where we factorize $r=3$ and $r=2$ as solutions.
Therefore, the solution is

$$
y = C_1 e^{3x} + C_2 e^{2x}
$$

**b)** $y'' + 4y = 0$

We take the characteristic equation as

$$
\begin{align}
r^2 + 4r =0 \\
\Rightarrow r(r+4) = 0
\end{align}
$$

Then we have the roots $r=0$ and $r=-4$

$$
y = C_1 e^{0x} + C_2 e^{-4x} = C_1 + C_2 e^{-4x}
$$

**c)** $y''' - 3y'' + 3y' - y = 0$

We take the characteristic equation as

$$
\begin{align}
r^3 -3r^2 + 3r -1 = 0 \\
\Rightarrow (r-1)^3 = 0
\end{align}
$$

Then we have the roots $r=1$

$$
y = C_1 e^{x} + C_2 xe^{x} + C_3 x^2 e^{x}
$$

---

Solve the IVPs:  
**a)** $y'' + y = 0; y(0)=2,\; y'(0)=1$

We take the characteristic equation as

$$
\begin{align}
r^2 + r = 0 \\
\Rightarrow r(r+1) = 0
\end{align}
$$

Then we have the roots $r=-1$ and $r=0$

$$
y = C_1 e^{-x} + C_2 e^{0x} = C_1 e^{-x} + C_2
$$

Remembering the IVP $y(0)=2,\; y'(0)=1$

$$
y(0) = C_1 e^{-0} + C_2 = C_1 + C_2 = 2
$$

If we calculate the derivative of the solution we have 

$$
\begin{align}
y'(x) = -C_1 e^{-x} \\
\Rightarrow y'(0) = -C_1 e^{-0} = 1 \\
\Rightarrow -C_1 = 1    \\
\Rightarrow C_1 = -1
\end{align}
$$

Substituting the valñue of $C_1$ we have $C_2 = 3$.
Therefore the solution to the equation is

$$
y = -e^{-x} + 3
$$

**b)** $y'' - 4y' + 4y = 0,\; y(0)=0,\; y'(0)=3$

We take the characteristic equation as

$$
\begin{align}
r^2 - 4r + 4 = 0 \\
\Rightarrow (r-2)^2 = 0
\end{align}
$$

Then we have the roots $r=2$

$$
y = C_1 e^{2x} + C_2 xe^{2x}
$$

Remembering the IVP $y(0)=2$

$$
y(0) = C_1 e^{2(0)} + C_2 (0)e^{2(0)} = C_1 = 0
$$

If we substitute the value of $C_1$ in the solution $y$ we have

$$
y(x) = C_2 xe^{2x}
$$

If we calculate the derivative of the solution we have 

$$
\begin{align}
y'(x) = C_2\\(e^{2x} + 2xe^{2x}\\) \\
\Rightarrow y'(0) = C_2\\(e^{2(0)} + 2(0)e^{2(0)}\\) = 3    \\
\Rightarrow C_2 = 3
\end{align}
$$

Finally we have $C_2 = 3$.
Therefore the solution to the equation is

$$
y = 3xe^{2x}
$$

---

## **Nonhomogeneous Equations**

### **Undetermined Coefficients**

Solve:  

**a)** $y'' + y = \sin(x)$

First we solve the homogeneous part

$$
y'' + y = 0
$$

Thus we take the caracteristic equation

$$
r^2 + 1 = 0
$$

Where $r = \pm i$ then, the solution takes the form

$$
y_h=C_1\cos(x)+C_2\sin(x)
$$

Since the non-homogeneous part is $\sin(x)$ we should find a solution with it, but that solution is already considered in $y_h$, then we take

$$
y_p = x(A\cos(x)+B\sin(x))
$$

Then we derivate $y_p$

$$
\begin{align}
y_{p}' = A\cos(x) + B\sin(x)+ x(B\cos(x)-A\sin(x))  \\
y_{p}'' = B\cos(x) - A\sin(x) +B\cos(x) - A\sin(x) - x(A\cos(x) + B\sin(x)) = 2B\cos(x)-2A\sin(x)-x(A\cos(x)+B\sin(x))
\end{align}
$$

Substituting in the original equation we have

$$
\begin{align}
y''+ y=\sin(x)  \\
\Rightarrow 2B\cos(x)-2A\sin(x)-x(A\cos(x)+B\sin(x)) + x(A\cos(x)+B\sin(x))=\sin(x) \\
\Rightarrow 2B\cos(x)-2A\sin(x)=1*\sin(x) +0*\cos(x)    \\
\end{align}
$$

Where we have the following equations system

$$
\begin{align}
-2A = 1 \Rightarrow A=-\frac{1}{2}  \\
2B = 0 \Rightarrow B = 0
\end{align}
$$

Therefore, the final particular solution is

$$
y_p = x(A\cos(x) + B\sin(x))= x(-\frac{1}{2}\cos(x))=-\frac{1}{2}x\cos(x)
$$

Finally the General Solution is 

$$
y=C_1\cos(x)+C_2\sin(x)-\frac{1}{2}x\cos(x)
$$

**b)** $y'' - 3y' + 2y = e^{2x}$

First we solve the homogeneous part

$$
y'' - 3y' + 2y = 0
$$

Thus we take the caracteristic equation

$$
r^2 - 3r + 2 = 0
$$

Where $r = 2$ and $r = 1$ then, the solution takes the form

$$
y_h=C_1e^{2x}+C_2e^{x}
$$

Since the non-homogeneous part is $e^{2x}$ we should find a solution with it, but that solution is already considered in $y_h$, then we take

$$
y_p = x(e^{2x})
$$

Then we derivate $y_p$

$$
\begin{align}
y_{p}' = e^{2x} + 2x e^{2x} \\
y_{p}'' = 2e^{2x} + 2\\[e^{2x} + 2x e^{2x}\\] = 4e^{2x}+ 4xe^{2x}
\end{align}
$$

Substituting in the original equation we have

$$
\begin{align}
y'' - 3y' + 2y = e^{2x} \\
\Rightarrow 4e^{2x} + 4x e^{2x} - 3e^{2x} - 6x e^{2x} + 2x e^{2x} = e^{2x}  \\
\Rightarrow e^{2x}=e^{2x}   \\
\end{align}
$$

Meaning the $y_p$ solution is right

Finally the General Solution is 
$$
y=y_h + y_p = C_1e^{2x}+C_2e^{x} + xe^{2x}
$$

**c)** $y'' + 4y = 3x^2$

First we solve the homogeneous part

$$
y'' + 4y = 0
$$

Thus we take the caracteristic equation

$$
r^2 + 4 = 0
$$

Where $r = 0 \pm 2i$ then, the solution takes the form

$$
y_h=C_1\sin(2x)+C_2\cos(2x)
$$

Since the RHS is $3x^2$
Then a candidate for the solution is 

$$
y_p=ax^2+bx+c
$$

We take out the derivatives

$$
\begin{align}
y_{p}' = 2ax +b \\
y_{p}'' = 2a
\end{align}
$$

We substitute it in the equation

$$
\begin{align}
2a +4(ax^{2}+bx+c)=3x^2 \\
\Rightarrow 2a +4ax^2 +4bx +4c = 3x^2
\end{align}
$$

so we have the following system

$$
\begin{align}
4a = 3 \Rightarrow a=\frac{3}{4}    \\
4b=0 \Rightarrow b=0    \\
2a + 4c = 0 \Rightarrow \frac{3}{2}+4c=0 \Rightarrow c=-\frac{3}{8}
\end{align}
$$

Therefore, the final particular solution is

$$
y_p = \frac{3}{4}x^2 -\frac{3}{8}
$$

Finally the General Solution is 

$$
y=C_1\sin(x)+C_2\cos(x)+\frac{3}{4}x^2 -\frac{3}{8}
$$

---

### **Annihilator Method**

Solve:  

**a)** $y'' - y = e^{x} + x$  

First we identify the annihilator $A=D^2(D -1)$.
Then we apply it in the ODE

$$
A(D)L(D)y = 0 \Rightarrow (D-1)D^2 (D^2 - 1)y=0
$$

Having the following characteristic equation:

$$
(D^2 - 1)(D - 1)D^2 = (D -1)(D+1)(D-1)D^2 = 0
$$

The roots we can see in that equation are $r = 1$ with multiplicity 2, $r = -1$ and $r = 0$ with multiplicity 2. So the general solution has the form.

$$
y = (C_1 +C_2 x)e^{x} + C_3 e^{-x} + C_4 + C_5 x
$$

which we can identify the homogeneous solution as

$$
y_c = C_1 e^{x} + C_3 e^{-x}
$$

and the particular solution

$$
y_p = C_2 xe^{x} + C_4 + C_5 x
$$

**b)** $y''' = \sin(x)$

Considering $g(x)=\sin(x)$, we propose the anihiliator $D^2 + 1$. Then we apply it in the ODE

$$
A(D)L(D)y = 0 \Rightarrow (D^2+1)(D^3)y=0
$$

Having the following characteristic equation:

$$
(D^2+1)(D^3) = 0
$$

The root we can see in that equation is $r = 0$ with multiplicity 3, and $r = \pm i$. So the general solution has the form.

$$
y = C_1 + C_2 x + C_3 x^{2} + C_4\cos(x) + C_5\sin(x)
$$

which we can identify the homogeneous solution as

$$
y_c = C_1 + C_2 x + C_3 x^{2}
$$

and the particular solution

$$
y_p = C_4\cos(x) + C_5\sin(x)
$$

---

### **Variation of Parameters**

Solve:

**a)** $y'' + y = \sec(x)$

We start from the auxiliar equation $m^2+1=0$, where we have the roots $m = \pm i$ so $y_c = C_1 \cos(x) + C_2 \sin(x)$. Here we identify $y_1 = \cos(x)$ and $y_2 = \sin(x)$, then we calculate the Wronkskian matrix

$$
W(\cos(x), \sin(x)) =
\left|
\begin{matrix}
\cos(x) & \sin(x) \\
-\sin(x) & \cos(x)
\end{matrix}
\right|
= \cos^{2}(x)+\sin^{2}(x) = 1
$$

and since $f(x) = \sec(x)$, we have

$$
W_1 =
\left|
\begin{matrix}
0 & \sin(x) \\
\sec(x) & \cos(x)
\end{matrix}
\right|
= - \tan(x)
$$

and

$$
W_2 =
\left|
\begin{matrix}
\cos(x) & 0 \\
-\sin(x) & \sec(x)
\end{matrix}
\right|
= 1
$$

where

$$
\begin{align}
u_1' = \frac{W_1}{W} = -\frac{\tan(x)}{1}=-\tan(x) \\
\Rightarrow u_1 = \int (-\tan(x))dx \\
= \ln(\cos(x)) + C
\end{align}
$$

and

$$
\begin{align}
u_2' = \frac{W_2}{W} = \frac{1}{1} = 1 \\
\Rightarrow u_2 = \int dx = x
\end{align}
$$

Then

$$
y_p = u_1 y_1 + u_2 y_2 = \ln(cos(x))\cos(x) + x\sin(x)
$$

And finally

$$
y = C_1\cos(x) + C_2\sin(x) + \ln(cos(x))\cos(x) + x\sin(x)
$$

**b)** $y'' - y = \frac{1}{x}$

We start from the auxiliar equation $m^2-1=0$, where we have the roots $m = \pm 1$ so $y_c = C_1 e^{x} + C_2 e^{-x}$. Here we identify $y_1 = e^{x}$ and $y_2 = e^{-x}$, then we calculate the Wronkskian matrix

$$
W(e^{x}, e^{-x}) =
\left|
\begin{matrix}
e^{x} & e^{-x} \\
e^{x} & -e^{-x}
\end{matrix}
\right|
= -1 - 1 = -2
$$

and since $f(x) = \frac{1}{x}$, we have

$$
W_1 =
\left|
\begin{matrix}
0 & e^{-x} \\
\frac{1}{x} & -e^{-x}
\end{matrix}
\right|
= -\frac{1}{x}e^{-x}
$$

and

$$
W_2 =
\left|
\begin{matrix}
e^{x} & 0 \\
e^{x} & \frac{1}{x}
\end{matrix}
\right|
= \frac{1}{x}e^{x}
$$

where

$$
\begin{align}
u_1' = \frac{W_1}{W} = \frac{\frac{1}{x}e^{-x}}{2}=\frac{1}{2x}e^{-x} \\
\Rightarrow u_1 = \int \frac{1}{2x}e^{-x}dx = F_1(x) + C
\end{align}
$$

since, primitive doesn't exist for this function and

$$
\begin{align}
u_2' = \frac{W_2}{W} = \frac{\frac{1}{x}e^{x}}{-2} = -\frac{1}{2x}e^{x} \\
\Rightarrow u_2 = -\int \frac{1}{2x}e^{x}dx = F_2(x) + C
\end{align}
$$

Then

$$
y_p = u_1 y_1 + u_2 y_2 = F_1(x) e^{x} + F_2(x) e^{-x}
$$

And finally

$$
y = C_1e^{x} + C_2e^{-x} + F_1(x) e^{x} + F_2(x) e^{-x}
$$

---

## **Cauchy–Euler**

Solve:

**a)** $x^2 y'' + xy' - y = 0$

For this exercise we try $y=x^{r}$, then we will calculate the derivatives

$$
\begin{align}
y' = rx^{r-1}   \\
y'' = r(r-1)x^{r-2}
\end{align}
$$

Then we substitute in the DE

$$
\begin{align}
x^{2}r(r-1)x^{r-2} + xrx^{r-1} - x^{r} = 0 \\
\Rightarrow r(r-1)x^{r} + rx^{r} -x^{r}=0   \\
\Rightarrow x^{r}\\[r(r-1)+r-1\\] = 0   \\
\Rightarrow r^2 - r + r -1 = 0  \\
\Rightarrow r^2 -1 = 0  \\
\Rightarrow r = \pm 1
\end{align}
$$

Therefore the general solution is $y = C_1 x^{-1} + C_2 x$

**b)** $x^2 y'' - 3xy' + 5y = x^3$

To solve this, we first look at the homogeneous part of the equation such

$$
x^2 y'' - 3xy' + 5y = 0
$$

Let $y = x^{r}, y' = rx^{r-1}, y''= r(r-1)x^{r-2}$, and then substitute in the equation

$$
\begin{align}
x^{2}r(r-1)x^{r-2} -3xrx^{r-1} + 5x^{r} = 0 \\
\Rightarrow r(r-1) - 3r + 5 = 0 \\
\Rightarrow r^{2} - r - 3r + 5 = 0 \\
\Rightarrow r^{2} - 4r + 5 = (r - (2+i))(r - (2-i))=0
\end{align}
$$

So we have a solution $y= C_{1}x^{2}\cos(\ln(x)) + C_{2}x^{2}\sin(\ln(-x))$.

Since RHS is $x^{3}$, we try $y_p = Ax^{3}$, $y' = 3Ax^{2}, y'' = 6Ax$ and substitute in the equation

$$
\begin{align}
x^{2}(6Ax)-3x(3Ax^{2})+5(Ax^{3}) = x^{3}    \\
\Rightarrow 6Ax^{3}-9Ax^{3}+5Ax^{3}=x^{3}   \\
\Rightarrow 2Ax^{3}=x^{3}   \\
\Rightarrow (2A)=1  \\
\Rightarrow A=\frac{1}{2}   
\end{align}
$$

Then $y_p = \frac{1}{2}x{3}$ and $y=C_{1}x^{2}\cos(\ln(x)) + C_{2}x^{2}\sin(\ln(-x)) + \frac{1}{2}x{3}$

---

# **Nonlinear Differential Equations**

Solve the autonomous equations and classify equilibria:  

**a)** $y' = y^2 - y$

We have then

$$
y' = y(y - 1)
$$

This equation is separable perse, so we can re-write the equation as:

$$
\begin{align}
\frac{dy}{dx} = y(y-1)  \\
\Rightarrow \frac{dy}{y(y-1)} = dx
\end{align}
$$

Then, we integrate the equation

$$
\int \frac{dy}{y(y-1)} = \int dx = x
$$

To integrate the first element of the equation we use the method of partial fractions, thus:

$$
\frac{1}{y(y-1)} = \frac{A}{y} + \frac{B}{y-1}
$$

Solving we have

$$
1 = A(y-1) + By = Ay - A + B \Rightarrow \left\{\begin{matrix}
A + B = 0 \\
-A = 1
\end{matrix}\right
$$

$\Rightarrow A=-1$ y $B=1$. Therefore:

$$
\frac{1}{y(y-1)} = -\frac{1}{y} + \frac{1}{y-1}
$$

Thus, the integral has the following form

$$
\begin{align}
\int \(-\frac{1}{y} + \frac{1}{y-1}\)dy = \int dx   \\
\Rightarrow -\ln{y}+\ln{y-1} = x + C    \\
\Rightarrow \ln{\frac{y-1}{y}} = x + C
\end{align}
$$

If we apply exponential function to the equation, we have:

$$
\begin{align}
\frac{y-1}{y} = e^{x + C} = Ce^{x}   \\
1-\frac{1}{y} = Ce^{x}   \\
\frac{1}{y} = 1 - Ce^{x}   \\
y = \frac{1}{1-Ce^{x}}
\end{align}
$$

**b)** $y' = y(4 - y^2)$

This equation is separable perse, so we can re-write the equation as:

$$
\begin{align}
\frac{dy}{dx} = y(4 - y^2)  \\
\Rightarrow \frac{dy}{y(4 - y^2)} = dx
\end{align}
$$

Then, we integrate the equation

$$
\int \frac{dy}{y(y-1)} = \int dx
$$

To integrate the first element of the equation we use the method of partial fractions, thus:

$$
\frac{1}{y(4 - y^2)} = \frac{1}{y(2+y)(2-y)} = \frac{A}{y} + \frac{B}{2 + y} + \frac{C}{2-y}
$$

Solving we have

$$
1 = A(2+y)(2-y) + By(2-y) + Cy(2+y) = 4A-Ay^2 + 2By - By^2 + 2Cy + Cy^2 \Rightarrow \left\{\begin{matrix}
-A - B + C = 0 \\
2B + 2C = 0 \\
4A = 1
\end{matrix}\right
$$

$\Rightarrow A=\frac{1}{4}$, $C=\frac{1}{8}$ y $B=-\frac{1}{8}$. Therefore:

$$
\frac{1}{y(4-y^2)} = \frac{1}{4y} - \frac{1}{8(2+y)} + \frac{1}{8(2-y)}
$$

Thus, the integral has the following form

$$
\begin{align}
\int \(\frac{1}{4y} - \frac{1}{8(2+y)} + \frac{1}{8(2-y)}\)dy = \int dx   \\
\Rightarrow \ln{4y}-\ln{8(2+y)}+\ln{8(2-y)} = x + C    \\
\Rightarrow \ln{32y(2-y)}-\ln{8(2+y)} = x + C    \\
\Rightarrow \ln{\frac{32y(2-y)}{8(2+y)}} = x + C    \\
\Rightarrow \ln{\frac{4y(2-y)}{(2+y)}} = x + C
\end{align}
$$

If we apply exponential function to the equation, we have:

$$
\begin{align}
\frac{4y(2-y)}{(2+y)} = e^{x + C} = Ce^{x}   \\
\Rightarrow 8y -4y^2 =2Ce^{x}+yCe^{x}   \\
\Rightarrow 4y^{2}+(Ce^{x}-8)y + 2Ce^{x}
\end{align}
$$

We have then a cadratic equation, so we apply the general formula to get $y$

$$
\begin{align}
y = \frac{-(Ce^{x}-8)\pm \sqrt{(Ce^{x}-8)^2 -4(4)(2Ce^{x})}}{2(4)}    \\
y = \frac{-(Ce^{x}-8)\pm \sqrt{(Ce^{x}-8)^2 -32Ce^{x}}}{8}
\end{align}
$$

---

Solve the nonlinear ODE:  

**a)** $y'' = y^2$

Let $v=\frac{dx}{dy}=y'$, then $y'' = \frac{dv}{dx}$

However by the chain rule:

$$
\frac{dv}{dx} = \frac{dv}{dy}\frac{dy}{dx}=\frac{dv}{dy}v
$$

So, $y'' = \frac{dv}{dy}v$

Substituting in the original equation we have

$$
v\frac{dv}{dy}=y^{2}
$$

which is a separable equation, so, we separate, having

$$
vdv=y^{2}dy
$$

Then we integrate

$$
\begin{align}
\int vdv = \int y^{2}dy \\
\Rightarrow \frac{v^{2}}{2} = \frac{y^{3}}{3} +  C  \\
\Rightarrow v^{2}=\frac{2}{3}y^{3} + C \\
\Rightarrow v = \sqrt{\frac{2}{3}y^{3} + C}    \\
\Rightarrow y' = \sqrt{\frac{2}{3}y^{3} + C}
\end{align}
$$

Which again is separable, so we have

$$
\begin{align}
\frac{dy}{dx} = \sqrt{\frac{2}{3}y^{3} + C} \\
\frac{dy}{\sqrt{\frac{2}{3}y^{3} + C}} = dx
\end{align}
$$

Then, we integrate the equation

$$
\begin{align}
\int \frac{dy}{\sqrt{\frac{2}{3}y^{3} + C}} = \int dx   \\
\Rightarrow x = G(y) + K
\end{align}
$$

Where G(y) is a function that represents a primitive more alike to what we are trying to calculate.


**b)** $y'' + y^3 = 0$

Let $v=\frac{dx}{dy}=y'$, then $y'' = \frac{dv}{dx}$

However by the chain rule:

$$
\frac{dv}{dx} = \frac{dv}{dy}\frac{dy}{dx}=\frac{dv}{dy}v
$$

So, $y'' = \frac{dv}{dy}v$

Substituting in the original equation we have

$$
v\frac{dv}{dy}=-y^{3}
$$

which is a separable equation, so, we separate, having

$$
vdv=-y^{3}dy
$$

Then we integrate

$$
\begin{align}
\int vdv = \int -y^{3}dy \\
\Rightarrow \frac{v^{2}}{2} = -\frac{y^{4}}{4} +  C  \\
\Rightarrow v^{2}=\frac{1}{2}y^{4} + C \\
\Rightarrow v = \sqrt{\frac{1}{2}y^{4} + C}    \\
\Rightarrow y' = \sqrt{\frac{1}{2}y^{4} + C}
\end{align}
$$

Which again is separable, so we have

$$
\begin{align}
\frac{dy}{dx} = \sqrt{\frac{1}{2}y^{4} + C} \\
\frac{dy}{\sqrt{\frac{1}{2}y^{4} + C}} = dx
\end{align}
$$

Then, we integrate the equation

$$
\begin{align}
\int \frac{dy}{\sqrt{\frac{1}{2}y^{4} + C}} = \int dx   \\
\Rightarrow x = G(y) + K
\end{align}
$$

Where G(y) is a function that represents a primitive more alike to what we are trying to calculate.

---

Determine whether the following nonlinear ODEs admit closed‑form solutions:

**a)** $y' = e^{y^2}$

This equation is separable so we can re-write it as 

$$
\begin{align}
\frac{dy}{dx} = e^{y^2} \\
\Rightarrow \frac{dy}{e^{y^2}} = dx
\end{align}
$$

However if we integrate the equation we are going to get something without a primitive. Therefore, the solution is not closed-form

**b)** $y' = \frac{1}{1+y^4}$

This equation is separable so we can re-write it as 

$$
\begin{align}
\frac{dy}{dx} = \frac{1}{1+y^4} \\
\Rightarrow (1+y^4)dy = dx  \\
\Rightarrow  dy +y^{4}dy = dx
\end{align}
$$

If we integrate the equation we have

$$
\begin{align}
\int (dy +y^{4}dy) = \int dx    \\
\Rightarrow  \int dy + \int y^{4}dy = \int dx    \\
\Rightarrow  x = y +\frac{y^{5}}{5} + C   \\
\end{align}
$$

Therefore, solution has closed-form

---

# **Systems of Differential Equations**

---

## **Linear Systems**

Solve the system:  

$$
\mathbf{x}' = 
\begin{pmatrix}
2 & 1 \\
0 & 3
\end{pmatrix}
\mathbf{x}
$$

Solve the system:  

$$
\mathbf{x}' = 
\begin{pmatrix}
0 & -1 \\
1 & 0
\end{pmatrix}
\mathbf{x}
$$

Classify the equilibrium point for each system:  

**a)**  

$$
\begin{pmatrix}
x' \\ y'
\end{pmatrix}
=
\begin{pmatrix}
-2 & 0 \\
0 & -3
\end{pmatrix}
\begin{pmatrix}
x \\ y
\end{pmatrix}
$$  

**b)**  

$$
\begin{pmatrix}
x' \\ y'
\end{pmatrix}
=
\begin{pmatrix}
1 & 4 \\
-1 & 1
\end{pmatrix}
\begin{pmatrix}
x \\ y
\end{pmatrix}
$$

---

## **Nonlinear Systems**

Linearize the system near the equilibrium and classify:  

**a)**  

$$
x' = x(1-y),\quad y' = y(x-1)
$$  

**b)**  

$$
x' = y - x^2,\quad y' = -x - y
$$

---

# **Series Solutions**

---

## **Power Series**

Find a power series solution about $x=0$:  

**a)** $y'' - xy = 0$  

**b)** $y'' + y = 0$

Determine the recurrence relation for the ODE:  

$$
y'' + x y' + y = 0
$$

---

## **Frobenius Method**

Solve using Frobenius near $x=0$:  

**a)** $x^2 y'' + xy' + y = 0$  

**b)** $x^2 y'' - xy' + y = 0$

---

# **Modeling with Differential Equations**

A tank initially contains 50 L of pure water. Brine with 0.2 kg/L enters at 3 L/min; mixture leaves at 2 L/min.  

**a)** Set up the differential equation.  
**b)** Solve for the amount of salt.

 A population grows according to the logistic model with carrying capacity 5000 and intrinsic rate 0.3.  

**a)** Write the differential equation.  
**b)** Solve for $P(t)$.

A mass‑spring system satisfies:  

$$
m y'' + c y' + ky = 0
$$  

For $m=1$, $c=4$, $k=5$:  

**a)** Classify the damping.  
**b)** Solve the ODE.

An RLC circuit satisfies:  

$$
L I' + RI + \frac{1}{C}\int Idt = E(t)
$$  

Convert to a second‑order ODE and solve for $I(t)$ when $E(t)=E_0\sin(\omega t)$.

A chemical reaction satisfies:  

$$
\frac{dA}{dt} = -kA^2
$$  

Solve for $A(t)$ and determine the half‑life.

---
