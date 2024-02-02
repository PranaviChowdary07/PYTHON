""" Operator Overloading & Method Overriding """
""" 8 + 4 --> 8,9 are operands,+ is operator """

a = 14
b = 4
print(a + b)
# behind code running
print(int.__add__(a,b))
# For string
a = "Pranavi"
b = "Kasthuri"
print(str.__add__(a,b))
