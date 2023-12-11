# CREATE TUPLE

fruits =('mango',"grapes","orange","mango")
# Functions
print(fruits.index("grapes"))   # 1.index
print(fruits.count("mango"))    # 2.count      -->It allows duplicate values
print(fruits)

# Inmutable,doesnot change 
# change the value but it convert into list

names = ('Pranavi','Sujith','Pavan','Potti','Lav')
nameList = list(names)      # Convert tuple to list
nameList[1] = "Abhi"
print(nameList)
names = tuple(nameList)     # Convert list to Tuple
print(names)
