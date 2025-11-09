import matplotlib.pyplot as plt
import numpy as np

def compute_tv():
    cf = 1                         # cash flow
    g  = 0.00                      # growth rate in decimal
    r1 = 0.05                      # 5%  discount rate in decimal
    r2 = 0.10                      # 10% discount rate in decimal
    n  = 100                       # number of years

    dct1 = cf; dct2 = cf           # discounted cash at 't' years
    tvt1 = 0; tvt2 = 0             # terminal value at 't' years
    xt = []                        # x value of years
    ydct1 = []; ydct2 = []         # y value of dct
    ytvt1 = []; ytvt2 = []         # y value of tvt

    for t in range(1, n):
        xt.append(t)
        dct1 = dct1 * (1+g)/(1+r1)
        tvt1 += dct1
        ydct1.append(round(dct1,10))
        ytvt1.append(tvt1)
        dct2 = dct2 * (1+g)/(1+r2)
        tvt2 += dct2
        ydct2.append(round(dct2,10))
        ytvt2.append(tvt2)

    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.set_figheight(10)
    fig.set_figwidth(20)

    ax1.set(xlabel='', ylabel='Aggregate', title='Terminal Value')
    ax1.grid()
    ax1.set_xticks([t for t in range(0, n+1, 5)])
    ax1.set_yticks([t for t in range(0, 20+1, 2)])
    ax1.set_xlim(0, n)
    ax1.plot(xt, ytvt1, label="5%")
    ax1.plot(xt, ytvt2, label="10%")
    ax1.legend()

    width = 0.4
    ax2.set(xlabel='Years', ylabel='Contribution', title='')
    ax2.grid()
    ax2.set_xlim(0, n)
    ax2.bar(np.array(xt)-width/2, ydct1, width, label="5%", alpha=0.9)
    ax2.bar(np.array(xt)+width/2, ydct2, width, label="10%", alpha=0.9)
    ax2.legend()

    # fig.savefig("tv.png")
    plt.show()