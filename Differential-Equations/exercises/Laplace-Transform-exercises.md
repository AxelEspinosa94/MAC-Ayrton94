
---

# **Laplace Transform**  
---

## **1. Transform Basics and Existence Conditions**

### **Exercise 1.1 — Compute basic Laplace transforms**
Compute the Laplace transform of each function:

1. $f(t) = 5$

    $$
    \begin{align*}
    \mathcal{L}\{5\}(s)=5\mathcal{L}\{1\}(s)  \\
    =5\cdot\frac{1}{s}    \\
    =\frac{5}{s}
    \end{align*}
    $$

2. $f(t) = t^3$

    $$
    \begin{align*}
    \mathcal{L}\{t^{3}\}(s)=\frac{3!}{s^{3}}    \\
    =\frac{6}{s^{3}}
    \end{align*}
    $$

3. $f(t) = e^{-4t}$

    $$
    \begin{align*}
    \mathcal{L}\{e^{-4t}\}(s)=\int_{0}^{\infty}e^{-(s-4)t}dt    \\
    = \frac{1}{s-4},\quad s>4
    \end{align*}
    $$

4. $f(t) = \sin{(7t)}$

    $$
    \begin{align*}
    \mathcal{L}\{\sin{(7t)}\}(s)=\frac{7}{s^{2}+49}
    \end{align*}
    $$

