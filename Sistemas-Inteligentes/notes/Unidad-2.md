# 🧩 Unidad 2 — Búsqueda No Informada (Resumen)

## 🎯 ¿Por qué buscamos?
El agente conoce **la meta**, pero **no sabe la secuencia de acciones** para alcanzarla. La búsqueda construye ese camino.

---

## 📐 Formalización del Problema de Búsqueda
Un problema se define como una **6‑tupla**:

- **Estado inicial:** $s_0$
- **Espacio de estados:** $S$
- **Acciones:** $A(s)$
- **Transición:** $Result(s,a) = s'$
- **Prueba de meta:** $IsGoal(s)$
- **Costo de ruta:** $c(s,a,s') \ge 0$

---

## 🧱 Estado vs Nodo
**Estado:** Representación del mundo en un momento.

**Nodo de búsqueda:** Elemento del árbol de búsqueda con:
- `state`
- `parent`
- `action`
- `path_cost (g)`

---

## 🚧 Frontera, Explorados y Estrategia
- **Frontera (open):** Nodos generados pero no expandidos.
- **Explorados (closed):** Estados ya visitados; evitan ciclos.
- **Estrategia:** Se define por **cómo se extraen nodos de la frontera**.

---

## 🌐 Búsqueda en Anchura (BFS)
- **Idea:** Explorar **nivel por nivel**.
- **Frontera:** Cola **FIFO**.
- **Propiedad clave:** Encuentra la solución **más corta en número de acciones**.

---

## 🌊 Búsqueda en Profundidad (DFS)
- **Idea:** Avanzar al nodo