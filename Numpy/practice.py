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

three_D_array = np.array([[['A','B','C'],[1,2,3],[1,2,3]],
                          [['D',2,3],['F',2,3],[1,'N',3]],
                          [[1,2,3],[1,2,3],[1,2,'T']]])
# print(three_D_array.ndim)
print("shape is:", three_D_array.shape) # 3,3,3: layers, rows and colums in each row

# To access elements in the array:, CALLED Chain indexing 
print(three_D_array[0][0][0]) # A
print(three_D_array[1][0][0]) # D
print(three_D_array[1][1][0]) # F

# Multidimensional Idexing 
print("using Multidimensional Idexing ",three_D_array[0,0,0]) # A

# Multidimensional Indexing is faster than Chain Indexing 

word = three_D_array[0,0,0] + three_D_array[1,2,1] + three_D_array[2,2,2]
print(word)




 
