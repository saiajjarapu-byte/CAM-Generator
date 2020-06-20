from SCCA import SCCA_data
from POLY import final_poly_data
from DWELL import final_dwell_data
import matplotlib.pyplot as plt

# LIST OF FUNCTIONS

# SCCA: WHEN INSTANTIATING THE CLASS, SCCA_data, YOU HAVE TO GIVE IT A CHOICE PARAMETER TO CHOOSE BETWEEN THE 5 SCCA CURVES TYPES
#       CALL final_array:: PARAMETERS: start_beta, end_beta, h
# POLY: WHEN INSTANTIATING THE CLASS,POLY_data,  PARAMETERS: start_beta, end_beta, h;
#       THEN CALL EITHER poly_345 FOR 345 POLY CURVE OR poly_4567 FOR 4567 POLY CURVE;
#       PARAMETERS: start_beta, end_beta, h
# DWELL: INSTANTIATE final_dwell_array:: PARAMETERS: choice, start_beta, end_beta, h

# CLASS INSTANCES
class1 = final_poly_data("poly_345", 0, 45, 2)
class2 = final_dwell_data("rise_dwell", 2, 45, 120)
class3 = final_poly_data("poly_345", 120, 270, 0)
class4 = final_dwell_data("fall_dwell", 0, 270, 360)

theta1, s1, v1, a1, j1 = class1.func_choice()
print(s1)
# plt.plot(theta1, s1)
# plt.show()



