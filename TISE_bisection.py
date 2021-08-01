## Solving time-independent schrödinger equation
## - (h_bar / (2m))^2 * phi'' + V(x) * phi = E * phi
## uses shooting method to find the eigenvalue

import time
from threading import Thread, ThreadError
from Numerov_algorithm import Numerov_algorithm

def bisection(lower_bound, upper_bound, mid_value, E_lower, E_upper, E_mid):
    if mid_value * lower_bound <= 0:
        new_upper_bound = E_mid
        return E_lower, new_upper_bound
    elif mid_value * upper_bound <= 0:
        new_lower_bound = E_mid
        return new_lower_bound, E_upper


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
    start_time = time.time()
    eigen_value_lower = 2
    eigen_value_upper = 4
    eigen_value_middle = float(eigen_value_lower + eigen_value_upper) / 2.0
    try_again = True
    

    while try_again:
        tise_lower = TISE(0, 0, 1, 0.0001, 1, eigen_value=eigen_value_lower, threshold=1e-3)
        tise_upper = TISE(0, 0, 1, 0.0001, 1, eigen_value=eigen_value_upper, threshold=1e-3)
        tise_middle = TISE(0, 0, 1, 0.0001, 1, eigen_value=eigen_value_middle, threshold=1e-3)

        t1 = Thread(target=tise_lower.solve_equation)
        t2 = Thread(target=tise_upper.solve_equation)
        t3 = Thread(target=tise_middle.solve_equation)
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()

        eigen_value_lower, eigen_value_upper = bisection(tise_lower.y_current, tise_upper.y_current, tise_middle.y_current, eigen_value_lower, eigen_value_upper, eigen_value_middle)
        eigen_value_middle = (eigen_value_lower + eigen_value_upper) / 2

        try_again = tise_middle.check_BC()

    end_time = time.time()
    ## checking
    print(f'wave function value at BC = {tise_middle.y_current}\neigenvalue = {eigen_value_middle}')
    print(f'time used: {end_time - start_time}s')