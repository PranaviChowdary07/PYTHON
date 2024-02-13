class Queue(object):
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        return self.queue==[]
    def enqueue(self,data):
        self.queue.insert(0,data)
        return '{} add queue'.format(data)
    def dequeue(self):
        return self.queue.pop()
    def sizequeue(self):
        return len(self.queue)
    
if __name__== '__main__':
    q = Queue()
    print(q.enqueue(1))
    print(q.enqueue(2))
    print(q.enqueue(3))
    print(q.enqueue(4))
    print(q.enqueue(5))
    print(q.enqueue(6))
    print(q.enqueue(7))
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print("Size of Queue:",q.sizequeue())
    print(q.isEmpty())

"""
OUTPUT:

1 add queue
2 add queue
3 add queue
4 add queue
5 add queue
6 add queue
7 add queueadd
1
2
3
Size of Queue: 4
False
         """