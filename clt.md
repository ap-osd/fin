# Central Limit Theorem

Suppose that a large sample of observations is obtained, each observation being randomly produced in a way that does not depend on the values of the other observations, and the average (arithmetic mean) of the observed values is computed. If this procedure is performed many times, resulting in a collection of observed averages, the central limit theorem says that if the sample size is large enough, the probability distribution of these averages will closely approximate a normal distribution. 

* Population of size $N$
* Collect $m$ samples of size $n$ from the population
* Calculate the mean of each of the samples
* Plot the means on a histogram
* The histogram will approximate a normal distribution

> Note: _Independent Identically Distributed_ (IID or iid or i.i.d) and _Random Sample_ are synonomous

Given:  
Population  
$N$ = Population size  
$x_1, x_2, x_3, \cdots ,x_N$ = Population variables   
$\mu$ = Population mean or True mean  
$\sigma^2$ = Population variance  
$\sigma$ = Population standard deviation


Sample  
$m$ = Number of samples  
$n$ = Sample size  
$X_1, X_2, X_3, \cdots ,X_n$ = Sample observations (Random variables)  
$\bar{X}_n$ = Sample mean  
$\hat{\sigma}^2$ = Sample variance  
$\hat{\sigma}$ = Sample standard deviation

CLT states that as $n \to \infty$, random variable $\bar{X}_n \sim \mathcal{N}(\mu, \frac{\sigma^2}{n})$

CLT states that as $n$ tends to infinity, the random variable of _sample means_ "follow" or "is distributed as" a Normal Distribution with a mean $\mu$ and variance $\frac{\sigma^2}{n}$.

Expected Value (Mean) of the _sample means_  
$E(\bar{X}_n) = \mu$

Variance of the _sample means_  
$Var(\bar{X}_n) = \frac{\sigma^2}{n}$

Standard Deviation of the _sample means_  
$\hat{\sigma} = \frac{\sigma}{\sqrt{n}}$



