class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)
        #self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()
            #self.items.pop(0)

    def size(self):
        return len(self.items)

q = Queue()
print(q.isEmpty())
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
