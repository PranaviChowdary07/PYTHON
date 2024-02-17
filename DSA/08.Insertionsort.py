def insertionsort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
arr = [34,12,4,14,23,11,6,22,16]
insertionsort(arr)

print("Insertion sorting:") 
for i in range(len(arr)):
  print(arr[i])


""" 
    Output:
    Insertion sorting:
4
6
11
12
14
16
22
23
34
      """