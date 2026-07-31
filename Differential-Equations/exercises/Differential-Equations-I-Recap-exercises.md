
---

# **Differential Equations – Extraordinary Exam Level Exercises**  
*Exercises organized by chapter, aligned with the Extended Theorem Compendium.*

---

# **Table of Contents**

0. [Introduction](#introduction)
   - [Classification and Basic Concepts](#classification-and-basic-concepts)
1. [First‑Order Differential Equations](#firstorder-differential-equations)
   - [Separable](#separable-equations)
   - [Exact Equations](#exact-equations)
   - [Linear](#linear-firstorder-equations)
   - [substitution](#substitution-methods)
      - [Homogeneus](#homogeneous)
      - [Bernoulli](#bernoulli)
      - [Riccatti](#riccati-special-case)
      - [Clairaut](#clairaut)
2. [Higher-Order Linear Differential Equations](#higherorder-linear-differential-equations)

# **Introduction**

## **Classification and Basic Concepts**

1. Classify each differential equation as linear/nonlinear, autonomous/non‑autonomous, and determine its order:  

   a) $y'' + y' + y = \sin x$
   Linear, non-autonomous, order 2

   b) $y' = y^2 - 3y + 2$  
   Non-Linear, autonomous, first order
   
   c) $x^2 y'' + xy' - y = 0$  
   Linear, non-autonomous, order 2
   
   d) $y' + \sqrt{xy} = 0$
   Non-linear, autonomous, first order

2. Determine whether the following equations are exact, linear, separable, or none:

   **a)** $(2xy + 3)dx + (x^2 + 4y)dy = 0$

   It is an exact DE since $M(x,y)=2xy + 3$ and $N(x,y)=x^2 + 4y$ and

$$
\frac{\partial M}{\partial y} = 2x = \frac{\partial N}{\partial x}
$$

   
   **b)** $y' = x e^{y}$  
   
   Separable since $\frac{dy}{dx}=g(x)h(y)$, where $g(x)=x$ and $h(y)=e^{y}$
   
   c) $y' + y = x^2$

   It is a linear DE since by definition it can be written as:
   
   $$
   a_n(x)y^{(n)} + \cdots + a_1(x)y' + a_0(x)y = g(x)
   $$
   
   where this equation is first order and $a_i(x)=1$ and $g(x)=x^2$

3. For each IVP, determine whether the Existence and Uniqueness Theorem guarantees a unique solution: 

   a) $y' = \sqrt{y},\; y(0)=0$ 

   If we calculate the y-partial derivative of $\sqrt{y}$, we have $\frac{1}{2\sqrty{y}}$ which is continuous to $x$ values near 0, however it is not coninous in $x=0$, therefore we can't confirm there is an unique solution to it

   b) $y' = \frac{1}{x-y},\; y(1)=1$

   Calculating the y-partial derivative of $\frac{1}{x-y}$ we have $\frac{1}{(x-y)^2}$, which is continous to $x$ values near 1, however is not continous in $x=1$, therefore we can't confirm there is an unique solution to it
   
   c) $y' = x^{1/3} y^{2/3},\; y(0)=0$
   
   Calculating the y-partial derivative of $x^{1/3} y^{2/3}$ we have $\frac{2x^{1/3}}{3y^{1/3}}$ which is continuous to $x$ values near 0, however it is not coninous in $x=0$, therefore we can't confirm there is an unique solution to it

---

# **First‑Order Differential Equations**

---

## **Separable Equations**

4. Solve the following separable equations (no need to simplify constants):  
   a) $y' = x^2 y^3$  

   We rewrite the equation to:
  
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
   -\frac{3}{2x^3} = y^2 \rightarrow y = if(x), i\in \mathbb{C}
   $$

   Therefore we can't find a solution to it, at least not in $\mathbb{R}$
   
   b) $y' = \frac{x}{1+y^2}$

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

   c) $y' = (y-1)(y+2)$

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
   \int \\(1+\frac{3}{y-1}\\)dy=\int dx
   $$

   $$
   y + 3ln(y-1) = x
   $$

   However we can't isolate y, so the equation may have multiple solutions

