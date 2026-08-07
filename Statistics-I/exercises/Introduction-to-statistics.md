---
title: "Statistics I – Unit I Exercise Notebook"
author: "Axel – Extraordinary Exam Practice"
---

# Statistics I – Unit I – Exercise Notebook

> Level: Undergraduate – Extraordinary exam  
> Topics: Importance of statistics, descriptive statistics, measurement scales, summaries, shape, and graphical representation.

---

## 1. Importance of Statistics in Decision Making

### Exercise 1.1
A company wants to launch a new product. They collect survey data from 500 potential customers about:
- **Interest level** (scale 1–5),
- **Income bracket** (low, medium, high),
- **Age** (in years).

**Tasks:**
**Identify** which variables are qualitative and which are quantitative.

qualitative: Interest level and age
quantitative: Income bracket

**Propose** at least three descriptive statistics or plots that management should see before deciding to launch.

1. A bar plot with X-Axis to be the Interest Level and the Y-Axis the number of Income bracket
2. By Income bracket we could make a box plot showing the distribution of the age
3. We could make a histogram showing the Interest level by age

**Explain** how sampling bias could affect the decision.

Since not all the ages are going to show equiparable interest levels or will be in the same income bracket, sampling bias would affect metrics such as the mean.

---

### Exercise 1.2
A hospital evaluates the effectiveness of a new treatment using data from 120 patients:
- Recovery time (days),
- Treatment type (A or B),
- Presence of side effects (yes/no).

**Tasks:**

**a)** Suggest a **statistical strategy** to compare treatments A and B using only descriptive statistics.

In the overview we could see the mean of the recovery time for both treatments, and get the max and min of the count of the side effects presence, so we can have a best-worst escenario for both treatments.

For further analysis I could believe the standard deviation would be a valuable metric for recovery time since we could get an interval that explains how in general are all the cases away from the mean.

To select the best treatment we must ensure to select the one with the least side effects and moreover a decent amount of recovery time, we could set up a variable `[recovery_time] < mean([recovery_time])` and `[side_effects] == False`, understanding the value of this variable will be either 1 or 0 we could count the cases, and make the selection

**b)** Describe how **outliers** in recovery time could mislead conclusions.

In short, Central Tendency measures would be affected, for example, if we have a small (and I mean very small) recovery time, let's say 0.5 days and in general the median is around 7-10 days, mean is going to drop below 7 days and that could be misleading.

**c)** Explain why **statistics is essential** in medical decision-making rather than relying on anecdotal evidence.

Quoting the Large Numbers Law, sample means tend to converge to population means, if a case reunites enough elements as other analyzed it is **almost sure** (in terms of what almost sure means) that it will fall in that field.

---

## 2. Measurement Scales

### Exercise 2.1
Classify each variable by measurement scale (nominal, ordinal, interval, ratio) and justify:

**a)** Blood type (A, B, AB, O) → Nominal, since they are categories but have no order specified.
**b)** Customer satisfaction (very dissatisfied, dissatisfied, neutral, satisfied, very satisfied) → Ordinal, since the order goes from very dissatisfied to very satisfied.  
**c)** Temperature in °C → Interval Scale, I mean, there exists 0 °C but it does reflect a temperature not the absense of it.
**d)** Number of defects per manufactured item → Ratio Scale, although **c)**, 0 defects mean there were no defects
**e)** Time of day in 24-hour format (e.g., 13:45) → Interval, there is no zero.

---

### Exercise 2.2
You are given the following variables:

- **X:** “Rank in a competition” (1st, 2nd, 3rd, …).  
- **Y:** “Score in the competition” (0–100).  
- **Z:** “Distance run” (meters).  

**Tasks:**
**a)** Determine the measurement scale of **X**, **Y**, and **Z**.

   -  **X**: Ordinal
   -  **Y**: Interval
   -  **Z**: Ratio

