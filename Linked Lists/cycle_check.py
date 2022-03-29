class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

    def cycle_check(self, node):
        l = []
        l.append(node)
        while node!= None and node.nextnode != None:
            if node.nextnode in l:
                return True
            else:
                l.append(node.nextnode)
                node = node.nextnode
        return False

a = Node(2)
b = Node(3)
c = Node(4)
a.nextnode = b
b.nextnode = c
c.nextnode = a
x = Node(2)
y = Node(3)
z = Node(4)
m = Node(7)
x.nextnode = y
y.nextnode = z
z.nextnode = m
print(a.cycle_check(c))
print(x.cycle_check(y))