5. Solve the IVPs:  
   a) $y' = xy,\; y(0)=3$

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
   \int \frac{dy}{y}=\int x dx \rightarrow ln(y) = \frac{x^2}{2}
   $$

   If an $e^x$ is applied to the equation we have

   $$
   y = e^{\frac{x^2}{2}} + C
   $$

   $C$ constant. Taking the initial value we have

   $$
   y(0) = e^{\frac{0^2}{2}} + C = e^{0} + C = 1 + C = 3 \rightarrow C = 2
   $$

   Therefore $y = e^{\frac{x^2}{2}} + 2$
   
   b) $y' = (1+y^2)\cos x,\; y(0)=0$

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
   \int \frac{dy}{(1+y^2)}=\int \cos x dx \rightarrow \arctan(y) = \sin x
   $$

   If $\tan x$ is applied to the equation we have

   $$
   y = \tan(\sin x) + C
   $$

   $C$ constant. Taking the initial value we have

   $$
   y(0) = \tan(\sin(0)) + C = \tan(0) + C = 0 + C = 0 \rightarrow C = 0
   $$

   Therefore $y = \tan(\sin x)$

6. Determine all equilibrium solutions and classify their stability:  
   a) $y' = y(3-y)$  

   An equilibrium solution is a constant solution $y(t)=C$ such that $y'=0$.

   So we equalize the right side to $0$:

   $$
   y(3-y)=0 \rightarrow y=0 \or y=3
   $$

   So the equilibrium solutions are $y=0$ and $y=3$.
   Now, the idea is to check what happens with solutions near each equilibrium, we can use the derivative criteria of $f(y)$ where

   $$
   y'=f(y)=y(3-y) \rightarrow f'(y)=3-2y
   $$

   If we set $y=0$, $f'(0)=3-0=3>0$. If $f'(y*)>0$, then the equilibrium $y*$ is unstable (near solutions go away).

   If we set $y=3$, $f'(3)=3-6=-3<0$. If $f'(y*)<0$, then the equilibrium $y*$ is asintotically stable (near solutions get close).

   b) $y' = y^2 - 4$

   Let's equalize $y^2-4=0$, so the equilibrium solutions are $y=2$ and $y=-2$, so we use the derivative criteria of $f(y)$ where

   $$
   y'=f(y)=y^2-4 \rightarrow f'(y)=2y
   $$

   If we set $y=-2$, $f'(-2)=2(-2)=-4<0$. If $f'(y*)<0$, then the equilibrium $y*$ is asintotically stable (near solutions get close).

   If we set $y=2$, $f'(2)=2(2)=4>0$. If $f'(y*)>0$, then the equilibrium $y*$ is unstable (near solutions get away).

---

## **Exact Equations**

7. Determine whether each equation is exact. If exact, solve it:  
   a) $(3x^2 + 2y)dx + (2x + 4y^3)dy = 0$

   $$
   M(x,y) = 3x^2 + 2y \rightarrow \frac{\partial M}{\partial y} = 2
   N(x,y) = 2x + 4y^3 \rightarrow \frac{\partial N}{\partial x} = 2
   $$
   
   Since $\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}$, the DE is exact. Then we solve the DE, first we inegrate $M$
   
   $$
   \int M(x,y)dx = \int (3x^2+2y)dx=\int 3x^2 dx + \int 2y dx = x^3+2yx + h(y)
   $$
   
   Now we take the derivative of this result on $y$ and equalize to $N$ having
   
   $$
   \frac{d}{dy}\\(x^3+2yx+h(y)\\)=N(x,y)=2x+4y^3 \rightarrow 2x + h'(y)=2x+4y^3 \rightarrow h'(y) = 2x+4y^3-2x=4y^3
   $$

   If we integrate $h'(y)$ on y we have that $h(y)=y^4$. Therefore the solution to the DE is $x^3+3xy+y^4=C$

   b) $(y\cos x - 2x)dx + (\sin x + x^2)dy = 0$
   
   $$
   M(x,y) = y\cos x -2x \rightarrow \frac{\partial M}{\partial y} = \cos x
   N(x,y) = \sin x + x^2 \rightarrow \frac{\partial N}{\partial x} = \cos x
   $$
   
   Since $\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}$, the DE is exact. Then we solve the DE, first we inegrate $M$
   
   $$
   \int M(x,y)dx = \int (y\cos x - 2x)dx=\int y\cos x dx - \int 2x dx = y\sin x - x^2 + h(y)
   $$
   
   Now we take the derivative of this result on $y$ and equalize to $N$ having
   
   $$
   \frac{d}{dy}\\(y\sin x - x^2 + h(y)\\) = N(x,y) = \sin x + x^2 \rightarrow \sin x + h'(y) = \sin x + x^2 \rightarrow h'(y) = x^2
   $$

   If we integrate $h'(y)$ on y we have that $h(y)=yx^2$. Therefore the solution to the DE is $y\sin x -x^2 + yx^2=C$

