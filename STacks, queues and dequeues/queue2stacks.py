class Queue2Stacks(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

q = Queue2Stacks()
q.enqueue(5)
q.enqueue(6)
print(q.dequeue())
q.enqueue(3)
print(q.dequeue())