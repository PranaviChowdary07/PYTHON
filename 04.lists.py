# create multiple data types
# Create List
nums = [3,5,6,7,14]
print(nums)
print(nums[3])

# add multiple data types -->use append -->it takes only single argument at a time
nums.append(14.4)
nums.append(True)
nums.append("Pranavi")
print(nums)

fruits = ['Apple','Mango','Grapes']
fruits.insert(1,'Guava')   #-->where to add (str,' ') like (2,'f')
fruits.extend(['cherry','orange'])  #-->to extend list
fruits[3]="Kiwi"        #-->to replace
fruits[1:2]=['strawberry','banana']  #-->to change multiple items  ([1:3] --> lessthan one value)

  # To remove items
fruits=['Apple', 'strawberry', 'banana', 'Mango', 'Kiwi', 'cherry', 'orange','Watermelon']
fruits.remove('cherry')
fruits.pop(2)    #-->a particular item =use index
del fruits[3]
fruits.clear()  #to clear all list
print(fruits)

# Sorting
names = ['abhi','anil','chitra',"pranavi",'potti',"pavan","Sujith","Nishanth","Lavanya"]
names[6:9]=['sujith','nishanth','lavanya']  #change capital to small
names.sort()  #->it takes capital letter first
# names.reverse()  #reverse order
names.sort(reverse = True)  #Descending Order

print(names)


n = [47,7,4,11,14,24,2,25,65,76,54]
n.sort(reverse= True)
print(n)

# Find Minimum And Maximum
p =[34,64,14,11,25,2,7,4,10,27,23,28]
print(min(p))
print(max(p))

""" Example Programs """

#Write a program to count the no.of in specified list within a range

n = [1,3,5,6,8,4,9,10.45,76,78,45,6]
lower_bound = 4
upper_bound = 76
count_within_range = len([num for num in n if lower_bound <= num <=upper_bound])
print(n)
print(count_within_range)

# Write a program to create list by concatenating given list with a range from 1 to n.
# Sample input :['p','q'],n=5,expected output = ['p1','q1','p2','q2','p3','q3','p4','q4','p5','q5']

a =[ 'p','q']
n = 5
result = [item + str(i) for i in range(1,n+1) for item in a]
print(result)