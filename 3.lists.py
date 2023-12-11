# Create List
nums = [3,5,6,7,14]
print(nums)
print(nums[3])

#add multiple data types -->use append -->it takes only single argument at a time
nums.append(14.4)
nums.append(True)
nums.append("Pranavi")
print(nums)

fruits = ['Apple','Mango','Grapes']
fruits.insert(1,'Guava')   #-->where to add (str,' ') like (2,'f')
fruits.extend(['cherry','orange'])  #-->to extend list
fruits[3]="Kiwi"        #-->to replace
fruits[1:2]=['strawberry','banana']  #-->to change multiple items
print(fruits)