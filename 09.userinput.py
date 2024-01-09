x = int(input("Enter the num1: "))
y = int(input("Enter the num2: "))
z = x +y
print("Result: ",z)

p = input("Enter any char: ")
while len(p) != 1:        # This  is used for condition -->To check len of char
    print("Please enter single char only")
    p = input("Enter any char: ")
    print(p)
    