                Data Structure  & Algorithims

+ Data Structure :- To store data in structure(organise)
+ Algorithim :- Step-by-step process

Two types:
  + 1.Bulit in Ds
  + 2.userdefined Ds

### 1.Bulit Ds :
   * List(Mutable)
   * Dictionary(Mutable)
   * Tuple(Unmutable)
   * Set(Mutable)

### 2.userdefined Ds :
+ Arrays
  * one dimensional
  * multi     "
+ Stack
+ Queue
+ Trees
+ Linked List:
    * single
    * double
    * circular
+ Graphs
+ HashMaps

### Searching & Sorting Techiniques
 * Bubble sort
 * Merge sort
 * Selection sort
 * Shell sort
 * Insertion sort


*Time Complexity & Space Complexity*

# *ARRAYS *
Def :- Arrays in Py are DS that can hold multiple values of the same type.
* It is linear datastructure
* Array supports one dimension array
 Ex: import array  as arr
 a = arr.array('d',[4.5,6.7])
 print(a)
* Numpy supports multi dimension
 Ex: import numpy as np
  a = np.array([[2,4,5,6],[4,7,45,24],[4,12,14,7,11,23]])
  print(a)

* Example program
import numpy as np

### Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr_1d)
### Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(arr_2d)
### Accessing elements in an array
print("\nAccessing elements:")
print("Element at row 1, column 2:", arr_2d[0, 1])
### Slicing arrays
print("\nSlicing arrays:")
print("First row:", arr_2d[0, :])
print("First column:", arr_2d[:, 0])
### Operations on arrays
print("\nOperations on arrays:")
arr_add = arr_1d + 10
print("Original array:", arr_1d)
print("After adding 10 to each element:", arr_add)
### Element-wise multiplication
arr_multiply = arr_1d * 2
print("\nOriginal array:", arr_1d)
print("After multiplying each element by 2:", arr_multiply)
### Element-wise division
arr_divide = arr_1d / 2
print("\nOriginal array:", arr_1d)
print("After dividing each element by 2:", arr_divide)

## Output

1D Array:
[1 2 3 4 5]

2D Array:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
Accessing elements:
Element at row 1, column 2: 2

Slicing arrays:
First row: [1 2 3]
First column: [1 4 7]

Operations on arrays:
Original array: [1 2 3 4 5]
After adding 10 to each element: [11 12 13 14 15]

Original array: [1 2 3 4 5]
After multiplying each element by 2: [ 2  4  6  8 10]

Original array: [1 2 3 4 5]
After dividing each element by 2: [0.5 1.  1.5 2.  2.5]

# STACKS
 - It is a linear data structure
 - It follows LIFO(Last In First Out).
 - New element is added at one-end & remove at that(same) only.
 - Insert element is called **"Push"**.
 - Delete element is called **"Pop"**.
 - Time Complexity **"O(1)"**.

# QUEUE
  - Queue is linear data structure
  * It follows FIFO(First In First Out).
  - Insertion of element is called **"Rear"**(Enqueue).
  * Deletion of element is called **"Front"**(Dequeue).
  - Time Complexity **"O(1)"**.
  * Ex:  Insert-->2|3|4|5 --->delete 5|4|3|2



