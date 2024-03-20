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
**Def :-** Arrays in Py are DS that can hold multiple values of the same type.
* It is linear datastructure
* Array supports one dimension array
 Ex: import array  as arr
 a = arr.array('d',[4.5,6.7])
 print(a)
* Numpy supports multi dimension
 Ex: import numpy as np
  a = np.array([[2,4,5,6],[4,7,45,24],[4,12,14,7,11,23]])
  print(a)

### **Example program**
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

# LINKED LIST
   * a linked list consists of nodes where each node contains a data field and a reference(link) to the next node in the list. 
   * It contains nodes,it has data & address ,first node called **"Head"** & end node called **"Tail"**.
   ## Types:
## **1.Sinlge LinkedList**
* It end node adress will be empty(null).
* A single linked list allows the traversal of data only in one way. 
* Time Complexity **O(N)**
* Ex:Box 1: [1] -> Box 2
     Box 2: [2] -> Box 3
     Box 3: [3] -> None
OR  head --> [1] --> [2] --> [3] --> None
## **2.Double LinkedList**   
* A doubly linked list or a two-way linked list is a more complex type of linked list that contains a pointer to the next as well as the previous node in sequence.
* It contains node has 2 address & 1 data.
* it contains three parts of data, a pointer to the next node, and a pointer to the previous node. This would enable us to traverse the list in the backward direction as well.
## **3.Circular LinkedList**
* It contains node has 2 adresss & 1 data ,in last node address belong to 1st address node.

# TREES
* Tree is non-linear data structure.
* It contains nodes,node to node connection called **"Edges"**.
* **Root:** the top (initial) node of the tree,where the all operation start.
* **Node:** Each item in the tree .(keyvalue)
* **Edge:** A tree has __n-1__ edges(n is no.of nodes).
* __Parent:__ A node has precedary(main) of any node.
* __Child:__ A node has descendent(sub-nodes) of any node.
* __Sibilings:__ A group of nodes which have same parent.
* __Leafnode:__ A node without children.
* **Level:** It is defined as __1+__ the no.of edges b/w the node & the root.
* **Height:** The no.of edges from the furthest leaf.(up to down like root to leafnode)
* **Depth:** The no.of edges from te node to the __tree root__.(leaft node to root)
* **Sub-tree:** A portion of a tree data structure that can be viewed as a complete tree in itself.
### Types:
+ Binary Tree
+ Binary search Tree
+ Red-Black Tree
+ AVL Tree
+ Heap Tree
   * The deciding factor of which tree type to use is performance.Performance is measured in terms of __inserting & retrieving data__.

# GRAPHS
* Graph is non-linear data structure
* **Def:** A graph is common DS that consists of finite set of __nodes__(or vertices) & set of edges connecting them.
  + Like a pair (x,y) is referred to as an edge,which communicates that the X vertex connects to Y vertex.
**Types**
#### **Undirected Graph**
  + Nodes are connected by edges that all are __biderectional__.
  + Also called **"Bidirectional"**,comes return .
    * Ex: If an edge connects **1 & 2** ,we can traverse from node **1 to 2** & form node **2 to 1**.
### **Directed Graph**
  + Nodes are connected by **directed edges** --that only go in __one direction__.
    * Ex: If an edges connects __1 & 2__,but the arroe headpoints towards **2**,we can travere from node **1 to 2**,not in **2 to 1** opposite direction. 
### Types of Graph Representation
***Adjancency List***
+ To create an adjancency list,an array of list is used.The size of the array is equal to no.of nodes.
+ A single index,array[i] represents the lit of nodes adjacent to the **ith**node.
 * 0 -->1 --> 2 --> 3
 * 1 --> 2 --> 0
 * 2 --> 0 --> 1
 * 3 --> 0

 # SORTING
 + Elements set either asceding/descending is called **"Sorting"**.
 + Sorting in data structure is the process of arranging different elements in a particular order based on a particular set of criteria.
  * Ex: Given elements are **1,4,2,7,5,3,9**  
      * After sorting:  -->**1,2,3,4,5,7,9**
### Types:
+ Insertion sort
+ Selection sort
+ Bubble sort
+ Merge sort
+ Quick sort
+ Shell sort
    ### *SELECTION SORT:*
* **Def:** Selection sort is a simple sorting algorithm that iterates through the input array repeatedly, selecting the minimum (or maximum) element from the unsorted portion and placing it at the beginning of the sorted portion. This process continues until the entire array is sorted.**(minimum to maximum)**

* *The algorithms maintains two subarrays in a given array*
   * 1.The subarray which i already sorted.
   * 2.Remaining subarray which is unsorted
* **Time Complexity:"O(n2)"**
  ### *Example*
* given array : [5,2,9,1,6]
  * First, we find the smallest element in the array, which is 1, and swap it with the element at the first position. Our array becomes [1, 2, 9, 5, 6].
  * Next, we move to the second position in the array (2). Since 2 is already in the correct position, we leave it there.
  * Now, we find the smallest element in the unsorted portion (5, 9, 6), which is 5, and swap it with the element at the third position. Our array becomes [1, 2, 5, 9, 6].
  * We find smallest in(9,6) which is 6.& swap it.
  * After final iteration the sort array becomes **[1,2,5,6,9]**

      ### *INSERTION SORT*
* The insertion sort is a straightforward & more efficient algorithm.
  * ***Concept of Insertion Sort***
    + THe array contains virtually in the two parts in Insertion Sort: __Unsortedpart__ & __Sorted part__.
    + The sorted part contains the first element of array & other unsorted subpart contains the rest of the array.
    + The first element in unsorted array is compared to sorted array.
    + Then we can place it into a proper sub-array
    + Time Complexity :**O(n2)**
       * ex: 23,45,12,22,2 -->given elements
          * 23-45,12,22,2 -->23 sorted , other elements are unsorted
          * 23,45-12,22,2 -->23,45 sorted
          * 12,23,45-22,2 --->12,23,45 sorted
          * 12,22,23,45-2 -->12,22,23,45 sorted
          * 2,12,22,23,45 --> All elements are sorted.

    ### ***MERGE SORT***
+ It follows __divide & conquer__ method.
+ One of the most popular & efficient sorting algorithm.
+ It divides the given list into 2 halves(parts),call itself for the two halves and then merges the two sorted halves.
+ We define **merge()** function  used to merging two halves.
+ The sublists are divided again & again untill we get only element.
+ Then we combine 1 element into 2 elements,them 2 into 4 sorting in process,untill we get sorted list.
+ Merge sort can be implement using 2 wats: **top-down approach** &  **bottom-up approach**.

    ### *BUBBLE SORT*
+ Time complexity:**O(n)**
+ The bubble sort uses straight forward logic,that works by repeating swapping the adjacent elements if they are not in right order.
+ It compares one pir at a time & swaps the first element is > the second element,otherwise move further to the next pair of elements to comparision
  * Ex: Given List **[8,5,2,6,12]
     + [8,5,2,6,12]  --> 8>5 it swap then 
     + [5,8,2,6,12]  --> 8>2 it swap
     + [5,2,8,6,12]  --> 8>6 it swap
     + [5,2,6,8,12]  --> 8<12 no  need to swap then go to first element
     + [5,2,6,8,12]  --> 5>2 it swap
     + [2,5,6,8,12]  -->no swap
       + **[2,5,6,8,12]** finally sorted list.
.
 