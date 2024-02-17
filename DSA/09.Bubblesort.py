def bubbleort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
arr = [22,11,45,23,11,3,6,12,100,14]
bubbleort(arr)
for i  in range(len(arr)):
    print(arr[i])

""" 
Output:
3
6
11
11
12
14
22
23
45
100
 """    