8. Find an integrating factor (if it exists) depending only on $x$ or only on $y$:  
   a) $(2xy - y)dx + (x^2 - x)dy = 0$
   
   $$
   M(x,y) = 2xy - y \rightarrow \frac{\partial M}{\partial y} = x - 1
   N(x,y) = x^2 - x \rightarrow \frac{\partial N}{\partial x} = x - 1
   $$
   
   Since $\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}$, the DE is exact. Therefore the integrating factor is $\mu = 1$
   b) $(y + x e^{xy})dx + (x + y e^{xy})dy = 0$
   
   $$
   M(x,y) = y + x e^{xy} \rightarrow \frac{\partial M}{\partial y} = 1 + x^2 e^{xy}
   N(x,y) = x + y e^{xy} \rightarrow \frac{\partial N}{\partial x} = 1 + y^2 e^{xy}
   $$
   
   Since $\frac{\partial M}{\partial y}\neq\frac{\partial N}{\partial x}$, the DE is not exact. 
   Now we have to prove either there exist an integrating factor dependant on $x$ or dependant on $y$. However
   - If $\frac{M_y - N_x}{N}=f(x)\rightarrow \mu = \mu(x)$
   - If $\frac{N_x - M_y}{M}=g(y)\rightarrow \mu = \mu(y)$

   Then we calculate $M_y - N_x = (1 + x^2 e^{xy}) - (1 + y^2 e^{xy}) = (x^2 - y^2)e^{xy}$, and now we test first $\mu(x)$
   
   $$
   \frac{M_y - N_x}{N} = \frac{(x^2 - y^2)e^{xy}}{x + y e^{xy}}
   $$

   However, it still depends on both, testing on $\mu(y)$ we have a similar situation, so there is no integrating factor that depends only on either $x$ or $y$

---

## **Linear First‑Order Equations**

9. Solve using the integrating factor method:  
   a) $y' + 3y = e^{-x}$
   Since the equation matches the general form $P(x) = 3$ and $Q(x) = e^{-x}$, then the integrating factor has the form:
   
   $$
   \mu(x) = e^{\int P(x)dx} \rightarrow \mu(x) = e^{\int 3dx} \rightarrow \mu(x) = e^{3x}
   $$

   Then we multiply $\mu(x)$ to the entire equation
   
   $$
   \mu(x)y'+3(\mu(x))y = \mu(x)e^{-x}
   $$
   
   We recognize the derivative as:
   
   $$
   (\mu(x)y)' = \mu(x)e^{-x} \rightarrow \\(e^{3x}y\\)' = e^{3x}e^{-x} \rightarrow \\(e^{3x}y\\)' = e^{2x}
   $$
   
   Then we integrate on x, having
   
   $$
   \int \\(e^{3x}y\\)' =  \int e^{2x} \rightarrow e^{3x}y = \frac{1}{2}e^{2x} + C \rightarrow y = \frac{e^{-x}}{2} + Ce^{-x}
   $$

   b) $y' - \frac{2}{x}y = x^3$
   Since the equation matches the general form $P(x) = \frac{2}{x}$ and $Q(x) = x^3$, then the integrating factor has the form:
   
   $$
   \mu(x) = e^{\int P(x)dx} \rightarrow \mu(x) = e^{\int \frac{2}{x}dx} \rightarrow \mu(x) = e^{2ln(x)} = x^2
   $$
   
   Then we multiply $\mu(x)$ to the entire equation
   
   $$
   \mu(x)y'+\frac{2}{x}(\mu(x))y = \mu(x)x^3
   $$
   
   We recognize the derivative as:
   
   $$
   (\mu(x)y)' = \mu(x)x^3 \rightarrow \\(x^2 y\\)' = x^2 x^3 \rightarrow \\(e^{3x}y\\)' = x^5
   $$
   
   Then we integrate on x, having
   
   $$
   \int \\(x^2 y\\)' =  \int x^5 \rightarrow x^2 y = \frac{1}{6}x^6 + C \rightarrow y = \frac{x^4}{6} + \frac{C}{x^2}
   $$

   c) $y' + y\tan x = \sin x$
   Since the equation matches the general form $P(x) = \tan x$ and $Q(x) = \sin x$, then the integrating factor has the form:
   
   $$
   \mu(x) = e^{\int P(x)dx} \rightarrow \mu(x) = e^{\int \tan x dx} \rightarrow \mu(x) = e^{-\ln(\cos x)} = \sec x
   $$
   
   Then we multiply $\mu(x)$ to the entire equation
   
   $$
   \mu(x)y'+\tan x(\mu(x))y = \mu(x)\sin x
   $$
   
   We recognize the derivative as:
   
   $$
   (\mu(x)y)' = \mu(x)\sin x \rightarrow \\(\sec x y\\)' = \sec x \sin x \rightarrow \\(\sec x y\\)' = \tan x
   $$
   
   Then we integrate on x, having
   
   $$
   \int \\(\sec x y\\)' = \int \tan x \rightarrow \sec x y = -\ln(\cos x) + C \rightarrow y = -\frac{\ln(\cos x)}{\sec x} + C\cos x
   $$

