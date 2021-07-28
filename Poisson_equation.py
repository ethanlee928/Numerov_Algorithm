## To solve poisson equation in the form:
## phi'' = -4 * pi * r * rho

import math
from Numerov_algorithm import Numerov_algorithm

class Poisson(Numerov_algorithm):
    
    def S(self, x):
        s = -0.5 * x * math.exp(-x)
        return s

    def K(self, x):
        return 0
    
    def solve_equation(self):
        return super().solve_equation()
    
    def analytic(self):
        self.x_current = self.x_old
        with open("analytics.txt", "w") as f:
            f.write(f'x\ty\n')
            while self.x_current < self.x_stop:
                self.y_current = 1 - 0.5 * (self.x_current + 2) * math.exp(-self.x_current)
                f.write(f'{self.x_current}\t{self.y_current}\n')
                self.x_old = self.x_current
                self.x_current += self.step_size

if __name__ == "__main__":
    poisson1 = Poisson(0.0, 0.0, 0.5, 0.05, 10.0)
    poisson2 = Poisson(0.0, 0.0, 0.5, 0.05, 10.0)
    poisson1.solve_equation()
    poisson2.analytic()