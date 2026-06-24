
---

# **📘 Theorem Compendium — Linear and Total Graphs**  
### *Graph Theory — Unit 5: Linear Graphs, Total Graphs, and Graph Factorization*

---

# **5.1 Linear Graphs**

## **5.1.1 Definition**

### **Definition — Line Graph**
Given a simple graph \(G = (V,E)\), its **line graph** \(L(G)\) is the graph whose:

- vertices correspond to edges of \(G\)  
- two vertices in \(L(G)\) are adjacent iff their corresponding edges in \(G\) share a common endpoint

Formally:

\[
V(L(G)) = E(G), \qquad
E(L(G)) = \{ \{e_i,e_j\} : e_i \cap e_j \neq \emptyset \}.
\]

---

## **5.1.2 Properties**

### **Theorem 5.1 — Degree in the Line Graph**
Let \(e = uv\) be an edge of \(G\). Then:

\[
\deg_{L(G)}(e) = (\deg_G(u)-1) + (\deg_G(v)-1).
\]

#### **Proof.**
In \(L(G)\), the vertex corresponding to \(e=uv\) is adjacent to all edges incident to \(u\) except \(e\), and all edges incident to \(v\) except \(e\).  
Thus:

- edges incident to \(u\): \(\deg_G(u)-1\)  
- edges incident to \(v\): \(\deg_G(v)-1\)

Sum gives the formula. ∎

---

### **Theorem 5.2 — Connectivity of Line Graphs**
If \(G\) is connected and has at least two edges, then \(L(G)\) is connected.

#### **Proof.**
Any two edges in a connected graph can be joined by a sequence of edges where consecutive edges share a vertex. This sequence becomes a walk in \(L(G)\). ∎

---

### **Theorem 5.3 — Characterization of Line Graphs (Whitney)**
For connected graphs other than \(K_3\), the line graph uniquely determines the original graph:

\[
L(G_1) \cong L(G_2) \implies G_1 \cong G_2.
\]

---

## **5.1.3 Characteristics**

- Line graphs eliminate degree‑1 vertices unless the original graph has isolated edges.  
- Cliques in \(L(G)\) correspond to stars in \(G\).  
- Cycles in \(G\) correspond to cycles in \(L(G)\).  
- \(L(G)\) is always claw‑free (contains no induced \(K_{1,3}\)).

---

# **5.2 Total Graphs**

## **5.2.1 Definition**

### **Definition — Total Graph**
The **total graph** \(T(G)\) of a graph \(G\) is defined as the graph whose:

- vertices represent **both** vertices and edges of \(G\)  
- adjacency occurs when:
  - two vertices of \(G\) are adjacent  
  - two edges of \(G\) are adjacent  
  - a vertex and an edge are incident

Formally:

\[
V(T(G)) = V(G) \cup E(G).
\]

---

## **5.2.2 Properties**

### **Theorem 5.4 — Degree in the Total Graph**
For a vertex \(v \in V(G)\):

\[
\deg_{T(G)}(v) = \deg_G(v) + \deg_G(v) = 2\deg_G(v).
\]

For an edge \(e = uv\):

\[
\deg_{T(G)}(e) = (\deg_G(u)-1) + (\deg_G(v)-1) + 2.
\]

#### **Proof.**
- A vertex \(v\) is adjacent in \(T(G)\) to:
  - its neighbors in \(G\)  
  - its incident edges  
  giving \(2\deg(v)\).

- An edge \(e=uv\) is adjacent to:
  - all edges incident to \(u\) except \(e\)  
  - all edges incident to \(v\) except \(e\)  
  - the two vertices \(u,v\)  
  giving the stated formula. ∎

---

## **5.2.3 Characteristics**

- \(T(G)\) contains \(G\) and \(L(G)\) as induced subgraphs.  
- \(T(G)\) is always connected if \(G\) is connected.  
- The chromatic number satisfies:

\[
\chi(T(G)) \ge \Delta(G)+1.
\]

- Total graphs encode full incidence structure of \(G\).

---

# **5.3 Graph Factorization**

## **5.3.1 Definition — Factor**
A **factor** of a graph \(G\) is a spanning subgraph \(H\) of \(G\).

That is:

\[
V(H) = V(G), \qquad E(H) \subseteq E(G).
\]

---

## **5.3.2 Definition — n‑Factor**
An **\(n\)-factor** is a factor where every vertex has degree exactly \(n\):

\[
\deg_H(v) = n \quad \forall v \in V(G).
\]

Special cases:

- **1‑factor** = perfect matching  
- **2‑factor** = spanning collection of cycles

---

## **5.3.3 Definition — Factorization**
A **factorization** of \(G\) is a partition of its edges into factors:

\[
E(G) = E(H_1) \cup E(H_2) \cup \cdots \cup E(H_k),
\quad H_i \text{ spanning}.
\]

---

## **5.3.4 Definition — n‑Factorization**
An **\(n\)-factorization** is a factorization where each factor is an \(n\)-factor.

---

## **5.3.5 Factorization of a Complete Graph**

### **Theorem 5.5 — 1‑Factorization of \(K_{2n}\)**
The complete graph \(K_{2n}\) is 1‑factorable:  
it can be decomposed into \(2n-1\) perfect matchings.

#### **Proof (Classical Round‑Robin).**
Label vertices \(1,2,\dots,2n\).  
Fix vertex \(2n\).  
Rotate the remaining \(2n-1\) vertices cyclically.  
Each rotation produces a perfect matching.  
All matchings are disjoint and cover all edges. ∎

---

### **Corollary 5.6**
\[
K_{2n} = M_1 \cup M_2 \cup \cdots \cup M_{2n-1},
\]
where each \(M_i\) is a perfect matching.

---

### **Theorem 5.7 — 2‑Factorization of Regular Graphs**
Every \(2k\)-regular graph can be decomposed into \(k\) 2‑factors.

#### **Proof Sketch.**
Use Petersen’s theorem: every regular graph of even degree has a 2‑factor.  
Remove it; the remainder is still regular of even degree.  
Repeat. ∎

---

# **5.4 Applications**

- **Network design:** line graphs model adjacency of communication links.  
- **Chemistry:** line graphs represent molecular bonds (e.g., Kekulé structures).  
- **Scheduling:** 1‑factorizations model round‑robin tournaments.  
- **Telecommunications:** total graphs encode full incidence for routing.  
- **Cycle decompositions:** 2‑factors represent cyclic routing or periodic tasks.

---

