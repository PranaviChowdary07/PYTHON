class Stack(object):
    # Intializing(constructor)
    def __init__(self):
        self.stack = []
        self.numofitems = 0
    # Ckecking empty
    def isEmpty(self):
        return self.stack == []
    # pushing element
    def push(self,data):
        self.stack.insert(self.numofitems,data)
        self.numofitems +=1  # increment index
        return'{} pushed to stack' .format(data)
    # deleting the element
    def pop(self):
        self.numofitems -=1
        data = self.stack.pop(self.numofitems)
        return'{} pop to stack' .format(data)
    def stacksize(self):
        return len(self.stack)
    
# testing

if __name__ == '__main__':
    s = Stack()
    print(s.push(2))
    print(s.push(3))
    print(s.push(4))
    print(s.push(6))
    print(s.push(12))
    print(s.pop())
    print(s.pop())
    print("Size of stack:",s.stacksize())



    """ 
     OUTPUT:
      
2 pushed to stack
3 pushed to stack
4 pushed to stack
6 pushed to stack
12 pushed to stack
12 pop to stack
6 pop to stack
Size of stack: 3
 """
    



