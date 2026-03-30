# to print the version of Numpy
# Numpy: Fast numerical computation using arrays instead of lists   
import numpy as np
print(np.__version__)  #2.4.1

my_list = [1,2,3,4,5]
my_list = my_list * 2
print(my_list) # Instead of multiplying no's with 2, will multiply items 2 times


# instead use a numpy array
array = np.array([1,2,3,4])
print("numpy array is", array, "type is:",type(array))
array = array *2
print("numpy array is", array, "type is:",type(array))
print(array.ndim)

two_D_array = np.array([[1,2,3,4]])
print(two_D_array.ndim)

two_D_array = np.array([[1,2,3,4]])
print(two_D_array.ndim)

three_D_array = np.array([[[1,2,3],[1,2,3],[1,2,3]],
[[1,2,3],[1,2,3],[1,2,3]],
[[1,2,3],[1,2,3],[1,2,3]]])
# print(three_D_array.ndim)
print("shape is:", three_D_array.shape)
