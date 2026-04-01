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

print(np.min(array)) # To print the minimum value from the array
print(np.max(array)) # To print the maximum value from the array

print(np.argmin(array)) # To print the index of min value in array
print(np.argmax(array)) # To print the index of max value in array

print(np.sum(array, axis=0)) # To print the sum of all columns individually 
print(np.sum(array, axis=1)) # To print the sum of all rows individually

# Filtering: Refers to the process of selecting elements from an array that match a given condition
ages = np.array([[21,17,19,20,16,30,18,65],
                 [39,22,15,99,18,19,20,71]])

teenagers = ages[ages < 18]
print("ages of teenagers is:",teenagers)

senior_citizens = ages[ages > 60]
print("age of senior citizens are:",senior_citizens)

print(ages) # Original array will not change 

adults = ages[(ages >= 18) & (ages < 60)] # Instead of using and use & (i.e. Logical and)
print("ages of adults are:",adults)

adults = ages[(ages < 18) | (ages >= 60)] # Instead of using and use & (i.e. Logical and)
print("ages of adults are:",adults)

evens = ages[ages % 2 == 0]
print(evens)

evens = ages[ages % 2 != 0]
print(evens)


# Boolean Indexing will flatten the data while creating the new array's so,
# to preserve the original shape use 'where'
print("The original shape of the array remains preserved") 
adults = np.where(ages > 18, ages, 0)  # Can't add descriptive strings, as it’s meant for array operations
print(adults)  

# To generate the random numbers:  like used for simulations, modelling, applying random transformations and testing purposes
# Use Random number generator: rng: gives access to libraries random 
rng = np.random.default_rng()
print("random number generated is:",rng.integers(1,7)) # can pass a range and last is excluded 

# For readability, can use as:
print("random number generated:",rng.integers(low=10, high= 70)) # Here, 70 is exclusive

# size is used  to specify the dimensions or the no of integers/numbers to be generated as:
print("6 random number generated using size:",rng.integers(low=10, high= 70, size = 6)) # Here, 70 is exclusive
print("random number generated specifying dimensions:\n",rng.integers(low=10, high= 70, size = (3,4)))

# If want to reproduce/generate the same results again, use: seed
rng = np.random.default_rng(seed=1)

# Different seed → different sequence
rng1 = np.random.default_rng(seed=1)
rng2 = np.random.default_rng(seed=1)

print(rng1.integers(0, 10, 3))
print(rng2.integers(0, 10, 3))
