
---
title: "Optimization – Unit II – Extraordinary Exam Exercise Notebook"
author: "Axel – MAC"
---

# Optimization – Unit II  
## Exercise Notebook – Extraordinary Level  
### Linear Programming Models

---

# 2.1 Concept of a Model: Classification and Structure

### **Exercise 2.1.1 — Model Identification**
For each scenario, identify:
1. Decision variables  
2. Objective function  
3. Constraints  
4. Parameters  
5. Model classification (deterministic/stochastic, linear/nonlinear)

Scenarios:
- A factory wants to minimize production cost.  
- A hospital wants to schedule nurses under uncertainty.  
- A delivery company wants to minimize fuel consumption.

---

### **Exercise 2.1.2 — Model Structure**
Explain whether each of the following is a valid mathematical model and justify:
1. A model with nonlinear constraints but linear objective.  
2. A model with missing constraints.  
3. A model with decision variables that cannot be interpreted.

---

### **Exercise 2.1.3 — Deterministic vs Stochastic**
Classify each model and explain why:
1. Inventory model with random demand.  
2. Production model with fixed machine hours.  
3. Diet model with uncertain nutrient content.

---

# 2.2 Linear Programming Models: Characteristics, Structure, Matrix Formulation

### **Exercise 2.2.1 — LP Formulation**
Formulate the following problem as an LP:

A company produces two products $x_1$ and $x_2$.  
Profit: $5x_1 + 8x_2$.  
Constraints:
- Labor: $2x_1 + x_2 \le 100$  
- Material: $x_1 + 3x_2 \le 90$  
- Non-negativity

Write:
1. Standard form  
2. Matrix form $Ax \le b$, $c^T x$

---

### **Exercise 2.2.2 — LP Characteristics**
Explain whether each situation satisfies LP assumptions:
1. Cost increases proportionally with production.  
2. Mixing two chemicals produces nonlinear reactions.  
3. Workforce productivity varies with fatigue.

---

### **Exercise 2.2.3 — Matrix Representation**
Convert the following LP into matrix form:

Maximize  


$$
Z = 4x_1 + 7x_2
$$


Subject to:  


$$
3x_1 + 2x_2 \le 60
$$




$$
x_1 + 4x_2 \le 48
$$




$$
x_1, x_2 \ge 0
$$



---

# 2.3 LP Model Types: Production, Diet, Blending

### **Exercise 2.3.1 — Production Planning Model**
Formulate a production planning LP with:
- 3 products  
- 2 resources  
- Profit maximization  
- Resource constraints  
- Non-negativity

---

### **Exercise 2.3.2 — Diet Model**
Construct a diet model with:
- 4 foods  
- 3 nutrients  
- Cost minimization  
- Minimum nutrient requirements

---

### **Exercise 2.3.3 — Blending Model**
A gasoline blend must satisfy:
- Octane ≥ 90  
- Sulfur ≤ 5  
- Cost minimization  

Components:
- A: octane 95, sulfur 3, cost 4  
- B: octane 85, sulfur 7, cost 3  

Formulate the LP.

---

# 2.4 Convex Sets, Feasible Region, Extreme Points, Optimality

### **Exercise 2.4.1 — Convexity**
Determine whether each set is convex:
1. A triangle in the plane  
2. A circle  
3. A set of two disjoint squares  
4. A feasible region defined by linear inequalities

Explain your reasoning.

---

### **Exercise 2.4.2 — Extreme Points**
Given the feasible region defined by:


$$
x_1 + x_2 \le 6,\quad x_1 \ge 0,\quad x_2 \ge 0
$$


Find all extreme points.

---

### **Exercise 2.4.3 — Optimality at Extreme Points**
Explain why the optimal solution of an LP must occur at an extreme point.  
Provide a geometric argument.

---

# 2.5 Graphical Solution of Two-Variable LP

### **Exercise 2.5.1 — Graphical Solution**
Solve graphically:

Maximize  


$$
Z = 3x_1 + 2x_2
$$


Subject to:  


$$
x_1 + x_2 \le 8
$$




$$
x_1 + 2x_2 \le 10
$$




$$
x_1, x_2 \ge 0
$$



Find:
1. Feasible region  
2. Extreme points  
3. Optimal solution  
4. Optimal value

---

### **Exercise 2.5.2 — Multiple Optima**
Construct an LP with two variables that has infinitely many optimal solutions.  
Explain why the objective function is parallel to a constraint boundary.

---

### **Exercise 2.5.3 — Unbounded Region**
Construct an LP with two variables whose feasible region is unbounded.  
Explain why the objective function increases without limit.

---

# 2.6 Types of Solutions: BFS, Feasible, Infeasible, Unbounded, Degenerate, Optimal, Multiple

### **Exercise 2.6.1 — Classifying Solutions**
For each LP, classify the solution as:
- Basic  
- Basic feasible  
- Infeasible  
- Unbounded  
- Degenerate  
- Optimal  
- Multiple optimal

LPs:

1.  


$$
\text{Max } Z = x_1 + x_2
$$




$$
x_1 + x_2 \le 5,\quad x_1, x_2 \ge 0
$$



2.  


$$
\text{Max } Z = x_1 + x_2
$$




$$
x_1 - x_2 \le -10,\quad x_1, x_2 \ge 0
$$



3.  


$$
\text{Max } Z = x_1
$$




$$
x_1 \ge 0,\quad x_2 \ge 0
$$



4.  


$$
\text{Max } Z = x_1 + x_2
$$




$$
x_1 + x_2 = 5,\quad x_1, x_2 \ge 0
$$



---

### **Exercise 2.6.2 — Degeneracy**
Provide an example of a degenerate BFS and explain why degeneracy occurs.

---

### **Exercise 2.6.3 — Multiple Optimal Solutions**
Provide an LP with multiple optimal solutions and identify all optimal points.

---

# 2.7 Solving LPs Using CAS, R, Excel

### **Exercise 2.7.1 — CAS Solution**
Using any CAS (Mathematica, Maple, SymPy), solve:

Maximize  


$$
Z = 4x_1 + 6x_2
$$


Subject to:  


$$
2x_1 + x_2 \le 12
$$




$$
x_1 + 3x_2 \le 15
$$




$$
x_1, x_2 \ge 0
$$



Report:
1. Optimal point  
2. Optimal value  
3. Extreme points tested

---

### **Exercise 2.7.2 — R Solution**
Write R code to solve the LP:

Maximize  


$$
Z = 5x_1 + 7x_2
$$


Subject to:  


$$
3x_1 + 2x_2 \le 18
$$




$$
x_1 + 4x_2 \le 16
$$




$$
x_1, x_2 \ge 0
$$



---

### **Exercise 2.7.3 — Excel Solver**
Explain how to solve a two-variable LP using Excel Solver:
1. Define decision cells  
2. Define objective cell  
3. Add constraints  
4. Choose solving method  
5. Interpret results

---

# End of Exercise Notebook