10. Solve the IVPs:  
   a) $y' + 4y = 8,\; y(0)=1$
   Since the equation matches the general form $P(x) = 4$ and $Q(x) = 8$, then the integrating factor has the form:
   
   $$
   \mu(x) = e^{\int P(x)dx} \rightarrow \mu(x) = e^{\int 4 dx} \rightarrow \mu(x) = e^{4x}
   $$
   
   Then we multiply $\mu(x)$ to the entire equation
   
   $$
   \mu(x)y'+4(\mu(x))y = \mu(x)8
   $$
   
   We recognize the derivative as:
   
   $$
   (\mu(x)y)' = 8\mu(x) \rightarrow \\(e^{4x} y\\)' = 8e^{4x} \rightarrow \\(e^{4x} y\\)' = 8e^{4x}
   $$
   
   Then we integrate on x, having
   
   $$
   \int \\(e^{4x} y\\)' = \int 8e^{4x} \rightarrow e^{4x} y = 2e^{4x} + C \rightarrow y = 2 + Ce^{4x}
   $$
   
   Since we have $y(0)=1$, then $y(0) = 2 + Ce^{0} = 1 \rightarrow 2 + C = 1 \rightarrow C=-1$. Therefore the solution of the IVP is $y = 2 -e^{4x}$

   b) $y' - \frac{1}{x}y = x,\; y(1)=2$
   Since the equation matches the general form $P(x) = \frac{1}{x}$ and $Q(x) = x$, then the integrating factor has the form:
   
   $$
   \mu(x) = e^{\int P(x)dx} \rightarrow \mu(x) = e^{\int \frac{1}{x} dx} \rightarrow \mu(x) = e^{\ln x} = x
   $$
   
   Then we multiply $\mu(x)$ to the entire equation
   
   $$
   \mu(x)y'+\frac{1}{x}(\mu(x))y = \mu(x)x
   $$
   
   We recognize the derivative as:
   
   $$
   (\mu(x)y)' = x\mu(x) \rightarrow \\(x y\\)' = x^2 \rightarrow \\(x y\\)' = x^2
   $$
   
   Then we integrate on x, having
   
   $$
   \int \\(x y\\)' = \int x^{2} \rightarrow x y = \frac{x^3}{3} + C \rightarrow y = \frac{x^2}{3} + \frac{C}{x}
   $$
   
   Since we have $y(1)=2$, then $y(1) = \frac{1^2}{3} + \frac{C}{1} = 2 \rightarrow \frac{1}{3} + C = 2 \rightarrow C=\frac{5}{3}$. Therefore the solution of the IVP is $y = \frac{x^2}{3} + \frac{5}{3x}$

---

## **Substitution Methods**

### **Homogeneous**

