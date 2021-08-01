## Solving time-independent schrödinger equation
## - (h_bar / (2m))^2 * phi'' + V(x) * phi = E * phi
## uses shooting method to find the eigenvalue

import math
import time
from Numerov_algorithm import Numerov_algorithm

class TISE(Numerov_algorithm):

    def __init__(self, x_old, y_old, y_prime_init, step_size, x_stop, mass=1, eigen_value=0.7, threshold=1e-4):
        super().__init__(x_old, y_old, y_prime_init, step_size, x_stop)
        self.mass = mass
        self.h_bar = 1.0
        self.eigen_value = eigen_value
        self.threshold = threshold

        self.x_old_init = x_old
        self.y_old_init = y_old
        

    def V(self, x):
        return 0

    def K(self, x):
        h_bar_square = self.h_bar * self.h_bar
        m = self.mass
        E = self.eigen_value
        k = (2 * m) * (E - self.V(x)) / h_bar_square
        # print(k, self.eigen_value)
        return k 
    
    def check_BC(self):
        if abs(self.y_current - 0) > self.threshold:
            return True
        else:
            return False


if __name__ == "__main__":
    
    eigen_value = 5
    try_again_step_size = 0.005
    try_again = True
    
    while try_again:
        eigen_value += try_again_step_size
        tise = TISE(0, 0, 1, 0.001, 1, eigen_value=eigen_value, threshold=1e-3)  
        tise.solve_equation()
        try_again = tise.check_BC()
        # print(tise.y_current, eigen_value)
    ## checking
    print(f'wave function value at BC = {tise.y_current}\neigenvalue = {eigen_value}')
    