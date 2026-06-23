
---

# 🟨 **ACORDEÓN DE JAVASCRIPT**  
### *Formato Markdown — Español*

---

# # ⭐ 1. Tipos de datos

### **Primitivos**
```js
string
number
boolean
null
undefined
symbol
bigint
```

### **No primitivos**
```js
object
array
function
```

---

# # ⭐ 2. Variables

```js
var   // scope de función, hoisting
let   // scope de bloque
const // no reasignable
```

---

# # ⭐ 3. Operadores útiles

### **Aritméticos**
```js
+ - * / % **
```

### **Comparación**
```js
==   // comparación flexible
===  // comparación estricta
!=
!== 
```

### **Lógicos**
```js
&&
||
!
```

### **Nullish**
```js
??   // usa el valor de la derecha si el de la izquierda es null o undefined
```

---

# # ⭐ 4. Funciones

### **Declaración**
```js
function suma(a, b) {
  return a + b;
}
```

### **Función flecha**
```js
const suma = (a, b) => a + b;
```

### **Funciones como valores**
```js
const f = () => console.log("Hola");
```

---

# # ⭐ 5. Objetos

```js
const persona = {
  nombre: "Axel",
  edad: 25,
  saludar() {
    console.log("Hola");
  }
};
```

### **Acceso**
```js
persona.nombre
persona["edad"]
```

---

# # ⭐ 6. Arreglos

```js
const nums = [1, 2, 3];
```

### **Métodos clave**
```js
push()     // agregar al final
pop()      // quitar último
shift()    // quitar primero
unshift()  // agregar al inicio
map()      // transformar
filter()   // filtrar
reduce()   // acumular
find()     // encontrar elemento
includes() // contiene?
```

---

# # ⭐ 7. DOM (Document Object Model)

### **Seleccionar elementos**
```js
document.getElementById("id")
document.querySelector(".clase")
document.querySelectorAll("p")
```

### **Modificar contenido**
```js
element.textContent = "Hola"
element.innerHTML = "<b>Hola</b>"
```

### **Modificar estilos**
```js
element.style.color = "red"
```

---

# # ⭐ 8. Eventos

### **Escuchar eventos**
```js
element.addEventListener("click", () => {
  console.log("click");
});
```

### **Eventos comunes**
```
click
input
submit
keydown
mouseover
load
```

---

# # ⭐ 9. Fetch API (HTTP desde JS)

### **GET**
```js
fetch("https://api.com/data")
  .then(res => res.json())
  .then(data => console.log(data));
```

### **POST**
```js
fetch("https://api.com/users", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ nombre: "Axel" })
});
```

---

# # ⭐ 10. Async / Await

```js
async function cargar() {
  const res = await fetch("https://api.com");
  const data = await res.json();
  console.log(data);
}
```

---

# # ⭐ 11. Manejo de errores

```js
try {
  // código
} catch (error) {
  console.error(error);
}
```

---

# # ⭐ 12. JSON

```js
const obj = { nombre: "Axel" };
const str = JSON.stringify(obj);
const copia = JSON.parse(str);
```

---

# # ⭐ 13. LocalStorage

```js
localStorage.setItem("nombre", "Axel");
localStorage.getItem("nombre");
localStorage.removeItem("nombre");
```

---

# # ⭐ 14. Clases (OOP)

```js
class Persona {
  constructor(nombre) {
    this.nombre = nombre;
  }
  saludar() {
    console.log("Hola " + this.nombre);
  }
}
```

---

# # ⭐ 15. Destructuring

### **Objetos**
```js
const { nombre, edad } = persona;
```

### **Arreglos**
```js
const [a, b] = [10, 20];
```

---

# # ⭐ 16. Spread y Rest

### **Spread**
```js
const copia = { ...persona };
```

### **Rest**
```js
function sumar(...nums) {
  return nums.reduce((a, b) => a + b);
}
```

---

# # ⭐ 17. Módulos

### **Exportar**
```js
export const x = 10;
```

### **Importar**
```js
import { x } from "./modulo.js";
```

---

# # ⭐ 18. Temporizadores

```js
setTimeout(() => console.log("Hola"), 1000);
setInterval(() => console.log("tick"), 1000);
```

---

# # ⭐ 19. this

- En funciones normales → depende del contexto  
- En funciones flecha → hereda el contexto externo  

---

# # ⭐ 20. Lo que SIEMPRE cae en examen

- DOM + eventos  
- Fetch API  
- Funciones flecha  
- map / filter / reduce  
- var vs let vs const  
- JSON  
- Async/await  
- Selectores del DOM  
- Manipulación de elementos  

---
