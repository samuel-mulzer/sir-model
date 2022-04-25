from math import exp

def solve(f0, f1, x_start):
    x_last = None
    x_current = x_start

    c = 0
    while x_last != x_current:
        x_last = x_current
        x_current = x_last - (f0(x_last) / f1(x_last))
        c += 1
        print(str(c) + ': ' + str(x_current))
    return x_current


R0 = 2.5
f0 = lambda x: x - exp(R0 * (x-1))
f1 = lambda x: 1 - R0 * exp(R0 * (x - 1))

solve(f0,f1,0.01)