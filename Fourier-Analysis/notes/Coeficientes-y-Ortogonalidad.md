
---

### Teoremario básico de Series de Fourier en $[-\pi,\pi]$

---

## 1. Definiciones fundamentales

### 1.1. Funciones periódicas

**Definición:**  
Una función $f:\mathbb{R}\to\mathbb{R}$ es **periódica de periodo** $T>0$ si

$$
f(x+T)=f(x)\quad \text{para todo }x\in\mathbb{R}.
$$

**Ejemplo:**  
- $f(x)=\sin x$ es periódica de periodo $2\pi$.  
- $f(x)=\cos(3x)$ es periódica de periodo $\frac{2\pi}{3}$.

---

### 1.2. Sistema trigonométrico en $[-\pi,\pi]$

**Definición:**  
Consideramos el conjunto de funciones

$$
\{1,\cos x,\sin x,\cos 2x,\sin 2x,\dots\}
$$

definidas en $[-\pi,\pi]$. A este conjunto se le llama **sistema trigonométrico**.

---

### 1.3. Producto interno en $L^2([-\pi,\pi])$

**Definición:**  
Para funciones reales $f,g$ integrables en $[-\pi,\pi]$, definimos

$$
\langle f,g\rangle = \int_{-\pi}^{\pi} f(x)g(x)\,dx.
$$

Decimos que $f$ y $g$ son **ortogonales** si $\langle f,g\rangle = 0$.

---

## 2. Ortogonalidad del sistema trigonométrico

### 2.1. Lema de ortogonalidad

**Lema:**  
En $[-\pi,\pi]$ se cumple:

1. $\displaystyle \int_{-\pi}^{\pi} \cos(nx)\,dx = 0$ para todo $n\ge 1$.  
2. $\displaystyle \int_{-\pi}^{\pi} \sin(nx)\,dx = 0$ para todo $n\ge 1$.  

3. $\displaystyle \int_{-\pi}^{\pi} \cos(nx)\cos(mx)\,dx = \begin{cases}
0, & n\ne m,\\
\pi, & n=m\ne 0,
\end{cases}$

4. $\displaystyle \int_{-\pi}^{\pi} \sin(nx)\sin(mx)\,dx = \begin{cases}
0, & n\ne m,\\
\pi, & n=m\ge 1,
\end{cases}$

5. $\displaystyle \int_{-\pi}^{\pi} \cos(nx)\sin(mx)\,dx = 0$ para todo $n,m\ge 0$.

**Demostración (idea):**  
- Para (1) y (2), se usa que $\cos(nx)$ y $\sin(nx)$ son funciones con simetría y oscilación completa en $[-\pi,\pi]$; la integral de un periodo completo es cero.  
- Para (3) y (4), se usa la identidad

$$
\cos(nx)\cos(mx)=\tfrac12[\cos((n-m)x)+\cos((n+m)x)]
$$

y se integra término a término. Cuando $n\ne m$, las integrales de cosenos no constantes en un periodo completo son cero; cuando $n=m$, queda una constante.  
- Para (5), se usa

$$
\sin(nx)\cos(mx)=\tfrac12[\sin((n+m)x)+\sin((n-m)x)]
$$

y se integra; ambas integrales son cero en $[-\pi,\pi]$.

$\square$

---

### 2.2. Consecuencia: sistema ortogonal

**Proposición:**  
El conjunto

$$
\{1,\cos x,\sin x,\cos 2x,\sin 2x,\dots\}
$$

es un sistema ortogonal en el espacio con producto interno $\langle f,g\rangle = \int_{-\pi}^{\pi} f(x)g(x)\,dx$.

**Demostración:**  
Se verifica que cualquier par distinto de funciones del sistema tiene producto interno cero usando el lema anterior.  

$\square$

---

## 3. Coeficientes de Fourier

### 3.1. Definición de coeficientes

**Definición:**  
Sea $f$ integrable en $[-\pi,\pi]$. Definimos sus **coeficientes de Fourier** como:

$$
a_0 = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\,dx,
$$

