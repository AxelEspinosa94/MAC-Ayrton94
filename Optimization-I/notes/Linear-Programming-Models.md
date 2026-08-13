# 📘 Optimization – Unit II  
## Theorem Compendium  
### Linear Programming Models

---

# 2.1 Concept of a Model: Classification and Structure

### **Definition — Model**
A **model** is a simplified representation of a real system used to analyze, predict, or optimize behavior.

### **Classification of Models**
1. **Deterministic vs. Stochastic**  
2. **Static vs. Dynamic**  
3. **Linear vs. Nonlinear**  
4. **Discrete vs. Continuous**

### **Structure of a Mathematical Model**
A model typically includes:
- **Decision variables**  
- **Objective function**  
- **Constraints**  
- **Parameters**  
- **Feasible region**

### **Theorem — Model Validity**
A model is valid if:


$$
\text{Model behavior} \approx \text{Real system behavior}
$$


within acceptable tolerance.

---

# 2.2 Linear Programming Models: Characteristics, Structure, Matrix Formulation

### **Definition — Linear Programming (LP)**
An LP model optimizes a linear objective subject to linear constraints.

### **General LP Structure**


$$
\text{Maximize or Minimize } Z = c_1x_1 + c_2x_2 + \cdots + c_nx_n
$$


subject to:


$$
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n \le b_1
$$




$$
\vdots
$$




$$
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n \le b_m
$$




$$
x_j \ge 0
$$



### **Matrix Formulation**


$$
\text{Maximize } Z = c^T x
$$


subject to:


$$
Ax \le b,\quad x \ge 0
$$



### **Characteristics of LP**
- Proportionality  
- Additivity  
- Divisibility  
- Certainty  

### **Theorem — Feasibility**
A solution \(x\) is feasible if:


$$
Ax \le b,\quad x \ge 0
$$



### **Theorem — Optimality**
If an LP has an optimal solution, at least one optimal solution occurs at an **extreme point** of the feasible region.

---

# 2.3 LP Model Types: Production, Diet, and Blending Models

### **Production Planning Model**
Objective: maximize profit or minimize cost.  
Variables: production quantities.  
Constraints: labor, materials, machine time.

### **Diet Model**
Objective: minimize cost while meeting nutritional requirements.  
Variables: quantities of foods.  
Constraints: nutrient minimums and maximums.

### **Blending (Mixing) Model**
Objective: minimize cost or maximize quality of a mixture.  
Variables: proportions of components.  
Constraints: quality specifications, availability.

### **Theorem — Linear Structure of Classical LP Models**
All three model types can be expressed as:


$$
\text{Min or Max } c^T x
$$


subject to:


$$
Ax \ge b,\ Ax \le b,\ Ax = b
$$



---

# 2.4 Convex Sets, Feasible Region, Extreme Points, Optimality

### **Definition — Convex Set**
A set \(S\) is convex if for any \(x,y\in S\) and any \(\lambda\in[0,1]\):


$$
\lambda x + (1-\lambda)y \in S
$$



### **Definition — Feasible Region**
The set of all points satisfying the constraints of an LP.

### **Theorem — Feasible Region Convexity**
The feasible region of any LP is a convex polyhedron.

### **Definition — Extreme Point**
A point in the feasible region that cannot be expressed as a convex combination of two other feasible points.

### **Fundamental Theorem of Linear Programming**
If an LP has an optimal solution, at least one optimal solution occurs at an extreme point of the feasible region.

---

# 2.5 Graphical Solution of a Two-Variable LP

### **Principle — Graphical Method**
For LPs with two decision variables:
1. Plot each constraint as a line.  
2. Identify the feasible region.  
3. Plot objective function lines.  
4. Move the objective line until reaching the last feasible extreme point.

### **Theorem — Optimality via Objective Function Movement**
The optimal solution lies at the extreme point where the objective function achieves its maximum or minimum value.

### **Corollary — Multiple Optima**
If the objective function is parallel to a constraint boundary, all points along that boundary segment are optimal.

---

# 2.6 Types of Solutions: Basic, Feasible, Infeasible, Unbounded, Degenerate, Optimal, Multiple

### **Definition — Basic Solution**
A solution obtained by setting \(n-m\) variables to zero in an LP with \(m\) constraints and \(n\) variables.

### **Definition — Basic Feasible Solution (BFS)**
A basic solution that satisfies all constraints.

### **Definition — Infeasible Solution**
Violates at least one constraint.

### **Definition — Unbounded Solution**
Objective function can increase or decrease indefinitely without violating constraints.

### **Definition — Degenerate Solution**
A BFS where one or more basic variables equal zero.

### **Definition — Optimal Solution**
A feasible solution that maximizes or minimizes the objective.

### **Definition — Multiple Optimal Solutions**
Occurs when more than one feasible point yields the same optimal objective value.

### **Theorem — BFS Optimality**
If an LP has an optimal solution, at least one optimal solution is a BFS.

---

# 2.7 Solving LP Models Using CAS, R, Excel

### **Principle — Software-Assisted LP Solving**
Software can:
- Plot feasible regions  
- Compute extreme points  
- Solve LPs using simplex or interior-point methods  
- Detect unboundedness or infeasibility  

### **Theorem — Deterministic Output**
Given identical inputs, CAS, R, and Excel produce identical LP solutions up to machine precision.

### **Corollary — Reproducibility**
Scripts, spreadsheets, and parameters must be saved to ensure reproducibility.

---

# End of Theorem Compendium
