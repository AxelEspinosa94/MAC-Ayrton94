
---

# 📘 **EXAMEN EXTRAORDINARIO — DESARROLLO WEB**  

---

# 🧠 **PARTE 1 — EXAMEN TEÓRICO**

---

# ## **SECCIÓN A — Cliente/Servidor y HTTP**

### **1. Modelo cliente–servidor**
El navegador envía una solicitud HTTP al servidor; el servidor la procesa y devuelve una respuesta (HTML, JSON, error, etc.).

### **2. Métodos HTTP**
- **GET**: obtener datos  
- **POST**: crear recursos  
- **PUT**: reemplazar un recurso completo  
- **PATCH**: actualizar parcialmente  
- **DELETE**: eliminar recursos  

### **3. Partes de una URL**
`protocolo://dominio:puerto/ruta?query#fragmento`

### **4. Códigos HTTP**
- **200**: OK  
- **301**: Movido permanentemente  
- **403**: Prohibido (no autorizado)  
- **404**: No encontrado  
- **500**: Error interno del servidor  

---

# ## **SECCIÓN B — HTML**

### **5. Qué es HTML**
Lenguaje de marcado para estructurar contenido web.

### **6. div vs section vs article vs main**
- **div**: contenedor sin semántica  
- **section**: bloque temático  
- **article**: contenido independiente  
- **main**: contenido principal del documento  

### **7. Accesibilidad web**
Buenas prácticas: texto alternativo, navegación por teclado, contraste adecuado, roles ARIA.

### **8. DOM**
Representación en memoria del documento HTML, manipulable con JavaScript.

---

# ## **SECCIÓN C — CSS**

### **9. Box model**
`content → padding → border → margin`

### **10. display**
- **block**: ocupa todo el ancho  
- **inline**: no respeta width/height  
- **inline-block**: respeta tamaño y se comporta inline  
- **flex**: layout 1D  
- **grid**: layout 2D  

### **11. Media queries**
```css
@media (max-width: 768px) {
  .box { width: 100%; }
}
```

### **12. Unidades**
- **px**: unidad absoluta  
- **em**: relativo al elemento padre  
- **rem**: relativo al root  
- **%**: relativo al contenedor  
- **vh/vw**: relativo al viewport  

---

# ## **SECCIÓN D — JavaScript**

### **13. var / let / const**
- **var**: scope de función, hoisting  
- **let**: scope de bloque  
- **const**: no reasignable  

### **14. Eventos**
`click`, `mouseover`, `submit`, `keydown`, etc.

### **15. addEventListener**
```js
element.addEventListener("click", () => {
  console.log("clicked");
});
```

### **16. Fetch API**
API del navegador para hacer solicitudes HTTP.

---

# ## **SECCIÓN E — Backend / APIs**

### **17. API REST**
Arquitectura basada en recursos y métodos HTTP.

### **18. JSON**
Formato de datos clave–valor.  
Ejemplo:
```json
{"nombre": "Ayrton", "edad": 25}
```

### **19. Stateless**
Cada solicitud es independiente; el servidor no guarda estado.

### **20. Endpoint**
URL que representa un recurso.  
Ejemplo: `/users/123`

---

# ## **SECCIÓN F — Seguridad**

### **21. XSS**
Inyección de JavaScript malicioso en el navegador.  
Prevención: sanitizar inputs, escapar HTML, usar `innerText`.

### **22. CSRF**
Un sitio malicioso fuerza al navegador a enviar solicitudes válidas.  
Prevención: tokens CSRF, SameSite cookies.

### **23. SQL Injection**
Inyección de SQL malicioso en consultas.  
Prevención: consultas preparadas.

### **24. HTTPS**
Cifra la comunicación y verifica identidad del servidor.

---

# ## **SECCIÓN G — Bases de Datos**

### **25. SQL vs NoSQL**
- SQL: tablas y relaciones  
- NoSQL: documentos, colecciones  

### **26. ORM**
Mapea objetos a tablas o documentos.

### **27. SELECT**
Consulta para obtener datos.  
Ejemplo:
```sql
SELECT * FROM usuarios WHERE edad > 18;
```

---

# ## **SECCIÓN H — Hosting**

### **28. Hosting / dominio**
- Hosting: servidor donde vive el sitio  
- Dominio: nombre que apunta a la IP del servidor  

### **29. CDN**
Red de servidores que distribuyen contenido de forma rápida.

### **30. GitHub Pages**
Servicio para publicar sitios estáticos desde un repositorio.

---

---

# # 💻 **PARTE 2 — EXAMEN PRÁCTICO**

---

# ## **SECCIÓN A — HTML**

### **1. Estructura HTML correcta**
```html
<header>
  <h1>APP</h1>
</header>

<nav>
  <a href="#">Home</a>
  <a href="#">App1</a>
  <a href="#">App2</a>
</nav>

<main>
  <article>
    <h2>Artículo</h2>
    <p>Contenido del artículo.</p>
  </article>

  <img src="url" alt="Descripción de la imagen">

  <form>
    <label>Nombre</label>
    <input type="text">

    <label>Email</label>
    <input type="email">

    <button type="submit">Enviar</button>
  </form>
</main>
```

---

# ## **SECCIÓN B — CSS**

### **2. Centrado + Flex + Responsive**
```css
.container {
  width: 800px;
  margin: 0 auto;
}

.layout {
  display: flex;
  gap: 20px;
}

@media (max-width: 768px) {
  .layout {
    flex-direction: column;
  }
}
```

---

# ## **SECCIÓN C — JavaScript**

### **3. Mostrar valor del input**
```html
<input id="nombre">
<button id="btn">Mostrar</button>
<p id="out"></p>

<script>
  btn.addEventListener("click", () => {
    out.textContent = nombre.value;
    nombre.value = "";
  });
</script>
```

---

### **4. Números pares**
```js
function pares(arr) {
  return arr.filter(n => n % 2 === 0);
}
```

---

# ## **SECCIÓN D — DOM**

### **5. Cambiar color y texto**
```html
<button id="cambiar">Cambiar</button>
<p id="texto">Texto original</p>

<script>
  cambiar.addEventListener("click", () => {
    document.body.style.background = "lightblue";
    texto.textContent = "Texto cambiado";
  });
</script>
```

---

# ## **SECCIÓN E — Fetch API**

### **6. Mostrar usuarios**
```js
fetch("https://jsonplaceholder.typicode.com/users")
  .then(res => res.json())
  .then(data => {
    const ul = document.createElement("ul");
    data.forEach(u => {
      const li = document.createElement("li");
      li.textContent = u.name;
      ul.appendChild(li);
    });
    document.body.appendChild(ul);
  });
```

---

# ## **SECCIÓN F — Seguridad**

### **7. Arreglar XSS**
```html
<div id="msg"></div>
<script>
  const name = new URLSearchParams(location.search).get("name");
  msg.textContent = "Hello " + name;
</script>
```

---

# ## **SECCIÓN G — SQL / NoSQL**

### **8. SQL mayores de 18**
```sql
SELECT * FROM usuarios WHERE edad > 18;
```

### **9. JSON válido**
```json
{
  "nombre": "Ayrton",
  "edad": 25,
  "correo": "correo@example.com"
}
```

---

# ## **SECCIÓN H — Deploy**

### **10. Subir sitio a GitHub Pages**
1. Crear repositorio  
2. Subir archivos  
3. Ir a Settings → Pages  
4. Seleccionar branch `main`  
5. Guardar  
6. El sitio queda disponible en `https://usuario.github.io/repositorio`

---

