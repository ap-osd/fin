## Price change over time without volatility

![bsm-S100-K100-V1](bsm-S100-K100-V1.png)

Given:  
A: _current_ owner of the asset, and _holds the asset_ until option expiry.  
B: _future_ owner of the asset, and _holds the bond_ required to buy the asset at option expiry.

Call
* B has the long call, which means B wants to buy the asset at expiry, so B has to pay for the rights.
* If A sold the asset today in exchange for the bond, then A would get the bond returns.
* Since A holds the asset until option expiry, and B earns the bond returns, A has to be paid for the "lost" bond returns. B pays A, and makes a notional "loss" of the bond returns.

Put
* A has the long put, which means A wants to sell the asset at expiry, so A has to pay for the rights.
* As B already holds the bond until expiry, B would get the bond returns.
* Since A holds the asset until option expiry, and B earns the bond returns, B does not have to be paid. A "pays" B with a notional "loss" of the bond returns by not having the bond.

## Price change over time with volatility

| Call = OTM, Put = ITM | Call = ATM, Put = ATM | Call = ITM, Put = OTM |
|:---:|:---:|:---:|
| ![bsm-S80-K100-V50](bsm-S80-K100-V50.png) | ![bsm-S100-K100-V20](bsm-S100-K100-V50.png) | ![bsm-S100-K100-V20](bsm-S120-K100-V50.png) |

## Price sensitivity to volatility

![bsm-S100-K100-r5-t1](bsm-S100-K100-r5-t1.png)

## Price change over time with $S$, $K$, $r$, $\sigma$ changes

| $S_{var}$ |  $K_{var}$ |
|:---:|:---:|
| ![bsm-Svar-K100-r5-V50](bsm-Svar-K100-r5-V50.png) | ![bsm-S100-Kvar-r5-V50](bsm-S100-Kvar-r5-V50.png) |

| $r_{var}$ | $\sigma_{var}$ |
|:---:|:---:|
| ![bsm-S100-K100-rvar-V50](bsm-S100-K100-rvar-V50.png) | ![bsm-S100-K100-r5-Vvar](bsm-S100-K100-r5-Vvar.png) |

## OTM Puts

![bsm-p-Svar-K100-r4-V50](bsm-p-Svar-K100-r4-V50.png)