11. Solve:  
   a) $y' = \frac{x+y}{x-y}$
   Let's substitute $y = vx, \quad y' = v + xv'$
   
   $$
   v + xv' = \frac{x(v+1)}{x(1-v)} \rightarrow xv' = \frac{x(v+1)-xv(1-v)}{x(1-v)}= \frac{(v+1)+(v^2 - v)}{1-v}=\frac{v^2+1}{1-v} \rightarrow v' = \frac{1}{x}\frac{v^2 +1}{1-v}
   $$

   We then make $v' = \frac{dv}{dx}$ and
   
   $$
   \frac{1-v}{v^2 +1}dv =\frac{dx}{x}
   $$

   So, if we split the equation we have that $\int \frac{dx}{x}=\ln x$, on the other side:
   
   $$
   \int \frac{1-v}{v^2 +1}dv=\int\frac{dv}{v^2 +1}-\int\frac{vdv}{v^2 +1}
   $$
   
   For Calculus we know that $\int\frac{dv}{v^2 +1}= \arctan(v)$ and let $u=v^2 +1$, so $du=2vdv\rightarrow vdv=\frac{du}{2}$, then
   
   $$
   \int \frac{1-v}{v^2 +1}dv = \arctan(v)- \frac{1}{2}\int\frac{du}{u}=\arctan(v)-\frac{1}{2}\ln(u)=\arctan(v)-\frac{1}{2}\ln(v^2 +1)
   $$
   
   So in the end we have the following equation
   
   $$
   \arctan(v)-\frac{1}{2}\ln(v^2 +1) =\ln(x) + C
   $$
   
   Considering $y=vx\rightarrow v\frac{y}{x}$, we substitute the value of $v$
   
   $$
   \arctan(\frac{y}{x})-\frac{1}{2}\ln(\frac{y}{x}^{2} +1) =\ln(x) + C
   $$

   By properties of $\ln$
   
   $$
   \ln(\frac{y}{x}^{2} +1)=\ln(\frac{x^2 + y^2}{x^2})=\ln(x^2 + y^2)-\ln(x^2)
   $$

   Therefore
   
   $$
   \arctan(\frac{y}{x})-\frac{1}{2}\\(\ln(x^2 + y^2)-\ln(x^2)\\) =  \arctan(\frac{y}{x})-\frac{1}{2}\ln(x^2 + y^2)-\frac{1}{2}\ln(x^2) = \arctan(\frac{y}{x})-\frac{1}{2}\ln(x^2 + y^2)+\frac{1}{2}2\ln(x) = \arctan(\frac{y}{x})-\frac{1}{2}\ln(x^2 + y^2)+\ln(x) =\ln(x) + C
   $$
   
   Finally having
   
   $$
   \arctan(\frac{y}{x})-\frac{1}{2}\ln(x^2 + y^2)= C
   $$
   
   Which is a valid form for an implicit solution

   b) $y' = \frac{y}{x} + \frac{x}{y}$
   Let's substitute $y = vx, \quad y' = v + xv'$
   
   $$
   v + xv' = \frac{vx}{x} + \frac{x}{vx} \rightarrow xv' = v+\frac{1}{v}-v=\frac{1}{v}\rightarrow v'=\frac{1}{vx}
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
   
   Considering $y=vx\rightarrow v\frac{y}{x}$, we substitute the value of $v$
   
   $$
   \frac{1}{2}\\(\frac{y}{x}\\)^2=\ln(x) + C
   $$
   
   where
   
   $$
   C = \\(\frac{y}{x}\\)^2 - \ln(x)
   $$
   
   Which is a valid form for an implicit solution

### **Bernoulli**

12. Solve:  
   a) $y' + y = y^3$
   For Bernoulli we use the substitution $v=y^{1-n}=y^{1-3}=y^{-2} \rightarrow v' = -\frac{2}{y^3}y'  \rightarrow y' = -\frac{y^3 v'}{2}=\frac{(v^{-1/2})^3 v'}{2}=\frac{v^{-3/2} v'}{2}$ then we have

   $$
   \frac{v^{-3/2} v'}{2} + v^{-1/2}=v^{-3/2}
   $$
   
   Then we dvide the equation by $v^{-3/2}$ having
   
   $$
   \frac{v'}{2} + v= 1 \rightarrow v' +2v = 2
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
   (\mu(x)v)' = 2\mu(x) \rightarrow \\(e^{2x}v\\)' = 2e^{2x}
   $$
   
   Then we integrate on x, having
   
   $$
   \int \\(e^{2x}v\\)' = \int 2e^{2x} \rightarrow e^{2x}v = e^{2x} + C \rightarrow v = 1 + Ce^{-2x}
   $$
   
   Then we substitute the value of $v=y^{-2}$ having
   
   $$
   y^{-2} = 1 +Ce^{-2x}\rightarrow y = \\(1 +Ce^{-2x}\\)^{-1/2}
   $$

   b) $y' - 2y = 3y^{-1}$
   For Bernoulli we use the substitution $v=y^{1-n}=y^{1-(-1)}=y^{2} \rightarrow v' = 2yy'  \rightarrow y' = \frac{v'}{2\sqrt(v)}$ then we have
   
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
   (\mu(x)v)' = 3\mu(x) \rightarrow \\(e^{-2x}v\\)' = 2e^{-2x}
   $$
   
   Then we integrate on x, having
   
   $$
   \int \\(e^{-2x}v\\)' = \int 3e^{-2x} \rightarrow e^{-2x}v = \frac{3}{2}e^{-2x} + C \rightarrow v = \frac{3}{2} + Ce^{2x}
   $$
   
   Then we substitute the value of $v=y^{2}$ having
   
   $$
   y^{2} = \frac{3}{2} +Ce^{2x}\rightarrow y = \\(1 +Ce^{-2x}\\)^{1/2}
   $$


### **Riccati (special case)**

