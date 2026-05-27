
---

# **Computer Graphics – Unit 2: Graphic Primitives**

# Computer Graphics – Unit 2: Graphic Primitives

## 1. Overview
This unit covers the fundamental building blocks of computer graphics: points, lines, polygons, and the raster algorithms used to generate them.  
According to the official syllabus, the topics include:

- 2.1 Initialization of a graphics environment  
- 2.2 Generation of points, lines, and polygons  
- 2.3 Raster techniques: DDA and Bresenham (lines and circles)  
- 2.4 User interaction methods  

---

## 2. Initialization of a Graphics Environment

### Definition 2.1 — Graphics Environment
A graphics environment is the combination of hardware and software that enables the creation, manipulation, and display of graphical primitives.

### Common Initialization Steps
1. **Create a window or viewport**  
   A rectangular region where rendering occurs.

2. **Initialize the graphics API**  
   Examples: OpenGL, DirectX, Vulkan, WebGL.

3. **Set up coordinate systems**  
   - World coordinates  
   - Normalized device coordinates  
   - Screen coordinates  

4. **Configure buffers**  
   - Color buffer  
   - Depth buffer  
   - Framebuffer  

---

## 3. Graphic Primitives

### Definition 3.1 — Primitive
A primitive is a basic geometric element used to construct more complex shapes.

### 3.1 Points
A point is the smallest addressable unit in a raster display, represented by pixel coordinates \((x, y)\).

### 3.2 Lines
A line segment is defined by two endpoints \((x_0, y_0)\) and \((x_1, y_1)\).

### 3.3 Polygons
A polygon is a closed shape formed by connecting multiple line segments.  
Properties:
- Must be closed  
- Can be convex or concave  
- Often represented as a list of vertices  

---

## 4. Rasterization

### Definition 4.1 — Rasterization
The process of converting geometric primitives into discrete pixels on a raster display.

Rasterization must:
- Approximate continuous geometry  
- Minimize aliasing  
- Be efficient for real‑time rendering  

---

## 5. DDA Algorithm (Digital Differential Analyzer)

### Definition 5.1 — DDA
DDA is an incremental algorithm for rasterizing lines by computing intermediate points using floating‑point arithmetic.

### Algorithm Summary
Given endpoints \((x_0, y_0)\) and \((x_1, y_1)\):

1. Compute  
   \[
   dx = x_1 - x_0,\quad dy = y_1 - y_0
   \]
2. Determine the number of steps:  
   \[
   steps = \max(|dx|, |dy|)
   \]
3. Compute increments:  
   \[
   x_{inc} = \frac{dx}{steps},\quad y_{inc} = \frac{dy}{steps}
   \]
4. Starting at \((x_0, y_0)\), generate points:  
   \[
   x_{k+1} = x_k + x_{inc},\quad y_{k+1} = y_k + y_{inc}
   \]

### Advantages
- Simple  
- Works for all slopes  

### Disadvantages
- Uses floating‑point arithmetic  
- Accumulated rounding errors  

---

## 6. Bresenham’s Line Algorithm

### Definition 6.1 — Bresenham Line Algorithm
A highly efficient integer‑based algorithm for rasterizing lines with minimal error.

### Key Idea
At each step, choose the pixel whose center is closest to the true line.

### Error Term
The algorithm maintains a decision variable \(p\) that determines whether to increment the y‑coordinate.

### Advantages
- Integer arithmetic only  
- Fast and accurate  
- Ideal for hardware implementation  

---

## 7. Bresenham’s Circle Algorithm

### Definition 7.1 — Midpoint Circle Algorithm
An extension of Bresenham’s method to rasterize circles using symmetry.

### Circle Equation
\[
x^2 + y^2 = r^2
\]

### Symmetry
Only one octant is computed; the remaining points are mirrored.

### Decision Variable
At each step, choose between:
- East pixel  
- South‑East pixel  

---

## 8. Polygon Generation

### Definition 8.1 — Polygon Rasterization
The process of filling a polygon interior with pixels.

### Common Techniques
- **Scanline fill**  
- **Edge tables (ET)**  
- **Active edge tables (AET)**  

### Convex vs. Concave
Convex polygons are easier to rasterize; concave polygons require decomposition.

---

## 9. User Interaction Methods

### Definition 9.1 — User Interaction
The mechanisms through which a user manipulates or provides input to a graphics system.

### Common Interaction Forms
- Mouse clicks (selecting points, dragging objects)  
- Keyboard input (commands, shortcuts)  
- Touch gestures  
- Event‑driven callbacks (e.g., `onClick`, `onKeyPress`)  

### Interaction in Graphics APIs
Most APIs provide:
- Event loops  
- Input handlers  
- Device abstraction layers  

---

## 10. Summary of Key Concepts

- Primitives are the foundation of all graphical objects.  
- Rasterization converts continuous geometry into pixels.  
- DDA uses floating‑point increments; Bresenham uses integer arithmetic.  
- Circle rasterization uses symmetry to reduce computation.  
- User interaction is essential for interactive graphics applications.  

---

## 11. Recommended Reading (from syllabus)
- Foley, van Dam, Feiner, Hughes — *Computer Graphics: Principles and Practice*  
- Buss — *3D Computer Graphics: A Mathematical Introduction with OpenGL*  
- Villar Patiño — *Apuntes de Graficación usando OpenGL*  
- Vince — *Mathematics for Computer Graphics*


---
