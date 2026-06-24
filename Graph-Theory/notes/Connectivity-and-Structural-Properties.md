
---

# **Graph Theory – Connectivity and Applications (Theorem Compendium)**  

---

## **1. Connectivity Concepts**

### **1.1 Definitions**

#### **Definition — Connected Graph**  
A graph $G = (V,E)$ is **connected** if for every pair of vertices $u,v \in V$, there exists a path joining them.

#### **Definition — Component**  
A **component** of a graph is a maximal connected subgraph.

#### **Definition — Cut Vertex (Articulation Point)**  
A vertex $v$ is a **cut vertex** if removing $v$ (and its incident edges) increases the number of connected components.

#### **Definition — Cut Edge (Bridge)**  
An edge $e$ is a **cut edge** if removing it increases the number of connected components.

#### **Definition — Block**  
A **block** is a maximal connected subgraph with no cut vertices.

---

## **2. Fundamental Theorems on Connectivity**

### **2.1 Cut Edges**

#### **Theorem — Characterization of Bridges**  
An edge $e = uv$ is a bridge **iff** it does not lie on any cycle of the graph.

**Proof.**  
- If $e$ lies on a cycle, removing it leaves an alternate path between $u$ and $v$, so connectivity is preserved.  
- If $e$ is not on a cycle, it is the *only* path between its endpoints; removing it disconnects them.  
∎

---

### **2.2 Cut Vertices**

#### **Theorem — Characterization of Articulation Points**  
A vertex $v$ is a cut vertex **iff** there exist two neighbors $u,w$ of $v$ such that every path from $u$ to $w$ contains $v$.

**Proof.**  
- If all $u$-$w$ paths use $v$, removing $v$ disconnects them.  
- If there exists a path avoiding $v$, removing $v$ does not disconnect the graph.  
∎

---

### **2.3 Blocks**

#### **Proposition — Blocks Partition the Graph**  
Every connected graph can be decomposed uniquely into blocks, and any two blocks intersect in at most one vertex (a cut vertex).

**Proof.**  
Follows from maximality of 2-connected subgraphs and the fact that articulation points are the only possible intersections.  
∎

---

## **3. Vertex and Edge Connectivity**

### **3.1 Definitions**

- **Vertex connectivity** $\kappa(G)$: minimum number of vertices whose removal disconnects $G$.  
- **Edge connectivity** $\lambda(G)$: minimum number of edges whose removal disconnects $G$.  
- **n‑connected graph**: a graph with $\kappa(G) \ge n$.

---

### **3.2 Whitney’s Inequalities**

#### **Theorem (Whitney)**  
For any nontrivial connected graph:

$$
\kappa(G) \le \lambda(G) \le \delta(G)
$$

where $\delta(G)$ is the minimum degree.

**Proof.**  
- Removing all edges incident to a minimum-degree vertex disconnects it → $\lambda(G) \le \delta(G)$.  
- Removing a vertex removes all its incident edges → $\kappa(G) \le \lambda(G)$.  
∎

---

## **4. Hall’s Marriage Theorem**

### **4.1 Definitions**

A bipartite graph $G = (X,Y,E)$ has a **perfect matching from $X$ to $Y$** if every vertex in $X$ is matched to a distinct vertex in $Y$.

---

### **4.2 Hall’s Theorem**

#### **Theorem (Hall’s Marriage Theorem)**  
A bipartite graph $G=(X,Y,E)$ has a matching saturating $X$ **iff** for every subset $S \subseteq X$:

$$
|N(S)| \ge |S|
$$

**Proof.**  
- **Necessity:** If a matching saturates $X$, each vertex in $S$ is matched to a distinct vertex in $N(S)$.  
- **Sufficiency:** Constructive proof via augmenting paths or induction on $|X|$.  
∎

---

## **5. Trees and Traversals**

### **5.1 Definitions**

- A **binary tree**: each node has ≤ 2 children.  
- A **strictly binary tree**: each internal node has exactly 2 children.

---

### **5.2 Traversal Theorems**

#### **Theorem — Node Count in Strictly Binary Trees**  
A strictly binary tree with $n$ internal nodes has exactly $n+1$ leaves.

**Proof.**  
Each internal node contributes 2 children; counting edges gives:

$$
2n = (n + 1) + (n - 1)
$$

where the right side is leaves + internal nodes minus root.  
Solving yields leaves = $n+1$.  
∎

---

### **5.3 Traversal Orders**

- **Preorder:** root → left → right  
- **Inorder:** left → root → right  
- **Postorder:** left → right → root  

---

## **6. Kruskal’s Algorithm and Menger’s Theorem**

### **6.1 Kruskal’s Algorithm**

#### **Theorem — Kruskal Produces a Minimum Spanning Tree**  
Kruskal’s algorithm always outputs a minimum spanning tree (MST).

**Proof Sketch.**  
Uses the **cut property**:  
> The lightest edge crossing any cut belongs to every MST.

Kruskal repeatedly selects such edges, never forming cycles.  
∎

---

### **6.2 Menger’s Theorem (Contextual Link)**

#### **Theorem (Menger)**  
For distinct vertices $u,v$:
- The **minimum number of vertices** whose removal separates $u$ and $v$  
  equals  
- The **maximum number of internally disjoint $u$-$v$ paths**.

This theorem underlies connectivity guarantees used in MST correctness proofs and network reliability.

---

## **7. Graph Ordering**

### **Definition — Topological Ordering**  
A **topological order** of a DAG is a linear ordering of vertices such that all directed edges go from earlier to later vertices.

#### **Theorem — DAGs Admit Topological Orderings**  
A directed graph has a topological ordering **iff** it has no directed cycles.

**Proof.**  
- If a cycle exists, no vertex can be first.  
- If acyclic, repeatedly remove vertices of indegree 0.  
∎

---

## **8. Network Concepts: Communication and Dominance**

### **8.1 Communication**

#### **Definition — Communication in Directed Graphs**  
Vertices $u$ and $v$ **communicate** if each is reachable from the other.  
This partitions the graph into **strongly connected components (SCCs)**.

---

### **8.2 Dominance**

#### **Definition — Dominator (in directed graphs)**  
A vertex $u$ **dominates** $v$ if every path from the start vertex $s$ to $v$ passes through $u$.

Used in compiler theory and control‑flow analysis.

---

## **9. Examples**

### **Example 1 — Cut Vertex**

```
a — b — c — d
      |
      e
```

Vertex **b** is a cut vertex.

---

### **Example 2 — Bridge**

```
a — b — c
```

Edge **b–c** is a bridge.

---

### **Example 3 — Hall’s Condition**
Let  
$X = \{x_1, x_2, x_3\}$,  
$Y = \{y_1, y_2, y_3\}$,  
Edges:  

$$
x_1y_1,\; x_2y_1,\; x_2y_2,\; x_3y_2,\; x_3y_3
$$

Check subsets:  
- $S=\{x_1,x_2\}$: $N(S)=\{y_1,y_2\}$, size 2 → OK  
- $S=\{x_1,x_2,x_3\}$: $N(S)=\{y_1,y_2,y_3\}$, size 3 → OK  

Perfect matching exists.

---

### **Example 4 — Kruskal MST**
Edges sorted by weight:  

$$
(1,2,1), (2,3,2), (1,3,3), (3,4,4)
$$

Kruskal picks:  

$$
(1,2), (2,3), (3,4)
$$

---

### **Example 5 — Topological Order**
Graph:  

$$
a \to b,\; a \to c,\; b \to d,\; c \to d
$$

One valid order:  

$$
a, b, c, d
$$

---
