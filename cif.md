# Compound Interest Equation

$A = P \left(1 + \frac{r}{n}\right)^{nt}$

where:
* $A$ = amount 
* $P$ = principal
* $r$ = rate (in decimal, e.g. 8\% is 0.08)
* $n$ = number of times compounded per year
* $t$ = number of years

# Annual Compound
$n=1$, it is compounded annually

**Amount**, given the principal and rate.

$A = P \left(1 + r\right)^t$

**Principal**, given the amount and rate.

$P = \frac{A}{\left(1 + r\right)^t}$

**Rate**, given the amount and principal.

$r = \left(\frac{A}{P}\right)^\frac{1}{t}-1$

# Continuous Compound
$t=1$, it is compounded for a year  
$r=1$, the amound doubles every period, which is 100%  
$P=1$, for unit principle  

$A = 1 \times \left(1 + \frac{1}{n}\right)^{n}$

$n = 1,   A = 2.00000$  
$n = 2,   A = 2.25000$  
$n = 10,  A = 2.59374$  
$n = 100, A = 2.70481$  
$n = 1000, A = 2.71692$  
$n = 10000, A = 2.71814$  
$n = 100000, A = 2.71826$    
$n = 1000000, A = 2.71828$    

$$ \text{For continuous compounding,}\quad n=\infty $$
$$ \lim_{n\to\infty} \left( 1 + \frac{1}{n} \right)^n = e = 2.718281828459045 $$

Assume $x = \frac{n}{r}$  

Replacing $n$ in $A = P \left(1 + \frac{r}{n}\right)^{nt}$  

$A = P \left(1 + \frac{1}{x}\right)^{x.rt}$  

$A = P \left[\left(1 + \frac{1}{x}\right)^{x}\right]^{rt}$  

$A = P \times e^{rt}$

Alternatively,  

Exponential Growth = $e^{rt}$  
Exponential Decay = $e^{-rt}$

# Derived Concepts

## Compounded Annual Growth Rate (GAGR)
$r = \left(\frac{A}{P}\right)^\frac{1}{t}-1$

## Compounded Continuous Growth Rate (Log return)
If $x = b^a$, then $\log_b x = a$  

$A = P \times e^{rt}$  
$\frac{A}{P} = e^{rt}$  

$\log_e\left(\frac{A}{P}\right) = rt$

$\ln\left(\frac{A}{P}\right) = rt$

$t = 1$, for a single period

$r = \ln\left(\frac{A}{P}\right)$

## Cash Flow
Given:  
$g$ = growth rate in decimal

$\text{CF} = CF_1 + CF_2 + CF_3 + \cdots + CF_n$

### Relative
$CF_t = CF_{t-1} \times (1+g)$

$\text{CF} = CF_0 \times (1+g) + CF_1 \times (1+g) + CF_2 \times (1+g) + \cdots + CF_{n-1} \times (1+g)$

### Absolute
$CF_t = CF_0 \times (1+g)^t$

$\text{CF} = CF_0 \times (1+g)^1 + CF_0 \times (1+g)^2 + CF_0 \times (1+g)^3 + \cdots + CF_0 \times (1+g)^n$

$\text{CF} = CF_0 \times \left[(1+g)^1 + (1+g)^2 + (1+g)^3 + \cdots + (1+g)^n\right]$

$\text{CF} = CF_0 \times \sum_{t=1}^{n} (1+g)^t$

## Discounted Cash Flow (DCF)
$\text{DCF} = DCF_1 + DCF_2 + DCF_3 + \cdots + DCF_n$

### Relative
$DCF_t = DCF_{t-1} \times \frac{1+g}{1+r}$

$\text{DCF} = DCF_0 \times \frac{1+g}{1+r} + DCF_1 \times \frac{1+g}{1+r} + DCF_2 \times \frac{1+g}{1+r} + \cdots + DCF_{n-1} \times \frac{1+g}{1+r}$

### Absolute
$DCF_t = CF_0 \times \frac{(1+g)^t}{(1+r)^t}$

