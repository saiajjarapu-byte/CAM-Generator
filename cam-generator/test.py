from numpy import *
from math import isclose
import pandas as pd

# # arr1 = open()
# arr1 = pd.read_csv(
#     r"C:\Users\Sai\Documents\College Classes\Senior Year\CAM Generator program\CAM-Generator\cam-generator\array.csv")
# arr2 = pd.read_csv(
#     r"C:\Users\Sai\Documents\College Classes\Senior Year\CAM Generator program\CAM-Generator\cam-generator\arr2.csv")
#
# array1 = ndarray.flatten(pd.DataFrame.to_numpy(arr1))
#
# array2 = ndarray.flatten(pd.DataFrame.to_numpy(arr2))
#
# # print(f'{arr1}')
# # print(f'shape of array1 {shape(array1)}, shape of array2 {shape(array2)} ')
# print(type(array1))
# isclose(array1, array2, rel_tol=0.000005)

dictionary = {1: 'accel'}


def choose(choice):
    if choice is 'accel':
        print('it worked')


choose(dictionary[1])
