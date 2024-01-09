# create function to use --> def keyword
def sayHello():
    print("Hii Ram")
    print("Good morning")

sayHello()     #--> call function

# Add info to function --> use arguments

def newName(name='User'):   # -->newName()  = default value
    print("Hello",name)
    print("Good Evng")
newName("Lavanya")


# Dont follow order
def name(name,age,country='India'):     # -->formal arguments
    print("hii",name)
    print("Age:",age)
    print("I am from",country)
name(age=23,name='pranavi')   # -->actual arguments

# multiple arguments

""" def add(n1,n2):    # Know the how many values
    result = n1 + n2
    print('Result:',result)
add(46,98)  """     

# Don't know how many values
def getSum(*s):
    result = 0
    for a in s:
        result += a
    print("Result:",result)
    print(s[3])             # which value to print in given list
getSum(1,4,5,76,34)

# return  ->take values from function
def sum(*nums):
    result = 0
    for x in nums:
        result += x
    return result

numSum =sum(4,45,7,3,56,77,34)
print(numSum)