$$
a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos(nx)\,dx,\quad n\ge 1,
$$

$$
b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\sin(nx)\,dx,\quad n\ge 1.
$$

La **serie de Fourier** asociada a $f$ es

$$
S_f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty}\big(a_n\cos(nx)+b_n\sin(nx)\big).
$$

---

### 3.2. Deducción de las fórmulas de los coeficientes

**Teorema:**  
Si $f$ admite una expansión en serie de Fourier

$$
f(x)\sim \frac{a_0}{2} + \sum_{n=1}^{\infty}\big(a_n\cos(nx)+b_n\sin(nx)\big),
$$

entonces los coeficientes vienen dados necesariamente por las fórmulas anteriores.

**Demostración:**  
Multiplicamos la serie formalmente por $\cos(mx)$ e integramos en $[-\pi,\pi]$:

$$
\int_{-\pi}^{\pi} f(x)\cos(mx)\,dx = \int_{-\pi}^{\pi}\left[\frac{a_0}{2} + \sum_{n=1}^{\infty}\big(a_n\cos(nx)+b_n\sin(nx)\big)\right]\cos(mx)\,dx.
$$

Usando linealidad e intercambiando suma e integral (formalmente):

$$
= \frac{a_0}{2}\int_{-\pi}^{\pi}\cos(mx)\,dx + \sum_{n=1}^{\infty} a_n\int_{-\pi}^{\pi}\cos(nx)\cos(mx)\,dx + \sum_{n=1}^{\infty} b_n\int_{-\pi}^{\pi}\sin(nx)\cos(mx)\,dx.
$$

Por ortogonalidad:
- $\int_{-\pi}^{\pi}\cos(mx)\,dx=0$ si $m\ge 1$,
- $\int_{-\pi}^{\pi}\cos(nx)\cos(mx)\,dx = 0$ si $n\ne m$, y $\pi$ si $n=m$,
- $\int_{-\pi}^{\pi}\sin(nx)\cos(mx)\,dx=0$ para todo $n,m$.

Entonces solo sobrevive el término con $n=m$:

$$
\int_{-\pi}^{\pi} f(x)\cos(mx)\,dx = a_m\pi.
$$

Por tanto,

$$
a_m = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos(mx)\,dx.
$$

Un argumento análogo multiplicando por $\sin(mx)$ da la fórmula de $b_m$, y multiplicando por $1$ da la de $a_0$.  

$\square$

---

### 3.3. Ejemplo: $f(x)=x$ en $[-\pi,\pi]$

Sea $f(x)=x$. Calculamos sus coeficientes.

- $a_0 = \frac{1}{\pi}\int_{-\pi}^{\pi} x\,dx = 0$ (función impar).  
- Para $n\ge 1$:

$$
a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} x\cos(nx)\,dx.
$$

El integrando es impar ($x$ impar, $\cos(nx)$ par), así que $a_n=0$.

$$
b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} x\sin(nx)\,dx.
$$

Aquí el integrando es par ($x$ impar, $\sin(nx)$ impar), entonces:

$$
b_n = \frac{2}{\pi}\int_{0}^{\pi} x\sin(nx)\,dx.
$$

Integramos por partes:

$$
\int_0^{\pi} x\sin(nx)\,dx = \left[-\frac{x\cos(nx)}{n}\right]_0^{\pi} + \frac{1}{n}\int_0^{\pi}\cos(nx)\,dx.
$$

Pero $\int_0^{\pi}\cos(nx)\,dx = \left[\frac{\sin(nx)}{n}\right]_0^{\pi}=0$. Entonces:

$$
\int_0^{\pi} x\sin(nx)\,dx = -\frac{\pi\cos(n\pi)}{n} = -\frac{\pi(-1)^n}{n}.
$$

Por tanto:

$$
b_n = \frac{2}{\pi}\left(-\frac{\pi(-1)^n}{n}\right) = -\frac{2(-1)^n}{n}.
$$

La serie de Fourier es:

$$
x \sim \sum_{n=1}^{\infty} b_n\sin(nx) = \sum_{n=1}^{\infty} \left(-\frac{2(-1)^n}{n}\right)\sin(nx)
= 2\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}\sin(nx).
$$

---

## 4. Convergencia puntual básica

### 4.1. Teorema de Dirichlet (versión clásica)

**Teorema (Dirichlet, versión informal):**  
Sea $f$ una función $2\pi$-periódica, acotada, por tramos monótona y con un número finito de discontinuidades en $[-\pi,\pi]$. Entonces, en cada punto $x$:

- Si $f$ es continua en $x$, la serie de Fourier converge a $f(x)$.  
- Si $f$ tiene una discontinuidad de salto en $x$, la serie converge a

$$
\frac{f(x^+)+f(x^-)}{2}.
$$

*(No demostramos este teorema completo aquí porque requiere técnicas más avanzadas, pero es la base teórica de muchos ejemplos.)*

---

### 4.2. Ejemplo de convergencia: $f(x)=x$

La función $f(x)=x$ en $[-\pi,\pi]$ es continua y se extiende como función impar $2\pi$-periódica. Por Dirichlet, su serie de Fourier

$$
x = 2\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}\sin(nx)
$$

converge a $x$ para todo $x\in(-\pi,\pi)$, y en los puntos $\pm\pi$ converge al valor medio de los límites laterales (que en este caso coinciden).

---

## 5. Identidades útiles: Parseval

### 5.1. Teorema de Parseval

**Teorema (Parseval):**  
Sea $f\in L^2([-\pi,\pi])$ con coeficientes de Fourier $a_0,a_n,b_n$. Entonces:

$$
\frac{1}{\pi}\int_{-\pi}^{\pi} |f(x)|^2\,dx = \frac{a_0^2}{2} + \sum_{n=1}^{\infty}\big(a_n^2 + b_n^2\big).
$$

**Idea de demostración:**  
- Se considera la serie de Fourier truncada

$$
S_N(x)=\frac{a_0}{2}+\sum_{n=1}^{N}(a_n\cos(nx)+b_n\sin(nx)).
$$

- Se calcula $\int_{-\pi}^{\pi} |S_N(x)|^2\,dx$ usando ortogonalidad; esto da exactamente

$$
\int_{-\pi}^{\pi} |S_N(x)|^2\,dx = \pi\left(\frac{a_0^2}{2} + \sum_{n=1}^{N}(a_n^2+b_n^2)\right).
$$

- Luego se usa que $S_N\to f$ en $L^2$ (bajo hipótesis adecuadas) y se pasa al límite $N\to\infty$.

$\square$ (idea)

---

### 5.2. Ejemplo de uso de Parseval

Tomemos $f(x)=x$ en $[-\pi,\pi]$. Ya sabemos que:
- $a_0=0$, $a_n=0$,
- $b_n = -\frac{2(-1)^n}{n}$.

Entonces Parseval dice:

$$
\frac{1}{\pi}\int_{-\pi}^{\pi} x^2\,dx = \sum_{n=1}^{\infty} b_n^2.
$$

Calculamos el lado izquierdo:

$$
\int_{-\pi}^{\pi} x^2\,dx = 2\int_0^{\pi} x^2\,dx = 2\left[\frac{x^3}{3}\right]_0^{\pi} = \frac{2\pi^3}{3}.
$$

Por tanto:

$$
\frac{1}{\pi}\cdot \frac{2\pi^3}{3} = \frac{2\pi^2}{3}.
$$

Ahora:

$$
b_n^2 = \left(-\frac{2(-1)^n}{n}\right)^2 = \frac{4}{n^2},
$$

así que:

$$
\sum_{n=1}^{\infty} b_n^2 = \sum_{n=1}^{\infty} \frac{4}{n^2} = 4\sum_{n=1}^{\infty} \frac{1}{n^2}.
$$

Igualando:

$$
\frac{2\pi^2}{3} = 4\sum_{n=1}^{\infty} \frac{1}{n^2}
\quad\Rightarrow\quad
\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}.
$$

Esto recupera la famosa identidad de la serie de Basel usando Fourier.

---