13. Solve the Riccati equation given a particular solution $y_p = x$:  

   $$
   y' = y^2 - xy + x^2
   $$

   The Riccati form can be identified as $a(x)=1, b(x)=-x$ and $c(x)=x^2$, and we have the particular solution $y_p = x$, Then we apply the substitution $y = y_p + \frac{1}{v}$, where $y'=y_{p}'-\frac{v'}{v^2}= 1- \frac{v'}{v^2}$. Substituting this result in the original equation we have:

   $$
   v' + (2a(x)y_{p}(x)+b(x))v =-a(x)
   \rightarrow v' +(2(1)x-x)v=-1
   \rightarrow v' +xv =-1
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
   (\mu(x)v)' = -\mu(x) 
   \rightarrow \\(e^{\frac{x^2}{2}}v\\)' = -e^{\frac{x^2}{2}}
   $$

   Then we integrate on x, having

   $$
   \int \\(e^{\frac{x^2}{2}}v\\)' = \int -e^{\frac{x^2}{2}}
   \rightarrow e^{\frac{x^2}{2}}v = \int -e^{\frac{x^2}{2}} + C 
   \rightarrow v = E(x) + Ce^{\frac{x^2}{2}}
   $$

   where $E(x)=\int -e^{\frac{x^2}{2}}$. Then we substitute the value of $v=\frac{1}{y-y_p}$ having

   $$
   y-y_p = \frac{1}{E(x) + Ce^{\frac{x^2}{2}}}
   \rightarrow y = \frac{1}{E(x) + Ce^{\frac{x^2}{2}}} + y_p
   $$

### **Clairaut**

14. Solve the Clairaut equation:  
   
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

## **2.1 Homogeneous with Constant Coefficients**

15. Solve:  
   a) $y'' - 5y' + 6y = 0$
   We take the characteristic equation as
   $$
   r^2 -5r +6=0
   $$
   where we factorize $r=3$ and $r=2$ as solutions.
   Therefore, the solution is
   $$
   y = C_1 e^{3x} + C_2 e^{2x}
   $$

   b) $y'' + 4y = 0$
   We take the characteristic equation as
   $$
   r^2 + 4r =0 \rightarrow r(r+4) = 0
   $$
   Then we have the roots $r=0$ and $r=-4$
   $$
   y = C_1 e^{0x} + C_2 e^{-4x} = C_1 + C_2 e^{-4x}
   $$

   c) $y''' - 3y'' + 3y' - y = 0$
   We take the characteristic equation as
   $$
   r^3 -3r^2 + 3r -1 = 0 \rightarrow (r-1)^3 = 0
   $$
   Then we have the roots $r=1$
   $$
   y = C_1 e^{x} + C_2 xe^{x} + C_3 x^2 e^{x}
   $$


16. Solve the IVPs:  
   a) $y'' + y = 0,\; y(0)=2,\; y'(0)=1$
   We take the characteristic equation as
   $$
   r^2 + r = 0 \rightarrow r(r+1) = 0
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
   y'(x) = -C_1 e^{-x} \rightarrow y'(0) = -C_1 e^{-0} = 1 \rightarrow -C_1 = 1\rightarrow C_1 = -1
   $$
   Substituting the valñue of $C_1$ we have $C_2 = 3$.
   Therefore the solution to the equation is
   $$
   y = -e^{-x} + 3
   $$

   b) $y'' - 4y' + 4y = 0,\; y(0)=0,\; y'(0)=3$
   We take the characteristic equation as
   $$
   r^2 - 4r + 4 = 0 \rightarrow (r-2)^2 = 0
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
   y'(x) = C_2\\(e^{2x} + 2xe^{2x}\\) \rightarrow y'(0) = C_2\\(e^{2(0)} + 2(0)e^{2(0)}\\) = 3 \rightarrow C_2 = 3
   $$
   Finally we have $C_2 = 3$.
   Therefore the solution to the equation is
   $$
   y = 3xe^{2x}
   $$

---

## **2.2 Nonhomogeneous Equations**

### **Undetermined Coefficients**

17. Solve:  
   a) $y'' + y = \sin x$
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
   y_{p}' = A\cos(x) + B\sin(x)+ x(B\cos(x)-A\sin(x))
   y_{p}'' = B\cos(x) - A\sin(x) +B\cos(x) - A\sin(x) - x(A\cos(x) + B\sin(x)) = 2B\cos(x)-2A\sin(x)-x(A\cos(x)+B\sin(x))
   $$
   Substituting in the original equation we have
   $$
   y''+ y=\sin(x)
   \rightarrow 2B\cos(x)-2A\sin(x)-x(A\cos(x)+B\sin(x)) + x(A\cos(x)+B\sin(x))=\sin(x)
   \rightarrow 2B\cos(x)-2A\sin(x)=1*\sin(x) +0*\cos(x)
   $$
   Where we have the following equations system
   $$
   -2A = 1 \rightarrow A=-\frac{1}{2}
   2B = 0 \rightarrow B = 0
   $$
   Therefore, the final particular solution is
   $$
   y_p = x(A\cos(x) + B\sin(x))= x(-\frac{1}{2}\cos(x))=-\frac{1}{2}x\cos(x)
   $$
   Finally the General Solution is 
   $$
   y=C_1\cos(x)+C_2\sin(x)-\frac{1}{2}x\cos(x)
   $$

   b) $y'' - 3y' + 2y = e^{2x}$
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
   y_{p}' = e^{2x} + 2x e^{2x}
   y_{p}'' = 2e^{2x} + 2\\[e^{2x} + 2x e^{2x}\\] = 4e^{2x}+ 4xe^{2x}
   $$
   Substituting in the original equation we have
   $$
   y'' - 3y' + 2y = e^{2x}
   \rightarrow 4e^{2x} + 4x e^{2x} - 3e^{2x} - 6x e^{2x} + 2x e^{2x} = e^{2x}
   \rightarrow e^{2x}=e^{2x}
   $$
   Meaning the $y_p$ solution is right
   
   Finally the General Solution is 
   $$
   y=y_h + y_p = C_1e^{2x}+C_2e^{x} + xe^{2x}
   $$

   c) $y'' + 4y = 3x^2$
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
   y_{p}' = 2ax +b
   y_{p}'' = 2a
   $$
   We substitute it in the equation
   $$
   2a +4(ax^{2}+bx+c)=3x^2
   \rightarrow 2a +4ax^2 +4bx +4c = 3x^2
   $$
   so we have the following system
   $$
   4a = 3 \rightarrow a=\frac{3}{4}
   4b=0 \rightarrow b=0
   2a + 4c = 0 \rightarrow \frac{3}{2}+4c=0 \rightarrow c=-\frac{3}{8}
   $$
   Therefore, the final particular solution is
   $$
   y_p = \frac{3}{4}x^2 -\frac{3}{8}
   $$
   Finally the General Solution is 
   $$
   y=C_1\sin(x)+C_2\cos(x)+\frac{3}{4}x^2 -\frac{3}{8}
   $$

### **Annihilator Method**

18. Solve:  
   a) $y'' - y = e^{x} + x$  
   First we identify the annihilator $A=D^2(D -1)$.
   Then we apply it in the ODE

   $$
   A(D)L(D)y = 0 \rightarrow (D-1)D^2 (D^2 - 1)y=0
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

   b) $y''' = \sin x$
   Considering $g(x)=\sin x$, we propose the anihiliator $D^2 + 1$. Then we apply it in the ODE

   $$
   A(D)L(D)y = 0 \rightarrow (D^2+1)(D^3)y=0
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

