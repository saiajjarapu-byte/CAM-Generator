from numpy import *
import pandas as pd


def poly_345(start_beta, end_beta, h):
    beta = end_beta - start_beta
    print(beta)
    theta = linspace(0, beta, num=100)
    S = h * (((10 * theta) ** 3) / (beta ** 3)) - \
        (((15 * theta) ** 4) / (beta ** 4)) + \
        (((6 * theta) ** 5) / (beta ** 5))
    V = h * (((30 * theta) ** 2) / (beta ** 3)) - \
        (((60 * theta) ** 3) / (beta ** 4)) + \
        (((30 * theta) ** 4) / (beta ** 5))
    A = h * (((60 * theta) ** 1) / (beta ** 3)) - \
        (((180 * theta) ** 2) / (beta ** 4)) + \
        (((120 * theta) ** 3) / (beta ** 5))
    J = h * ((60 / beta ** 3) - ((360 * theta) / (beta ** 4)) +
             ((360 * (theta ** 2)) / (beta ** 5)))

    return theta, S, V, A, J


t, s, v, a, j = poly_345(0, 45, 2)
print(s)
#
# df = pd.DataFrame(t).T
# df.to_excel(
#     excel_writer=r"C:\Users\Sai\Documents\College Classes\Senior Year\CAM Generator program\CAM-Generator\cam-generator\pythonvsmatlab.xlsx")
