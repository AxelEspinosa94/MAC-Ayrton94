
---

# ✅ **Computer Graphics – Unit 3: Geometric Transformations **

# Computer Graphics – Unit 3: Geometric Transformations

## 1. Overview
This unit covers the mathematical foundations of geometric transformations in 2D and 3D.  
According to the official syllabus, the topics include:

- 3.1 Affine transformations  
  - Rotation  
  - Translation  
  - Scaling  
  - Shear  
  - Reflection  
- 3.1.1 Linear transformations  
- 3.1.2 Rigid transformations  
- 3.1.3 Orientation‑preserving transformations  
- 3.2 Homogeneous coordinates  
- 3.3 Composition of affine transformations  
- 3.4 3D transformations  
- 3.5 3D objects  

---

## 2. Affine Transformations

### Definition 2.1 — Affine Transformation
An affine transformation is a function  
$$
T(\mathbf{x}) = A\mathbf{x} + \mathbf{b}
$$  
where $A$ is a linear transformation and $\mathbf{b}$ is a translation vector.

Affine transformations preserve:
- Lines  
- Parallelism  
- Ratios of distances  

---

## 3. Linear Transformations

### Definition 3.1 — Linear Transformation
A transformation is linear if it satisfies:
$$
T(\mathbf{x} + \mathbf{y}) = T(\mathbf{x}) + T(\mathbf{y})
$$
$$
T(c\mathbf{x}) = cT(\mathbf{x})
$$

Examples:
- Rotation  
- Scaling  
- Shear  
- Reflection  

Translation is **not** linear (but is affine).

---

## 4. Basic 2D Transformations

### 4.1 Translation
$$
T(x, y) = (x + t_x,\; y + t_y)
$$

### 4.2 Scaling
$$
S(x, y) = (sx \cdot x,\; sy \cdot y)
$$

### 4.3 Rotation
Rotation by angle $\theta$ around the origin:
$$
R(\theta) =
\begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix}
$$

### 4.4 Shear
Horizontal shear:
$$
H_x =
\begin{bmatrix}
1 & k \\
0 & 1
\end{bmatrix}
$$

Vertical shear:
$$
H_y =
\begin{bmatrix}
1 & 0 \\
k & 1
\end{bmatrix}
$$

### 4.5 Reflection
Reflection across the x‑axis:
$$
\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}
$$

Reflection across the y‑axis:
$$
\begin{bmatrix}
-1 & 0 \\
0 & 1
\end{bmatrix}
$$

---

## 5. Rigid and Orientation‑Preserving Transformations

### Definition 5.1 — Rigid Transformation
A transformation that preserves distances and angles.  
Includes:
- Rotation  
- Translation  

### Definition 5.2 — Orientation‑Preserving Transformation
A transformation with determinant $> 0$.  
Examples:
- Rotation  
- Uniform scaling  

Reflections **reverse** orientation (determinant < 0).

---

## 6. Homogeneous Coordinates

### Definition 6.1 — Homogeneous Coordinates
A representation that adds an extra coordinate to allow affine transformations to be expressed as matrix multiplications.

A 2D point $(x, y)$ becomes:
$$
(x, y, 1)
$$

### 6.1 Matrix Forms

#### Translation
$$
T =
\begin{bmatrix}
1 & 0 & t_x \\
0 & 1 & t_y \\
0 & 0 & 1
\end{bmatrix}
$$

#### Scaling
$$
S =
\begin{bmatrix}
s_x & 0 & 0 \\
0 & s_y & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

#### Rotation
$$
R =
\begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

---

## 7. Composition of Transformations

### Definition 7.1 — Composition
Applying multiple transformations in sequence corresponds to multiplying their matrices.

$$
T_{\text{combined}} = T_n \cdots T_2 T_1
$$

**Order matters** (matrix multiplication is not commutative).

Example:
- Scale → Rotate → Translate  
$$
M = T \cdot R \cdot S
$$

---

## 8. 3D Transformations

### 8.1 3D Translation
$$
T =
\begin{bmatrix}
1 & 0 & 0 & t_x \\
0 & 1 & 0 & t_y \\
0 & 0 & 1 & t_z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

### 8.2 3D Scaling
$$
S =
\begin{bmatrix}
s_x & 0 & 0 & 0 \\
0 & s_y & 0 & 0 \\
0 & 0 & s_z & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

### 8.3 3D Rotations
Rotation around x‑axis:
$$
R_x(\theta) =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos\theta & -\sin\theta & 0 \\
0 & \sin\theta & \cos\theta & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Rotation around y‑axis:
$$
R_y(\theta) =
\begin{bmatrix}
\cos\theta & 0 & \sin\theta & 0 \\
0 & 1 & 0 & 0 \\
-\sin\theta & 0 & \cos\theta & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Rotation around z‑axis:
$$
R_z(\theta) =
\begin{bmatrix}
\cos\theta & -\sin\theta & 0 & 0 \\
\sin\theta & \cos\theta & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

---

## 9. 3D Objects

### Definition 9.1 — 3D Object
A geometric entity defined by:
- Vertices  
- Edges  
- Faces  
- Surface normals  

Common representations:
- Polygon meshes  
- Parametric surfaces  
- Implicit surfaces  

---

## 10. Summary of Key Concepts

- Affine transformations combine linear transformations and translations.  
- Homogeneous coordinates unify all transformations into matrix multiplication.  
- Composition order is crucial.  
- 3D transformations extend 2D concepts with additional rotation axes.  
- 3D objects require vertex, edge, face, and normal data for rendering.

---

## 11. Recommended Reading
- Foley, van Dam, Feiner, Hughes — *Computer Graphics: Principles and Practice*  
- Buss — *3D Computer Graphics: A Mathematical Introduction with OpenGL*  
- Vince — *Mathematics for Computer Graphics*  

---

