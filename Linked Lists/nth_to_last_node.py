class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None


    def nth_to_last_node(self,n,head):
        l = []
        l.append(head)
        while head != None and head.nextnode!= None:
            l.append(head.nextnode)
            head = head.nextnode

        return l[-n]

    def nth_to_last_node1(self, n, head):
        left_pointer = head
        right_pointer = head
        for i in range(n-1):
            if not right_pointer.nextnode:
                raise LookupError('Error: n is larger than the linked list')
            right_pointer = right_pointer.nextnode

        while right_pointer.nextnode:

            left_pointer = left_pointer.nextnode
            right_pointer = right_pointer.nextnode
        return left_pointer


x = Node(2)
y = Node(3)
z = Node(4)
m = Node(7)
x.nextnode = y
y.nextnode = z
z.nextnode = m
r = x.nth_to_last_node(1,x)
print(r.value)

