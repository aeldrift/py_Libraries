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
round_array = np.array([1.01,2.5,3.99]) #  2,3,4
print("ceil:", np.ceil(round_array))

# To round down, use floor 
round_array = np.array([1.01,2.5,3.99]) #  1,2,3
print("floor:", np.floor(round_array))

# To return the value of pi 
print("value of pi is:",np.pi)

# Combining the scalar and the vectorised functions together

radii = np.array([1,2,3])
print(np.pi * radii ** 2 )

# Element-wise Arithmetic 
''' Applying operations element by element between two arrays'''

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print('sum of arrays is:',array1 + array2) #sum of arrays is: [5 7 9]
print('difference of arrays is:',array1 - array2) # difference of arrays is: [-3 -3 -3]
print('Division of arrays is:',array1 / array2) # Division of arrays is: [0.25 0.4  0.5 ]
print('Exponent of arrays is:',array1 ** array2) # Division of arrays is: [0.25 0.4  0.5 ]

# Comparison Operators 
scores = np.array([56,79,100,20,89])
print(scores > 70)
print(scores == 100)

# Assume, let's assigning 0 credits to one 60having marks less than 60
scores[scores < 60] = 0
print("scores is:",scores)

# Broadcasting
''' Allows numpy to perform operations on arrays 
with different shapes by virtually expanding dimensions 
so they match the larger array's shape
The dimensions have same size or 
One of the dimensions have size of 1'''


array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
array2 = np.array([[11,12,13],[14,15,16],[17,18,19]])
print(array1.shape)
print(array2.shape)
print(array1 * array2) # possible when either dim matches or is 1

# Aggregate the functions 
# It summarises the data and typically return a single value 

array = np.array([[1,2,3],
                 [5,6,7]])

print(np.sum(array)) # 1+2+3+4+5+6+7 = 24
print(np.mean(array))
print(np.std(array)) # To print the standard deviation 
print(np.var(array)) # To print the variation
print(np.min(array))
print(np.max(array))

