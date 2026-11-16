# --------------------------Module-------------------------
'''Modules are pre-defines orelse user created python files which 
consists of set of statements and operations '''

# To use modules we have predefined functions

'''Print directory of math module''' 
# import math
# print(dir(math))

# import tensorflow
# print(dir(tensorflow))

# from math import ceil,factorial
# print(factorial(5))
# print(ceil(9.1))

# from math import *
# print(factorial(10))
# print(sqrt(81))
# print(ceil(10.1))
# print(floor(10))
# print(Date())

# '''Leap year'''
# n = int(input("Enter the year:"))
# if (n%4==0) and (n%100 != 0):
#     print("leap")
# elif (n%400==0):
#     print("Not leap")
# else:
#     print("Not a leap year")


import calendar
print(calendar.isleap(2023))