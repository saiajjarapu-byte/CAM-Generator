from numpy import *


class rise:
    accel = {'b': 0, 'c': 1, 'd': 0, 'Ca': 4}
    mod_trap = {'b': 0.25, 'c': 0.50, 'd': 0.25, 'Ca': 4.8881}
    mod_sine = {'b': 0.25, 'c': 0, 'd': 0.75, 'Ca': 5.5280}
    harm_disp = {'b': 0, 'c': 0, 'd': 1, 'Ca': 4.9348}
    cyc_disp = {'b': 0.50, 'c': 0, 'd': 0.50, 'Ca': 6.2832}

    def __init__(self, choice):
        self.choice = choice
        self.b = None
        self.c = None
        self.d = None
        self.Ca = None
        self.x1 = Nonego
        self.x2 = None
        self.x3 = None
        self.x4 = None
        self.x5 = None

    def constants(self):
        constants = {'accel': self.accel,
                     'mod_trap': self.mod_trap,
                     'mod_sine': self.mod_sine,
                     'harm_disp': self.harm_disp,
                     'cyc_disp': self.cyc_disp}

        if self.choice is 'accel':
            self.b = constants['accel']['b']
            self.c = constants['accel']['c']
            self.d = constants['accel']['d']
            self.Ca = constants['accel']['Ca']
            # print(f'CONSTANT ACCELERATION, b = {b}, c = {c}, d = {d}, Ca = {Ca}')
        elif self.choice is 'mod_trap':
            self.b = constants['mod_trap']['b']
            self.c = constants['mod_trap']['c']
            self.d = constants['mod_trap']['d']
            self.Ca = constants['mod_trap']['Ca']
            # print(f'MODEFIED TRAP, b = {b}, c = {c}, d = {d}, Ca = {Ca}')
        elif self.choice is 'mod_sine':
            self.b = constants['mod_sine']['b']
            self.c = constants['mod_sine']['c']
            self.d = constants['mod_sine']['d']
            self.Ca = constants['mod_sine']['Ca']
            # print(f'MODEFIED SINE, b = {b}, c = {c}, d = {d}, Ca = {Ca}')
        elif self.choice is 'harm_disp':
            self.b = constants['harm_disp']['b']
            self.c = constants['harm_disp']['c']
            self.d = constants['harm_disp']['d']
            self.Ca = constants['harm_disp']['Ca']
            # print(f'HARMONIC DISP, b = {b}, c = {c}, d = {d}, Ca = {Ca}')
        elif self.choice is 'cyc_disp':
            self.b = constants['cyc_disp']['b']
            self.c = constants['cyc_disp']['c']
            self.d = constants['cyc_disp']['d']
            self.Ca = constants['cyc_disp']['Ca']
            # print(f'CYCLODIAL DISP, b = {b}, c = {c}, d = {d}, Ca = {Ca}')

        print(f'{self.choice}, b = {self.b}, c = {self.c}, d = {self.d}, Ca = {self.Ca}')
        return self.b, self.c, self.d, self.Ca

    def eval(self):
        self.x1 = linspace(0, (self.b / 2))
        self.x2 = linspace((self.b / 2), (1 - self.d) / 2)
        self.x3 = linspace((1 - self.d) / 2, ((1 + self.d) / 2))
        self.x4 = linspace((1 + self.d) / 2, 1 - (self.b / 2))
        self.x5 = linspace(1 - (self.b / 2), 1)





