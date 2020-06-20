from numpy import *
import matplotlib.pyplot as plt


class POLY_data:
    """
    Class to calculate the theta, S, V, A, J for the poly curves
    OPTIONS:
    "poly_365" for 3,4,5 Polynomial curve
    "poly_4567" for 4,5,6,7 Polynomial curve
    """

    def __init__(self, start_beta, end_beta, h):
        self.beta = end_beta - start_beta
        self.h = h
        self.theta = None
        self.S = None
        self.V = None
        self.A = None
        self.J = None

    def poly_345(self):
        self.theta = linspace(0, self.beta, num=100)

        self.S = self.h * (((10 * self.theta) ** 3) / (self.beta ** 3)) - \
                 (((15 * self.theta) ** 4) / (self.beta ** 4)) + \
                 (((6 * self.theta) ** 5) / (self.beta ** 5))

        self.V = self.h * (((30 * self.theta) ** 2) / (self.beta ** 3)) - \
                 (((60 * self.theta) ** 3) / (self.beta ** 4)) + \
                 (((30 * self.theta) ** 4) / (self.beta ** 5))

        self.A = self.h * (((60 * self.theta) ** 1) / (self.beta ** 3)) - \
                 (((180 * self.theta) ** 2) / (self.beta ** 4)) + \
                 (((120 * self.theta) ** 3) / (self.beta ** 5))

        self.J = self.h * ((60 / self.beta ** 3) - ((360 * self.theta) / (self.beta ** 4)) +
                           ((360 * (self.theta ** 2)) / (self.beta ** 5)))

    def poly_4567(self):
        self.theta = linspace(0, self.beta, num=100)

        self.S = self.h * (((35 * (self.theta ** 4)) / self.beta ** 4) - ((84 * (self.theta ** 5)) / self.beta ** 5) +
                           ((70 * (self.theta ** 6)) / self.beta ** 6) - ((20 * (self.theta ** 7)) / self.beta ** 7))

        self.V = self.h * (((140 * (self.theta ** 3)) / self.beta ** 4) - ((420 * (self.theta ** 4)) / self.beta ** 5) +
                           ((420 * (self.theta ** 5)) / self.beta ** 6) - ((20 * (self.theta ** 7)) / self.beta ** 7))

        self.A = self.h * (
                ((420 * (self.theta ** 2)) / self.beta ** 4) - ((1680 * (self.theta ** 3)) / self.beta ** 5) +
                ((2100 * (self.theta ** 4)) / self.beta ** 6) - ((840 * (self.theta ** 5)) / self.beta ** 7))

        self.A = self.h * (
                ((840 * (self.theta ** 1)) / self.beta ** 4) - ((5040 * (self.theta ** 2)) / self.beta ** 5) +
                ((8400 * (self.theta ** 3)) / self.beta ** 6) - ((4200 * (self.theta ** 4)) / self.beta ** 7))


class final_poly_data(POLY_data):
    """
        Class to select the poly curve method based on the user input
        Child Class to POLY_data Parent Class
    """

    def __init__(self, choice, start_beta, end_beta, h):
        super().__init__(start_beta, end_beta, h)
        self.choice = choice
        self.selection = None

    def func_choice(self):
        """
        Based on the user input choice parameter,
        the method executes the methods from the POLY_data class
        :return: theta, S, V, A, J
        """
        self.selection = {"poly_345": self.poly_345,
                          "poly_4567": self.poly_4567}
        self.selection[self.choice]()

        return self.theta, self.S, self.V, self.A, self.J


c1 = final_poly_data("poly_345", 0, 45, 2)
theta, S, V, A, J = c1.func_choice()
print(theta)
# print(f'Shape of theta:: {shape(theta)}\nShape of S:: {shape(S)}\nShape of V:: {shape(V)}\nShape of A:: {shape(A)}\nShape of J:: {shape(J)}')
