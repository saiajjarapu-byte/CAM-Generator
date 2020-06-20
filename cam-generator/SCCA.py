from numpy import *


class SCCA_data:
    """
        Class to calculate the theta, S, V, A, J for the SCCA curves
    """
    # CONSTANTS FOR EACH CURVE
    accel = {"b": 0, "c": 1, "d": 0, "Ca": 4}
    mod_trap = {"b": 0.25, "c": 0.50, "d": 0.25, "Ca": 4.8881}
    mod_sine = {"b": 0.25, "c": 0, "d": 0.75, "Ca": 5.5280}
    harm_disp = {"b": 0, "c": 0, "d": 1, "Ca": 4.9348}
    cyc_disp = {"b": 0.50, "c": 0, "d": 0.50, "Ca": 6.2832}

    def __init__(self, choice):
        self.choice = choice
        self.b = None
        self.c = None
        self.d = None
        self.Ca = None
        self.constants = None
        self.t = None
        self.x1 = None
        self.x2 = None
        self.x3 = None
        self.x4 = None
        self.x5 = None
        self.s1 = None
        self.s2 = None
        self.s3 = None
        self.s4 = None
        self.s5 = None
        self.s = None
        self.v1 = None
        self.v2 = None
        self.v3 = None
        self.v4 = None
        self.v5 = None
        self.v = None
        self.a1 = None
        self.a2 = None
        self.a3 = None
        self.a4 = None
        self.a5 = None
        self.a = None
        self.j1 = None
        self.j2 = None
        self.j3 = None
        self.j4 = None
        self.j5 = None
        self.j = None

    def constants(self):
        """
        FUNCTION TO SELECT THE b, c, d, Ca CONSTANTS BASED ON THE USER SELECTION
        :return:
        """
        self.constants = {"accel": self.accel,
                          "mod_trap": self.mod_trap,
                          "mod_sine": self.mod_sine,
                          "harm_disp": self.harm_disp,
                          "cyc_disp": self.cyc_disp}

        if self.choice is "accel":
            self.b = self.constants["accel"]["b"]
            self.c = self.constants["accel"]["c"]
            self.d = self.constants["accel"]["d"]
            self.Ca = self.constants["accel"]["Ca"]
            # print(f'CONSTANT ACCELERATION, b = {b}, c = {c}, d = {d}, Ca = {Ca}')
        elif self.choice is 'mod_trap':
            self.b = self.constants['mod_trap']["b"]
            self.c = self.constants["mod_trap"]["c"]
            self.d = self.constants["mod_trap"]["d"]
            self.Ca = self.constants["mod_trap"]["Ca"]
            # print(f'MODEFIED TRAP, b = {b}, c = {c}, d = {d}, Ca = {Ca}')
        elif self.choice is 'mod_sine':
            self.b = self.constants["mod_sine"]["b"]
            self.c = self.constants["mod_sine"]["c"]
            self.d = self.constants["mod_sine"]["d"]
            self.Ca = self.constants["mod_sine"]["Ca"]
            # print(f'MODEFIED SINE, b = {b}, c = {c}, d = {d}, Ca = {Ca}')
        elif self.choice is 'harm_disp':
            self.b = self.constants["harm_disp"]["b"]
            self.c = self.constants["harm_disp"]["c"]
            self.d = self.constants["harm_disp"]["d"]
            self.Ca = self.constants["harm_disp"]["Ca"]
            # print(f'HARMONIC DISP, b = {b}, c = {c}, d = {d}, Ca = {Ca}')
        elif self.choice is 'cyc_disp':
            self.b = self.constants["cyc_disp"]["b"]
            self.c = self.constants["cyc_disp"]["c"]
            self.d = self.constants["cyc_disp"]["d"]
            self.Ca = self.constants["cyc_disp"]["Ca"]
            # print(f'CYCLODIAL DISP, b = {b}, c = {c}, d = {d}, Ca = {Ca}')

    def theta(self):
        """
        FUNCTION TO CALCULATE THE NON-DIMENSIONALIZED ANGLE FOR EACH ZONE OF THE SCCA CURVE
        :return:
        """
        SCCA_data.constants(self)
        # print(f'{type(self.choice)}, b = {self.b}, c = {self.c}, d = {self.d}, Ca = {self.Ca}')
        self.x1 = linspace(0, (self.b / 2), num=100)
        self.x2 = linspace((self.b / 2), ((1 - self.d) / 2), num=100)
        self.x3 = linspace((1 - self.d) / 2, ((1 + self.d) / 2), num=100)
        self.x4 = linspace((1 + self.d) / 2, 1 - (self.b / 2), num=100)
        self.x5 = linspace(1 - (self.b / 2), 1, num=100)

    def displacement(self):
        """
        FUNCTION TO CALCULATE THE NON-DIMENSIONALIZED DISPLACEMENT FOR EACH ZONE OF THE SCCA CURVE
        :return:
        """
        SCCA_data.theta(self)
        try:
            self.s1 = ((self.b / pi) * self.x1) - (((self.b / pi) ** 2) * sin((pi / self.b) * self.x1))
        except ZeroDivisionError:
            self.s1 = NaN

        self.s2 = ((self.x2 ** 2) / 2) + \
                  (self.b * ((1 / pi) - 0.5) * self.x2) + \
                  ((self.b ** 2) * (0.125 - (1 / (pi ** 2))))

        try:
            self.s3 = (((self.b / pi) + (self.c / 2)) * self.x3) + \
                      ((self.d / pi) ** 2) + \
                      ((self.b ** 2) * (0.125 - ((1 / pi) ** 2))) - \
                      (((1 - self.d) ** 2) / 8) - \
                      (((self.d / pi) ** 2) * cos((pi / self.d) * (self.x3 - ((1 - self.d) / 2))))
        except ZeroDivisionError:
            self.s3 = NaN

        self.s4 = ((-self.x4 ** 2) / 2) + \
                  (((self.b / pi) + 1 - (self.b / 2)) * self.x4) + \
                  (((2 * (self.d ** 2)) - (2 * (self.b ** 2))) * (((1 / (pi ** 2)) - 0.125) - 0.25))

        try:
            self.s5 = ((self.b / pi) * self.x5) + \
                      ((2 * ((2 * (self.d ** 2)) - (2 * (self.b ** 2)))) / (pi ** 2)) + \
                      ((((1 - self.b) ** 2) - (self.d ** 2)) / 4) - \
                      (((self.b / pi) ** 2) * sin((pi / self.b) * (self.x5 - 1)))
        except ZeroDivisionError:
            self.s5 = NaN

    def velocity(self):
        """
        FUNCTION TO CALCULATE THE NON-DIMENSIONALIZED VELOCITY FOR EACH ZONE OF THE SCCA CURVE
        :return:
        """
        SCCA_data.theta(self)
        try:
            self.v1 = (self.b / pi) - ((self.b / pi) * cos((pi / self.b) * self.x1))
        except ZeroDivisionError:
            self.v1 = NaN

        self.v2 = self.x2 + (self.b * ((1 / pi) - 0.5))

        try:
            self.v3 = (self.b / pi) + (self.c / 2) + (
                    (self.d / pi) * sin((pi / self.d) * (self.x3 - ((1 - self.d) / 2))))
        except ZeroDivisionError:
            self.v3 = NaN

        self.v4 = -self.x4 + (self.b / pi) + 1 - (self.b / 2)

        try:
            self.v5 = (self.b / pi) - ((self.b / pi) * cos((pi / self.b) * (self.x5 - 1)))
        except ZeroDivisionError:
            self.v5 = NaN

    def acceleration(self):
        """
        FUNCTION TO CALCULATE THE NON-DIMENSIONALIZED ACCELERATION FOR EACH ZONE OF THE SCCA CURVE
        :return:
        """
        SCCA_data.theta(self)
        try:
            self.a1 = sin((pi / self.b) * self.x1)
        except ZeroDivisionError:
            self.a1 = NaN

        self.a2 = 1

        try:
            self.a3 = cos((pi / self.d) * (self.x3 - ((1 - self.d) / 2)))
        except ZeroDivisionError:
            self.a3 = NaN

        self.a4 = -1

        try:
            self.a5 = (pi / self.b) * cos((pi / self.b) * (self.x5 - 1))
        except ZeroDivisionError:
            self.a5 = NaN

    def jerk(self):
        """
        FUNCTION TO CALCULATE THE NON-DIMENSIONALIZED JERK FOR EACH ZONE OF THE SCCA CURVE
        :return:
        """
        SCCA_data.theta(self)
        try:
            self.j1 = (pi / self.b) * cos((pi / self.b) * self.x1)
        except ZeroDivisionError:
            self.j1 = NaN

        self.j2 = 0

        try:
            self.j3 = -((pi / self.d) * sin((pi / self.d) * (self.x3 - ((1 - self.d) / 2))))
        except ZeroDivisionError:
            self.j3 = NaN

        self.j4 = 0

        try:
            self.j5 = (pi / self.b) * cos((pi / self.b) * (self.x5 - 1))
        except ZeroDivisionError:
            self.j5 = NaN

    def final_array(self, start_beta, end_beta, h):
        """
        FUNCTION TO GATHER ALL THE CALCULATED VALUED FOR EACH ZONE AND SORT BASED ON USER CHOICE INPUT AND
        RETURN THE FINAL DATA ARRAY FOR ALL FIVE ZONES IN ONE ARRAY
        OPTIONS:
        "accel" FOR ACCELERATION CURVE
        "mod_sine" FOR MODIFIED SINE CURVE
        "mod_trap" FOR MODIFIED TRAPEZOID CURVE
        "harm_disp" FOR SIMPLE HARMONIC DISPLACEMENT CURVE
        "cyc_disp" FOR CYCLODIAL DISPLACEMENT CURVE

        :param start_beta:
        :param end_beta:
        :param h:
        :return: theta, s, v, a, j
        """
        beta = end_beta - start_beta
        SCCA_data.theta(self)
        SCCA_data.displacement(self)
        SCCA_data.velocity(self)
        SCCA_data.acceleration(self)
        SCCA_data.jerk(self)
        if self.choice is "accel":
            self.t = beta * concatenate((self.x2, self.x4))
            self.s = self.Ca * h * concatenate((self.s2, self.s4))
            self.v = self.Ca * h * concatenate((self.v2, self.v4))
            self.a = self.Ca * h * concatenate(((ones(100, ) * self.a2), (ones(100, ) * self.a4)))
            self.j = self.Ca * h * concatenate(((zeros(100, ) * self.j2), (zeros(100, ) * self.j4)))
        elif self.choice is "harm_disp":
            self.t = beta * concatenate((self.x2, self.x3, self.x4))
            self.s = self.Ca * h * concatenate((self.s2, self.s3, self.s4))
            self.v = self.Ca * h * concatenate((self.v2, self.v3, self.v4))
            self.a = self.Ca * h * concatenate(
                ((ones(100, ) * self.a2), (ones(100, ) * self.a3), (ones(100, ) * self.a4)))
            self.j = self.Ca * h * concatenate(
                ((zeros(100, ) * self.j2), (zeros(100, ) * self.j3), (zeros(100, ) * self.j4)))
        elif self.choice is "mod_trap" or self.choice is "mod_sine" or self.choice is "cyc_disp":
            self.t = beta * concatenate((self.x1, self.x2, self.x3, self.x4, self.x5))
            self.s = self.Ca * h * concatenate((self.s1, self.s2, self.s3, self.s4, self.s5))
            self.v = self.Ca * h * concatenate((self.v1, self.v2, self.v3, self.v4, self.v5))
            self.a = self.Ca * h * concatenate(
                (self.a1, (ones(100, ) * self.a2), self.a3, (ones(100, ) * self.a4), self.a5))
            self.j = self.Ca * h * concatenate(
                (self.j1, (zeros(100, ) * self.j2), self.j3, (zeros(100, ) * self.j2), self.j5))

        return self.t, self.s.flatten(), self.v.flatten(), self.a.flatten(), self.j.flatten()
