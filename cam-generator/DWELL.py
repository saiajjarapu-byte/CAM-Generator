from numpy import *


class dwell_data:
    """
    Class to calculate the theta, S, V, A, J for the dwell
    """

    def __init__(self, start_beta, end_beta, h):
        self.h = h
        self.start_beta = start_beta
        self.end_beta = end_beta
        self.theta = None
        self.S = None
        self.V = None
        self.A = None
        self.J = None

    def rise_dwell(self):
        # print("Rise dwell function called in child class")
        self.theta = linspace(self.start_beta, self.end_beta, num=100)
        self.S = self.h * ones((1, len(self.theta)))
        self.V, self.A, self.J = zeros((1, len(self.theta))), zeros((1, len(self.theta))), zeros((1, len(self.theta)))

    def fall_dwell(self):
        # print("Fall dwell function called in child class")
        self.theta = linspace(self.start_beta, self.end_beta, num=100)
        self.S, self.V, self.A, self.J = zeros((1, len(self.theta))), zeros((1, len(self.theta))), zeros(
            (1, len(self.theta))), zeros((1, len(self.theta)))


class final_dwell_data(dwell_data):
    """
    Class to select the dwell method based on the user input
    Child Class to dwell_data Parent Class
    """

    def __init__(self, choice, start_beta, end_beta, h):
        super().__init__(start_beta, end_beta, h)
        self.choice = choice
        self.selection = None

    def func_choice(self):
        """
        Based on the user input choice parameter,
        the method executes the methods from the dwell_data class
        :return: theta, S, V, A, J
        """
        self.selection = {"rise_dwell": self.rise_dwell,
                          "fall_dwell": self.fall_dwell}
        self.selection[self.choice]()

        return self.theta, self.S.flatten(), self.V.flatten(), self.A.flatten(), self.J.flatten()


c1 = final_dwell_data("rise_dwell", 0, 45, 2)
theta, S, V, A, J = c1.func_choice()
print(
    f'Shape of theta:: {shape(theta)}\nShape of S:: {shape(S)}\n'
    f'Shape of V:: {shape(V)}\nShape of A:: {shape(A)}\nShape of J:: {shape(J)}')
