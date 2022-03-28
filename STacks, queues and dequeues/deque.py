class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0, item)

    def removeFront(self):
        if not self.isEmpty():
            return self.items.pop()

    def removeRear(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

d = Deque()
d.addFront(2)
d.addFront(3)
d.addRear(5)
print(d.removeFront())
print(d.removeRear())