**b)** For each variable, state whether **mean**, **median**, and **standard deviation** are meaningful and why.

   -  **X**: No one, as it is defined there are going to be unique values, and getting statistics out of it would be meaningless.
   -  **Y**: The three measures would be meaningful because they can give useful metrics, however I'd say the mean and the sd since this variable is bounded.
   -  **Z**: The median since is unaffected by outliers.

**c)** Give an example of a **misuse of statistics** that arises from treating an ordinal variable as ratio.

If we take **X** and consider n values without repetition the mean and median will be close to a single value and the sd will not have a specific meaning.

---

## 3. Measures of Central Tendency and Position

### Exercise 3.1
A dataset of exam scores (out of 100) is:

$$
\{45, 52, 52, 60, 61, 68, 70, 70, 70, 92\}
$$

**Tasks:**
**a)** Compute the **mean**, **median**, and **mode**.

   -  $\bar{X}=\frac{45 + 52 + 52 + 60 + 61 + 68 + 70 + 70 + 70 + 92}{10} = \frac{640}{10} = 64$
   -  $m(X)=m\{45, 52, 52, 60, 61, 68, 70, 70, 70, 92\} = \frac{61+68}{2} = \frac{129}{2} = 69.5$
   -  $M(X) = 70$

**b)** Compute the **first quartile $Q_1$**, **third quartile $Q_3$**, and **interquartile range (IQR)**.

Data $\{45, 52, 52, 60, 61, 68, 70, 70, 70, 92\}$ is already sorted, then we slice it as

$$
M1 = \{45, 52, 52, 60, 61\}
M2 = \{68, 70, 70, 70, 92\}
$$

where 

$$
Q_1 = m(M_1) = 52
Q_2 = m(M_2) = 70
$$

and finally $IQR = Q_3 - Q_1 = 70 - 52 = 18$.

**c)** Discuss whether the mean or median is more appropriate to describe the “typical” performance and justify.

The problem is that the mean is a good estimator when there isn't outliers, but when they are there, mean is not very useful, on the other hand median is invariant to the outliers, this describes the "typical" performance.

---

### Exercise 3.2
Consider the following income data (in thousands of dollars):

$$
\{18, 20, 22, 23, 24, 25, 26, 27, 120\}
$$

**Tasks:**
**a)** Compute the **mean** and **median**.

   - $\bar{X}=\frac{18+20+22+23+24+25+26+27+120}{9}=\frac{305}{9} ~ 33.9$
   - $m(X)=m(\{18, 20, 22, 23, 24, 25, 26, 27, 120\})=24$

**b)** Explain how the **outlier** affects the mean and median.

   - Speaking of the mean, the outlier increases the mean by 13k dollars, considering how the amounts are distributed, it is a big difference
   - The median on the other hand seems barely unnafected, because without the outlier, the median is 23.5k, giving a difference of 500 USD which is an infimous difference compared to the mean

**c)** Suppose a policymaker uses only the mean to describe “average income”. Discuss the **risk** of this choice.

Mean is severely affected by outliers, one example of this can be seen in **b)**

---

### Exercise 3.3 (Theoretical)
Let $x_1, x_2, \dots, x_n$ be real numbers.

**Tasks:**
**a)** Show that the value $a$ that minimizes $\sum_{i=1}^n (x_i - a)^2$ is the **sample mean** $\bar{x}$.

This means that we must find a value for $a$ that minimizes

$$
\sum_{i=1}^n (x_i - a)^2 
$$

Using the derivative criteria to find local minimums we have:

$$
\frac{d}{dx}\sum_{i=1}^n (x_i - a)^2 = \sum_{i=1}^n 2(x_i - a) = 0
\rightarrow \sum_{i=1}^n (x_i - a) = 0
\rightarrow na = \sum_{i=1}^n x_i
\rightarroq a = \frac{1}{n}\sum_{i=1}^n x_i = \bar{x}
$$

Therefore, $a=\bar{x}$ is the value that minimizes the expression

**b)** Argue why this property makes the mean sensitive to outliers.

