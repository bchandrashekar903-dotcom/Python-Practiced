# ------------------------ARRAYS------------------------#
# Built in Array 
# import array 
# ar = array.array('i',[1,2,3,4,5])
# print(ar)
# print(type(ar))

# import array as arr
# a = arr.array('f',[1,4,6,3,7])
# print(a)

# from array import *
# a = array('u',['h','e','l','l','o'])
# print(a)

# Numpy Array is faster than built in array because it is implemented in C 

# import numpy as np
# ar = np.array([[1,2,3,4,5],[34,45,567,7,876]])
# print(ar)


# ---------------------...2D->ARRAYS...---------------------#
# from numpy import *
# arr = array([[1,32,12,324,23,45],[12,32,43,54,65,76]])
# print(arr)
# print(arr.ndim)
# print(arr.size)
# print(arr.shape)

# from pandas import *
# arr = array([213,23,32])
# print(arr)

# import numpy as np
# print(np.zeros((3,4),int)) 
# print(np.ones((3,4),int)) 
# print(np.eye(3),int)


# --------------Operations on numpy array----------------#
# import numpy as np
# arr = np.array([1,2,3,4,27,4,3])
# # print(np.sort(arr))
# print(sorted(arr))
# print(np.min(arr))
# print(arr.max())
# # print(np.max(arr))
# print(arr.sum())  

import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0:,2:])
print(arr[2:,1:])
# print(arr[1:,1:])
print(arr[0:2,0:2])
print(arr[1:3,1:3])