---
title: "Statistics I – Unit II – Extraordinary Exam Exercise Notebook"
author: "Axel – MAC"
---

# Statistics I – Unit II  
## Exercise Notebook – Extraordinary Level  
### Methods for Obtaining Probability Functions of Random Variables

---

# 2.1 Introduction to Distribution–Derivation Methods

### **Exercise 2.1.1 — Conceptual Foundations**
Explain the difference between:
1. The *CDF method*,
2. The *Jacobian transformation method*,
3. The *MGF method*.

Provide one example scenario where each method is the most efficient choice.

---

### **Exercise 2.1.2 — Identifying the Correct Method**
For each transformation, state which method is most appropriate and justify:

1. $Y = X^2$, where $X \sim N(0,1)$.  
2. $Y = \max(X_1, X_2, X_3)$, where $X_i$ are i.i.d. exponential.  
3. $Y = X_1 + X_2 + X_3$, where $X_i$ are independent gamma.  
4. $Y = \frac{X_1}{X_2}$, where $X_1, X_2$ are independent chi-square.

---

# 2.2 CDF Method and Applications

### **Exercise 2.2.1 — Monotone Transformation**
Let $X \sim \text{Uniform}(0,1)$. Define $Y = \sqrt{X}$.

1. Compute $F_Y(y)$.  
2. Derive $f_Y(y)$.  
3. Sketch the density and comment on its shape.

---

### **Exercise 2.2.2 — Non-Monotone Transformation**
Let $X \sim N(0,1)$. Define $Y = X^2$.

1. Use the CDF method to derive $F_Y(y)$.  
2. Differentiate to obtain $f_Y(y)$.  
3. Identify the distribution of $Y$.

---

### **Exercise 2.2.3 — Distribution of a Ratio**
Let $X \sim \text{Uniform}(0,2)$. Define $Y = \frac{1}{X}$.

1. Compute the CDF of $Y$.  
2. Derive the PDF.  
3. Determine the support of $Y$.

---

# 2.3 Transformation Method (Jacobian)

### **Exercise 2.3.1 — Linear Transformation**
Let $X \sim \text{Exponential}(\lambda)$. Define $Y = aX + b$ with $a > 0$.

1. Derive $f_Y(y)$ using the Jacobian method.  
2. Verify that the support is correctly transformed.  
3. Interpret the effect of $a$ and $b$ on the distribution.

---

### **Exercise 2.3.2 — Absolute Value Transformation**
Let $X \sim N(0,1)$. Define $Y = |X|$.

1. Use the Jacobian method to derive $f_Y(y)$.  
2. Identify the resulting distribution.  
3. Compute $E(Y)$.

---

### **Exercise 2.3.3 — Joint Transformation**
Let $(X,Y)$ have joint density  


$$
f_{X,Y}(x,y) = e^{-(x+y)}, \quad x>0, y>0.
$$


Define the transformation:


$$
U = X+Y,\quad V = \frac{X}{X+Y}.
$$



1. Compute the Jacobian determinant.  
2. Derive the joint density $f_{U,V}(u,v)$.  
3. Identify the marginal distribution of $V$.  
4. Interpret the meaning of $V$.

---

# 2.4 Moment Generating Function (MGF) Method

### **Exercise 2.4.1 — Sum of Independent Variables**
Let $X_1, X_2 \sim \text{Exponential}(\lambda)$ independent. Define $Y = X_1 + X_2$.

1. Compute the MGF of $Y$.  
2. Identify the distribution of $Y$.  
3. Derive the PDF explicitly.

---

### **Exercise 2.4.2 — Linear Transformation via MGF**
Let $X \sim N(\mu, \sigma^2)$. Define $Y = aX + b$.

1. Compute $M_Y(t)$.  
2. Identify the distribution of $Y$.  
3. Explain why the MGF method is faster than the Jacobian method here.

---

### **Exercise 2.4.3 — Gamma MGF Derivation**
Let $X_1, X_2, X_3$ be independent exponential($\lambda$). Define $Y = X_1 + X_2 + X_3$.

1. Compute the MGF of $Y$.  
2. Identify the distribution.  
3. Derive the mean and variance using the MGF.

---

# 2.5 Order Statistics

### **Exercise 2.5.1 — Minimum of Exponentials**
Let $X_1, X_2, \dots, X_n$ be i.i.d. exponential($\lambda$). Define $Y = X_{(1)}$.

1. Derive the PDF of $Y$.  
2. Identify the distribution.  
3. Compute $E(Y)$.

---

### **Exercise 2.5.2 — Maximum of Uniforms**
Let $X_1, \dots, X_n \sim \text{Uniform}(0,1)$. Define $M = X_{(n)}$.

1. Derive the PDF of $M$.  
2. Compute $E(M)$.  
3. Compute $Var(M)$.

---

### **Exercise 2.5.3 — Joint Distribution of Two Order Statistics**
Let $X_1, \dots, X_n$ be i.i.d. with density $f$ and CDF $F$. Derive the joint PDF of:


$$
(X_{(1)}, X_{(n)}).
$$



Then apply it to the case where $X_i \sim \text{Uniform}(0,1)$.

---

# 2.6 Distributions of Broad Use: t, Chi-square, F

### **Exercise 2.6.1 — Chi-square from Normal Variables**
Let $Z_1, Z_2, Z_3 \sim N(0,1)$ independent. Define:


$$
Y = Z_1^2 + Z_2^2 + Z_3^2.
$$



1. Identify the distribution of $Y$.  
2. Derive its PDF.  
3. Compute its MGF.

---

### **Exercise 2.6.2 — Student’s t Distribution**
Let $Z \sim N(0,1)$ and $V \sim \chi^2_k$ independent. Define:


$$
T = \frac{Z}{\sqrt{V/k}}.
$$



1. Derive the PDF of $T$.  
2. Show that $T$ is symmetric.  
3. Explain why the t distribution has heavier tails than the normal.

---

### **Exercise 2.6.3 — F Distribution**
Let $U \sim \chi^2_{d_1}$ and $V \sim \chi^2_{d_2}$ independent. Define:


$$
F = \frac{U/d_1}{V/d_2}.
$$



1. Derive the PDF of $F$.  
2. Show that $F > 0$.  
3. Show that if $T \sim t_k$, then $T^2 \sim F_{1,k}$.

---

# 2.7 Software-Based Derivation (CAS, R, Excel)

### **Exercise 2.7.1 — R Implementation**
Given a random variable $X \sim \text{Gamma}(3,2)$:

1. Write R code to compute its PDF, CDF, and MGF.  
2. Use simulation to approximate the distribution of $Y = X^2$.  
3. Compare the simulated density with the theoretical one obtained via the Jacobian method.

---

### **Exercise 2.7.2 — Excel Workflow**
Given 10,000 samples of a normal variable in column A:

1. Use Excel to compute empirical mean, variance, skewness, and kurtosis.  
2. Use Excel to approximate the distribution of $Y = |X|$.  
3. Compare with the theoretical half-normal distribution.

---

### **Exercise 2.7.3 — CAS Derivation**
Using a CAS (Mathematica, Maple, etc.):

1. Symbolically derive the PDF of $Y = X^2$ for $X \sim N(0,1)$.  
2. Derive the MGF of a chi-square distribution.  
3. Verify the identity $T^2 \sim F_{1,k}$ using symbolic manipulation.

---

# End of Exercise Notebook
