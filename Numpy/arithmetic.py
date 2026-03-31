# Scalar Arithmatic 
import numpy as np
array = np.array([1,2,3])
print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5 )

# Vectorised maths functions: can apply functions to entire array without using the loop 

sq_array = np.array([4,16,9])
print("sqrt is:", np.sqrt(sq_array)) # 2,4,3

round_array = np.array([1.23,4.98,67.55, 65.41]) #  1, 5, 68, 65
print("round off:",np.round(round_array))

round_array = np.array([1.01,2.5,3.99]) #  1,2,4
print("round off:", np.round(round_array))

# To round up, use: ceiling 
round_array = np.array([1.01,2.5,3.99]) #  1,2,4
print("ceil:", np.ceil(round_array))

# To round down, use floor 
round_array = np.array([1.01,2.5,3.99]) #  1,2,4
print("floor:", np.floor(round_array))