Simply by saying that if a mean is calculated considering outliers the difference between each point and the mean will be considerably. This means the minimum will not be a true minimum.

**c)** Explain why the **median** is more robust in the presence of extreme values.

This is due to the median definition. Outliers lay usually at the extreme values and they are typically a minority of all data

---

## 4. Measures of Dispersion

### Exercise 4.1
Using the exam scores from Exercise 3.1:

$$
\{45, 52, 52, 60, 61, 68, 70, 70, 70, 92\}
$$

**Tasks:**
**a)** Compute the **sample variance** and **sample standard deviation**.

   -  $\bar{x}=\frac{1}{10}\sum_{i=1}^10 x_i = 64$
   -  $s^2 =\frac{1}{9}\sum_{i=1}^10 (x_i -\bar{x})^2 ~ 1183.34$
   -  $s=\sqrt{1182.45} ~ 34.4$

**b)** Compute the **coefficient of variation** (CV = $s / \bar{x}$).

$$
CV = \frac{s}{\bar{x}} = \frac{34.4}{64}=0.5375
$$

**c)** Interpret the CV in terms of relative variability of the scores.

In general:

$$
0 \leq CV \lt 0.1 \rightarrow \text{low variability}
0.1 \leq CV \lt 0.5 \rightarrow \text{moderate variability}
0.5 \leq CV \lt 1 \rightarrow \text{high variability}
1 \lt CV \rightarrow \text{extremely high variability}
$$

In other words, data vary too much related to the mean, but not uncontrollably.

---

### Exercise 4.2
Two classes took the same exam:

- Class A: mean = 70, standard deviation = 5, size = 30.  
- Class B: mean = 70, standard deviation = 15, size = 30.

**Tasks:**

**a)** Explain why the **same mean** does not imply similar performance.

In short, because the sd is different. In terms of the coefficient of variation Class A vary less than Class B related to the mean.

**b)** Interpret the difference in **standard deviation** in terms of consistency.

So, from the 30 students in Class A it is safe to say that their grades were in the interval $[65, 75]$, and Class B is in the interval $[55, 85]$. In terms of a teacher side it would be weird to have very little variability in a group of grades, which means Class B are more consistent than A.

**c)** Suggest a situation where a **higher dispersion** might be desirable.

Technically you would want a higher dispersion when you have a lot of data.

---

### Exercise 4.3 (Variance Decomposition)
Let $x_1, \dots, x_n$ be a sample with mean $\bar{x}$. For any constant $c$, consider:

$$
S(c) = \sum_{i=1}^n (x_i - c)^2
$$

**Tasks:**

**a)** Show that:

$$
S(c) = \sum_{i=1}^n (x_i - \bar{x})^2 + n(\bar{x} - c)^2
$$

We use the definition and we add a $0$.

$$
S(c) = \sum_{i=1}^n (x_i - c)^2 = \sum_{i=1}^n (x_i -\bar{x} +\bar{x} - c)^2
=\sum_{i=1}^n \[(x_i - \bar{x})^2 +2(x_i - \bar{x})(\bar{x} - c) + (\bar{x} - c)^2\]
$$

By lineality

$$
=\sum_{i=1}^n (x_i - \bar{x})^2 +2\sum_{i=1}^n (x_i - \bar{x})(\bar{x} - c) + \sum_{i=1}^n (\bar{x} - c)^2
$$

Since $\bar{x}-c$ is a constant, then

$$
=\sum_{i=1}^n (x_i - \bar{x})^2 +2\sum_{i=1}^n (x_i - \bar{x})(\bar{x} - c) + n(\bar{x} - c)^2
$$

And finally, since $\sum_{i=1}^n (x_i - \bar{x})) = 0$, then:

$$
=\sum_{i=1}^n (x_i - \bar{x})^2 + n(\bar{x} - c)^2
$$

QED

**b)** Use this identity to argue that $S(c)$ is minimized when $c = \bar{x}$.