### **Variation of Parameters**

19. Solve:  
   a) $y'' + y = \sec x$
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
   u_1' = \frac{W_1}{W} = -\frac{\tan(x)}{1}=-\tan(x) \rightarrow u_1 = \int (-\tan(x))dx = \ln(\cos(x)) + C
   $$

   and

   $$
   u_2' = \frac{W_2}{W} = \frac{1}{1} = 1 \rightarrow u_2 = \int dx = x
   $$

   Then

   $$
   y_p = u_1 y_1 + u_2 y_2 = \ln(cos(x))\cos(x) + x\sin(x)
   $$

   And finally

   $$
   y = C_1\cos(x) + C_2\sin(x) + \ln(cos(x))\cos(x) + x\sin(x)
   $$

   b) $y'' - y = \frac{1}{x}$
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
   u_1' = \frac{W_1}{W} = \frac{\frac{1}{x}e^{-x}}{2}=\frac{1}{2x}e^{-x} \rightarrow u_1 = \int \frac{1}{2x}e^{-x}dx = F_1(x) + C
   $$

   since, primitive doesn't exist for this function and

   $$
   u_2' = \frac{W_2}{W} = \frac{\frac{1}{x}e^{x}}{-2} = -\frac{1}{2x}e^{x}\rightarrow u_2 = -\int \frac{1}{2x}e^{x}dx = F_2(x) + C
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

## **2.3 Cauchy–Euler**

