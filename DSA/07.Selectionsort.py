a = [23,12,21,3,4,10,6,9,33,24,11]

for i in range(len(a)):
    min_i = i
    for j in range(i+1,len(a)):
        if a[min_i]>a[j]:
            min_i = j
    a[i],a[min_i] = a[min_i],a[i]     # swap
print("Sorting elements in Selection sort:")
for i in range(len(a)):
    print(a[i])


""" 
Output:
Sorting elements in Selection sort:
3
4
6
9
10
11
12
21
23
24
33 """