Since $n(\bar{x}-c)\ge 0$, minimum occurs when $c=\bar{x}$

**c)** Explain the interpretation of $n(\bar{x} - c)^2$ in terms of “penalty” for choosing a center different from the mean.

If $c\neq \bar{x}$, then $n(\bar{x} - c)^2\ge 0$ and therefore $S(c) = \sum_{i=1}^n (x_i - \bar{x})^2 > 0$.

---

## 5. Measures of Shape: Skewness and Kurtosis

### Exercise 5.1
Consider two distributions of exam scores:

- **Distribution A:** symmetric around 70.  
- **Distribution B:** heavily right-skewed with many low scores and few very high scores.

**Tasks:**
**a)** Describe qualitatively the **skewness** of A and B.

By the Theorem that establishes that if a distribution is symmetric around its mean, then **skewness** for Distribution A is 0.

Distribution B is right skewed

**b)** Explain how skewness affects the relationship between **mean** and **median**.

Its a position matter indeed, mean is always going to be the local maximum of the distribution. On the other hand, median is literaly the medium point in the distribution range.

**c)** For Distribution B, state whether the mean is greater or smaller than the median and justify.

As I said, mean would be the local maximum of the distribution and median would be either before or after it, but in general would be less than the mean.

---

### Exercise 5.2
You are given the following standardized moments for a dataset:

$$
\gamma_1 = 1.2, \quad \gamma_2 = 5.0
$$

**Tasks:**

**a)** Interpret the **skewness** $\gamma_1$.

This means that $\frac{1}{n}\sum (x_i - \bar{x})^3 > s^3$ implicating a positive skewness or right skewed

**b)** Compute the **excess kurtosis** and interpret its meaning.

$$
\text{Excess Kurtosis} = \gamma_2 -3 = 5-3 = 2
$$

**c)** Explain how high kurtosis affects the probability of extreme values.

Because it doesn't have an upper bound, so high kurtosis means the distribution plot is too big and therefore the existence of extreme values.

---

### Exercise 5.3 (Computation)
A small dataset is:

$$
\{2, 3, 3, 4, 9\}
$$

**Tasks:**

**a)** Compute the **mean** and **standard deviation**.

   -  $\mu(x) = \frac{2+3+3+4+9}{5} = \frac{21}{5} = 4.2$
   -  $\sigma^{2}(x) = \frac{1}{4}\sum_{i=1}^n (x_i - \mu(x))^2 = \frac{1}{4}\sum_{i=1}^n (x_i - 4.2)^2 = \frac{30.8}{4} = 7.7\rightarrow \sigma ~ 2.77 $

**b)** Compute the **skewness** using:

$$
\gamma_1 = \frac{\frac{1}{n}\sum (x_i - \mu(x))^3}{\sigma^3}
$$

Substituting the values for $\mu(x)$ and $\sigma$ we have:

$$
\gamma_1 = \frac{\frac{1}{n}\sum (x_i - 4.2)^3}{(2.77)^3} ~ 0.91
$$

**c)** Comment on whether the distribution is symmetric, left-skewed, or right-skewed.

Since it is $\gt 0$, we conclude it is right-skewed.

---

## 6. Tabular and Graphical Presentation

### Exercise 6.1 – Frequency Table and Bar Chart
A survey records the preferred type of transport of 80 people:

- Car: 32  
- Bus: 18  
- Bicycle: 10  
- Walking: 12  
- Metro: 8  

**Tasks:**
**a)** Construct a **frequency table** with absolute and relative frequencies.

| Category | Frequency | Relative Frequency | Percentage |
|---------|-----------|--------------------|------------|
| Car     |    32     |        40%         |    40%     |
| Bus     |    18     |       22.5%        |   62.5%    |
| Bicycle |    10     |       12.5%        |    75%     |
| Walking |    12     |        15%         |    90%     |
| Metro   |     8     |        10%         |  **100%**  |
| **Total** |    80     |    **!00%**        |            |