5. $f(t) = t e^{2t}$

    $$
    \begin{align*}
    \mathcal{L}\{t e^{2t}\}(s)=\int_{0}^{\infty}e^{-st}te^{2t}dt    \\
    =\int_{0}^{\infty}te^{(2-s)t}dt    \\
    \end{align*}
    $$

    We will integrate this by parts, so let $u=t,\quad dv=e^{(2-s)t}$, then $du=dt,\quad v=\frac{1}{2-s}e^{(2-s)t}$, so 

    $$
    \begin{align*}
    \int_{0}^{\infty}te^{(2-s)t}dt=\left[t\frac{1}{2-s}e^{(2-s)t}\right]_{0}^{\infty}-\frac{1}{2-s}\int_{0}^{\infty}e^{(2-s)t}dt  \\
    =\frac{1}{2-s}\left[\left(te^{(2-s)t}\right)_{0}^{\infty}-\mathcal{L}\{e^{2t}\}(s)\right]
    \end{align*}
    $$

    since $s>2$, $\mathcal{L}\{e^{2t}\}(s)=\frac{1}{s-2}$, besides $2-s<0$, which means that when $t\rightarrow\infty,\quad \frac{t}{e^{(2-s)t}}\rightarrow 0$ (This can be demonstrated by L'Hopital). So

    $$
    \begin{align*}
    \mathcal{L}\{t e^{2t}\}(s)=\frac{1}{2-s}\left[0-\frac{1}{s-2}\right]   \\
    = \frac{1}{2-s}\left[\frac{1}{s-2}\right] \\
    = \frac{1}{(s-2)^{2}}
    \end{align*}
    $$

---

### **Exercise 1.2 — Existence of the Laplace transform**
For each function, determine whether the Laplace transform exists. Justify using exponential order.

1. $f(t) = t^2 e^{3t}$

    The Laplace transform for this function is

    $$
    \begin{align*}
    \mathcal{L}\{t^{2}e^{3t}\}(s)=\frac{2!}{(s-3)^{3}}  \\
    =\frac{2}{(s-3)^{3}}
    \end{align*}
    $$

    that exists for $s>3$

2. $f(t) = e^{t^2}$

    It is said to be of exponential order $\alpha$ if there exist constants $M>0,\quad\alpha\in\mathcal{R}$, and $T>0$ such that

    $$
    \begin{align*}
    |e^{t^2}|\leq Me^{\alpha t}
    \end{align*}
    $$

    In general $e^{t^{2}}>0,\quad \forall t\in\mathcal{R}$, so the expression becomes

    $$
    \begin{align*}
    e^{t^2}\leq Me^{\alpha t}   \\
    t^{2}\leq \ln{(M)}+\alpha t
    \end{align*}
    $$

    However $t^{2}$ grows faster than any linear function, which implies there is no values for $\alpha,M>0$ satisfying the exponential order definition. Therefore, the Laplace transform does not exist for $f$.

3. $f(t) = \ln(t+1)$

    By the definition of exponential order we have

    $$
    |\ln{(t+1)}|\leq Me^{\alpha t}
    $$

    Where $f>0$ if $t>0$. Considering this, if we apply $e^{x}$ to both sides we have

    $$
    t+1\leq e^{Me^{\alpha t}}
    $$

    where $t+1$ grows slower than the exponential function for $M\alpha > 0$. This means the Laplace transform exists for $s>0$

4. $f(t) = \frac{1}{t+2}$

    $f$ behaves like $\frac{1}{t}$ which grows slower than the exponential function for all $M,\alpha >0$, therefore, the Laplace transform exists for $s>0$

5. f(t) = e^{-5t}\sin(3t)

    Sin function oscilates between 0 and 1, which means 

    $$
    f(t)\leq e^{-5t}
    $$

    which actually fits in the exponential order definition, therefore, the Laplace transform exists for $s>-5$

---

## **2. Laplace Transform of Elementary Functions**

### **Exercise 2.1 — Using properties**
Compute:

1. $\mathcal{L}\{e^{3t}\cos{(2t)}\}$

    $$
    \begin{align*}
    \mathcal{L}\{e^{3t}\cos{(2t)}\} = \int_{0}^{\infty}e^{3t}\cos{(2t)}e^{-st}dt  \\
    =\int_{0}^{\infty}e^{(3-s)t}\cos{(2t)}dt
    \end{align*}
    $$

    Let $u=\cos{(2t)},\quad dv=e^{(3-s)t}dt$, then $du=-2\sin{(2t)},\quad v=\frac{e^{(3-s)t}}{3-s}$. Then

    $$
    \int_{0}^{\infty}e^{(3-s)t}\cos{(2t)}dt=\left[\cos{(2t)}\frac{e^{(3-s)t}}{3-s}\right]_{0}^{\infty}+\frac{2}{3-s}\int_{0}^{\infty}e^{(3-s)t}\sin{(2t)}dt
    $$

    Since $s>3$, then $e^{(3-s)t}=e^{-(s-3)t}\rightarrow 0$, and $|\cos{(2t)}|\leq 1$. So

    $$
    \lim_{t\rightarrow\infty}\frac{e^{-(s-3)t}\cos{(2t)}}{3-2}=0
    $$

    On the other hand, in $t=0$

    $$
    \frac{e^{0}\cos{(0)}}{3-s}=\frac{1}{3-s}
    $$

    So, the first part of the integral is

    $$
    \left[\cos{(2t)}\frac{e^{(3-s)t}}{3-s}\right]_{0}^{\infty}=0-\left(\frac{1}{3-s}\right)=\frac{1}{s-3}
    $$

    Then we have

    $$
    \begin{align*}
    \int_{0}^{\infty}e^{(3-s)t}\cos{(2t)}dt=\frac{1}{s-3}+\frac{2}{3-s}\int_{0}^{\infty}e^{(3-s)t}\sin{(2t)}dt  \\
    =\frac{1}{s-3}\left(1-2\int_{0}^{\infty}e^{(3-s)t}\sin{(2t)}dt\right)
    \end{align*}
    $$

    Let $I_c = \int_{0}^{\infty}e^{(3-s)t}\cos{(2t)}dt$ and $I_s = \int_{0}^{\infty}e^{(3-s)t}\sin{(2t)}dt$ where

    $$
    I_c = \frac{1}{s-3}(1-2I_s)
    $$

    This is a recursive equation, so our next move is to solve $I_s$ and to obtain a expression in terms of $I_c$. So, let $u=\sin{(2t)},\quad dv=e^{(3-s)t}dt$, then $du=2\cos{(2t)},\quad v=\frac{e^{(3-s)t}}{3-s}$. Then

    $$
    \begin{align*}
    I_s =\int_{0}^{\infty}e^{(3-s)t}\sin{(2t)}dt=\left[\sin{(2t)}\frac{e^{(3-s)t}}{3-s}\right]_{0}^{\infty}-\frac{2}{3-s}\int_{0}^{\infty}e^{(3-s)t}\cos{(2t)}dt \\
    = 0 - \frac{2}{3-s}I_c
    \end{align*}
    $$

    Substituting in the first result we have

    $$
    \begin{align*}
    I_c=\frac{1}{s-3}(1-2\left(-\frac{2}{3-s}I_c\right))   \\
    \Rightarrow\frac{1}{s-3}(1-\frac{4}{s-3}I_c)   \\
    \Rightarrow I_c=\frac{1}{s-3}-\frac{4}{(s-3)^{2}}I_c  \\
    \Rightarrow I_c\left(1+\frac{4}{(s-3)^{2}}\right)=\frac{1}{s-3}   \\
    \Rightarrow I_c\left(\frac{(s-3)^{2} + 4}{(s-3)^{2}}\right)=\frac{1}{s-3}   \\
    \Rightarrow I_c\left((s-3)^{2}+4\right)= s-3    \\
    \Rightarrow I_c=\frac{s-3}{(s-3)^{2}+4}
    \end{align*}
    $$

    $\therefore\mathcal{L}\{e^{3t}\cos{(2t)}\}=\frac{s-3}{(s-3)^{2}+4}$.

    Using the First shifting theorem we have

    $$
    \mathcal{L}\{e^{3t}\cos{(2t)}\}=F(s-3)
    $$

    where $F(s)=\mathcal{L}\{\cos{(2t)}\}(s)=\frac{s}{s^{2}+2^{2}}=\frac{s}{s^{2}+4}$.

    So, $F(s-3)=\frac{s-3}{(s-3)^{2}+4}$

2. $\mathcal{L}\{t^2 e^{-t}\}$

    By the first shifting theorem

    $$
    \mathcal{L}\{t^2 e^{-t}\}=F(s+1)
    $$

    where

    $$
    F(s)=\mathcal{L}\{t^{2}\}(s)=\frac{2!}{s^{3}}=\frac{2}{s^3}
    $$

    So $F(s+1)=\frac{2}{(s+1)^3}$

3. $\mathcal{L}\{t\sin{(4t)}\}$

    By the Differentiation property in s-domain. If $\mathcal{L}\{f(t)\}(s)=F(s)$, then

    $$
    \mathcal{L}\{tf(t)\}(s) = -F'(s)
    $$

    So, $F(s)=\mathcal{L}\{\sin{(4t)}\}(s)=\frac{4}{s^{2}+16}$, and

    $$
    \begin{align*}
    F'(s)=\frac{d}{ds}\frac{4}{s^{2}+16}    \\
    =-\frac{8s}{(s^{2}+16)^{2}}
    \end{align*}
    $$

    Therefore

    $$
    \mathcal{L}\{t\sin{(4t)}\}=-\left(-\frac{8s}{(s^{2}+16)^{2}}\right)=\frac{8s}{(s^{2}+16)^{2}}
    $$

4. $\mathcal{L}\{t^3 f(t)\}$ given $\mathcal{L}\{f(t)\}=F(s)$

    Again, by the differentiation property in s-domain, If $\mathcal{L}\{f(t)\}(s)=F(s)$, then

    $$
    \mathcal{L}\{t^{3}f(t)\}(s) = (-1)^{3}F^{(3)}(s) = -F'''(s)
    $$

5. $\mathcal{L}\{f'(t)\}$ in terms of $F(s)$, $f(0)$

    By the differentiation property in time domain, we know that

    $$
    \mathcal{L}\{f'(t)\}(s)=sF(s)-f(0)
    $$

---

## **3. Fundamental Theorems**

### **Exercise 3.1 — First shifting theorem**
Compute:

1. $\mathcal{L}\{e^{5t}\sin{(3t)}\}$

    $$
    \begin{align*}
    F(s)=\mathcal{L}\{f(t)\}(s)=\mathcal{L}\{\sin{(3t)}\}(s)    \\
    = \frac{3}{s^{2}+9}
    \end{align*}
    $$

    So $F(s-5)=\frac{3}{(s-5)^{2}+9}$.

2. $\mathcal{L}\{e^{-2t}t^2\}$

    $$
    F(s)=\mathcal{L}\{t^{2}\}=\frac{2}{s^{3}}
    $$

    So, $F(s+2)=\frac{2}{(s+2)^{3}}$.

---

### **Exercise 3.2 — Differentiation in the s-domain**
Given $F(s)=\mathcal{L}\{f(t)\}$, compute:

1. $\mathcal{L}\{t f(t)\}$

    $$
    \mathcal{L}\{t f(t)\}= -F'(s)
    $$

2. $\mathcal{L}\{t^2 f(t)\}$

    $$
    \mathcal{L}\{t^{2} f(t)\}= (-1)^{2}F''(s)=F''(s)
    $$

3. $\mathcal{L}\{t e^{-3t}\}$

    $$
    \mathcal{L}\{t e^{-3t}\}= -F'(s)=-\frac{1}{s-(-3)}=-\frac{1}{s+3}
    $$

---

## **4. Inverse Laplace Transform**

### **Exercise 4.1 — Basic inverse transforms**
Find:

1. $\mathcal{L}^{-1}\left\{\frac{3}{s^2+9}\right\}$

    We know $\mathcal{L}\{\sin{(3t)}\}(s)=\frac{3}{s^{2}+9}$. Thus

    $$
    \mathcal{L}^{-1}\left\{\frac{3}{s^2+9}\right\}=\sin{(3t)}
    $$

2. $\mathcal{L}^{-1}\left\{\frac{s}{(s+2)^2+16}\right\}$

    We write $\frac{s}{(s+2)^2+16}$ in terms of $s+2$

    $$
    \begin{align*}
    \frac{s}{(s+2)^2+16}=\frac{(s+2)-2}{(s+2)^{2}+16}   \\
    =\frac{(s+2)}{(s+2)^{2}+16}-\frac{2}{(s+2)^{2}+16}
    \end{align*}
    $$

    The first term is

    $$
    \frac{(s+2)}{(s+2)^{2}+16}=\mathcal{L}\{e^{-2t}\cos{(4t)}\}(s)
    $$

    as we demonstrated in Section 2.1. On the other hand

    $$
    \frac{2}{(s+2)^{2}+16}=\mathcal{L}\{e^{-2t}\sin{(4t)}\}(s)
    $$

    Therefore, $f(t)$ is

    $$
    f(t)= e^{-2t}\cos{(4t)}-e^{-2t}\sin{(4t)}=e^{-2t}\left(\cos{(4t)}-\sin{(4t)}\right)
    $$

3. $\mathcal{L}^{-1}\left\{\frac{5}{(s-3)^3}\right\}$

    We can rewrite the expression as

    $$
    \frac{5}{(s-3)^3}=\frac{5}{2}\frac{2}{(s-3)^{3}}
    $$

    By definition $\mathcal{L}\{t^{2}\}(s)=\frac{2}{s^{3}}$. And by the first shifting theorem $\mathcal{L}\{e^{3t}t^{2}\}(s)=F(s-3)=\frac{2}{(s-3)^{3}}$

    $$
    \begin{align*}
    \mathcal{L}^{-1}\left\{\frac{5}{(s-3)^3}\right\}=\mathcal{L}^{-1}\left\{\frac{5}{2}\frac{2}{(s-3)^3}\right\}    \\
    =\frac{5}{2}\mathcal{L}^{-1}\left\{\frac{2}{(s-3)^3}\right\}    \\
    =\frac{5}{2}e^{3t}t^{2}
    \end{align*}
    $$

---

### **Exercise 4.2 — Partial fractions**
Compute:

1. $\mathcal{L}^{-1}\left\{\frac{2s+7}{s^2+4s+5}\right\}$

    Completing the square an through some algebra gives us

    $$
    \begin{align*}
    \frac{2s+7}{(s+2)^{2}+1}    \\
    \Rightarrow \frac{2(s+2)+3}{(s+2)^{2}+1}    \\
    \Rightarrow 2\frac{s+2}{(s+2)^{2}+1}+\frac{3}{(s+2)^{2}+1}    \\
    \Rightarrow 2\frac{s+2}{(s+2)^{2}+1}+3\frac{1}{(s+2)^{2}+1}
    \end{align*}
    $$

    Considering the first shifting theorem and that $\mathcal{L}\{\cos{(t)}\}=\frac{s}{s^{2}+1}$ and $\mathcal{L}\{\sin{(t)}\}=\frac{1}{s^{2}+1}$, then

    $$
    2\frac{s+2}{(s+2)^{2}+1}+3\frac{1}{(s+2)^{2}+1} = 2\mathcal{L}\{e^{-2t}\cos{(t)}\} + 3\mathcal{L}\{e^{-2t}\sin{(t)}\}
    $$

    Therefore

    $$
    \mathcal{L}^{-1}\left\{\frac{2s+7}{s^2+4s+5}\right\}=2e^{-2t}\cos{(t)}+3e^{-2t}\sin{(t)}
    $$

2. $\mathcal{L}^{-1}\left\{\frac{3s+1}{s(s+2)}\right\}$

    We perform partial fractions as

    $$
    \begin{align*}
    \frac{3s+1}{s(s+2)}=\frac{A}{s}+\frac{B}{s+2}   \\
    \Rightarrow 3s+1=A(s+2)+ Bs \\
    \Rightarrow 3s+1=(A+B)s +2A    \\
    \Rightarrow 1=2A\rightarrow A=\frac{1}{2}\quad A+B=3\rightarrow B=\frac{5}{2}   \\
    \Rightarrow \frac{3s+1}{s(s+2)}=\frac{1}{2s}+\frac{5}
    {2(s+2)}   \\
    \Rightarrow \frac{3s+1}{s(s+2)}=\frac{1}{2}\frac{1}{s}+\frac{5}{2}\frac{1}{s+2}
    \end{align*}
    $$

    By definition $\mathcal{L}^{-1}\left(\frac{1}{s}\right)=1$ and $\mathcal{L}^{-1}\left(\frac{1}{s+2}\right)=e^{-2t}$.

    Therefore

    $$
    \mathcal{L}^{-1}\left\{\frac{3s+1}{s(s+2)}\right\}=\frac{1}{2}+\frac{5}{2}e^{-2t}
    $$

3. $\mathcal{L}^{-1}\left\{\frac{4}{(s+1)(s^2+9)}\right\}$

    We perform partial fractions as

    $$
    \begin{align*}
    \frac{4}{(s+1)(s^2+9)}=\frac{A}{s+1}+\frac{Bs+C}{s^{2}+9}   \\
    \Rightarrow 4=A(s^{2}+9)+ (Bs+C)(s+1) \\
    \Rightarrow 4=As^{2}+9A+ Bs^{2}+Bs + Cs + C \\
    \Rightarrow 4=(A+B)s^{2} + (B+C)s + 9A + C \\
    \Rightarrow A+B=0\rightarrow A=-B \quad -9B+C=4, B+C=0\rightarrow 10B=-4\rightarrow B=-\frac{4}{10}=-\frac{2}{5},\quad A = \frac{2}{5}=C   \\
    \Rightarrow \frac{4}{(s+1)(s^{2}+9)}=\frac{2}{5}\frac{1}{s+1}-\frac{2}{5}\frac{s-1}{s^{2}+9}    \\
    \Rightarrow \frac{4}{(s+1)(s^{2}+9)}=\frac{2}{5}\frac{1}{s+1}-\frac{2}{5}\left(\frac{s}{s^{2}+9}-\frac{1}{s^{2}+9}\right)    \\
    \Rightarrow \frac{4}{(s+1)(s^{2}+9)}=\frac{2}{5}\frac{1}{s+1}-\frac{2}{5}\left(\frac{s}{s^{2}+9}-\frac{1}{3}\frac{3}{s^{2}+9}\right)    \\
    \end{align*}
    $$

    By definition $\mathcal{L}^{-1}\left(\frac{1}{s+1}\right)=e^{-t}$.

    Moreover, $\mathcal{L}^{-1}\left(\frac{s}{s^{2}+9}\right)=\cos{(3t)}$, and $\mathcal{L}^{-1}\left(\frac{3}{s^{2}+9}\right)=\sin{(3t)}$

    Therefore

    $$
    \mathcal{L}^{-1}\left\{\frac{3s+1}{s(s+2)}\right\}=\frac{2}{5}e^{-t}-\frac{2}{5}\left[\cos{(3t)}-\frac{1}{3}\sin{(3t)}\right]
    $$

---

## **5. Step, Shifted, and Piecewise Functions**

### **Exercise 5.1 — Heaviside step function**
Compute the Laplace transform:

1. $f(t)=u(t-3)$

    $$
    \mathcal{L}\{u(t-3)\}(s)=\frac{e^{-3s}}{s}
    $$

    By the Proposition 1.13

2. $f(t)=u(t-2)(t-2)$

    $$
    \begin{align*}
    \mathcal{L}\{f(t)\}(s)=\mathcal{L}\{u(t-2)(t-2)\}(s)    \\
    =e^{-2s}\mathcal{L}\{t\}(s) \\
    =e^{-2s}\left[\mathcal{L}\{t\}(s)\right] \\
    =e^{-2s}\left[\frac{1}{s^{2}}\right]
    \end{align*}
    $$

3. $f(t)=u(t-1)\sin(t-1)$

    $$
    \begin{align*}
    \mathcal{L}\{f(t)\}(s)=\mathcal{L}\{u(t-1)\sin{(t-1)}\}(s)    \\
    =e^{-s}\mathcal{L}\{\sin{t}\}(s) \\
    =e^{-2s}\left[\frac{1}{s^{2}+1}\right]
    \end{align*}
    $$

---

### **Exercise 5.2 — Inverse Laplace with shifts**
Find:

1. $\mathcal{L}^{-1}\left\{e^{-4s}\frac{1}{s^2+1}\right\}$

    $$
    \begin{align*}
    e^{-4s}F(s)=e^{-4s}\frac{1}{s^2+1}  \\
    \Rightarrow F(s)=\frac{1}{s^{2}+1}=\mathcal{L}\{\sin{(t)}\} \\
    \Rightarrow \mathcal{L}^{-1}\left\{e^{-4s}\frac{1}{s^2+1}\right\}=u(t-4)\sin{(t-4)}
    \end{align*}
    $$

2. $\mathcal{L}^{-1}\left\{e^{-2s}\frac{s}{s^2+9}\right\}$

    $$
    \begin{align*}
    e^{-2s}F(s)=e^{-2s}\frac{s}{s^2+9}  \\
    \Rightarrow F(s)=\frac{s}{s^{2}+9}=\mathcal{L}\{\cos{(3t)}\} \\
    \Rightarrow \mathcal{L}^{-1}\left\{e^{-2s}\frac{s}{s^2+9}\right\}=u(t-2)\cos{(3(t-2))}
    \end{align*}
    $$

---

## **6. Periodic and Impulse Functions**

### **Exercise 6.1 — Periodic functions**
Let  

$$
f(t)=
\begin{cases}
1, & 0\le t<2,\\
0, & 2\le t<4,
\end{cases}
$$

with period $T=4$.  
Compute $\mathcal{L}\{f(t)\}$.

$$
\begin{align*}
\mathcal{L}\{f(t)\}=\frac{1}{1-e^{-4s}}\int_{0}^{4}(e^{-st}f(t))dt  \\
=\frac{1}{1-e^{-4s}}\left[\int_{0}^{2}e^{-st}dt+\int_{2}^{4}0dt\right]   \\
=\frac{1}{1-e^{-4s}}\int_{0}^{2}e^{-st}dt    \\
=\frac{1}{1-e^{-4s}}\left[-\frac{e^{-st}}{s}\right]_{0}^{2} \\
=\frac{1}{1-e^{-4s}}\left[-\frac{e^{-2s}-1}{s}\right]   \\
=\frac{1}{1-e^{-4s}}\left[\frac{1-e^{-2s}}{s}\right]   \\
=\frac{1}{(1-e^{-2s})(1+e^{-2s})}\left[\frac{1-e^{-2s}}{s}\right]   \\
=\frac{1}{1+e^{-2s}}\frac{1}{s}
\end{align*}
$$

---

### **Exercise 6.2 — Dirac delta**
Compute:

1. $\mathcal{L}\{\delta(t-3)\}$ 

    $$
    \mathcal{L}\{\delta(t-3)\}=e^{-3s}
    $$

2. $\mathcal{L}\{e^{2t}\delta(t-1)\}$

    $$
    \begin{align*}
    \mathcal{L}\{e^{2t}\delta(t-1)\}(s)=\int_{\mathcal{R}^{+}}e^{2t}e^{-st}\delta(t-1)dt    \\
    =\int_{\mathcal{R}^{+}}e^{(2-s)t}\delta(t-1)dt
    \end{align*}
    $$

    Let $r=2-s$, then

    $$
    \begin{align*}
    \mathcal{L}\{e^{2t}\delta(t-1)\}(s)=\int_{\mathcal{R}^{+}}e^{(2-s)t}\delta(t-1)dt   \\
    =\int_{\mathcal{R}^{+}}e^{rt}\delta(t-1)dt  \\
    =e^{r} \\
    =e^{(2-s)}
    \end{align*}
    $$

    Using the property $\mathcal{L}\{f(t)\delta(t-a)\}(s)=f(a)e^{-as}$. Then

    $$
    \mathcal{L}\{e^{2t}\delta(t-1)\}(s)=f(1)e^{-s}=e^{2}e^{-s}=e^{(2-s)}
    $$

3. $\mathcal{L}^{-1}\{e^{-5s}\}$

    $$
    \mathcal{L}^{-1}\{e^{-5s}\}=\delta(t-5)
    $$

---

## **7. Convolution**

### **Exercise 7.1 — Direct convolution**
Compute:

1. $(f*g)(t)$ for $f(t)=t$, $g(t)=e^{-t}$

    $$
    \begin{align*}
    (f*g)(t)=\int_{0}^{t}f(\tau)g(t-\tau)d\tau  \\
    =\int_{0}^{t}\tau e^{-(t-\tau)}d\tau    \\
    =\int_{0}^{t}\tau e^{(\tau-t)}d\tau
    \end{align*}
    $$

    Integrating by parts, let $u=\tau$, $dv=e^{(\tau-t)}d\tau$, then $du=d\tau$ and $v=e^{(\tau-t)}$. So

    $$
    \begin{align*}
    \int_{0}^{t}\tau e^{(\tau-t)}d\tau=\left[\tau e^{(\tau-t)}\right]_{0}^{t}-\int_{0}^{t}e^{(\tau-t)}d\tau \\
    =(te^{0}-0)-\int_{0}^{t}e^{(\tau-t)}    \\
    =t-\int_{0}^{t}e^{(\tau-t)}
    \end{align*}
    $$

    For the second integral, let $u=\tau-t$, $du=d\tau$. Then

    $$
    \begin{align*}
    t-\int_{0}^{t}e^{(\tau-t)}=t-\int_{0}^{t}e^{u}du    \\
    =t-\left[e^{u}\right]_{0}^{t}   \\
    =t-\left[e^{(\tau-t)}\right]_{0}^{t}   \\
    =t-(e^{0}-e^{-t})   \\
    =e^{-t}+ t-1
    \end{align*}
    $$

2. $(f*g)(t)$ for $f(t)=\sin{(t)}$, $g(t)=\cos{(t)}$

    $$
    \begin{align*}
    (f*g)(t)=\int_{0}^{t}f(\tau)g(t-\tau)d\tau  \\
    =\int_{0}^{t}(\sin{(\tau)}\cos{(t-\tau)})d\tau    \\
    =\int_{0}^{t}(\sin{(\tau)}(\cos{(t)}\cos{(\tau)}+\sin{(t)}\sin{(\tau)}))d\tau  \\
    =\cos{(t)}\int_{0}^{t}\cos{(\tau)}\sin{(\tau)}d\tau +\sin{(t)}\int_{0}^{t}\sin{(\tau)}^{2}d\tau
    \end{align*}
    $$

    For the first integral, Let $u=\sin{(\tau)},\quad du=\cos{(\tau)}d\tau$. Then

    $$
    \int_{0}^{t}\cos{(\tau)}\sin{(\tau)}d\tau =\int_{0}^{t}udu=\left[\frac{u^{2}}{2}\right]_{0}^{t}=\left[\frac{\sin{(\tau)}^{2}}{2}\right]_{0}^{t}=\frac{\sin{(t)}^{2}}{2}
    $$

    On the second one we perform the formula for the sine

    $$
    \begin{align*}
    \int_{0}^{t}\sin{(\tau)}^{2}d\tau=\left[\frac{1}{2}(\tau-\sin{(\tau)}\cos{(\tau)})\right]_{0}^{t}   \\
    =\frac{1}{2}(t-\sin{(t)}\cos{(t)})
    \end{align*}
    $$

    Finally, we substitute in the initial integral having

    $$
    \cos{(t)}\frac{\sin{(t)}^{2}}{2} +\sin{(t)}\frac{1}{2}(t-\sin{(t)}\cos{(t)})=\frac{t\sin{(t)}}{2}
    $$

---

### **Exercise 7.2 — Using convolution theorem**
Find:

1. $\mathcal{L}^{-1}\left\{\frac{1}{(s+1)(s+2)}\right\}$

    Using the convolution theorem

    $$
    \mathcal{L}\{(f*g)(t)\}(s)=F(s)G(s)
    $$

    We know that $\mathcal{L}\{e^{at}\}(s)=\frac{1}{s-a}$. Then

    $$
    \mathcal{L}\{e^{-t}\}=\frac{1}{s+1}
    $$

    and

    $$
    \mathcal{L}\{e^{-2t}\}=\frac{1}{s+2}
    $$ 

    Thus

    $$
    \frac{1}{(s+1)(s+2)}=\frac{1}{s+1}\frac{1}{s+2}\Rightarrow \mathcal{L}^{-1}\left\{\frac{1}{(s+1)(s+2)}\right\}=(e^{-t}*e^{-2t})(t)
    $$

    Finally, we compute the convolution:

    $$
    \begin{align*}
    (e^{-t}*e^{-2t})(t)=\int_{0}^{t}e^{-\tau}e^{-2(t-\tau)}d\tau \\
    =\int_{0}^{t}e^{-\tau}e^{(2\tau-2t)}d\tau \\
    =\int_{0}^{t}e^{-\tau}e^{(2\tau-2t)}d\tau \\
    =\int_{0}^{t}e^{(\tau-2t)}d\tau \\
    =e^{-2t}\int_{0}^{t}e^{(\tau)}d\tau \\
    =e^{-2t}\left[e^{\tau}\right]_{0}^{t}   \\
    =e^{-2t}\left[e^{t}-1\right]   \\
    =e^{-t}-e^{-2t}
    \end{align*}
    $$

2. $\mathcal{L}^{-1}\left\{\frac{1}{(s^2+1)^2}\right\}$

    Using the convolution theorem

    $$
    \mathcal{L}\{(f*g)(t)\}(s)=F(s)G(s)
    $$

    We know that $\mathcal{L}\{\sin{(t)}\}(s)=\frac{1}{s^{2}+1}$. Then

    $$
    \mathcal{L}\{\sin{(t)}\}=\frac{1}{s^{2}+1}
    $$

    Thus

    $$
    \frac{1}{(s^{2}+1)^{2}}=\frac{1}{s^{2}+1}\frac{1}{s^{2}+1}\Rightarrow \mathcal{L}^{-1}\left\{\frac{1}{(s^{2}+1)^{2}}\right\}=(\sin{(t)}*\sin{(t)})(t)
    $$

    Finally, we compute the convolution

    $$
    \begin{align*}
    (\sin{(t)}*\sin{(t)})(t)=\int_{0}^{t}\sin{(\tau)}\sin{(t-\tau)}d\tau \\
    =\int_{0}^{t}\sin{(\tau)}(\cos{(\tau)}\sin{t}-\cos{(t)}\sin{(\tau)})d\tau \\
    =\sin{t}\int_{0}^{t}\sin{(\tau)}\cos{(\tau)}-\cos{(t)}\int_{0}^{t}\sin{(\tau)}^{2}d\tau \\
    =\sin{(t)}\left[\frac{\sin{(\tau)}^{2}}{2}\right]_{0}^{t}-\cos{(t)}\left[\frac{1}{2}(\tau-\sin{(\tau)}\cos{(\tau)})\right]_{0}^{t}  \\
    =\sin{(t)}\frac{\sin{(t)}^{2}}{2}-\cos{(t)}\frac{t-\sin{(t)}\cos{(t)}}{2}    \\
    =\frac{\sin{(t)}^{3}}{2}-\frac{t\cos{(t)}-\sin{(t)}\cos{(t)}^{2}}{2}    \\
    =\frac{\sin{(t)}^{3}}{2}-\frac{t\cos{(t)}-\sin{(t)}(1-\sin{(t)}^{2})}{2}    \\
    =\frac{\sin{(t)}^{3}}{2}-\frac{t\cos{(t)}-\sin{(t)}+\sin{(t)}^{3}}{2}    \\
    =\frac{\sin{(t)}-t\cos{(t)}}{2}    \\
    \end{align*}
    $$

---

## **8. Solving ODEs with Laplace Transform**

### **Exercise 8.1 — First-order ODE**
Solve using Laplace transform:

$$
y' + 3y = 5e^{-2t},\quad y(0)=1.
$$

By linearity

$$
\begin{align*}
\mathcal{L}\{y'\}+3\mathcal{L}\{y\}= 5\mathcal{L}\{e^{-2t}\}    \\
\text{By shifting}  \\
\Rightarrow (sY-y(0))+3Y=5\mathcal{L}\{e^{-2t}\} \\
\Rightarrow (sY-1)+3Y=\frac{5}{s+2} \\
\Rightarrow (s+3)Y=\frac{s+7}{s+2}  \\
\Rightarrow Y=\frac{s+7}{(s+2)(s+3)}
\end{align*}
$$

We calculate the inverse transform of $Y$

First, we perform partial fractions

$$
\begin{align*}
\frac{s+7}{(s+2)(s+3)}=\frac{A}{s+2}+\frac{B}{s+3}  \\
\Rightarrow s+7=A(s+3)+B(s+2)   \\
\Rightarrow s+7=As+3A+Bs+2B \\
\text{where}    \\
A+B=1\rightarrow B=1-A,\quad\text{and}   \\
3A+2B=7\rightarrow 3A+2-2A=7\rightarrow A=5\rightarrow B=-4 \\
\frac{s+7}{(s+2)(s+3)}=\frac{5}{s+2}-\frac{4}{s+3}  
\end{align*}
$$

We apply the inverse and by linearity

$$
\mathcal{L}^{-1}\{Y\}=\mathcal{L}^{-1}\left\{\frac{5}{s+2}-\frac{4}{s+3}\right\}=5e^{-2t}-4e^{-3t}
$$

Therefore $y=5e^{-2t}-4e^{-3t}$

---

### **Exercise 8.2 — Second-order ODE**
Solve:

$$
y'' + 4y = \sin(2t),\quad y(0)=0,\quad y'(0)=1.
$$

By linearity

$$
\begin{align*}
\mathcal{L}\{y''\}+4\mathcal{L}\{y\}= \mathcal{L}\{\sin{(2t)}\}    \\
\text{By shifting}  \\
\Rightarrow (s^{2}Y-sy(0)-y'(0))+4Y=\frac{2}{s^{2}+4} \\
\Rightarrow (s^{2}Y-1)+4Y=\frac{2}{s^{2}+4} \\
\Rightarrow (s^{2}+4)Y=\frac{2}{s^{2}+4}+1  \\
\Rightarrow Y=\frac{2}{(s^{2}+4)^{2}}+\frac{1}{s^{2}+4}     \\
\Rightarrow Y=\frac{1}{2}\left(\frac{2}{s^{2}+4}\right)^{2}+\frac{1}{2}\frac{2}{s^{2}+4}
\end{align*}
$$

In the first term, we recognize the convolution, so when applying the inverse we have

$$
\mathcal{L}^{-1}\left\{\left(\frac{2}{s^{2}+4}\right)^{2}\right\}=(\sin{(2t)}*\sin{(2t)})=\frac{\sin{(2t)}-2t\cos{(2t)}}{4}
$$

Since $\mathcal{L}^{-1}\left\{\frac{2}{s^{2}+4}\right\}=\sin{(2t)}$. We have

$$
\begin{align*}
Y=\frac{1}{2}\left(\frac{2}{s^{2}+4}\right)^{2}+\frac{1}{2}\frac{2}{s^{2}+4}    \\
=\frac{1}{2}\left(\frac{\sin{(2t)}-2t\cos{(2t)}}{4}\right)+\frac{1}{2}\sin{(2t)}    \\
=\frac{5}{8}\sin{(2t)}-\frac{t}{4}\cos{(2t)}
\end{align*}
$$

---

### **Exercise 8.3 — ODE with step input**
Solve:

$$
y'' + y = u(t-3),\quad y(0)=0,\quad y'(0)=0.
$$

Let's apply the Laplace transform to the DE

$$
\mathcal{L}\{y''\}+\mathcal{L}\{y\}=\mathcal{L}\{u(t-3)\}
$$

By shifting and step

$$
\begin{align*}
\Rightarrow s^{2}Y-sy(0)-y'(0)+Y=\frac{e^{-3s}}{s}   \\
\Rightarrow (s^{2}+1)Y=\frac{e^{-3s}}{s}   \\
\Rightarrow Y =\frac{e^{-3s}}{s(s^{2}+1)}
\end{align*}
$$

For what it seems $y$ has the form $g(t)=u(t-a)f(t-a)$. Thus

$$
\begin{align*}
Y =\frac{e^{-3s}}{s(s^{2}+1)}    \\
\text{where}    \\
F(s)=\frac{1}{s(s^{2}+1)}
\end{align*}
$$

Let's use partial fractions, so

$$
\begin{align*}
\frac{1}{s(s^{2}+1)}=\frac{A}{s}+\frac{Bs+C}{s^{2}+1}   \\
\Rightarrow 1=A(s^{2}+1)+s(Bs+C)    \\
\Rightarrow 1=As^{2}+A+Bs^{2}+Cs    \\
\text{where}    \\
A+B=0,\quad B=-A    \\
C=0 \\
A=1,\quad B=-1  \\
\therefore \frac{1}{s(s^{2}+1)}=\frac{1}{s}-\frac{s}{s^{2}+1}
\end{align*}
$$

Therefore

$$
y=\mathcal{L}^{-1}\{Y\}=\mathcal{L}^{-1}\left\{\frac{e^{-3s}}{s(s^{2}+1)}\right\}=u(t-3)\left[1-\cos{(t-3)}\right]
$$

---

### **Exercise 8.4 — ODE with impulse**
Solve:

$$
y'' - y = \delta(t-1),\quad y(0)=0,\quad y'(0)=0.
$$

Applying Laplace, we have

$$
\begin{align*}
\mathcal{L}\{y''\}-\mathcal{L}\{y\}=\mathcal{L}\{\delta(t-1)\}  \\
\text{by shifting}  \\
s^{2}Y-sy(0)-y'(0)-Y=e^{-s}   \\
\Rightarrow s^{2}Y-Y=e^{-s}   \\
\Rightarrow (s^{2}-1)Y=e^{-s}   \\
\Rightarrow Y=\frac{e^{-s}}{s^{2}-1}    \\
\Rightarrow Y=\frac{e^{-s}}{(s-1)(s+1)}
\end{align*}
$$

It is noticed that $y$ is a shifted function, so $Y=e^{-s}F(s)=e^{-s}\frac{1}{(s-1)(s+1)}$.

Let's use partial fractions

$$
\begin{align*}
\frac{1}{(s-1)(s+1)}=\frac{A}{s-1}+\frac{B}{s+1}    \\
\Rightarrow 1=A(s+1)+B(s-1) \\
\Rightarrow 1=As+A+Bs-B \\
A+B=0,\text{and}\quad A-B=1    \\
2A=1\rightarrow A=\frac{1}{2}\text{and}\quad B=-\frac{1}{2} \\
\frac{1}{(s-1)(s+1)}=\frac{1}{2}\frac{1}{s-1}-\frac{1}{2}\frac{1}{s+1}
\end{align*}
$$

Applying the inverse transform to this result we have

$$
\mathcal{L}^{-1}\left\{\frac{1}{2}\frac{1}{s-1}-\frac{1}{2}\frac{1}{s+1}\right\}=\frac{e^{t}}{2}-\frac{e^{-t}}{2}=\sinh{t}
$$

Considering shiftinh

$$
y=u(t-1)\sinh{(t-1)}
$$

---

## **9. Mixed Problems (Exam-Level)**

### **Exercise 9.1**
Find the inverse Laplace transform:

$$
F(s)=\frac{e^{-3s}(2s+5)}{s^2+4}.
$$

Let's notice that $F(s)$ has the form of a shifted function, this means $F(s)=e^{-3s}G(s)$, where 

$$
\begin{align*}
G(s)=\frac{2s+5}{s^{2}+4}   \\
=2\frac{s}{s^{2}+4}+\frac{5}{2}\frac{2}{s^{2}+4}    \\
=2\mathcal{L}\{\cos{(2t)}\}+\frac{5}{2}\mathcal{L}\{\sin{2t}\}
\end{align*}
$$

Therefore

$$
\mathcal{L}^{-1}\{F(s)\}=\mathcal{L}^{-1}\{e^{-3s}G(s)\}=u(t-3)\left(2\cos{(2(t-3))}+\frac{5}{2}\sin{(2(t-3))}\right)
$$

---

### **Exercise 9.2**
Solve the IVP:

$$
y'' - 2y' + y = t e^{t},\quad y(0)=1,\quad y'(0)=0.
$$

Let's apply the transform to get

$$
\begin{align*}
\mathcal{L}\{y''\}-2\mathcal{L}\{y'\}+\mathcal{L}\{y\}=\mathcal{L}\{te^{t}\}    \\
\text{by shifting}  \\
(s^{2}Y-sy(0)-y'(0))-2(sY-y(0))+Y=\frac{1}{(s-1)^{2}}   \\
\Rightarrow (s^{2}-2s+1)Y-s+2=\frac{1}{(s-1)^{2}}  \\
\Rightarrow (s-1)^{2}Y=\frac{1}{(s-1)^{2}}+s-2    \\
\Rightarrow Y=\frac{1}{(s-1)^{4}}+\frac{s-2}{(s-1)^{2}}   \\
\Rightarrow Y=\frac{1}{6}\frac{6}{(s-1)^{4}}+\frac{1}{s-1}-\frac{1}{(s-1)^{2}}   \\
\text{by shifting}   \\
\Rightarrow Y=\frac{1}{6}\mathcal{L}\left\{e^{t}t^{3}\right\}+\mathcal{L}\left\{e^{t}\right\}-\mathcal{L}\left\{e^{t}t\right\}
\end{align*}
$$

Therefore

$$
y(t)=\frac{1}{6}e^{t}t^{3}+e^{t}-te^{t}=e^{t}(\frac{1}{6}t^{3}+1-t)
$$


---

### **Exercise 9.3**
Compute:

$$
\mathcal{L}\{u(t-2)\cos(3(t-2))\}.
$$

Since is a shifted function

$$
\begin{align*}
\mathcal{L}\{u(t-2)\cos(3(t-2))\}=e^{-2s}\mathcal{L}\{\cos{(3t)}\}(s)   \\
=e^{-2s}\frac{s}{s^{2}+9}
\end{align*}
$$

---

### **Exercise 9.4**
Find:

$$
\mathcal{L}^{-1}\left\{\frac{s+1}{(s+1)^2+9}\right\}.
$$

By shifting we identify

$$
\begin{align*}
\mathcal{L}\{e^{t}f(t)\}=F(s-(-1))=\frac{s-(-1)}{(s-(-1))^2+9}  \\
\text{so}   \\
F(s)=\frac{s}{s^{2}+9}  \\
\Rightarrow \mathcal{L}^{-1}\{F(s)\}=\cos{(3t)} \\
\therefore \mathcal{L}^{-1}\left\{\frac{s+1}{(s+1)^2+9}\right\}=e^{t}\cos{(3t)}
\end{align*}
$$

---

### **Exercise 9.5**
Solve:

$$
y'' + 9y = \delta(t-\pi),\quad y(0)=0,\quad y'(0)=0.
$$

Let's apply Laplace

$$
\begin{align*}
\mathcal{L}\{y''\}+9\mathcal{L}\{y\}=\mathcal{L}\{\delta(t-\pi)\}   \\
(s^{2}Y)+9Y=e^{-\pi s}  \\
\Rightarrow Y=e^{-\pi s}\frac{1}{s^{2}+9}   \\
\text{by shifting}  \\
F(s)=\frac{1}{s^{2}+9}=\frac{1}{3}\frac{3}{s^{2}+9} \\
\Rightarrow F(s)=\frac{1}{3}\mathcal{L}\{\sin{(3t)}\}
\end{align*}
$$

Therefore

$$
y(t)=\frac{1}{3}u(t-\pi)\sin{3(t-\pi)}
$$

---

## **10. Challenge Problems (Optional)**

### **Exercise 10.1**
Show that:

$$
\mathcal{L}^{-1}\left\{\frac{1}{s(s^2+4)}\right\}
= \frac{1}{4}(1-\cos 2t).
$$

First we use partial fractions

$$
\begin{align*}
\frac{1}{s(s^{2}+4)}=\frac{A}{s}+\frac{Bs+C}{s^{2}+4}   \\
\Rightarrow 1=A(s^{2}+4)+s(Bs+C)    \\
\Rightarrow 1=As^{2}+4A+Bs^{2}+Cs   \\
C=0,\quad 4A=1\rightarrow A=\frac{1}{4},\quad B=-\frac{1}{4}    \\
\Rightarrow \frac{1}{s(s^{2}+4)}=\frac{1}{4s}-\frac{1}{4}\frac{s}{s^{2}+4}=\frac{1}{4}\left(\frac{1}{s}-\frac{s}{s^{2}+4}\right)
\end{align*}
$$

Applying Laplace inverse to the expression obtained by partial fractions

$$
\frac{1}{4}\mathcal{L}^{-1}\left\{\frac{1}{s}-\frac{s}{s^{2}+4}\right\} =\frac{1}{4}\left[\mathcal{L}^{-1}\left\{\frac{1}{s}\right\}-\mathcal{L}^{-1}\left\{\frac{s}{s^{2}+4}\right\}\right]=\frac{1}{4}\left[1-\cos{(2t)}\right]
$$

---

### **Exercise 10.2**
Compute:

$$
\mathcal{L}^{-1}\left\{\frac{e^{-2s}}{s^2(s+1)}\right\}.
$$

Since it is a shifted function, then

$$
\begin{align*}
\mathcal{L}\{g(t)\}(s)=e^{-2s}F(s)=e^{-2s}\frac{1}{s^{2}(s+1)}  \\
\text{by partial fractions} \\
\frac{1}{s^{2}(s+1)}=\frac{A}{s}+\frac{B}{s^{2}}+\frac{C}{s+1}   \\
\Rightarrow 1=As(s+1) + B(s+1)+Cs^{2}   \\
\Rightarrow 1=As^{2}+As+Bs+B+Cs^{2}   \\
B=1,\quad A=-1,\quad C=1    \\
\therefore \frac{1}{s^{2}(s+1)}=-\frac{1}{s}+\frac{1}{s^{2}}+\frac{1}{s+1}
\end{align*}
$$

Applying inverse to the expression obtained we have

$$
f(t)=t-1+e^{-t}
$$

Therefore

$$
\mathcal{L}^{-1}\left\{\frac{e^{-2s}}{s^2(s+1)}\right\}=u(t-2)f(t-2)=u(t-2)((t-2)-1+e^{-(t-2)})
$$

---

### **Exercise 10.3**
Solve:

$$
y'' + 2y' + 5y = u(t-1)e^{-(t-1)},\quad y(0)=0,\quad y'(0)=0.
$$

Let's apply Laplace

$$
\begin{align*}
\mathcal{L}\{y''\}+2\mathcal{L}\{y'\}+5\mathcal{L}\{y\}=\mathcal{L}\{u(t-1)e^{-(t-1)}\} \\
\text{by shifting}
(s^{2}Y)+2(sY)+5Y=e^{-s}\mathcal{L}\{e^{-t}\}(s)    \\
\Rightarrow (s^{2}+2s+5)Y=e^{-s}\frac{1}{s+1}   \\
\Rightarrow Y=e^{-s}\frac{1}{(s+1)((s^{2}+2s+5))}   \\
\text{by partial fractions} \\
\frac{1}{(s+1)((s^{2}+2s+5))}=\frac{A}{s+1}+\frac{Bs+C}{s^{2}+2s+5}    \\
\Rightarrow 1=A(s^{2}+2s+5)+(Bs+C)(s+1) \\
\Rightarrow 1=As^{2}+2As+5A+Bs^{2}+Bs+Cs+C \\
A+B=0,\quad 2A+B+C=0,\quad 5A+C=1\rightarrow C=1-5A \\
\rightarrow B=3A-1, \rightarrow 4A=1\rightarrow A=\frac{1}{4}   \\
B=-\frac{1}{4},\quad C=-\frac{1}{4} \\
\therefore Y=e^{-s}\frac{1}{(s+1)((s^{2}+2s+5))}=e^{-s}\left[\frac{1}{4}\frac{1}{s+1}-\frac{1}{4}\frac{s+1}{s^{2}+2s+5}\right]  \\
=e^{-s}\left[\frac{1}{4}\frac{1}{s+1}-\frac{1}{4}\frac{s+2-2+1}{(s+2)^{2}+1}\right]  \\
=e^{-s}\frac{1}{4}\left[\frac{1}{s+1}-\frac{s+2}{(s+2)^{2}+1}+\frac{1}{(s+2)^{2}+1}\right]
\end{align*}
$$

Applying inverse we have

$$
y(t)=\frac{1}{4}u(t-1)f(t-1)
$$

where

$$
f(t)=e^{-t}-e^{2t}(\cos{(t)}+\sin{(t)})
$$

Finally

$$
y(t)=\frac{1}{4}u(t-1)e^{-(t-1)}-e^{2(t-1)}(\cos{(t-1)}+\sin{(t-1)})
$$

---
