
---

# 📘 **Statistics I – Unit I Theorem & Definition Compendium**

## 1. Introduction to Statistics

### 1.1 Importance of Statistics
**Definition — Statistics**  
Statistics is the discipline that deals with the collection, organization, analysis, interpretation, and presentation of data.

**Principle — Decision Making**  
Statistical methods provide quantitative evidence that supports decision-making under uncertainty.

**Theorem (Law of Large Numbers — Informal)**  
As the sample size increases, sample averages converge to the population mean.

---

## 2. Descriptive Statistics

### 2.1 Measurement Scales

**Definition — Nominal Scale**  
A scale that classifies data into categories without any order (e.g., colors, gender).

**Definition — Ordinal Scale**  
A scale that classifies data into ordered categories, but differences between categories are not measurable (e.g., rankings).

**Definition — Interval Scale**  
A numeric scale with equal intervals but no true zero (e.g., Celsius temperature).

**Definition — Ratio Scale**  
A numeric scale with equal intervals and a meaningful zero (e.g., weight, height).

**Lemma — Ratio Implies Interval**  
Every ratio-scale variable is also an interval-scale variable, but not vice versa.

---

### 2.2 Measures of Central Tendency & Position

**Definition — Mean**  

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i
$$

**Definition — Median**  
The middle value of an ordered dataset.

**Definition — Mode**  
The most frequent value in a dataset.

**Definition — Quantile**  
A value that divides the ordered data into equal-sized subsets.

**Theorem — Median Minimizes Absolute Deviations**  
The median $m$ of a dataset minimizes the function  

$$
\sum_{i=1}^n |x_i - m|.
$$

**Theorem — Mean Minimizes Squared Deviations**  
The mean $\bar{x}$ minimizes  

$$
\sum_{i=1}^n (x_i - a)^2.
$$

**Corollary — Uniqueness of the Mean**  
The minimizer of the sum of squared deviations is unique.

---

### 2.3 Measures of Dispersion

**Definition — Range**  

$$
\text{Range} = x_{\max} - x_{\min}
$$

**Definition — Variance**  

$$
s^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})^2
$$

**Definition — Standard Deviation**  

$$
s = \sqrt{s^2}
$$

**Definition — Interquartile Range (IQR)**  

$$
\text{IQR} = Q_3 - Q_1
$$

**Theorem — Non-negativity of Variance**  
For any dataset,  

$$
s^2 \ge 0,
$$

with equality iff all observations are identical.

**Lemma — Variance Decomposition**  
For any constant $c$:  

$$
\sum (x_i - c)^2 = \sum (x_i - \bar{x})^2 + n(\bar{x} - c)^2.
$$

---

### 2.4 Measures of Shape: Skewness & Kurtosis

**Definition — Skewness**  

$$
\gamma_1 = \frac{\frac{1}{n}\sum (x_i - \bar{x})^3}{s^3}
$$

**Definition — Kurtosis**  

$$
\gamma_2 = \frac{\frac{1}{n}\sum (x_i - \bar{x})^4}{s^4}
$$

**Theorem — Symmetry Implies Zero Skewness**  
If a distribution is symmetric around its mean, then  

$$
\gamma_1 = 0.
$$

**Lemma — Excess Kurtosis**  

$$
\text{Excess Kurtosis} = \gamma_2 - 3.
$$

---

### 2.5 Tabular & Graphical Data Presentation

**Definition — Frequency Table**  
A tabular summary showing counts or proportions for each category or class interval.

**Definition — Bar Chart**  
A graphical representation of categorical data using bars proportional to frequency.

**Definition — Line Chart**  
A graph connecting data points, typically used for time series.

**Definition — Stem-and-Leaf Plot**  
A textual visualization that preserves the original data values.

**Definition — Box-and-Whisker Plot**  
A graphical summary showing median, quartiles, and potential outliers.

**Theorem — Tukey’s Boxplot Outlier Rule**  
A value $x$ is considered an outlier if  

$$
x < Q_1 - 1.5\,\text{IQR} \quad \text{or} \quad x > Q_3 + 1.5\,\text{IQR}.
$$

---

### 2.6 Software-Based Statistical Computation (CAS, R, Excel)

**Definition — CAS (Computer Algebra System)**  
Software capable of symbolic and numeric computation (e.g., Mathematica, Maple).

**Definition — R**  
A programming language specialized for statistical computing and graphics.

**Definition — Spreadsheet Software (Excel)**  
A grid-based tool for data manipulation and statistical analysis.

**Theorem — Reproducibility Principle**  
Statistical results computed via software must be reproducible using the same dataset and code.

**Lemma — Deterministic Output**  
Given identical input and deterministic functions, R and Excel produce identical numerical results up to machine precision.

---

