import matplotlib.pyplot as plt 
import numpy as np
from scipy.integrate import odeint

class solver:
    def __init__(self, model, x0, t, s, args, names):
        self.model = model
        self.x0 = x0
        self.tspan = np.arange(0, t, s)
        self.s = s
        self.args = args
        self.names = names

    def __euler__(self, x, t):
        return self.model(x, t, *self.args) *  self.s

    def __rk4__(self, x, t):
        k1 = self.model(x, t, *self.args)
        k2 = self.model(x + self.s/2 * k1, t + self.s/2, *self.args)
        k3 = self.model(x + self.s/2 * k2, t + self.s/2, *self.args)
        k4 = self.model(x + self.s * k3, t + self.s, *self.args)
        return (k1 + 2*k2 + 2*k3 + k4) / 6 * self.s

    def solve(self, method='odeint'):
        if method in ['euler', 'rk4']:
            x = np.array(self.x0, dtype=np.float64)
            solution = [x.copy()]
            for t in self.tspan[1:]:
                if method == 'euler':
                    dx = self.__euler__(x,t)
                elif method == 'rk4':
                    dx = self.__rk4__(x,t)
                x += dx
                solution.append(x.copy())
            solution = np.array(solution)
        else:
            solution = odeint(self.model, self.x0, self.tspan, args=self.args)

        self.solution = solution.transpose()
        return self.solution


    def show(self, size=(5,3), dpi=200):
        fig, ax = plt.subplots(1, 1, figsize=size, dpi=dpi)
        c = 0
        for i in self.solution:
            ax.plot(self.tspan, i, '-', label=self.names[c])
            c += 1
        ax.legend()
        plt.show()
