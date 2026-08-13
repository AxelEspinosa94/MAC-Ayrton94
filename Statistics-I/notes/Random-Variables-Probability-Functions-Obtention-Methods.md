
---

# 📘 **Statistics I – Unit II – Theorem Compendium**  
### *Methods for Obtaining Probability Functions of Random Variables*

---

## ## 2.1 Introduction to Methods for Obtaining Probability Functions

### **Definition — Random Variable Transformation Problem**  
Given a random variable $X$ with known distribution, the goal is to determine the distribution of a new variable $Y = g(X)$.

### **Definition — Joint Transformation Problem**  
Given random variables $X_1, X_2, \dots, X_n$, obtain the distribution of a statistic  

$$
Y = h(X_1, \dots, X_n).
$$

### **Principle — Distribution Derivation Framework**  
Every method for obtaining the distribution of $Y$ relies on one of the following:
1. **Distribution functions (CDF method)**  
2. **Transformations (Jacobian method)**  
3. **Moment generating functions (MGFs)**  
4. **Order statistics**  
5. **Known families of distributions**

---

## ## 2.2 Method of Distribution Functions (CDF Method)

### **Definition — CDF Method**  
To find the distribution of $Y = g(X)$, compute:

$$
F_Y(y) = P(Y \le y)
$$

and differentiate (if continuous):

$$
f_Y(y) = \frac{d}{dy} F_Y(y).
$$

### **Theorem — Monotone Transformation CDF Rule**  
If $Y = g(X)$ is **strictly increasing**, then:

$$
F_Y(y) = F_X(g^{-1}(y)).
$$

If **strictly decreasing**:

$$
F_Y(y) = 1 - F_X(g^{-1}(y)).
$$

### **Corollary — PDF Rule for Monotone Transformations**  
If $g$ is monotone and differentiable:

$$
f_Y(y) = f_X(g^{-1}(y)) \left| \frac{d}{dy} g^{-1}(y) \right|.
$$

### **Lemma — CDF Method for Non-Monotone Transformations**  
If $g$ is not monotone, partition the domain into monotone intervals:

$$
F_Y(y) = \sum_{x: g(x) \le y} f_X(x)\,dx.
$$

---

## ## 2.3 Method of Transformations (Jacobian Method)

### **Definition — Jacobian Transformation Method**  
For a transformation $Y = g(X)$ with inverse $X = g^{-1}(Y)$:

$$
f_Y(y) = f_X(g^{-1}(y)) \left| \frac{d}{dy} g^{-1}(y) \right|.
$$

### **Theorem — Multivariate Jacobian Formula**  
Let $(X_1, \dots, X_n)$ have joint density $f_X$.  
Let $(Y_1, \dots, Y_n) = g(X_1, \dots, X_n)$ be a bijective transformation with inverse $g^{-1}$.  
Then:

$$
f_Y(y_1,\dots,y_n)
= f_X(x_1,\dots,x_n)
\left| \det J_{g^{-1}}(y_1,\dots,y_n) \right|,
$$

where $J_{g^{-1}}$ is the Jacobian matrix of the inverse transformation.

### **Corollary — Linear Transformations**  
If $Y = aX + b$ with $a \neq 0$:

$$
f_Y(y) = \frac{1}{|a|} f_X\left(\frac{y-b}{a}\right).
$$

### **Lemma — Sum of Independent Variables (Convolution)**  
If $Y = X_1 + X_2$ and $X_1, X_2$ independent:

$$
f_Y(y) = \int_{-\infty}^{\infty} f_{X_1}(t) f_{X_2}(y-t)\, dt.
$$

---

## ## 2.4 Method of Moment Generating Functions (MGF Method)

### **Definition — Moment Generating Function (MGF)**  

$$
M_X(t) = E(e^{tX}).
$$

### **Theorem — Uniqueness of MGFs**  
If two random variables have the same MGF in an open interval around $t=0$, they have the same distribution.

### **Theorem — MGF of Linear Transformations**  
If $Y = aX + b$:

$$
M_Y(t) = e^{bt} M_X(at).
$$

### **Theorem — Sum of Independent Variables**  
If $X_1, \dots, X_n$ are independent:

$$
M_{X_1 + \cdots + X_n}(t) = \prod_{i=1}^n M_{X_i}(t).
$$

### **Corollary — Deriving Known Distributions**  
MGFs can be used to derive:
- Normal distribution,
- Gamma distribution,
- Chi-square distribution,
- Poisson distribution,
- Binomial distribution.

---

## ## 2.5 Order Statistics

### **Definition — Order Statistics**  
Given i.i.d. variables $X_1, \dots, X_n$, define:

$$
X_{(1)} \le X_{(2)} \le \cdots \le X_{(n)}.
$$

### **Theorem — PDF of the $k$-th Order Statistic**  
If $X_i$ have density $f$ and CDF $F$:

$$
f_{X_{(k)}}(x)
= \frac{n!}{(k-1)!(n-k)!}
[F(x)]^{k-1}
[1-F(x)]^{n-k}
f(x).
$$

### **Corollary — Minimum and Maximum**  
- Minimum:

  $$
  f_{X_{(1)}}(x) = n[1-F(x)]^{n-1} f(x).
  $$

- Maximum:

  $$
  f_{X_{(n)}}(x) = n[F(x)]^{n-1} f(x).
  $$

### **Lemma — Joint PDF of Two Order Statistics**  
For $X_{(i)}$ and $X_{(j)}$, $i < j$:

$$
f_{X_{(i)}, X_{(j)}}(u,v)
= \frac{n!}{(i-1)!(j-i-1)!(n-j)!}
[F(u)]^{i-1}
[f(u)]
[F(v)-F(u)]^{j-i-1}
[1-F(v)]^{n-j}
f(v).
$$

---

## ## 2.6 Distributions of Broad Use: t, Chi-square, F

### **Definition — Chi-square Distribution**  
If $Z_1, \dots, Z_k$ are i.i.d. $N(0,1)$:

$$
\chi^2_k = \sum_{i=1}^k Z_i^2.
$$

### **Theorem — MGF of Chi-square**  

$$
M_{\chi^2_k}(t) = (1 - 2t)^{-k/2}, \quad t < \frac{1}{2}.
$$

---

### **Definition — Student’s t Distribution**  
If $Z \sim N(0,1)$ and $V \sim \chi^2_k$ independent:

$$
T = \frac{Z}{\sqrt{V/k}}.
$$

### **Theorem — Symmetry of t Distribution**  
The t distribution is symmetric around 0.

### **Corollary — Heavy Tails**  
For any finite $k$, the t distribution has heavier tails than the normal distribution.

---

### **Definition — F Distribution**  
If $U \sim \chi^2_{d_1}$ and $V \sim \chi^2_{d_2}$ independent:

$$
F = \frac{U/d_1}{V/d_2}.
$$

### **Theorem — Support of F Distribution**  

$$
F > 0.
$$

### **Lemma — Relationship Between t and F**  
If $T \sim t_k$, then:

$$
T^2 \sim F_{1,k}.
$$

---

## ## 2.7 Obtaining Distributions Using CAS, R, Excel

### **Principle — Software-Assisted Derivation**  
Symbolic or numeric tools can compute:
- CDFs,
- PDFs,
- MGFs,
- Convolutions,
- Order statistics,
- Transformations.

### **Theorem — Deterministic Output**  
Given identical input and deterministic functions, CAS, R, and Excel produce identical results up to machine precision.

### **Corollary — Reproducibility Requirement**  
Scripts and data must be saved to ensure reproducibility of distribution derivations.

---

