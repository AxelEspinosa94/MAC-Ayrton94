
---

# **Graph Theory – Matrix Representations of Graphs**

## **1. Adjacency Matrix**

### **Definition 1.1 — Adjacency Matrix**
Let $G = (V,E)$ be a graph with vertices  

$$
V = \\{v_1, v_2, \dots, v_n\\}.
$$

The **adjacency matrix** $A = \[a_{ij}\]$ is an $n \times n$ matrix defined by:

$$
a_{ij} =
\begin{cases}
1 & \text{if } v_i v_j \in E, \\
0 & \text{otherwise}.
\end{cases}
$$

For **directed graphs**,  

$$
a_{ij} = 1 \text{ if there is an arc } v_i \to v_j.
$$

---

### **Theorem 1.1 — Walk Counting**
For any graph with adjacency matrix $A$:

$$
(A^k)_{ij}
$$

equals the number of **walks of length $k$** from vertex $v_i$ to vertex $v_j$.

**Proof.** Follows from matrix multiplication: each multiplication step counts all possible intermediate vertices. ∎

---

### **Example 1.1**
Graph:

$$
E = \\{ab, bc, ca\\}
$$

Adjacency matrix (ordering $(a,b,c)$):

$$
A =
\begin{pmatrix}
0 & 1 & 1 \\
1 & 0 & 1 \\
1 & 1 & 0
\end{pmatrix}
$$

Number of walks of length 2 from $a$ to $a$:

$$
(A^2)_{11} = 2.
$$

---

## **2. Incidence Matrix**

### **Definition 2.1 — Incidence Matrix**

Let $G = (V,E)$ with  

$$
V = \\{v_1,\dots,v_n\\}, \quad E = \\{e_1,\dots,e_m\\}.
$$

The **incidence matrix** $M = \[m_{ij}\]$ is an $n \times m$ matrix defined by:

$$
m_{ij} =
\begin{cases}
1 & \text{if vertex } v_i \text{ is incident to edge } e_j, \\
0 & \text{otherwise}.
\end{cases}
$$

For **directed graphs**, a common convention is:

$$
m_{ij} =
\begin{cases}
1 & \text{if } e_j \text{ enters } v_i, \\
-1 & \text{if } e_j \text{ leaves } v_i, \\
0 & \text{otherwise}.
\end{cases}
$$

---

### **Lemma 2.1 — Degree from Incidence Matrix**
For a simple graph:

$$
\deg(v_i) = \sum_{j=1}^m m_{ij}.
$$

---

### **Example 2.1**
Graph:
$$
E = \\{ab, bc, ca\\}
$$

Incidence matrix (edges ordered $(ab, bc, ca)$):

$$
M =
\begin{pmatrix}
1 & 0 & 1 \\
1 & 1 & 0 \\
0 & 1 & 1
\end{pmatrix}
$$

---

## **3. Accessibility Matrix**

### **Definition 3.1 — Accessibility Matrix**
Given adjacency matrix $A$, the **accessibility matrix** (or reachability matrix) $R$ is:

$$
R = A + A^2 + \cdots + A^{n-1},
$$

where:

$$
r_{ij} > 0 \iff \text{there exists a path from } v_i \text{ to } v_j.
$$

---

### **Theorem 3.1 — Reachability Criterion**
Vertices $v_i$ and $v_j$ are connected (in the same component) iff:

$$
r_{ij} > 0.
$$

---

### **Example 3.1**
For the triangle graph:

$$
A =
\begin{pmatrix}
0 & 1 & 1 \\
1 & 0 & 1 \\
1 & 1 & 0
\end{pmatrix}
$$

$$
R = A + A^2 =
\begin{pmatrix}
2 & 2 & 2 \\
2 & 2 & 2 \\
2 & 2 & 2
\end{pmatrix}
$$

All vertices are mutually reachable.

---

## **4. Circuit Matrix**

### **Definition 4.1 — Circuit Matrix**
Let $G$ have $q$ fundamental circuits and $m$ edges.  
The **circuit matrix** $B$ is a $q \times m$ matrix where:

$$
b_{ij} =
\begin{cases}
1 & \text{if edge } e_j \text{ is in circuit } C_i, \\
0 & \text{otherwise}.
\end{cases}
$$

---

### **Theorem 4.1 — Rank of Circuit Matrix**
For a connected graph with $n$ vertices and $m$ edges:

$$
\text{rank}(B) = m - n + 1.
$$

This equals the **cyclomatic number** (number of independent cycles).

---

### **Example 4.1**
Graph: square with diagonal  
$$
E = \\{ab, bc, cd, da, ac\\}
$$

Fundamental cycles:

- (C_1 = ab, bc, ca)
- (C_2 = bc, cd, da, ac)

Circuit matrix:

$$
B =
\begin{pmatrix}
1 & 1 & 0 & 0 & 1 \\
0 & 1 & 1 & 1 & 1
\end{pmatrix}
$$

---

## **5. Path Matrix**

### **Definition 5.1 — Path Matrix**
Let $P$ be a matrix where:

$$
p_{ij} =
\begin{cases}
1 & \text{if there exists a simple path between } v_i \text{ and } v_j, \\
0 & \text{otherwise}.
\end{cases}
$$

This is similar to accessibility matrix but **ignores walk multiplicity**.

---

### **Example 5.1**
For a tree, every pair of vertices has exactly one simple path:

$$
p_{ij} = 1 \quad \forall i \ne j.
$$

---

## **6. Applications Using CAS, Excel, or Computational Tools**

### **6.1 Using CAS (Computer Algebra Systems)**

Tools like **Wolfram Mathematica**, **SageMath**, or **Maple** can:

- compute adjacency/incidence matrices automatically  
- compute powers $A^k$ to count walks  
- compute accessibility matrices  
- detect cycles and generate circuit matrices  
- compute eigenvalues of adjacency matrices (spectral graph theory)

**Example (SageMath):**
```python
G = Graph({0:[1,2], 1:[2]})
A = G.adjacency_matrix()
A^3   # counts walks of length 3
```

---

### **6.2 Using Excel**

Excel can be used to:

- build adjacency matrices manually  
- compute matrix powers using `MMULT`  
- detect connectivity by summing powers  
- visualize graphs using conditional formatting  

**Example:**
```
=MMULT(A1:C3, A1:C3)
```

---

### **6.3 Using Python (NetworkX)**

```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([(1,2),(2,3),(3,1)])

A = nx.adjacency_matrix(G).todense()
```

---

### **6.4 Using MATLAB / Octave**

```matlab
A = [0 1 1; 1 0 1; 1 1 0];
A2 = A^2;
```

---

# **Conclusion**

This teoremario covers the fundamental matrix representations of graphs:

- adjacency matrix  
- incidence matrix  
- accessibility matrix  
- circuit matrix  
- path matrix  

and provides computational applications using CAS, Excel, Python, and MATLAB.

---