**b)** Design a **bar chart** (describe axes, bar heights, and labels).

```mermaid
bar
    title: Transportation Frequency
    x-axis: Categories
    y-axis: Frequency
    Car: 32
    Bus: 18
    Bicycle: 10
    Walking: 12
    Metro: 8
```

**c)** Explain one **misleading design choice** that could distort interpretation of the bar chart.

The only one I can come up to is to use the Accumulative Relative Frequency, because doing so would imply that the plot would only be increasing without showing the true behaviour of the data.

---

### Exercise 6.2 – Stem-and-Leaf Plot
The following are waiting times (in minutes) at a service desk:

$$
\{5, 7, 8, 9, 10, 11, 12, 13, 15, 18, 19, 20, 21, 22, 25\}
$$

**Tasks:**

**a)** Construct a **stem-and-leaf plot**.

Stem-and-Leaf Plot
------------------

Stem | Leaves
-----|-------------------------
  0  | 5 7 8 9
  1  | 0 1 2 3 5 8 9
  2  | 0 1 2 5

Key: 1 | 5 = 15


**b)** Identify the **median** and **quartiles** from the plot.

   -  $median = 13$
   -  $Q_1 = 9.5$ and $Q_3 = 19.5$

**c)** Comment on the **shape** (symmetry, skewness) of the distribution.

So we have the median is $14.33$ and the sd is $6.16$, which means the skewness is

$$
\gamma_1 = \frac{35.76}{233.75} ~ 0.15
$$

so, by definition is right skewed, but considering is close to zero we could affirm is almos simetric

---

### Exercise 6.3 – Box-and-Whisker Plot and Outliers
Using the waiting times from Exercise 6.2, suppose two additional observations are recorded: 40 and 45 minutes.

**Tasks:**

**a)** Recompute $Q_1$, $Q_3$, and IQR.

$Q_1 = 9.5$, $Q_3 = 19.5$ and $IQR = 10$

**b)** Using Tukey’s rule, determine whether 40 and 45 are **outliers**:

$$
\text{Lower fence} = Q_1 - 1.5 \cdot \text{IQR}, \quad
\text{Upper fence} = Q_3 + 1.5 \cdot \text{IQR}
$$

Substituing we have $45 \gt 40 \gt 19.5 + 1.5 = 21$. So, yes, they are outliers

**c)** Describe how these outliers would appear in a **box-and-whisker plot**.

```mermaid
---
title: Boxplot - Transportation Data
---
boxplot
    title: Data Boxplot
    orientation: horizontal
    min: 5
    q1: 9.5
    median: 13
    q3: 19.5
    max: 45
```

---

### Exercise 6.4 – Line Chart (Time Series)
Daily sales (in units) of a product over 10 days are:

$$
\{50, 52, 49, 60, 65, 70, 68, 72, 75, 80\}
$$

**Tasks:**

**a)** Describe how to construct a **line chart** for these data.

So, assuming data is sorted by day we get the differences by period:

$$
\[2,	-3,	11,	5,	5,	-2, 4,	3,	5\]
$$

and we trace the plot

```mermaid
line
    title: Line Plot of Data
    xAxisTitle: Index
    yAxisTitle: Value
    data:
        label: Values
        points:
            1: 2
            2: -3
            3: 11
            4: 5
            5: 5
            6: -2
            7: 4
            8: 3
            9: 5
```

**b)** Identify any **trend** or pattern.

After day 3 we observe a small decrecing tendency

**c)** Explain why a line chart is more appropriate than a bar chart for this dataset.

Because data is Ratio-Interval like, if it was nominal a bar chart would be better.

---

## 7. Software-Based Computation (CAS, R, Excel)

### Exercise 7.1 – R Script Design
You have a dataset of 200 observations of a variable “reaction time” (milliseconds).

**Tasks:**
**a)** Write a **pseudo-code or R-like script** to:
   - Read the data,
   - Compute mean, median, variance, skewness, and kurtosis,
   - Produce a histogram and boxplot.