20. Solve:  
   a) $x^2 y'' + xy' - y = 0$
   To this exercise we try $y=x^{r}$, then we calculate the derivatives
   
   $$
   y' = rx^{r-1}
   y'' = r(r-1)x^{r-2}
   $$

   Then we substitute in the DE

   $$
   x^{2}r(r-1)x^{r-2} + xrx^{r-1} - x^{r} = 0 \rightarrow r(r-1)x^{r} + rx^{r} -x^{r}=0
   \rightarrow x^{r}\\[r(r-1)+r-1\\] = 0
   \rightarrow r^2 - r + r -1 = 0
   \rightarrow r^2 -1 = 0
   \rightarrow r = \pm 1
   $$

   Therefore the general solution is $y = C_1 x^{-1} + C_2 x$

   b) $x^2 y'' - 3xy' + 5y = x^3$
   To solve this, we first look at the homogeneous part of the equation such

   $$
   x^2 y'' - 3xy' + 5y = 0
   $$

   Let $y = x^{r}, y' = rx^{r-1}, y''= r(r-1)x^{r-2}$, and then substitute in the equation

   $$
   x^{2}r(r-1)x^{r-2} -3xrx^{r-1} + 5x^{r} = 0
   \rightarrow r(r-1) - 3r + 5 = 0
   \rightarrow r^{2} - r - 3r + 5 = 0
   \rightarrow r^{2} - 4r + 5 = (r - (2+i))(r - (2-i))=0
   $$

   So we have a solution $y= C_{1}x^{2}\cos(\ln(x)) + C_{2}x^{2}\sin(\ln(-x))$.

   Since RHS is $x^{3}$, we try $y_p = Ax^{3}$, $y' = 3Ax^{2}, y'' = 6Ax$ and substitute in the equation

   $$
   x^{2}(6Ax)-3x(3Ax^{2})+5(Ax^{3}) = x^{3}
   \rightarrow 6Ax^{3}-9Ax^{3}+5Ax^{3}=x^{3}
   \rightarrow 2Ax^{3}=x^{3}
   \rightarrow (2A)=1
   \rightarrow A=\frac{1}{2}
   $$

   Then $y_p = \frac{1}{2}x{3}$ and $y=C_{1}x^{2}\cos(\ln(x)) + C_{2}x^{2}\sin(\ln(-x)) + \frac{1}{2}x{3}$

---

# **3. Nonlinear Differential Equations**

21. Solve the autonomous equations and classify equilibria:  
   a) $y' = y^2 - y$  
   b) $y' = y(4 - y^2)$

22. Solve the nonlinear ODE:  
   a) $y'' = y^2$  
   b) $y'' + y^3 = 0$

23. Determine whether the following nonlinear ODEs admit closed‑form solutions:  
   a) $y' = e^{y^2}$  
   b) $y' = \frac{1}{1+y^4}$

---

# **4. Systems of Differential Equations**

---

## **4.1 Linear Systems**

24. Solve the system:  
   $$
   \mathbf{x}' = 
   \begin{pmatrix}
   2 & 1 \\
   0 & 3
   \end{pmatrix}
   \mathbf{x}
   $$

25. Solve the system:  
   $$
   \mathbf{x}' = 
   \begin{pmatrix}
   0 & -1 \\
   1 & 0
   \end{pmatrix}
   \mathbf{x}
   $$

26. Classify the equilibrium point for each system:  
   a)  
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
   b)  
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

## **4.2 Nonlinear Systems**

27. Linearize the system near the equilibrium and classify:  
   a)  
   $$
   x' = x(1-y),\quad y' = y(x-1)
   $$  
   b)  
   $$
   x' = y - x^2,\quad y' = -x - y
   $$

---

# **5. Series Solutions**

---

## **5.1 Power Series**

28. Find a power series solution about $x=0$:  
   a) $y'' - xy = 0$  
   b) $y'' + y = 0$

29. Determine the recurrence relation for the ODE:  
   $$
   y'' + x y' + y = 0
   $$

---

## **5.2 Frobenius Method**

30. Solve using Frobenius near $x=0$:  
   a) $x^2 y'' + xy' + y = 0$  
   b) $x^2 y'' - xy' + y = 0$

---

# **6. Modeling with Differential Equations**

31. A tank initially contains 50 L of pure water. Brine with 0.2 kg/L enters at 3 L/min; mixture leaves at 2 L/min.  
   a) Set up the differential equation.  
   b) Solve for the amount of salt.

32. A population grows according to the logistic model with carrying capacity 5000 and intrinsic rate 0.3.  
   a) Write the differential equation.  
   b) Solve for $P(t)$.

33. A mass‑spring system satisfies:  
   $$
   m y'' + c y' + ky = 0
   $$  
   For $m=1$, $c=4$, $k=5$:  
   a) Classify the damping.  
   b) Solve the ODE.

34. An RLC circuit satisfies:  
   $$
   L I' + RI + \frac{1}{C}\int Idt = E(t)
   $$  
   Convert to a second‑order ODE and solve for $I(t)$ when $E(t)=E_0\sin(\omega t)$.

35. A chemical reaction satisfies:  
   $$
   \frac{dA}{dt} = -kA^2
   $$  
   Solve for $A(t)$ and determine the half‑life.

---
