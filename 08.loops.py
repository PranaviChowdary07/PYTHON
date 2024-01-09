# While loop
a = 0
while a < 10:
    a += 1
    
    if a == 3:
        print("a value is 3 is now")
        continue
    print(a,"Learning Python")

# For Loop
for  x  in range (5):      # how many values print
    print(x)

for a  in range(1,10):      # where to start and end 
    print(a)


for p in range (1,100,10):   # add value to p
    print(p)

# Example
name = ['Pranavi','Sujith','Pavan','Potti','Lavanya','Nishanth']    # print list,tuple,set
for i in name:
    print(i)
else:
    print("Bye!!")

# print characters
name = "Pranavi"
for i in name:
    print(i)


# use break,and continue
people =  ['Pranavi','Sujith','Pavan','Potti','Lavanya','Nishanth']
for i in people:
  
    if i == "Potti":
        #break
          continue
    print(i)