$\text{DCF} = \frac{CF_1}{(1+r)^1} + \frac{CF_2}{(1+r)^2} + \frac{CF_3}{(1+r)^3} + \cdots + \frac{CF_n}{(1+r)^n}$

$\text{DCF} = \frac{CF_0 \times (1+g)^1}{(1+r)^1} + \frac{CF_0 \times (1+g)^2}{(1+r)^2} + \frac{CF_0 \times (1+g)^3}{(1+r)^3} + \cdots + \frac{CF_0 \times (1+g)^n}{(1+r)^n}$

$\text{DCF} = CF_0 \times \left[\frac{(1+g)^1}{(1+r)^1} + \frac{(1+g)^2}{(1+r)^2} + \frac{(1+g)^3}{(1+r)^3} + \cdots + \frac{(1+g)^n}{(1+r)^n} \right]$

$\text{DCF} = CF_0 \times \sum_{t=1}^{n} \frac{(1+g)^t}{(1+r)^t}$

## Terminal Value
Terminal value is the Discounted Cash Flow from $n+1$ years until $\infty$.

Growth rate changes to a nominal value of $g$ where $g < r$.

$\text{TV} = \frac{CF_{n+1}}{(1+r)^{n+1}} + \frac{CF_{n+2}}{(1+r)^{n+2}} + \frac{CF_{n+3}}{(1+r)^{n+3}} + \cdots + \frac{CF_{\infty}}{(1+r)^\infty}$

$CF_{n+t} = CF_n \times (1+g)^{n+t}$

$\text{TV} = \frac{CF_n \times (1+g)^{n+1}}{(1+r)^{n+1}} + \frac{CF_n \times (1+g)^{n+2}}{(1+r)^{n+2}} + \frac{CF_n \times (1+g)^{n+3}}{(1+r)^{n+3}} + \cdots + \frac{CF_n \times (1+g)^{n+\infty}}{(1+r)^{n+\infty}}$

$\text{TV} = CF_n \times \left[\frac{(1+g)^{n+1}}{(1+r)^{n+1}} + \frac{(1+g)^{n+2}}{(1+r)^{n+2}} + \frac{(1+g)^{n+3}}{(1+r)^{n+3}} + \cdots + \frac{(1+g)^{n+\infty}}{(1+r)^{n+\infty}} \right]$

$\text{TV} = CF_n \times \sum_{t=n+1}^{\infty} \frac{(1+g)^t}{(1+r)^t}$

Substituting the terms for the DCF as a generic geometric series:  
This is a geometric series (see Appendix A) with the first term $\frac{1 + g}{1 + r}$ and common ratio $\frac{1 + g}{1 + r}$ .

$\text{TV} = CF_n \times \frac{\frac{1 + g}{1 + r}}{1 - \frac{1 + g}{1 + r}}$

Simplify the denominator:  

$1 - \frac{1 + g}{1 + r} = \frac{r -g}{1 + r}$

Now the TV expression becomes:

$\text{TV} = CF_n \times \frac{\frac{1 + g}{1 + r}}{\frac{r -g}{1 + r}}$

$\text{TV} = CF_n \times \frac{1 + g}{r -g}$

Assuming:  
$g = 0$, zero growth rate

Then:

$\text{TV} = CF_n \times \frac{1}{r}$


# Appendix A
## Geometric Series
**Basis of generic geometric series:**

$S = a + ar + ar^2 + ar^3 + \cdots + ar^{n-1}$

Where:
$a$ is the first term,
$r$ is the common ratio,
$n$ is the number of terms.

**Sum of a Finite Geometric Series:**

For a finite geometric series with $n$ terms, the sum $S_n$ is given by:

$S_n = a \frac{1 - r^n}{1 - r} \quad \text{for} \quad r \neq 1$

**Sum of an Infinite Geometric Series:**

For an infinite geometric series where $|r| < 1$ for convergence, the sum is:

$S_{\infty} = \frac{a}{1 - r} \quad \text{for} \quad |r| < 1$
