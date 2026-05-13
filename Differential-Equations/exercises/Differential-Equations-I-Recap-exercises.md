
---

# **Differential Equations – Extraordinary Exam Level Exercises**  
*Exercises organized by chapter, aligned with the Extended Theorem Compendium.*

---

# **0. Introduction**

## **0.1 Classification and Basic Concepts**

1. Classify each differential equation as linear/nonlinear, autonomous/non‑autonomous, and determine its order:  
   a) $y'' + y' + y = \sin x$  
   b) $y' = y^2 - 3y + 2$  
   c) $x^2 y'' + xy' - y = 0$  
   d) $y' + \sqrt{xy} = 0$

2. Determine whether the following equations are exact, linear, separable, or none:  
   a) $(2xy + 3)dx + (x^2 + 4y)dy = 0$  
   b) $y' = x e^{y}$  
   c) $y' + y = x^2$

3. For each IVP, determine whether the Existence and Uniqueness Theorem guarantees a unique solution:  
   a) $y' = \sqrt{y},\; y(0)=0$  
   b) $y' = \frac{1}{x-y},\; y(1)=1$  
   c) $y' = x^{1/3} y^{2/3},\; y(0)=0$

---

# **1. First‑Order Differential Equations**

---

## **1.1 Separable Equations**

4. Solve the following separable equations (no need to simplify constants):  
   a) $y' = x^2 y^3$  
   b) $y' = \frac{x}{1+y^2}$  
   c) $y' = (y-1)(y+2)$

5. Solve the IVPs:  
   a) $y' = xy,\; y(0)=3$  
   b) $y' = (1+y^2)\cos x,\; y(0)=0$

6. Determine all equilibrium solutions and classify their stability:  
   a) $y' = y(3-y)$  
   b) $y' = y^2 - 4$

---

## **1.2 Exact Equations**

7. Determine whether each equation is exact. If exact, solve it:  
   a) $(3x^2 + 2y)dx + (2x + 4y^3)dy = 0$  
   b) $(y\cos x - 2x)dx + (\sin x + x^2)dy = 0$

8. Find an integrating factor (if it exists) depending only on $x$ or only on $y$:  
   a) $(2xy - y)dx + (x^2 - x)dy = 0$  
   b) $(y + x e^{xy})dx + (x + y e^{xy})dy = 0$

---

## **1.3 Linear First‑Order Equations**

9. Solve using the integrating factor method:  
   a) $y' + 3y = e^{-x}$  
   b) $y' - \frac{2}{x}y = x^3$  
   c) $y' + y\tan x = \sin x$

10. Solve the IVPs:  
   a) $y' + 4y = 8,\; y(0)=1$  
   b) $y' - \frac{1}{x}y = x,\; y(1)=2$

---

## **1.4 Substitution Methods**

### **Homogeneous**

11. Solve:  
   a) $y' = \frac{x+y}{x-y}$  
   b) $y' = \frac{y}{x} + \frac{x}{y}$

### **Bernoulli**

12. Solve:  
   a) $y' + y = y^3$  
   b) $y' - 2y = 3y^{-1}$

### **Riccati (special case)**

13. Solve the Riccati equation given a particular solution $y_p = x$:  
   $$
   y' = y^2 - xy + x^2
   $$

### **Clairaut**

14. Solve the Clairaut equation:  
   $$
   y = xy' + (y')^2
   $$

---

# **2. Higher‑Order Linear Differential Equations**

---

## **2.1 Homogeneous with Constant Coefficients**

15. Solve:  
   a) $y'' - 5y' + 6y = 0$  
   b) $y'' + 4y = 0$  
   c) $y''' - 3y'' + 3y' - y = 0$

16. Solve the IVPs:  
   a) $y'' + y = 0,\; y(0)=2,\; y'(0)=1$  
   b) $y'' - 4y' + 4y = 0,\; y(0)=0,\; y'(0)=3$

---

## **2.2 Nonhomogeneous Equations**

### **Undetermined Coefficients**

17. Solve:  
   a) $y'' + y = \sin x$  
   b) $y'' - 3y' + 2y = e^{2x}$  
   c) $y'' + 4y = 3x^2$

### **Annihilator Method**

18. Solve:  
   a) $y'' - y = e^{x} + x$  
   b) $y''' = \sin x$

### **Variation of Parameters**

19. Solve:  
   a) $y'' + y = \sec x$  
   b) $y'' - y = \frac{1}{x}$

---

## **2.3 Cauchy–Euler**

20. Solve:  
   a) $x^2 y'' + xy' - y = 0$  
   b) $x^2 y'' - 3xy' + 5y = x^3$

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
