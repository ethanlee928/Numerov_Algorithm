# TISE Hydrogen
# R'' - (l * (l + 1) / r - 2 - E * r) * R = 0

from TISE_bisection import TISE
import time
from threading import Thread

mass_of_electron = 9.10938356e-31   # in KG

class TISE_hydrogen(TISE):
    def __init__(self, x_old, y_old, y_prime_init, step_size, x_stop, mass=mass_of_electron, eigen_value=5.447e-19, threshold=1e-4, l=1):
        super().__init__(x_old, y_old, y_prime_init, step_size, x_stop, mass=mass, eigen_value=eigen_value, threshold=threshold)
        self.l = l
        self.h_bar = 1.05457e-34    # in SI

    def K(self, x):
        l = self.l
        E = self.eigen_value
        if x == 0:
            return 0
        else:
            k = -(l * (l + 1) / x - 2 - E * x)
            return k
        
    def solve_equation(self):
        self.initialize_3_diff()
        with open("TISE_hydrogen_result.txt", "w") as f:
            f.write(f'r\tR\n')
            f.write(f'{self.x_old}\t{self.y_old}\n')
            f.write(f'{self.x_current}\t{self.y_current / self.x_current}\n')
            while self.x_new <= self.x_stop:
                self.three_diff_formula()
                f.write(f'{self.x_current}\t{self.y_current / self.x_current}\n')

if __name__ == "__main__":
    hydrogen = TISE_hydrogen(0, 0, 1e-10, 1e-14, 5e-11)
    hydrogen.solve_equation()