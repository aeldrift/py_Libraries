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
 
word = three_D_array[0,0,0] + three_D_array[1,2,1] + three_D_array[2,2,2] # The words are concatinated using indexing
print(word)

# Slicing

array = np.array([[1,2,3,4], # idx: 0
                  [5,6,7,8], # idx: 1
                  [9,10,11,12], # idx: 2
                  [13,14,15,16]]) # idx: 3
# array(Start:End:Step)
print(array[0]) # 1,2,3,4
print(array[1]) # 5,6,7,8
print(array[2]) # 9,10,11,12

# Or can use the negative indexing as:
print("-ve indexed slicing:", array[-1]) # 13,14,15,16

print("-ve indexed slicing:", array[-1]) # 13,14,15,16
print("-ve indexed slicing:", array[-2]) # 9,10,11,12

# End

print(array[0:4]) # last index is EXCLUDED
print(array[1:3]) # last index is EXCLUDED
print(array[0:]) # will select everything to the end

# Step

print("start:end:step\n", array[0:4:2])
print("start:end:step\n", array[::2]) # To acess all the indices

print("start:end:-ve step\n", array[::-1]) # To print all the rows reversed
print("start:end:-ve step\n", array[::-2]) # To print all the rows reversed and step every 2nd row


 
