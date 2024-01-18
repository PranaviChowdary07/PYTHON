# def function we replace lambda function
add = lambda a, b : a + b
multiply = lambda a ,b :a * b
div = lambda a, b :a / b

result = add(1,2)
print(result)

# Example     --> take only single expression but many arguments   (exp -->like a %2==0) 
""" def is_even(x):
    return x % 2 == 0 """   # replace lamdba
nums = [2,5,4,7,9,56,46,10,74,3,5,8,9,34,21,22,26]
""" even = list(filter(is_even, nums))"""
even = list(filter(lambda a: a % 2 == 0,nums))
print(even)