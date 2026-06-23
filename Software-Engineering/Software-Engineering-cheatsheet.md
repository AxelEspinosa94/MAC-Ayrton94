
---

# 🧩 Acordeón de **Ingeniería de Software**  

---

# 1. **Introducción a la Ingeniería de Software**

## 1.1 Conceptos fundamentales
- Ingeniería de Software = disciplina para **desarrollar, operar y mantener software** con calidad.  
- Crisis del software → sobrecostos, retrasos, mala calidad.  
- Software = programas + datos + documentación.

---

## 1.2 Procesos de producción de software (SDLC)

### **1.2.1 Modelo en Cascada**
```mermaid
flowchart TD
A[Requerimientos] --> B[Diseño]
B --> C[Implementación]
C --> D[Pruebas]
D --> E[Despliegue]
E --> F[Mantenimiento]
```

### **1.2.2 Modelo de Prototipos**
```mermaid
flowchart TD
A[Recolección de requisitos] --> B[Prototipo rápido]
B --> C[Evaluación del usuario]
C -->|Refina| A
C --> D[Producto final]
```

### **1.2.3 Modelo Incremental**
```mermaid
flowchart LR
A[Requerimientos] --> B[Incremento 1]
B --> C[Incremento 2]
C --> D[Incremento 3]
D --> E[Producto completo]
```

### **1.2.4 Modelo Evolutivo**
```mermaid
flowchart TD
A[Requerimientos iniciales] --> B[Versión 1]
B --> C[Retroalimentación]
C --> D[Versión 2]
D --> E[Retroalimentación]
E --> F[Versión n]
```

### **1.2.5 Modelo Espiral**
```mermaid
flowchart TD
A[Identificación de objetivos] --> B[Análisis de riesgos]
B --> C[Desarrollo y validación]
C --> D[Planificación]
D --> A
```

### **1.2.6 RUP (Rational Unified Process)**
```mermaid
flowchart LR
A[Inicio] --> B[Elaboración] --> C[Construcción] --> D[Transición]
```

---

## 1.3 Productos de la Ingeniería de Software
- Sistemas transaccionales  
- Sistemas integrados de gestión (ERP)  
- Sistemas de apoyo a decisiones  
- Comercio electrónico  
- Gestión del conocimiento  

---

# 2. **Administración de Proyectos de Software**

## 2.1 Etapas
- Inicio  
- Planeación  
- Ejecución  
- Control  
- Cierre  

## 2.2 Áreas clave (PMI)
- Alcance  
- Tiempo  
- Costo  
- Calidad  
- Recursos humanos  
- Comunicación  
- Riesgos  
- Abastecimiento  
- Integración  

## 2.3 Estimación
- Puntos de función  
- Complejidad por casos de uso  

---

# 3. **Ingeniería de Requerimientos**

## 3.1 Tipos
- Funcionales  
- No funcionales  

## 3.2 Técnicas de recolección
- Entrevistas  
- Cuestionarios  
- Lluvia de ideas  
- Prototipos  
- Casos de uso  

## 3.3 Documento SRS (IEEE 830)
- Correcto  
- No ambiguo  
- Completo  
- Consistente  
- Verificable  
- Modificable  

---

# 4. **Modelado**

## 4.1 Modelos
- Contexto  
- Comportamiento  

---

## 4.2 Diagramas (con ejemplos Mermaid)

### **4.2.1 DFD (Nivel 0)**
```mermaid
flowchart LR
A[Usuario] -->|Solicitud| B[Proceso Principal]
B -->|Respuesta| A
B --> C[Base de Datos]
```

### **4.2.2 Diagrama de Actividades**
```mermaid
flowchart TD
A[Inicio] --> B{¿Valida?}
B -->|Sí| C[Procesar]
B -->|No| D[Rechazar]
C --> E[Fin]
D --> E
```

### **4.2.3 Diagrama de Secuencia**
```mermaid
sequenceDiagram
actor U as Usuario
participant S as Sistema
U->>S: Enviar solicitud
S->>S: Validar datos
S-->>U: Respuesta
```

### **4.2.4 Diagrama de Clases**
```mermaid
classDiagram
class Usuario {
  +id
  +nombre
  +login()
}
class Pedido {
  +id
  +fecha
  +total
}
Usuario "1" --> "*" Pedido
```

### **4.2.5 Diagrama de Estados**
```mermaid
stateDiagram-v2
[*] --> Nuevo
Nuevo --> Procesando
Procesando --> Enviado
Enviado --> Entregado
```

---

# 5. **Diseño de Software**

## 5.1 Diseño arquitectónico
- MVC  
- Microservicios  
- Cliente-servidor  
- Arquitectura en capas  

## 5.2 Diseño de interfaz
- Usabilidad  
- Accesibilidad  

## 5.3 Diseño de componentes
- Cohesión alta  
- Acoplamiento bajo  

## 5.4 Diseño de implementación
- Diagrama de despliegue  

---

# 6. **Verificación, Validación y Pruebas**

## 6.1 V&V
- Verificación → ¿lo construimos bien?  
- Validación → ¿construimos lo que se necesitaba?  

## 6.2 Caja blanca
- Ruta básica  
- Condiciones  
- Ciclos  
- Flujo de datos  

## 6.3 Caja negra
- Clases de equivalencia  
- Pairwise  
- Aleatoria  

## 6.4 Tipos de pruebas
- Unidad  
- Integración  
- Sistema  
- Seguridad  
- Estrés  
- Desempeño  

---

# 7. **Estándares y Mejores Prácticas**

- CMMI  
- MoProsoft  
- NYCE  
- Scrum, XP, Kanban  
- COBIT  
- ITIL  

---

# 🎯 **Resumen para examen**
- Aprende los **modelos de proceso** y sus diferencias.  
- Memoriza **propiedades del SRS**.  
- Domina **diagramas UML básicos**.  
- Ten claro **patrones arquitectónicos**.  
- Repasa **tipos de pruebas**.  
- Conoce **CMMI, MoProsoft, ITIL, COBIT** a nivel conceptual.  

---

