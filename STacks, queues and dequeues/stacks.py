class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            self.items.pop()


    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

s = Stack()
print(s.isEmpty())
s.push(2)
s.push(3)
print(s.peek())
s.pop()
s.pop()
s.pop()
