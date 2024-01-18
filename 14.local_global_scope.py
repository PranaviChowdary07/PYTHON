# Local scope --> uses only particular  local function 
def greet():
    x = 'Hii'
     #print(x)
    return x
    """  def say():    #but it uses many local functions
        print("from say",x)
    say() """

a = greet()   # it takes only value not the variable
print(a)


# Global Variable

n = 99
m = 0
def example():
    global n, m  #  use same variable  it takes  local scope when we use this it takes global
    n = 67
    m = 23
    print('in function x :',n)
    print('in function y:',m)
example()
print('out function x :',n)
print('out function y :',m)

print(globals()['n'])
