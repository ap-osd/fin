import matplotlib.pyplot as plt
from datetime import date

def compute_npv():
    xg = []
    ydctg = []   # y discounted cash at 't' years during growth
    ypvtg = []   # y present value at 't' years during growth
    xt = []
    ydctt = []   # y discounted cash at 't' years during terminal
    ypvtt = []   # y present value at 't' years during terminal

    cf = 1
    r = 0.05
    g = 0.10

    n = 100
    ng = 20         # ng years of growth
    nt = n-ng       # nt years of terminal

    dct = cf        # discounted cash at 't' years, initial value at t=0
    pvt = cf        # present value at 't' years, initial value at t=0

    # Initial phase
    xg.append(0)
    ydctg.append(dct)
    ypvtg.append(pvt)

    # Growth phase
    for t in range(1, ng+1):
        dct = dct * (1+g)/(1+r)
        pvt += dct
        xg.append(t)
        ydctg.append(round(dct,2))
        ypvtg.append(round(pvt,10))
    fcf = sum(ydctg)

    # Terminal phase
    xt.append(xg[-1])
    ypvtt.append(ypvtg[-1])
    gt = 0
    for t in range(1, nt+1):
        dct = dct * (1+gt)/(1+r)
        pvt += dct
        xt.append(ng+t)
        ydctt.append(round(dct,2))
        ypvtt.append(round(pvt,10))
    tv = sum(ydctt)

    tvinf = round(dct*1/r, 2)

    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.set_figheight(10)
    fig.set_figwidth(10)

    ax1.set(xlabel='', ylabel='Aggregate', title='Net Present Value | ' + r'$r=$' + str(r) + ", " + r'$g=$' + str(g) + ", " + r'$g_t=$' + str(gt))
    ax1.grid()
    ax1.plot(xg, ypvtg, label='Growth')
    ax1.plot(xt, ypvtt, label='Terminal')
    ax1.set_xlim(0, n)
    ax1.set_ylim(bottom=0)
    ax1.legend()

    ax2.set(xlabel='Years', ylabel='Contribution', title='Discounted Cash Flow')
    ax2.grid()
    ax2.set_xlim(0, n)
    ax2.bar(xg, ydctg, alpha=0.8, label='Growth')
    ax2.bar(xt[1:], ydctt, alpha=0.8, label='Terminal')
    ax2.legend()

    fig.savefig("npv.png")
    plt.show()


def main():
    compute_npv()

if __name__ == "__main__":
    main()
