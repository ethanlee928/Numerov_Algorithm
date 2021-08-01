## To solve linear second order differential equations in the form:
## y'' + k(x)y = S(x)
import math

class Numerov_algorithm:
    def __init__(self, x_old, y_old, y_prime_init, step_size, x_stop):
        self.x_old = x_old
        self.x_current = x_old + step_size
        self.x_new = x_old + step_size * 2
        self.y_old = y_old
        self.y_current = None
        self.y_new = None
        self.y_prime_init = y_prime_init
        self.step_size = step_size
        self.x_stop = x_stop

    def S(self, x):
        return 0
    
    def K(self, x):
        return 4 * math.pi

    def initialize_3_diff(self):
        # 2 point formula
        self.y_current = (self.y_prime_init * self.step_size) + self.y_old
    
    def three_diff_formula(self):
        h = self.step_size
        k_new = self.K(self.x_new)
        k_current = self.K(self.x_current)
        k_old = self.K(self.x_old)
        S_on_right = (h * h / 12) * (self.S(self.x_new) + 10 * self.S(self.x_current) + self.S(self.x_old))

        y_new_coef = 1 + (h * h * k_new * k_new) / 12
        y_current_coef = -2 * (1 - 5 * h * h * k_current * k_current / 12)
        y_old_coef = 1 + h * h * k_old * k_old / 12

        ## updating
        self.y_new = (S_on_right - y_current_coef * self.y_current - y_old_coef * self.y_old) / y_new_coef
        self.y_old = self.y_current
        self.y_current = self.y_new
        self.x_old = self.x_current
        self.x_current = self.x_new
        self.x_new += self.step_size

    def solve_equation(self):
        self.initialize_3_diff()
        with open("results.txt", "w") as f:
            f.write(f'x\tphi\n')
            f.write(f'{self.x_old}\t{self.y_old}\n')
            f.write(f'{self.x_current}\t{self.y_current}\n')        
            while self.x_new <= self.x_stop:
                self.three_diff_formula()
                # print(self.y_current)
                f.write(f'{self.x_current}\t{self.y_current}\n')


if __name__ == "__main__":
    function1 = Numerov_algorithm(0, 1, 0, 0.01, 6)
    function1.solve_equation()
        