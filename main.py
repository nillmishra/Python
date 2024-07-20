import numpy as np
list1 = [1,2,3,4]
array1 = np.array(list1)
print(array1)

array2 = np.zeros((2,3))
print(array2)

array3 = np.array([[[1, 2, 3], [4, 5, 6]]])
print(array3)
print(array3.shape)

array4 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(array4)


array5 = np.array([1, 2, 3, 4])
array6 = np.array([1, 1, 1, 1])

# Addition
result = array5+array6
print("Addition result:", result)


result1 = np.add(array5, array6)
print("np.add result:", result1)

# Subtraction
result2 = array5 - array6
print("Subtraction result:", result2)

result3 = np.subtract(array5, array6)
print("np.subtract result:", result3)

# Multiplication
result4 = array5 * array6
print("Multiplication result:", result4)

result5 = np.multiply(array5, array6)
print("np.multiply result:", result5)


#print power
array7 = np.array([1,2,3,4,5,6,7])
result6 = array7**2
print(result6)

result7 = np.power(array7, 2)
print(result7)

array8 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("Original array:")
print(array8)
print("Original array shape:", array8.shape)

reshapedArray = np.reshape(array8, (4, 2))  # Corrected the syntax here
print("Reshaped array:")
print(reshapedArray)
print("Reshaped array shape:", reshapedArray.shape)

#transposing the array
trasposeArray = np.transpose(reshapedArray)
print(trasposeArray)



