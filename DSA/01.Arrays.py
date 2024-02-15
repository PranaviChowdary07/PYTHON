import array as arr
import numpy as np

# defining array
a = arr.array('d',[2,4.6,6.4])     #syntax : arr.array("datatype",[])
# Add the element
a.append(5.5)
# Extend the list
a.extend([3.5,2.2,1.1])
# Remove element
a.pop()   # It removes last element in list, but particular elemnt we use index "a.pop(2)""
print(a)

# defining multi dimensional array : In this give same length for lists
multi = np.array([[4,5,6,7,5,12],[3,2,5,6,14,23]])
print(multi)
print('')

# Example program for arrays with diff operations
print ("Ouput :")
# Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr_1d)

# Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(arr_2d)

# Accessing elements in an array
print("\nAccessing elements:")
print("Element at row 1, column 2:", arr_2d[0, 1])

# Slicing arrays
print("\nSlicing arrays:")
print("First row:", arr_2d[0, :])
print("First column:", arr_2d[:, 0])

# Operations on arrays
print("\nOperations on arrays:")
arr_add = arr_1d + 10
print("Original array:", arr_1d)
print("After adding 10 to each element:", arr_add)

# Element-wise multiplication
arr_multiply = arr_1d * 2
print("\nOriginal array:", arr_1d)
print("After multiplying each element by 2:", arr_multiply)

# Element-wise division
arr_divide = arr_1d / 2
print("\nOriginal array:", arr_1d)
print("After dividing each element by 2:", arr_divide)


