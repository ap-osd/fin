
# Terminal Value
## Using Discounted Cash Flow (DCF)

**Present Value of Perpetuity**

For an infinite series of constant cash flows:

$\text{DCF} = \sum_{t=1}^{\infty} \frac{CF}{(1 + r)^t}$

Since CF is constant, we can factor it out of the summation:

$\text{DCF} = CF \times \sum_{t=1}^{\infty} \frac{1}{(1 + r)^t}$

**Substituting the terms for the DCF as a generic geometric series:**    
This is a geometric series (see Appendix A) with the first term $\frac{1}{1 + r}$ and common ratio $\frac{1}{1 + r}$ .

$\text{DCF}_{\infty} = CF \times \frac{\frac{1}{1 + r}}{1 - \frac{1}{1 + r}}$

**Simplify the denominator:**

$1 - \frac{1}{1 + r} = \frac{r}{1 + r}$

**Now the DCF expression becomes:**

$\text{DCF}_{\infty} = CF \times \frac{\frac{1}{1 + r}}{\frac{r}{1 + r}} = CF \times \frac{1}{r}$

Thus, the DCF for an infinite series of constant cash flows (or Present Value of Perpetuity) simplifies to:

$\text{DCF}_{\infty} = \text{PV}_{\infty} = CF \times \frac{1}{r}$

Assuming FCF=1.  
Then:

$\boxed{\text{DCF}_{\infty} = \text{PV}_{\infty} = \frac{1}{r}}$

## Using Perpetuity Growth Model (Gordon Growth Model)

$\text{TV}_{\infty} = \frac{CF_{n} \times (1 + g)}{r - g}$

Where:  
 $CF_n$ = Cash Flow in the final forecasted year (e.g., Year n)  
 $g$ = Perpetuity growth rate (the rate at which cash flows will grow forever)  
 $r$ = Discount rate

Assumimg  
 $g=0$ ; zero percent growth  
 $CF_n = 1$ ; unit FCF
 
Then:  
$\text{TV}_{\infty} = \frac{1 \times (1 + 0)}{r - 0}$

$\boxed{\text{TV}_{\infty} = \frac{1}{r}}$

## Example
For $5$% discount rate, $r=0.05$, $\text{TV}_{\infty} = \frac{1}{0.05} \Rightarrow \boxed{\text{TV}_{\infty} = 20}$

For $10$% discount rate, $r=0.1$, $\text{TV}_{\infty} = \frac{1}{0.1} \Rightarrow \boxed{\text{TV}_{\infty} = 10}$

![TV](tv.png "Terminal Value")

``` python
import tv

tv.compute_tv()
```
