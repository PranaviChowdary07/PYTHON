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