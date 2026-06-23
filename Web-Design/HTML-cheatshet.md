
---

# 🟥 **ACORDEÓN DE HTML**  
### *Formato Markdown — Español*

---

# # ⭐ 1. ¿Qué es HTML?

**HTML (HyperText Markup Language)** es el lenguaje que define la **estructura** de una página web.

- No es un lenguaje de programación  
- Es un lenguaje de **marcado**  
- Define **qué** aparece en la página, no **cómo se ve** (eso es CSS)

---

# # ⭐ 2. Estructura básica de un documento HTML

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Título</title>
</head>
<body>
  Contenido
</body>
</html>
```

---

# # ⭐ 3. Etiquetas esenciales

### **Texto**
```html
<h1>Encabezado</h1>
<p>Párrafo</p>
<span>Texto en línea</span>
```

### **Enlaces**
```html
<a href="https://example.com">Ir</a>
```

### **Imágenes**
```html
<img src="img.png" alt="Descripción">
```

### **Listas**
```html
<ul>
  <li>Elemento</li>
</ul>

<ol>
  <li>Elemento</li>
</ol>
```

---

# # ⭐ 4. Estructura semántica

### **Contenedores semánticos**
```html
<header>Encabezado</header>
<nav>Navegación</nav>
<main>Contenido principal</main>
<section>Sección temática</section>
<article>Contenido independiente</article>
<aside>Contenido lateral</aside>
<footer>Pie de página</footer>
```

### **div vs section vs article**
- **div** → contenedor sin significado  
- **section** → bloque temático  
- **article** → contenido independiente (post, noticia)  

---

# # ⭐ 5. Formularios

### **Formulario básico**
```html
<form action="/submit" method="POST">
  <label>Nombre</label>
  <input type="text" name="nombre">

  <label>Email</label>
  <input type="email" name="email">

  <button type="submit">Enviar</button>
</form>
```

### **Tipos de input comunes**
```html
<input type="text">
<input type="email">
<input type="password">
<input type="number">
<input type="checkbox">
<input type="radio">
<input type="file">
<input type="date">
```

---

# # ⭐ 6. Atributos importantes

```html
id="identificador"
class="clase"
src="ruta"
href="enlace"
alt="texto alternativo"
title="tooltip"
placeholder="texto"
required
disabled
readonly
```

---

# # ⭐ 7. Tablas

```html
<table>
  <thead>
    <tr><th>Nombre</th><th>Edad</th></tr>
  </thead>
  <tbody>
    <tr><td>Axel</td><td>25</td></tr>
  </tbody>
</table>
```

---

# # ⭐ 8. Multimedia

### **Audio**
```html
<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
</audio>
```

### **Video**
```html
<video controls>
  <source src="video.mp4" type="video/mp4">
</video>
```

---

# # ⭐ 9. Metaetiquetas importantes

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Descripción del sitio">
```

---

# # ⭐ 10. Comentarios

```html
<!-- Esto es un comentario -->
```

---

# # ⭐ 11. Buenas prácticas

- Usar etiquetas **semánticas**  
- Siempre incluir `alt` en imágenes  
- Mantener indentación limpia  
- Usar `label` asociado a inputs  
- Incluir `<meta viewport>` para responsive  
- No abusar de `<div>` (divitis)  

---

# # ⭐ 12. Accesibilidad (A11Y)

- `alt` descriptivo  
- Navegación por teclado  
- Roles ARIA cuando sea necesario  
- Contraste adecuado  
- Formularios con `label`  

---

# # ⭐ 13. SEO básico

- Usar `<title>`  
- Usar `<meta description>`  
- Encabezados jerárquicos (`h1 → h2 → h3`)  
- URLs limpias  
- Texto alternativo en imágenes  

---

# # ⭐ 14. Integración con CSS y JS

### **CSS**
```html
<link rel="stylesheet" href="styles.css">
```

### **JS**
```html
<script src="app.js"></script>
```

### **JS al final del body (buena práctica)**
```html
<script src="app.js" defer></script>
```

---

# # ⭐ 15. Lo que SIEMPRE cae en examen

- Estructura básica de HTML  
- Etiquetas semánticas  
- Formularios  
- Atributos importantes  
- Imágenes con `alt`  
- Meta viewport  
- Diferencia entre div / section / article  
- Cómo se enlaza CSS y JS  

---