```R
# ================================
# Load data
# ================================

# data <- scan("data.txt")
data <- c(2, -3, 11, 5, 5, -2, 4, 3, 5)

# ================================
# Compute descriptive statistics
# ================================

mean_value     <- mean(data)
median_value   <- median(data)
variance_value <- var(data)

# Skewness y kurtosis require 'moments' packages
if (!require(moments)) {
    install.packages("moments")
    library(moments)
}

skew_value     <- skewness(data)
kurtosis_value <- kurtosis(data)

# Print results
cat("Mean: ", mean_value, "\n")
cat("Median: ", median_value, "\n")
cat("Variance: ", variance_value, "\n")
cat("Skewness: ", skew_value, "\n")
cat("Kurtosis: ", kurtosis_value, "\n")

# ================================
# Plots
# ================================

# Histogram
hist(
    data,
    main = "Histogram of Data",
    xlab = "Values",
    col = "lightblue",
    border = "black"
)

# Boxplot
boxplot(
    data,
    main = "Boxplot of Data",
    ylab = "Values",
    col = "lightgreen"
)
```

**b)** Explain how you would **check reproducibility** of your results.

Save the file and upload it in a repo

**c)** Discuss one **advantage** and one **risk** of relying on software output without understanding the underlying statistics.

Without full context you would be underating or overating metrics, which could lead to wrong conclusions.

---

### Exercise 7.2 – Excel Workflow
A dataset of 100 heights (in cm) is stored in an Excel sheet in column A.

**Tasks:**

**a)** Describe the steps to compute:
   - Mean and median,
   - Standard deviation,
   - Quartiles and IQR.

```vba
MEAN(RANGE)
AVERAGE(RANGE)
DESVEST(RANGE)
QUARTILE(RANGE, 1) --> 1st
QUARTILE(RANGE, 3) --> 3rd
```

**b)** Explain how to create a **box-and-whisker plot** in Excel.

You select the range of the nominal data you want to show, then select the Box-and-whisker plot in the Insert tab.

**c)** Discuss how **data entry errors** could affect the computed statistics and how to detect them.

In general if there is a non valid value in Excel the whole operation will result in an error, however many times we use the IFERROR function which assigns a default value, and that could implicate some misleading errors.

---

### Exercise 7.3 – CAS Comparison
You compute the variance of the same dataset using:
- R,
- Excel,
- A CAS (e.g., Wolfram Mathematica).

You obtain slightly different numerical values due to rounding and different default formulas.

**Tasks:**
**a)** Explain the difference between **population variance** and **sample variance** and how software might choose one by default.

Difference is evident since one is applied over the total population and the other over a sample. by default R, Python and many other languages alike choose the population as default. To apply it over a sample, one performs the sampling first and then you calculate de variance.

In Excel there are specialized functions to calculate the sample and population variance following a behaviour alike

**b)** Discuss why **documentation** is crucial when interpreting software results.

Broadly speaking defaults vary from projects, repos and environments.

**c)** Propose a strategy to ensure **consistency** across different tools.

-  Code must be reproductible in any tool/lang
-  Plotting libraries are common in technologies as R, Python and JavaScript, so every code we make, it must follow the same packaging rules so the migration can be easy

---

# Selected Short Answers (for Self-Check)

> These are **partial** answers for quick verification, not full solutions.

- **Exercise 3.1**  
  - Mean: $\bar{x} = 64$.  
  - Median: $64.5$.  
  - Mode: $70$.  

- **Exercise 3.2**  
  - Mean: $\approx 33.3$.  
  - Median: $24$.  

- **Exercise 4.1**  
  - Sample variance: $\approx 190.7$.  
  - Standard deviation: $\approx 13.8$.  

- **Exercise 5.3**  
  - Mean: $4.2$.  
  - Standard deviation: $\approx 2.86$.  
  - Skewness: positive (right-skewed).

---