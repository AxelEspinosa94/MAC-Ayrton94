
---

# 🎨 **ACORDEÓN DE CSS**  
### *Formato Markdown — Español*

---

# # ⭐ 1. Selectores

### **Selectores básicos**
```css
elemento { }
.clase { }
#id { }
```

### **Selectores combinados**
```css
div p      /* descendiente */
div > p    /* hijo directo */
div + p    /* hermano siguiente */
div ~ p    /* hermanos generales */
```

### **Pseudoclases**
```css
:hover
:active
:focus
:nth-child(n)
:first-child
:last-child
```

### **Pseudoelementos**
```css
::before
::after
::first-letter
::selection
```

---

# # ⭐ 2. Modelo de Caja (Box Model)

```
content → padding → border → margin
```

### Propiedades clave:
```css
width
height
padding
border
margin
box-sizing: border-box;
```

---

# # ⭐ 3. Display

### **block**
- Ocupa todo el ancho  
- Respeta width/height  
- Salta de línea

### **inline**
- No respeta width/height  
- No salta de línea

### **inline-block**
- Inline + respeta tamaño

### **flex (layout 1D)**
```css
display: flex;
flex-direction: row | column;
justify-content: center | space-between;
align-items: center;
gap: 10px;
```

### **grid (layout 2D)**
```css
display: grid;
grid-template-columns: repeat(3, 1fr);
gap: 20px;
```

---

# # ⭐ 4. Position

```css
position: static;   /* default */
position: relative; /* referencia para absolute */
position: absolute; /* se posiciona respecto al padre relativo */
position: fixed;    /* fijo en pantalla */
position: sticky;   /* se pega al hacer scroll */
```

---

# # ⭐ 5. Unidades

### **Absolutas**
- `px`

### **Relativas**
- `em` → relativo al padre  
- `rem` → relativo al root  
- `%` → relativo al contenedor  
- `vh` / `vw` → relativo al viewport  

---

# # ⭐ 6. Colores

```css
color: red;
color: #ff0000;
color: rgb(255,0,0);
color: rgba(255,0,0,0.5);
```

---

# # ⭐ 7. Tipografía

```css
font-family: Arial, sans-serif;
font-size: 16px;
font-weight: bold;
line-height: 1.5;
text-align: center;
text-transform: uppercase;
```

---

# # ⭐ 8. Bordes y sombras

```css
border: 1px solid #000;
border-radius: 10px;

box-shadow: 0 4px 10px rgba(0,0,0,0.2);
text-shadow: 1px 1px 2px #000;
```

---

# # ⭐ 9. Fondos

```css
background-color: #eee;
background-image: url("img.png");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
```

---

# # ⭐ 10. Flexbox (resumen rápido)

```css
display: flex;
flex-direction: row | column;
justify-content: center | space-between | space-around;
align-items: center | flex-start | flex-end;
flex-wrap: wrap;
```

---

# # ⭐ 11. Grid (resumen rápido)

```css
display: grid;
grid-template-columns: repeat(3, 1fr);
grid-template-rows: auto;
gap: 20px;
```

---

# # ⭐ 12. Media Queries (Responsive)

```css
@media (max-width: 768px) {
  .container {
    flex-direction: column;
  }
}
```

---

# # ⭐ 13. Animaciones y transiciones

### **Transiciones**
```css
transition: all 0.3s ease;
```

### **Animaciones**
```css
@keyframes mover {
  from { transform: translateX(0); }
  to   { transform: translateX(100px); }
}

.elemento {
  animation: mover 2s infinite alternate;
}
```

---

# # ⭐ 14. Variables CSS

```css
:root {
  --color-principal: #3498db;
}

div {
  color: var(--color-principal);
}
```

---

# # ⭐ 15. Z-index

```css
position: relative;
z-index: 10;
```

> Solo funciona con elementos posicionados (relative, absolute, fixed).

---

# # ⭐ 16. Overflow

```css
overflow: hidden;
overflow: scroll;
overflow: auto;
```

---

# # ⭐ 17. Cursor

```css
cursor: pointer;
cursor: not-allowed;
cursor: grab;
```

---

# # ⭐ 18. Reset CSS básico

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

---

# # ⭐ 19. Buenas prácticas

- Usar `box-sizing: border-box;`  
- Evitar IDs para estilos (usar clases)  
- Mantener estilos modulares  
- Usar variables CSS  
- Usar flex y grid en lugar de floats  

---

# # ⭐ 20. Lo que SIEMPRE cae en examen

- Box model  
- Flexbox  
- Grid  
- Media queries  
- Selectores  
- Unidades relativas  
- Position  
- Transiciones  

---

