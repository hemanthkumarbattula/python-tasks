class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None


    def reverse1(self,head):
        l = []
        l.append(head)
        while head != None and head.nextnode!= None:
            l.append(head.nextnode)
            head = head.nextnode
        l = l[::-1]
        for i in range(len(l)):
            print(i)
            if i == len(l)-1:
                l[i].nextnode = None
                break
            l[i].nextnode = l[i+1]
        return l[0]

    def reverse(self, head):
        current = head
        previous = None
        next = None
        while current:
            next  = current.nextnode
            current.nextnode = previous
            previous = current
            current = next
        return previous



x = Node(2)
y = Node(3)
z = Node(4)
m = Node(7)
x.nextnode = y
y.nextnode = z
z.nextnode = m
r = x.reverse(x)

